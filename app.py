import telnetlib

port     = 23
HOST     = "192.168.2.254"
user     = "admin"
password = "xxx"

tn = telnetlib.Telnet(HOST)

tn.read_until("Login: ")
tn.write(user + "\n")
if password:
	tn.read_until("Password: ")
	tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print tn.read_all()

