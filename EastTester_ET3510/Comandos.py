import pyvisa
rm = pyvisa.ResourceManager()
lcr = rm.open_resource('TCPIP0::192.168.0.123::4321::SOCKET', write_termination = '\n',read_termination='\n')
print(lcr.query("*IDN?"))
