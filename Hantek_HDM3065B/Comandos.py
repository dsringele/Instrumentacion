import pyvisa
rm = pyvisa.ResourceManager()
mul = rm.open_resource('TCPIP0::192.168.0.203::5025::SOCKET', write_termination = '\n',read_termination='\n')
print(mul.query("*IDN?"))
volt = mul.query("MEAS:VOLT? CH1")