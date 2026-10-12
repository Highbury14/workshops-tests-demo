[CmdletBinding()]
param(
    [Parameter(Mandatory=$false, ValueFromRemainingArguments=$true)]
    $RemainingArgs
)

# Define the log file location inside your app folder
$LogFile = Join-Path $PSScriptRoot "adk_web_executions.log"

# Write-Host "Starting 'adk web'. Terminal output is being redirected..." -ForegroundColor Yellow
# Write-Host "All outputs are APPENDING to: $LogFile" -ForegroundColor Cyan

# Group the initialization headers and the adk stream execution together
& {
    # Write-Output "`n"
    # Write-Output "=========================================================================="
    Write-Output "--- [$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] New adk web Session ---"
    # Write-Output "=========================================================================="
    
    # Run adk web and pass any extra flags you type at the command line
    adk web @RemainingArgs
} *>&1 | Out-File -FilePath $LogFile -Append -Encoding utf8

# Catch the terminal termination details if it stops or crashes
$ExitCode = $LASTEXITCODE

$EndStatus = "--- [$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Session Stopped (Exit Code: $ExitCode) ---"
$EndStatus | Out-File -FilePath $LogFile -Append -Encoding utf8

# Write-Host "adk web has terminated (Exit Code: $ExitCode)." -ForegroundColor Green
