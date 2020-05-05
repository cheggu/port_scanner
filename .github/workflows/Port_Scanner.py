
import socket, sys, os, time

#Main menu
def Main():
    while True:
        print("----------------------------------------------")
        print("""    0:     Exit
    1:     Scan range
    2:     Scan common ports
    3:     Scan specific port
    4:     Scan specific MULTIPLE ports
    5:     Scan ports from config file""")
        print("----------------------------------------------")

        ipt_menu = input("-> ")
        if ipt_menu == "0":
            break

        elif ipt_menu == "1":
            RHOST = input("Target IP:\n")
            RPORT_low = input("Port Low Range:")
            RPORT_high = input("Port High Range:")

            Scan_Range(RHOST, int(RPORT_low), int(int(RPORT_high) + 1))

        elif ipt_menu == "2":
            RHOST = input("Target IP:\n")
            ipt_common = input("Scan thorougly (around 100 ports) or quick scan (around 10)?\nEnter 'all' for thorough scan or 'quick' for quick scan.\n")
            if ipt_common == "all":
                Scan_Common_Large(RHOST)
            elif ipt_common == "quick":
                Scan_Common_Small(RHOST)
            else:
                print("Invalid input, returning to menu...\n")

        elif ipt_menu == "3":
            RHOST = input("Target IP:\n")
            RPORT = input("Target Port:\n")
        
            Scan_Specific(RHOST,RPORT)

        elif ipt_menu == "4":
            RHOST = input("Target IP:\n")
            RPORTS = []
            print("Enter 'stop' to stop listing ports")
            while True:
                ipt_ports = input("Enter port: ")
                if ipt_ports == "stop":
                    break
                else: 
                    RPORTS.append(ipt_ports)

            Scan_Specifics(RHOST,RPORTS)

        elif ipt_menu == "5":
            RHOST = input("Target IP:\n")
            
            Scan_Config(RHOST)

        else:
            print("Invalid input")

#setting some variables for global use and logo
def Bootstrap():
    global DIR
    DIR = os.getcwd()

    try:
        config = open(file="config.txt",mode='r')
        print("Config file loaded...\n")
    except:
        print("Config file not found...")
        print("Creating new config file at " + DIR + "\config.txt...\n")
        config = open(file="config.txt",mode='w')
    config.close()

    os.system('COLOR 4')
    print("E Z   P O R T   S C A N N E R\nby chegger#1337") 
    

#Scans a user-defined ports on a target ip address
def Scan_Range(target, low, high):
    #defining variables
    lst_success = []
    

    #sock
    for i in range(int(low), int(high)):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            start = time.perf_counter()
            sock.connect((target, i))
            print("SUCCESS at port", str(i))
            print("Response time:", "{:.0f}".format(((time.perf_counter()-start)*1000)), "MS")
            lst_success.append(i)
            sock.close()
        except:
            print("FAIL at port", str(i))
            sock.close()

    #success/fail logic and exporting to txt
    if len(lst_success) < 1:
        print("No open ports found.")
    else:
        print("Success at ports:")
        for item in lst_success:
            print(item)
        while True:
            ipt_export_ports = input("Would you like to export the ports to a txt document? (y/n):\n")
            if ipt_export_ports == "y":
                fil = open("ports.txt", mode='w')
                fil.writelines(("OPEN PORTS FOR IP ADDRESS '" + target + "':\n\n"))
                for item in lst_success:
                    fil.writelines(str(item))
                print("File written to " + DIR + "\ports.txt")
                fil.close()
                break
            elif ipt_export_ports == "n":
                print("User chose not to export, returning to main menu...")
                break
            else:
                print("Invalid input!")

#Scans a large list of common ports on a target ip address
def Scan_Common_Large(target):
    #defining variables
    
    lst_success = []
    lst_common_large = [1,5,7,9,11,13,17,18,19,20,21,22,23,25,37,39,42,43,49,
                  50,53,63,67,68,69,70,71,72,73,79,80,88,95,101,102,105,
                  107,109,110,111,113,115,117,119,123,137,138,139,143,161,
                  162,163,164,174,177,178,179,191,194,199,201,202,204,206,
                  209,210,213,220,245,347,363,369,370,372,389,427,434,435,
                  443,444,445,464,468,487,488,496,500,535,538,546,547,554,
                  563,565,587,610,611,612,631,636,674,694,749,750,765,767,
                  873,992,993,994,995]

    #sock
    for item in lst_common_large:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            start = time.perf_counter()
            sock.connect((target, item))
            print("SUCCESS at port", item)
            print("Response time:", "{:.0f}".format(((time.perf_counter()-start)*1000)), "MS")
            lst_success.append(item)
            sock.close()
        except:
            print("FAIL at port", item)
            sock.close()

    #success/fail logic and exporting to txt    
    if len(lst_success) < 1:
        print("No open ports found.")
    else:
        print("Success at ports:")
        for item in lst_success:
            print(item)
        while True:
            ipt_export_ports = input("Would you like to export the ports to a txt document? (y/n):\n")
            if ipt_export_ports == "y":
                fil = open("ports.txt", mode='w')
                fil.writelines(("OPEN PORTS FOR IP ADDRESS '" + target + "':\n\n"))
                for item in lst_success:
                    fil.writelines(str(item) + "\n")
                print("File written to " + DIR + "\ports.txt")
                fil.close()
                break
            elif ipt_export_ports == "n":
                print("User chose not to export, returning to main menu...")
                break
            else:
                print("Invalid input!")      

#Scans a small list of common ports on a target ip address                
def Scan_Common_Small(target):
    #defining variables
    
    lst_success = []
    lst_common_small = [21,22,23,25,80,110,143,443,445,3389]

    #sock
    for item in lst_common_small:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            start = time.perf_counter()
            sock.connect((target, item))
            print("SUCCESS at port", item)
            print("Response time:", "{:.0f}".format(((time.perf_counter()-start)*1000)), "MS")
            lst_success.append(item)
            sock.close()
        except:
            print("FAIL at port", item)
            sock.close()

    #success/fail logic and exporting to txt    
    if len(lst_success) < 1:
        print("No open ports found.")
    else:
        print("Success at ports:")
        for item in lst_success:
            print(item)
        while True:
            ipt_export_ports = input("Would you like to export the ports to a txt document? (y/n):\n")
            if ipt_export_ports == "y":
                fil = open("ports.txt", mode='w')
                fil.writelines(("OPEN PORTS FOR IP ADDRESS '" + target + "':\n\n"))
                for item in lst_success:
                    fil.writelines(str(item) + "\n")
                print("File written to " + DIR + "\ports.txt")
                fil.close()
                break
            elif ipt_export_ports == "n":
                print("User chose not to export, returning to main menu...")
                break
            else:
                print("Invalid input!")      

#Scans user-defined port on a target ip address
def Scan_Specific(target, port):   
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        start = time.perf_counter()
        sock.connect((target,int(port)))
        print("SUCCESS... Port " + port + " IS open.")
        print("Response time:", "{:.0f}".format(((time.perf_counter()-start)*1000)), "MS")
        sock.close()
    except:
        print("FAIL... Port " + port + " is NOT open.")
        sock.close()

#Scans user-defined ports on a target ip address    
def Scan_Specifics(target,ports):
    lst_success = []

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            start = time.perf_counter()
            sock.connect((target,int(port)))
            print("SUCCESS... Port " + port + " IS open.")
            print("Response time:", "{:.0f}".format(((time.perf_counter()-start)*1000)), "MS")
            lst_success.append(port)
            sock.close()
        except:
            print("FAIL... Port " + port + " is NOT open.")
            sock.close()
    
    #success/fail logic and exporting to txt   
    if len(lst_success) < 1:
        print("No open ports found.")
    else:
        print("Success at ports:")
        for item in lst_success:
            print(item)
        while True:
            ipt_export_ports = input("Would you like to export the ports to a txt document? (y/n):\n")
            if ipt_export_ports == "y":
                fil = open("ports.txt", mode='w')
                fil.writelines(("OPEN PORTS FOR IP ADDRESS '" + target + "':\n\n"))
                for item in lst_success:
                    fil.writelines(str(item) + "\n")
                print("File written to " + DIR + "\ports.txt")
                fil.close()
                break
            elif ipt_export_ports == "n":
                print("User chose not to export, returning to main menu...")
                break
            else:
                print("Invalid input!")    

#Scan config file of ports
def Scan_Config(target):
    lst_success = []
    config = open(file="config.txt",mode='r')
    lst_config = config.readlines()
    config.close()
    if len(lst_config) > 0:
        for port in lst_config:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                start = time.perf_counter()
                sock.connect((target,int(port)))
                print("SUCCESS... Port " + port + " IS open.")
                print("Response time:", "{:.0f}".format(((time.perf_counter()-start)*1000)), "MS")
                lst_success.append(port)
                sock.close()
            except:
                print("FAIL... Port " + str(int(port)) + " is NOT open.")
                sock.close()
    
        #success/fail logic and exporting to txt   
        if len(lst_success) < 1:
            print("No open ports found.")
        else:
            print("Success at ports:")
            for item in lst_success:
                print(item)
            while True:
                ipt_export_ports = input("Would you like to export the ports to a txt document? (y/n):\n")
                if ipt_export_ports == "y":
                    fil = open("ports.txt", mode='w')
                    fil.writelines(("OPEN PORTS FOR IP ADDRESS '" + target + "':\n\n"))
                    for item in lst_success:
                        fil.writelines(str(item) + "\n")
                    print("File written to " + DIR + "\ports.txt")
                    fil.close()
                    break
                elif ipt_export_ports == "n":
                    print("User chose not to export, returning to main menu...")
                    break
                else:
                    print("Invalid input!") 
    else:
         print("No ports found in config.txt...")
         print("Returning to menu...")

Bootstrap()
Main()
