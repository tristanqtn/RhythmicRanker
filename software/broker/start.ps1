# requires InfluxDB cluster and correct connection credentials in .env file

# Install Python dependencies
Write-Host "Installing Python dependencies...`n"
poetry install


# Run Python backend
Write-Host "`nRunning Python backend...`n"
python broker.py
