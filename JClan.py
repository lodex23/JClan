import os
import time

os.system('clear')
#Intro JClan Banner
print("                                                             8 8888     ,o888888o.    8 8888                  .8.          b.             8")
time.sleep(.1)
print("                                                             8 8888    8888     `88.  8 8888                 .888.         888o.          8")
time.sleep(.1)
print("                                                             8 8888 ,8 8888       `8. 8 8888                :88888.        Y88888o.       8")
time.sleep(.1)
print("                                                             8 8888 88 8888           8 8888               . `88888.       .`Y888888o.    8")
time.sleep(.1)
print("                                                             8 8888 88 8888           8 8888              .8. `88888.      8o. `Y888888o. 8")
time.sleep(.1)
print("                                                             8 8888 88 8888           8 8888             .8`8. `88888.     8`Y8o. `Y88888o8")
time.sleep(.1)
print("                                                  88.        8 8888 88 8888           8 8888            .8' `8. `88888.    8   `Y8o. `Y8888")
time.sleep(.1)
print("                                                  `88.       8 888' `8 8888       .8' 8 8888           .8'   `8. `88888.   8      `Y8o. `Y8")
time.sleep(.1)
print("                                                    `88o.    8 88'     8888     ,88'  8 8888          .888888888. `88888.  8         `Y8o.`")
time.sleep(.1)
print("                                                      `Y888888 '        `8888888P'    8 888888888888 .8'       `8. `88888. 8            `Yo")
time.sleep(1)

#Welcome text
print("                                             --------------------------------------------------------------------------------------------------------")
print("                                                                                 Greetings my JClan Members")
print("                                                                            I'M Happy to present u the JClan Tool")
print("                                                           This Tool will help u get started Beeing usefull in our Secret Society :)")
print("                                             --------------------------------------------------------------------------------------------------------")

input("                                                                                 Press enter to continue...")
os.system('clear')


member = "Jeffrey"




#Main Page
def Home():
        cmd_home = input(member + ">")


        if cmd_home == "help":
            print("if u want to use a tool inside JClan than u simply type 'use + toolname'")
            print("------------------------------------------------------------------------")
            print("tor                          |   Turn on the tor service")
            print("ping                         |   Ping a target")
            print("nmap                         |   Gather information about IP")
            print("clear                        |   Clear's the terminal (no need to type 'use')")
            print("exit")
            print("------------------------------------------------------------------------")
            print("")
            Home()

        elif cmd_home == "use tor":
            Tor_Service()

        elif cmd_home == "use ping":
            Ping()

        elif cmd_home == "use nmap":
            nmap()

        elif cmd_home == "clear":
            os.system('clear')
            Home()

        elif cmd_home == "exit":
            exit()


        else:
            print(cmd_home + " Is not found")
            Home()




#Tor service Function
def Tor_Service():
    os.system('service tor start')
    Home()

#Ping Function
def Ping():
    os.system('clear')
    Ping_target = input("Target>")
    os.system("ping " + Ping_target + " -c 5")
    input("Press enter to go back")
    os.system('clear')
    Home()


#Nmap Function
def nmap():
    print("Comming soon....")
    input("Press enter to go back")
    os.system('clear')
    Home()





Home()
