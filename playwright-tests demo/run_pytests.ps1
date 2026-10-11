[CmdletBinding()]
param(
    [Parameter(Mandatory=$false, ValueFromRemainingArguments=$true)]
    $RemainingArgs
)

# Get the absolute path for the log file in the current folder
$LogFile = Join-Path $PSScriptRoot "pytests_execution.log"

# Group the timestamp and pytest execution into a single stream and append to the log
& {
    # Write-Output "`n"
    Write-Output "--- [$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] PyTest Run Execution Beginning ---"
    
    # Format and log the exact command being executed with its arguments
    $CommandString = "python -m pytest"
    if ($RemainingArgs) {
        $CommandString += " " + ($RemainingArgs -join " ")
    }
    Write-Output "Executed Pytests-command: $CommandString"

    # Run pytest and pass any arguments given to this script
    python -m pytest @RemainingArgs
} *>&1 | Out-File -FilePath $LogFile -Append -Encoding utf8

# Capture the native exit code immediately after execution finishes
$PytestExitCode = $LASTEXITCODE

# Log the result status to the file
$EndStatus = "--- [$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] PyTest Run Ended with Exit Code: $PytestExitCode ---"
$EndStatus | Out-File -FilePath $LogFile -Append -Encoding utf8

# Provide clear console output based on the result
# if ($PytestExitCode -eq 0) {
#   Write-Host "PyTests completed successfully (Exit Code: 0). Log appended to: $LogFile" -ForegroundColor Green
# } else {
#   Write-Host "PyTests failed or encountered an error (Exit Code: $PytestExitCode). Log appended to: $LogFile" -ForegroundColor Red
# }

# Exit the script with the captured code so CI/CD tools know if it failed
# exit $PytestExitCode
