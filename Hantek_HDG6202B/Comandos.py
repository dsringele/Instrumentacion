import pyvisa
rm = pyvisa.ResourceManager()
gen = rm.open_resource('TCPIP0::192.168.0.203::5025::SOCKET', write_termination = '\n',read_termination='\n')
print(gen.query("*IDN?"))
