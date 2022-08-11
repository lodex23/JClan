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
    os.system('clear')
    print("          _   _       __  __       _        ____")
    print(" | \ |'|    U|' \/ '|u U  /'\  u  U|  _'\ u ")
    print("<|  \| |>   \| |\/| |/  \/ _ \/   \| |_) |/ ")
    print("U| |\  |u    | |  | |   / ___ \    |  __/   ")
    print(") |_| \_|     |_|  |_|  /_/   \_\   |_|      ")
    print(" ||   \\,-. <<,-,,-.    \\    >>   ||>>_    ")
    print(" (_')  (_/   (./  \.)  (__)  (__) (__)__) ")
    print("--------------------------------------------------------")
    print("Welcome " + member + " to the automation nmap script")
    print("use this tool for recon on a remote host ")
    print("--------------------------------------------------------")
    print("First of all fill in the target (ip)")
    nmap_target = input("Target>")
    print("[+] Target set to " + nmap_target)
    time.sleep(1)


    def Function_nmap_cmd():
        nmap_cmd = input("nmap>")

        if nmap_cmd == "help":
            print("--------------------------------")
            print("the nmap function works the same as the JClan main page")
            print("Just type 'use' before the module u want to use ")
            print("if u want to see the module list than type 'show modules'")
            print("--------------------------------")
            input("Press enter to continue...")
            Function_nmap_cmd()

        elif nmap_cmd == "show modules":
            print("-------------------------------")
            print("nmap/ip/protocol")
            print("nmap/service/version")
            print("nmap/all/hosts               | very slow|")
            print("nmap/http/enumeration")
            print("nmap/os/detection")
            print("nmap/port/scan")
            print("nmap/vuln/script")
            print("-------------------------------")
            Function_nmap_cmd()
        elif nmap_cmd == "use nmap/ip/protocol":

            ip_protocol = input("nmap/ip/protocol>")
            if ip_protocol == "run":
                os.system('sudo nmap -sO ' + nmap_target)
                Function_nmap_cmd()
            else:
                print("[-] " + ip_protocol + " not found!")
                Function_nmap_cmd()

        elif nmap_cmd == "use nmap/service/version":
            service_version = input("nmap/service/version>")
            if service_version == "run":
                os.system('sudo nmap -sV ' + nmap_target)
                Function_nmap_cmd()
            else:
                print("[-] " + service_version + " not found!")
                Function_nmap_cmd()

        elif nmap_cmd == "use nmap/all/hosts":
            all_hosts = input("nmap/all/hosts>")
            if all_hosts == "run":
                os.system('sudo nmap -sV ' + nmap_target + ' Pn')
                Function_nmap_cmd()
            else:
                print("[-] " + all_hosts + " not found!")
                Function_nmap_cmd()

        elif nmap_cmd == "use nmap/http/enumeration":
            http_enumeration = input("nmap/http/enumeration>")
            if http_enumeration == "run":
                os.system('sudo nmap -sV --script=http-enum ' + nmap_target)
                Function_nmap_cmd()
            else:
                print("[-] " + http_enumeration + " not found!")
                Function_nmap_cmd()

        elif nmap_cmd == "use nmap/os/detection":
            os_detection = input("nmap/os/detection>")
            if os_detection == "run":
                os.system('sudo nmap -o ' + nmap_target)
                Function_nmap_cmd()

            else:
                print("[-] " + os_detection + " not found!")

        elif nmap_cmd == "use nmap/port/scan":
            port_scan = input("nmap/port/scan>")
            if port_scan == "run":
                p1 = input("Port:")
                os.system('sudo nmap -p ' + p1 + " " + nmap_target)
                Function_nmap_cmd()
            else:
                print("[-] " + port_scan + " not found!")

        elif nmap_cmd == "use nmap/vuln/script":
            vuln_script = input("nmap/vuln/script>")
            if vuln_script == "run":
                os.system('sudo nmap --script vuln ' + nmap_target)
                Function_nmap_cmd()
            else:
                print("[-] " + vuln_script + " not found!")
                Function_nmap_cmd()

        elif nmap_cmd == "back":
            Home()

        else:
            print("[-] " + nmap_cmd + " not found!")
            Function_nmap_cmd()





    Function_nmap_cmd()


    os.system('clear')
    Home()





Home()
