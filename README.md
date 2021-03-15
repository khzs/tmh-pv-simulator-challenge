 # TMH PV Simulator Challenge
 
This application generates simulated power values in two parts and uses RabbitMQ to connect them.
*  `meter.py` generates random values simulating a power consumption of a household during 24 hours then sends them to 
   a RabbitMQ queue
*  `simulator.py` generates values based on a photovoltaic power curve and combines them with the household values
   received from the RabbitMQ queue
   
For a more detailed specification see the [original task description](docs/PV Simulator Challenge.pdf).

> The following instructions for setup and execution are tailored towards systems with apt and bash

## Dependencies

RabbitMQ 

> https://rabbitmq.com/install-debian.html#apt-bintray-quick-start

Python 3 and pip
```
sudo apt update
sudo apt install python3-pip -y
pip3 install pika tqdm scipy
```
The software has currently been tested in the following configuration
* Ubuntu Focal
* Python 3.8 
* RabbitMQ 3.8.14

## Execution

```
python3 meter.py && python3 pvsimulator.py
```

The meter process can be followed on the progress bar, then the PV Simulator writes every item to the 
[file output](#File-output) and also the items of each full hour to the console.

PV Simulator will continue to listen for messages until `Crtl + C` is pressed.

### Unit Tests

```
python3 -m unittest tests/*.py -v
```

## File output

The file is named `output.csv`. The last two columns are :
* **Sum**: The sum of the household consumption and the PV simulator values as per requested in the 
  [original task description](docs/PV Simulator Challenge.pdf)
* **Diff**: The difference of the household consumption and the PV simulator values shows how much power the household
  needs to draw from the main power line (if positive) or how much reserve energy is generated from the Photovoltaic
  module (if negative)
