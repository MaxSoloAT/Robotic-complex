import socket
print("Import soket OK!")
import serial
print("Import serial OK!")
import glob
print("Import glob OK!")

def Password_check():
        if Data_pass!='pass':
                conn.close()
        else: print("Password OK!")

def scan():
        return glob.glob('/dev/ttyS*')+glob.glob('/dev/ttyUSB*')+glob.glob('/de$

print("Wait setup serial port")

if __name__ == '__main__':
        print ("Found port")
        for name in scan():
                print name
                Arduino_adr=name
                ard_ser=serial.Serial(Arduino_adr,9600)
print("Serial port setup OK!")

server_UP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket up OK!")

server_UP.bind(('192.168.43.185',8089))
print("Socket bind OK!")

server_UP.listen(1)
print("Listen OK!")
conn,adr=server_UP.accept()
print("Accept OK!")
Data_pass=conn.recv(128)
if len(Data_pass)>0:
        Password_check()

while (1):
        Data=conn.recv(128)
        if len(Data)>0:
                #print(Data)
                ard_ser.write(Data)

