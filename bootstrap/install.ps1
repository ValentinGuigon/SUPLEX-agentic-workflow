param(
    [string]$RepoUrl = "https://github.com/ValentinGuigon/SUPLEX-agentic-workflow",
    [string]$Ref = "main",
    [string]$SourceRoot = "",
    [string]$WorkflowMode = ""
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

try {
    if ([string]::IsNullOrWhiteSpace($WorkflowMode)) {
        $WorkflowMode = if ([string]::IsNullOrWhiteSpace($env:SUPLEX_WORKFLOW_MODE)) { "standard" } else { $env:SUPLEX_WORKFLOW_MODE }
    }

    if ($WorkflowMode -notin @("standard", "sans-sucre")) {
        throw "SUPLEX bootstrap failed: Workflow mode must be 'standard' or 'sans-sucre'."
    }

    if ([string]::IsNullOrWhiteSpace($SourceRoot)) {
        $tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("suplex-bootstrap-" + [System.Guid]::NewGuid().ToString("N"))
        New-Item -ItemType Directory -Path $tempRoot | Out-Null
        $archiveUrl = (($RepoUrl.TrimEnd("/")) -replace "\.git$", "") + "/archive/refs/heads/$Ref.zip"
        $archivePath = Join-Path $tempRoot "suplex-template.zip"
        Invoke-WebRequest -UseBasicParsing -Uri $archiveUrl -OutFile $archivePath
        Expand-Archive -LiteralPath $archivePath -DestinationPath $tempRoot -Force
        $sourceRoot = Get-ChildItem -LiteralPath $tempRoot -Directory | Where-Object { $_.Name -like "SUPLEX-agentic-workflow-*" } | Select-Object -First 1 -ExpandProperty FullName
        if (-not $sourceRoot) {
            throw "Unable to determine staged SUPLEX archive contents."
        }
    } else {
        $sourceRoot = (Resolve-Path -LiteralPath $SourceRoot).Path
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

    & $pythonCommand @pythonArgs (Join-Path $sourceRoot "bootstrap\\init_suplex.py") --target-dir $targetDir --source-root $sourceRoot --repo-url $RepoUrl --ref $Ref --workflow-mode $WorkflowMode
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }
}
finally {
    if ($tempRoot -and (Test-Path -LiteralPath $tempRoot)) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force
    }
}
