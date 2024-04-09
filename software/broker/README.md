# Jury's Interface

This broker allows to forward input data from the object to the internal Node.js API.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.x
- `poetry` package manager
- Internal API running

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/tristanqtn/Rhythmic-Ranker
   ```

2. Navigate to the project directory:

   ```bash
   cd Rhythmic-Ranker/SI/broker
   ```

3. Install the required Python packages:

   ```bash
    poetry install
   ```

## Usage

Don't forget to run this code in the correct venv.

```bash
poetry shell
```

Start the Flask server:

```bash
python backend.py
```

Open your web browser and navigate to http://localhost:5000.

You should see the data from your InfluxDB database displayed in real-time on the webpage.

**Configuration:**

INFLUXDB_URL: The URL of your InfluxDB instance.

INFLUXDB_TOKEN: The authentication token for accessing your InfluxDB instance.

INFLUXDB_ORG: The organization name associated with your InfluxDB instance.

INFLUXDB_BUCKET: The name of the bucket in your InfluxDB instance containing the data you want to display.

## API Routes

### CRUD Operations

**POST /metrics**

- **Parameter:** nona
- **Usage:**
  Use this method on the given path to post a metric measurement to be forward to the internal API.

## Automation

An automation script for the deployment of this micro service. To run it place yourself in the current directory (here `./interface`), enable a peotry shell with `poetry shell` and run the following command:

```powershell
# for Windows
./start.ps1
```

```bash
# for Linux
./start.sh
```

## Author

- Tristan QUERTON: tristan.querton@edu.ece.fr
