import pyvisa
rm = pyvisa.ResourceManager()
osc = rm.open_resource('TCPIP0::192.168.0.204::5025::SOCKET', write_termination = '\n',read_termination='\n')
print(osc.query("*IDN?"))
