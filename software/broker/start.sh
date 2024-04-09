#!/bin/bash
# requires InfluxDB cluster and correct connection credentials in .env file

# Install Python dependencies
echo "Installing Python dependencies..."
poetry install

# Run Python backend
echo "Running Python backend..."
python broker.py
