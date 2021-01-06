import  socket  as so
import  threading  as th
import  time  as  tm
import  sys

protocol = so.SOCK_DGRAM
addFamilyName = so.AF_INET

s = so.socket(addFamilyName,protocol)

def  receiver(WinIp,WinPort):

        s.bind((WinIp,WinPort))

        while True:
                data=s.recvfrom(4000)
                clientIP=data[1][0]
                receivedData=data[0].decode()
                print("\n\nReceived msg:  "+receivedData+"\n")
                tm.sleep(1.0)


def  sender(LinIp,LinPort):

        while True:
                data=input("\nEnter msg you want to send:  ")
                print("Sended msg: "+data)
                data=data.encode()
                s.sendto(data,(LinIp,LinPort))
                tm.sleep(1.0)


LinIp=input("\nEnter Linux Server IP:  ")
LinPort=int(input("\nEnter Linux Port: "))

WinIp=input("\nEnter Windows Server IP:  ")
WinPort=int(input("\nEnter Widows Port: "))


t1 = th.Thread(target=receiver,args=(WinIp,WinPort))
t2 = th.Thread(target=sender,args=(LinIp,LinPort))

t1.start()
t2.start()

