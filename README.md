# Mindsphere-APIs-Visualization-with-Grafana

This project amis to fetch data from Siemens's Mindsphere RESTful APIs and then visualize it with Grafana.

In the project, Flask server works as the backend server. It will fetch data from Mindshpere RESTful APIs, parse the data, and then send it in JSON format when receiving request sent from frontend.

On the other side, Grafana is used as the frontend for data visualization. It will send request to the Flask server, parse the returned JSON object and then draw statistical diagram on the assigned dashboard.

## Table of Contents

- [Mindsphere-APIs-Visualization-with-Grafana](#mindsphere-apis-visualization-with-grafana)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Usage](#usage)
  - [License](#license)

## Install

This project requires [Flask](https://flask.palletsprojects.com/en/1.1.x/), [Grafana](https://grafana.com/), and [Docker](https://www.docker.com/).

In this project, I run my Flask server on Google [Cloud Platform](https://cloud.google.com/gcp/getting-started) and install Grafana in docker container. You can also install them under localhost or on cloud platform like AWS, Azure, and GCP.

Lauch docker container with simple JSON plugin

```sh
docker run -d -p 3000:3000 --name=grafana -e 'GF_INSTALL_PLUGINS=grafana-simple-json-datasource' grafana/grafana
```

## Usage

After installing Grafana with simple JSON plugin, you need to set the URL of your RESTful APIs server as the datasoruce of the dashboard.

1. Click **Configuration** -> **Datasource** -> **Add data source** -> **SimpleJson**(under Others)

2. Add the URL of your RESTful APIs server and then click **Save & Test**
![](https://i.imgur.com/1flzTRt.png)

3. Create a new dashboard and add a new panel

4. Select the target metric
![](https://i.imgur.com/VQG9EGb.png)

5. Get the updated panel
![](https://i.imgur.com/DJK0Ecu.png)

## License

MIT © 2020 Bing-Jie Hsieh