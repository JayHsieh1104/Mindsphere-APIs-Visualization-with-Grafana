# Grafana Installation and APIs Connection

Used as the frontend for data visualization, Grafana will send requests to the Flask server, parse the returned JSON object, and then draw statistical diagrams on the assigned dashboard.

Here we will introduce How to install Grafana and display retrieved API data.

## Table of Contents

- [Grafana Installation and APIs Connection](#grafana-installation-and-apis-connection)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [APIs Connection](#apis-connection)
  - [License](#license)

## Installation

In the project, we need [Grafana](https://grafana.com/) and [Grafana SimpleJson Datasource Plugin](https://grafana.com/grafana/plugins/grafana-simple-json-datasource), and [Docker](https://www.docker.com/).

We will install docker and run Grafana with Grafana Simple JSON plugin in a docker container.

1. Visit [Docker Official Website](https://www.docker.com/) for the docker installation tutorial
2. Open a terminal and lauch docker container with simple JSON plugin
    ```sh 
    docker run -d -p 3000:3000 --name=grafana -e 'GF_INSTALL_PLUGINS=grafana-simple-json-datasource' grafana/grafana
    ```

## APIs Connection

After installing Grafana with simple JSON plugin, you need to set the URL of your RESTful APIs server as the data soruce of the Grafana dashboard.

1. Click **Configuration** -> **Datasource** -> **Add data source** -> **SimpleJson**

2. Add the URL of your Flask server (or a RESTful APIs server) and then click **Save & Test**
![](https://i.imgur.com/1flzTRt.png)

3. Create a new dashboard and add a new panel

4. Select a target metric
![](https://i.imgur.com/VQG9EGb.png)

5. Get the information panel of the selected metric.
![](https://i.imgur.com/DJK0Ecu.png)

## License

MIT © 2020 Bing-Jie Hsieh