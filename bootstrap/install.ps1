param(
    [string]$RepoUrl = "https://github.com/ValentinGuigon/SUPLEX-agentic-workflow",
    [string]$Ref = "main",
    [string]$SourceRoot = ""
)

$ErrorActionPreference = "Stop"

$targetDir = (Get-Location).Path
$tempRoot = $null

try {
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

    & py -3 (Join-Path $sourceRoot "bootstrap\\init_suplex.py") --target-dir $targetDir --source-root $sourceRoot --repo-url $RepoUrl --ref $Ref
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }
}
finally {
    if ($tempRoot -and (Test-Path -LiteralPath $tempRoot)) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force
    }
}
