# REQUIRES THE INFLUX DB CLUSTER TO BE DEPLOYED AND ACCESSIBLE TO WORK
Write-Host "Executing program in: $(Get-Location)"

# Load environment variables from .env file
Write-Host "`nPLEASE CHECK ENV VARIABLES :"
$envFile = Get-Content -Path .env
$envFile

# Deploy INFLUXDB cluster in separate console window
Write-Host "`nDeploying InfluxDB cluster inside K8S..."
$apiPath = Join-Path -Path $PSScriptRoot -ChildPath "infrastructure"
try{
    Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", "& { Set-Location $apiPath; .\start.ps1 }"
    Start-Sleep -Seconds 5
}
catch {
    Write-Error "Failed to start API endpoint: $_"
}

Write-Host "`nINFLIXDB CLUSTER SHOULD BE CONFIGURED BEFORE MOVING ON !`n"
pause

# Deploy API endpoint in separate console window
Write-Host "`nDeploying broker endpoint..."
$brokerPath = Join-Path -Path $PSScriptRoot -ChildPath "broker"
try{
    Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", "& { Set-Location $brokerPath; poetry install; python broker.py; }"
    Start-Sleep -Seconds 5
}
catch {
    Write-Error "Failed to start broker endpoint: $_"
}

# Deploy API endpoint in separate console window
Write-Host "`nDeploying api endpoint..."
$apiPath = Join-Path -Path $PSScriptRoot -ChildPath "api"
try{
    Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", "& { Set-Location $apiPath; npm i; npm run test; npm run start; }"
    Start-Sleep -Seconds 5
}
catch {
    Write-Error "Failed to start API endpoint: $_"
}


# Deploy interface in separate console window
Write-Host "`nDeploying interface..."
$interfacePath = Join-Path -Path $PSScriptRoot -ChildPath "interface"
try {
    Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", "& { Set-Location $interfacePath; poetry install; pytest; python backend.py; }"
    Start-Sleep -Seconds 5
}
catch {
    Write-Error "Failed to start interface: $_"
}


Write-Host "`nDEPLOYMENT COMPLETED"

