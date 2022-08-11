import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 4444))
print("Listening on port 4444")
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection whit {address} Succesfull")
    time.sleep

    def msg_func():
        try:
            print("send a message to the JClan Chatroom (Make sure u encrypt the message!!!)")
            msg = input("msg>")
            if msg == "exit":
                exit()
            else:
                clientsocket.send(bytes("----------------------------------------------------------------", "utf-8"))
                time.sleep(.5)
                clientsocket.send(bytes("Welcome to the JClan Taskbar!", "utf-8"))
                time.sleep(.5)
                clientsocket.send(bytes("Here u will see daily or weekly tasks That helps our secret society to grow", "utf-8"))
                time.sleep(.5)
                clientsocket.send(bytes("-------------------------------------------------------------------------------------", "utf-8"))
                time.sleep(.5)
                clientsocket.send(bytes("How to Submit a Task?", "utf-8"))
                time.sleep(.2)
                clientsocket.send(bytes("-------------------------", "utf-8"))
                time.sleep(.5)
                clientsocket.send(bytes("STEP1> Make a folder providing all the documents/Infromation that is asked!", "utf-8"))
                time.sleep(1)
                clientsocket.send(bytes("", "utf-8"))
                clientsocket.send(bytes("STEP2> Compress the folder into a zip file", "utf-8"))
                time.sleep(.1)
                clientsocket.send(bytes("", "utf-8"))
                clientsocket.send(bytes("STEP3> Connect to our ftp server and upload the zip file there (make sure your Member ID is mentioned in the file name!!!)", "utf-8"))
                time.sleep(.5)
                clientsocket.send(bytes("-------------------------", "utf-8"))
                print("Message send!")
                time.sleep(2)

                return msg_func()
        except:
            print("Message could not send!!")
            return msg_func()

    msg_func()
