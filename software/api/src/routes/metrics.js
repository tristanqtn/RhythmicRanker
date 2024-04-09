const express = require("express");
const path = require("path");
const dotenv = require("dotenv");

const { InfluxDB, Point } = require("@influxdata/influxdb-client");
const metrics = express.Router();

const envPath = path.resolve(__dirname, "..", "..", "..", ".env");
dotenv.config({ path: envPath });

const { INFLUX_URL, INFLUX_TOKEN, INFLUX_ORG, INFLUX_BUCKET } = process.env;

const influxDB = new InfluxDB({
  url: INFLUX_URL,
  token: INFLUX_TOKEN,
});

const writeApi = influxDB.getWriteApi(INFLUX_ORG, INFLUX_BUCKET);
const queryApi = influxDB.getQueryApi(INFLUX_ORG);

process.on("exit", () => {
  console.log("Closing InfluxDB write API.");
  writeApi.close();
});

metrics
  /**
   * This function handles POST requests for the metric API.
   * @route POST /metrics
   * @group METRICS - Methods for the metric API
   * @param {string} user.body.required - JSON measurement
   * measurement: {
   * "sensor": "height",
   * "measurement": 12
   * }
   * @returns {object} 200 succes - Metric has been added to the INFLUX
   * @returns {Error}  400 error - insertion failed
   */
  .post("/", (req, resp) => {
    console.log(`Received: ${JSON.stringify(req.body)}`);
    const point1 = new Point(req.body.sensor).intField(
      "measurement",
      req.body.measurement
    );
    //console.log(`${point1}`);
    writeApi.writePoint(point1);
    let respObj = {
      msg: `${point1}`,
    };
    resp.status(200).json(respObj);
    writeApi.flush(); // Add this line to force a synchronous write
  })

  /**
   * This function handles GET requests for the metric API.
   * @route GET /metrics
   * @group METRICS - Methods for the metric API
   * @returns {object} 200 succes - Returns an array containing all metrics
   * @returns {Error}  400 error - Problem occurs while reading Influx
   */
  .get("/", (req, resp) => {
    let myArray = [];
    const query = `from(bucket: "${INFLUX_BUCKET}") |> range(start: -1h)`;
    queryApi.queryRows(query, {
      next(row, tableMeta) {
        const o = tableMeta.toObject(row);
        myArray.push(o);
      },
      error(error) {
        console.error(error);
        //console.log("\nFinished ERROR");
      },
      complete() {
        //console.log("\nFinished SUCCESS");
        // Sort the array by _time in increasing order and _field in alphabetical order
        myArray.sort((a, b) => {
          // Assuming _time is a string representing date/time
          const timeComparison = new Date(a._time) - new Date(b._time);

          // Assuming _field is a string
          const fieldComparison = a._field.localeCompare(b._field);

          // If timeComparison is non-zero, use it; otherwise, use fieldComparison
          return timeComparison !== 0 ? timeComparison : fieldComparison;
        });
        let respObj = {
          status: "OK",
          count: myArray.length,
          content: myArray,
        };
        resp.status(200).json(respObj);
      },
    });
  });

module.exports = metrics;
