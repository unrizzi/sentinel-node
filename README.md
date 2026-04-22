# SentinelNode

SentinelNode is a network security monitoring tool developed in Python. It identifies active TCP connections and classifies them based on known malicious signatures and behavioral persistence patterns to detect potential threats such as cryptominers and botnets.

## Features

* Active network connection monitoring.
* Port-based threat identification.
* Traffic filtering for trusted services.
* Behavioral analysis for persistent connections.
* Automated Discord notifications.
* Persistent system logging.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/unrizzi/sentinel-node.git
cd sentinel-node
```

2. Create a .env file in the root directory. This file must contain your Discord Webhook URL to enable remote alerting:

```
DISCORD_WEBHOOK_URL=your_webhook_url_here
```

## Setup and Execution

### Windows Environment

The project includes a batch script to automate the environment configuration and execution. Run the following file:

```
start.bat
```

This script handles the creation of the virtual environment, dependency installation via ```requirements.txt```, and the initialization of the monitoring loop.

### Manual Execution

To run the application manually, ensure Python 3 is installed and follow these steps:
1. Initialize a virtual environment: ```python -m venv venv```
2. Activate the environment: ```venv\Scripts\activate```
3. Install dependencies: ```pip install -r requirements.txt```
4. Execute the main script: ```python main.py```