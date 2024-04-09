const express = require("express");
const metrics = require("./routes/metrics");
const healthRouter = require("./routes/health");
const data_stream = require("./routes/stream");
const bodyParser = require("body-parser");
const path = require("path");
const dotenv = require("dotenv");

const envPath = path.resolve(__dirname, "..", "..", ".env");
dotenv.config({ path: envPath });

const port = process.env.INTERNAL_INPUT_API_PORT;
const IP = process.env.INTERNAL_INPUT_API_IP;

let options = {
  swaggerDefinition: {
    info: {
      description: "Data Input API Endpoint",
      title: "Swagger",
      version: "1.0.0",
    },
    host: `${IP}:${port}`,
    basePath: "/",
    produces: ["application/json"],
    consumes: ["application/json"],
    schemes: ["http"],
  },
  basedir: __dirname, //app absolute path
  files: ["./routes/*.js"], //Path to the API handle folder
};

const app = express();

const expressSwagger = require("express-swagger-generator")(app);
expressSwagger(options);

app.use(
  bodyParser.urlencoded({
    extended: false,
  })
);
app.use(bodyParser.json());

app.get("/", (req, res) => res.sendFile(path.join(__dirname, "/index.html")));

app.use("/health", healthRouter);
app.use("/metrics", metrics);
app.use("/stream", data_stream);

const server = app.listen(port, IP, (err) => {
  if (err) throw err;
  console.log(`Server listening the port: http://${IP}:${port}`);
});

module.exports = server;
