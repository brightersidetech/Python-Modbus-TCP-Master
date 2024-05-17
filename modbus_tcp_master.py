import sys, time
from pyModbusTCP.client import ModbusClient

# Modbus class
class Modbus:
    def __init__(self, host, port, unit_id):
        self.host = host
        self.port = port
        self.unit_id = unit_id
        self.auto_open = False
        self.auto_close = False
        self.running = False
        self.response = None
        self.modbus_master = None

    # Connection to modbus TCP slave
    def modbus_connect(self):
        if not self.modbus_master:
            print("Connecting to Modbus Server...", self.host, self.port)
            self.modbus_master = ModbusClient(host=self.host, port=self.port, unit_id=self.unit_id,
                                              auto_open=self.auto_open, auto_close=self.auto_close)
            if self.modbus_master.open():
                print("Connected to Modbus Server at: ", self.host)
                self.running = True
            else:
                print("Connection to Modbus Server at :", self.host, " Failed!")
                self.modbus_master = None

    # Disconnect from Modbus TCP slave
    def disconnect(self):
        if self.running:
            print("Closing Modbus Server Connection at ", self.host)
            self.running = False
            self.modbus_master.close()
            self.modbus_master = None

    # Send Modbus request (Read or write registers)
    def modbus_request(self, start_address=0, no_registers=5, function_code=3, data=[]):
        if self.modbus_master:
            # Choose function code based on function code, send request
            if function_code == 1:
                self.response = self.modbus_master.read_coils(start_address, no_registers)
            elif function_code == 3:
                self.response = self.modbus_master.read_holding_registers(start_address, no_registers)
            elif function_code == 2:
                self.response = self.modbus_master.read_discrete_inputs(start_address, no_registers)
            elif function_code == 4:
                self.response = self.modbus_master.read_input_registers(start_address, no_registers)
            elif function_code == 5:
                self.response = self.modbus_master.write_single_coil(start_address, data[0])
            elif function_code == 6:
                self.response = self.modbus_master.write_single_register(start_address, data[0])
            elif function_code == 15:
                self.response = self.modbus_master.write_multiple_coils(start_address, data)
            elif function_code == 10:
                self.response = self.modbus_master.write_multiple_registers(start_address, data)

            # Check response
            if self.response:
                print("Modbus response: ", self.response)
                if function_code == "Read Coils (0x01)" or function_code == "Read Discrete Inputs (0x02)":
                    self.response = [int(self.response[i])  for i in range(0, len(self.response)) ]
            else:
                print("read error")

        return self.response
    
if __name__ == '__main__':
    # Create first Modbus Master instance and connect to first server
    server_1 = Modbus('127.0.0.1', 502, 1)
    server_1.modbus_connect()

    # Create second Modbus Master instance and connect to second server
    server_2 = Modbus('127.0.0.1', 503, 1)
    server_2.modbus_connect()

    while True:
        # Send request to server 1
        reponse_1 = server_1.modbus_request()
        print(reponse_1)

        # Send request to server 2
        reponse_2 = server_2.modbus_request()
        print(reponse_2)
    
        time.sleep(2)
