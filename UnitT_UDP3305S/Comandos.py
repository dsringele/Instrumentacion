import pyvisa
rm = pyvisa.ResourceManager()
fue = rm.open_resource('TCPIP0::192.168.0.200::5025::SOCKET', write_termination = '\n',read_termination='\n')
print(fue.query("*IDN?"))
volt = fue.query("MEAS:VOLT? CH1")
curr = fue.query("MEAS:CURR? CH1")

fue.write("APPL CH1,5.0,1.0")
fue.write("OUTP CH1,ON")
fue.write("OUTP CH1,OFF")