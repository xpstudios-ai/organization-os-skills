# Human-in-the-loop reproduction loop.
# Copy this file, edit only the marked section, and run it locally.
# Do not paste credentials or sensitive raw payloads into captured answers.

$ErrorActionPreference = "Stop"

function Invoke-Step {
    param([Parameter(Mandatory = $true)][string]$Instruction)
    Write-Host ""
    Write-Host ">>> $Instruction"
    [void](Read-Host "    Press Enter when done")
}

function Read-Capture {
    param([Parameter(Mandatory = $true)][string]$Question)
    Write-Host ""
    Write-Host ">>> $Question"
    return Read-Host "    >"
}

# --- edit below ---------------------------------------------------------

Invoke-Step "Open the app and navigate to the failing workflow."
$reproduced = Read-Capture "Perform the failing action. Did it reproduce? (y/n)"
$symptom = Read-Capture "Enter a minimal redacted error or observed symptom"

# --- edit above ---------------------------------------------------------

Write-Host ""
Write-Host "--- Captured ---"
Write-Host "REPRODUCED=$reproduced"
Write-Host "SYMPTOM=$symptom"
