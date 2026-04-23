param(
    [string]$SuplexRepoUrl = "https://github.com/ValentinGuigon/SUPLEX-agentic-workflow",
    [string]$SuplexRef = "main",
    [string]$SuplexSourceRoot = "",
    [string]$SuplexWorkflowMode = ""
)

$ErrorActionPreference = "Stop"

$targetDir = (Get-Location).Path
$tempRoot = $null
$attemptedInterpreters = @("py -3", "python")

function Test-Python3Command {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Command,

        [string[]]$Arguments = @()
    )

    if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
        return $false
    }

    $probeArgs = $Arguments + @("-c", "import sys; raise SystemExit(0 if sys.version_info[0] == 3 else 1)")
    & $Command @probeArgs 1>$null 2>$null
    return ($LASTEXITCODE -eq 0)
}

function Resolve-RawBaseUrl {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoUrl,

        [Parameter(Mandatory = $true)]
        [string]$Ref
    )

    $trimmed = $RepoUrl.Trim()
    if ($trimmed -match '^https://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$') {
        return "https://raw.githubusercontent.com/$($Matches[1])/$($Matches[2])/$Ref"
    }

    if ($trimmed -match '^git@github\.com:([^/]+)/([^/]+?)(?:\.git)?$') {
        return "https://raw.githubusercontent.com/$($Matches[1])/$($Matches[2])/$Ref"
    }

    throw "Unsupported remote repo URL for lightweight staging: $RepoUrl"
}

function Invoke-DownloadToPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Uri,

        [Parameter(Mandatory = $true)]
        [string]$DestinationPath
    )

    $parent = Split-Path -Parent $DestinationPath
    if ($parent -and -not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }

    Invoke-WebRequest -UseBasicParsing -Uri $Uri -OutFile $DestinationPath
}

function Stage-RemoteSourceLightweight {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoUrl,

        [Parameter(Mandatory = $true)]
        [string]$Ref,

        [Parameter(Mandatory = $true)]
        [string]$TempRoot
    )

    $sourceRoot = Join-Path $TempRoot "staged-source"
    New-Item -ItemType Directory -Path $sourceRoot -Force | Out-Null

    $rawBaseUrl = Resolve-RawBaseUrl -RepoUrl $RepoUrl -Ref $Ref
    $manifestPath = Join-Path $TempRoot "payload-manifest.txt"
    Invoke-DownloadToPath -Uri "$rawBaseUrl/bootstrap/payload_manifest.txt" -DestinationPath $manifestPath

    $entries = Get-Content -LiteralPath $manifestPath |
        ForEach-Object { $_.Trim() } |
        Where-Object { $_ -and -not $_.StartsWith("#") }

    foreach ($entry in @("bootstrap/init_suplex.py") + $entries) {
        $destinationPath = Join-Path $sourceRoot ($entry -replace '/', '\')
        Invoke-DownloadToPath -Uri "$rawBaseUrl/$entry" -DestinationPath $destinationPath
    }

    return $sourceRoot
}

function Stage-RemoteSourceArchive {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoUrl,

        [Parameter(Mandatory = $true)]
        [string]$Ref,

        [Parameter(Mandatory = $true)]
        [string]$TempRoot
    )

    $archiveUrl = (($RepoUrl.TrimEnd("/")) -replace "\.git$", "") + "/archive/refs/heads/$Ref.zip"
    $archivePath = Join-Path $TempRoot "suplex-template.zip"
    Invoke-WebRequest -UseBasicParsing -Uri $archiveUrl -OutFile $archivePath
    Expand-Archive -LiteralPath $archivePath -DestinationPath $TempRoot -Force
    return Get-ChildItem -LiteralPath $TempRoot -Directory | Where-Object { $_.Name -like "SUPLEX-agentic-workflow-*" } | Select-Object -First 1 -ExpandProperty FullName
}

try {
    if ([string]::IsNullOrWhiteSpace($SuplexWorkflowMode)) {
        $SuplexWorkflowMode = if ([string]::IsNullOrWhiteSpace($env:SUPLEX_WORKFLOW_MODE)) { "standard" } else { $env:SUPLEX_WORKFLOW_MODE }
    }

    if ($SuplexWorkflowMode -notin @("standard", "sans-sucre")) {
        throw "SUPLEX bootstrap failed: Workflow mode must be 'standard' or 'sans-sucre'."
    }

    if ([string]::IsNullOrWhiteSpace($SuplexSourceRoot)) {
        $tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("suplex-bootstrap-" + [System.Guid]::NewGuid().ToString("N"))
        New-Item -ItemType Directory -Path $tempRoot | Out-Null
        try {
            $sourceRoot = Stage-RemoteSourceLightweight -RepoUrl $SuplexRepoUrl -Ref $SuplexRef -TempRoot $tempRoot
        }
        catch {
            Write-Warning "SUPLEX lightweight staging failed; falling back to full archive download. $($_.Exception.Message)"
            $sourceRoot = Stage-RemoteSourceArchive -RepoUrl $SuplexRepoUrl -Ref $SuplexRef -TempRoot $tempRoot
        }
        if (-not $sourceRoot) {
            throw "Unable to determine staged SUPLEX bootstrap source contents."
        }
    } else {
        $sourceRoot = (Resolve-Path -LiteralPath $SuplexSourceRoot).Path
    }

    if (Test-Python3Command -Command "py" -Arguments @("-3")) {
        $pythonCommand = "py"
        $pythonArgs = @("-3")
    } elseif (Test-Python3Command -Command "python") {
        $pythonCommand = "python"
        $pythonArgs = @()
    } else {
        throw "SUPLEX bootstrap failed: Python 3 is required. Attempted interpreters: $($attemptedInterpreters -join ', '). Install Python 3 and ensure either 'py -3' or 'python' runs Python 3, then rerun the bootstrap."
    }

    & $pythonCommand @pythonArgs (Join-Path $sourceRoot "bootstrap\\init_suplex.py") --target-dir $targetDir --source-root $sourceRoot --repo-url $SuplexRepoUrl --ref $SuplexRef --workflow-mode $SuplexWorkflowMode
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }
}
finally {
    if ($tempRoot -and (Test-Path -LiteralPath $tempRoot)) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force
    }
}
