# Mindsphere APIs Visualization with Grafana

This project aims to fetch data from Siemens's Mindsphere RESTful APIs and then visualize it with Grafana.

In the project, Grafana is used as the frontend for data visualization. It will send a request to the Flask server, parse the returned JSON object and then draw a statistical diagram on the assigned dashboard.

On the backend side, A Flask server is responsible for fetching data from Mindshpere RESTful APIs, parsing the data, and responding in JSON format when receiving requests sent from the frontend.

## Table of Contents

- [Mindsphere APIs Visualization with Grafana](#mindsphere-apis-visualization-with-grafana)
  - [Table of Contents](#table-of-contents)
  - [System Architecture](#system-architecture)
  - [Installation](#installation)
  - [Example Results](#example-results)
  - [License](#license)

## System Architecture

![](https://i.imgur.com/e5uM2Wp.png)

## Installation

Please refer to the README files under the Frontend and Backend folders.

## Example Results

* A highly interactive interface displaying the time series data fetched from Siemens's MindSphere APIs; the source of APIs data can be customers' devices.
* Provide customers a clear and user-friendly monitor system; easily supervisor the target value with an assigned period.

![](https://i.imgur.com/cD7YoxQ.png)

![](https://i.imgur.com/DJK0Ecu.png)

## License

MIT © 2020 Bing-Jie Hsieh
