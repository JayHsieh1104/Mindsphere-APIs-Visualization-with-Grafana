# Flask Server Based on Mindsphere APIs

Working as the backend server, the Flask server will fetch data from Mindshpere RESTful APIs, parse the data, and then send it in JSON format when receiving a request sent from the frontend.

## Table of Contents

- [Flask Server Based on Mindsphere APIs](#flask-server-based-on-mindsphere-apis)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Deployment Steps:](#deployment-steps)
  - [License](#license)

## Installation

This backend server requires [Flask](https://flask.palletsprojects.com/en/1.1.x/), and a cloud platform for running the Flask server.

In this example, the server is deployed to [MindSphere Cloud Foundry](https://developer.mindsphere.io/paas/index.html). It's a platform powered by Cloud Foundry and can be accessed via MindSphere, Siemens's cloud service.

### Deployment Steps:
1. Open Cloud Foundry Command Line Interface (CF CLI)
2. Login Cloud Foundry via CF CLI
    `cf login -a https://api.cf.eu1.mindsphere.io --sso`
3. Received token from the enrolled email account
4. Enter the token received in step(3) on the login website, and then get another token
5. Enter the token received in step(4) on CF CLI and then successfully login CF CLI
6. Change the current path to the folder the python program of the Flask server located at
7. Edit manifest.yml and related config files
8. Use command `cf push` to deploy the Flask server to Cloud Foundry
9. Remember the public URL for Frontend APIs connection

Also, the Flask server can be run under localhost or be deployed to other cloud platforms like [AWS](https://aws.amazon.com/), [Azure](https://azure.microsoft.com/en-us/), and [GCP](https://cloud.google.com/gcp/getting-started).

## License

MIT © 2020 Bing-Jie Hsieh