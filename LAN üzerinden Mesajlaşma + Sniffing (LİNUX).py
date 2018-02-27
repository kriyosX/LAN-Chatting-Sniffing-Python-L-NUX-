import socket
import time

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

mesaj+ = "iletilecek mesaj"
mesaj+ ="iletilecek mesaj2"
time.sleep(3) # isterseiz mesajınızı belirli aralıklarla gönderebilirsiniz
mesaj+ = "iletilecek mesaj3"

# isterseniz mesaj sayısını arttırabilirsiniz

ip = "ip adresiniz"
port = mesajlaşacağınız port

s.connect((ip.port)) # Port ve IP bağlanma
s.send(mesaj) #Mesajı Gönderme
