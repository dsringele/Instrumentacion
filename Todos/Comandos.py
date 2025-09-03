import pyvisa
rm = pyvisa.ResourceManager()

fue = rm.open_resource('TCPIP0::192.168.0.200::5025::SOCKET', write_termination = '\n',read_termination='\n')
mul = rm.open_resource('TCPIP0::192.168.0.201::5025::SOCKET', write_termination = '\n',read_termination='\n')
lcr = rm.open_resource('TCPIP0::192.168.0.202::4321::SOCKET', write_termination = '\n',read_termination='\n')
gen = rm.open_resource('TCPIP0::192.168.0.203::5025::SOCKET', write_termination = '\n',read_termination='\n')
osc = rm.open_resource('TCPIP0::192.168.0.204::5025::SOCKET', write_termination = '\n',read_termination='\n')

print(fue.query("*IDN?"))
print(mul.query("*IDN?"))
print(lcr.query("*IDN?"))
print(gen.query("*IDN?"))
print(osc.query("*IDN?"))
