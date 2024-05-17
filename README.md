# Python Modbus TCP Master
This is an implmentation of a Modbus TCP Master in python to connect to svevaral Modbus TCP slaves at teh asme time.
The Implementation uses the Python pyModbusTCP Library. The Implemenation allows to create multiple Modbus Master instances and each can connect to a seperate Modbus TCP slave

## Instructions

### Install the pyModbusTCP Library
```pip install -r requirements.txt```

### Create a Modbus Master Instance
- Each Modbus Master instance is created from the ```Modbus Class``` and connects to a Modbus slave
- When creating an instace, pass the IP address of the slave, the port and slave id
- Configure the desired Modbus Request using the ```modbus_request()``` function

### Run the script
```python modbus_tcp_master.py```


