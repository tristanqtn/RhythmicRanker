# Node.js API Deployment on Local Server

## Overview

This document provides a guide to deploying a Node.js API on a local server and accessing it from other devices on the same network. Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine, commonly used for building scalable network applications.

## Prerequisites

Before proceeding, ensure the following prerequisites are met:

- Node.js and npm are installed on the local server.
- Basic understanding of Node.js and Express.js for API development.
- Devices on the same network can communicate with the local server.

## Deployment Steps

### Step 1: Set Up Node.js API

1. Browe to the `/api` folder containing our API source code:
2. Install Express.js and any other dependencies:

   ```bash
   npm install
   ```

3. If updates a required do not hesitate to bring packages up to date after verifying conformity.

### Step 2: Run the Node.js API Server

This application requires an InfluxDB instance to work. Make sure you deploy one has shown [here](../infrastructure/README.md). Once you got all InfluxDB creditentials information rename the `.env` file as follows:

```bash
cp .env.example .env
```

Then set all variable in this file using your local config and the InfluxDB information.

Start the Node.js API server:

**Dev Mode:**

```bash
npm run dev
```

**Run Mode:**

```bash
npm run start
```

Make surte to always maintain the connection to the InfluxDB instance and perform some health checks.

### Step 3: Verify Local Access

Verify that the API is accessible locally by sending HTTP requests to http://localhost:<port> where <port> is the port your Node.js API server is running on (3000 by default).

## Accessing API from Other Devices

To access the Node.js API from other devices on the same network, follow these steps:

Find the local IP address of the server running the Node.js API. This information must be given to the app itself in the `.env` file. You can typically find this using:

```bash
ipconfig (Windows)
```

or

```bash
ifconfig (Linux/Mac)
```

Use the local IP address and the port number of the Node.js server to access the API from other devices on the same network. For example:

```php
http://<local_ip_address>:<port>
```

Replace <local_ip_address> with the IP address of the server running the API, and <port> with the port number your Node.js server is listening on. This will be useful when the connected device will be sending the metrics over the network. Ensure that any firewall or security settings on the server allow incoming connections on the specified port.

## API Routes

### CRUD Operations

**POST /metrics**

- **Parameter:** none
- **Usage:**
  Use this method on the given path to add a new metric measurement to the Influx DB. In the post request send a JSON body containing the following information: `{ "sensor": "height", "measurement": 3 }`.

**GET /metrics**

- **Parameter:** none
- **Usage:**
  Use this method on the given path to retrieve all Influx DB entries from the last 60 minutes.

**GET /stream**

- **Parameter:** none
- **Usage:**
  Use this method on the given path to obtain a continuous stream of InfluxDB content.

### Other Routes

**GET /api-docs**

- **Parameter:** none
- **Usage:**
  Obtain complete documentation of the API.

**GET /health/influx**

- **Parameter:** none
- **Usage:**
  Obtain the health of the INFLUX DB instance.

**GET /health/api**

- **Parameter:** none
- **Usage:**
  Obtain the health of the API.

**IMPORTANT**: This application requires an InfluxDB to work perfectly. If you don't have one, you can use the one provided by using the Helm deployment in this repo.

## Automation

An automation script for the deployment of this micro service. To run it place yourself in the current directory (here `./api`) and run the following command:

```powershell
# for Windows
./start.ps1
```

```bash
# for Linux
./start.sh
```

## Testing

Some basic tests have been implemented to help devs. To run them make sure the InfluxDB is running and that a tunnel is open to that instance. Also make sure the the `env`variables are correctly set.

```bash
npm run test
```

## Conclusion

By following this guide, you have successfully deployed a Node.js API on a local server and learned how to access it from other devices on the same network. Ensure to follow security best practices and configure any necessary network settings for secure access.

## Author

- Tristan QUERTON: tristan.querton@edu.ece.fr
