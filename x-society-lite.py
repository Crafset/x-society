import os
import time
from colorama import init, Fore
import geocoder
import requests
from bs4 import BeautifulSoup
import socket
import threading
import psutil
import random
import string
import pywifi
from pywifi import const

#-- SYSTEM
os.system('clear')


#-- HACKING TEXT
texte = Fore.GREEN,"X-SOCIETY :\n"
for caractere in texte:
    print(caractere, end='', flush=True)
    time.sleep(0.1)  

print()

#-- HELP TEXT
texte2 = """> Type 'help' to get list of commands."""
for caractere in texte2:
    print(caractere, end='', flush=True)
    time.sleep(0.01)  

print()

#-- CHOICE
while True :
    choice = input("> ")

    #-- HELP
    if choice == "help":
        texte5 = """    Type :
    -help
    -phone
    -ip
    -sherlock
    -wifi
    -blackout
    -clear
    -restart
    -exit\n"""
        for caractere in texte5:
            print(caractere, end='', flush=True)
            time.sleep(0.01)     

    #-- PHONE HELP    
    elif choice == "phone help":
        texte6 = "    -locate\n"
        for caractere in texte6:
            print(caractere, end='', flush=True)
            time.sleep(0.01) 
    #-- PHONE LOCATE  
    elif choice == "phone locate":
        print("soon...\n")   


    #-- IP HELP    
    elif choice == "ip help":
        texte7 = """    -locate\n"""
        for caractere in texte7:
            print(caractere, end='', flush=True)
            time.sleep(0.01) 

    #-- IP LOCATE
    elif choice == "ip locate":
        def localiser_ip(ip):
                g = geocoder.ip(ip)     
                if g.ok:
                    texte11 = f"    -Country   : {g.country}\n"
                    for caractere in texte11:
                        print(caractere, end='', flush=True)
                        time.sleep(0.01)
                    texte12 = f"    -City      : {g.city}\n"
                    for caractere in texte12:
                        print(caractere, end='', flush=True)
                        time.sleep(0.01)
                    texte13 = f"    -Latitude  : {g.lat}\n"
                    for caractere in texte13:
                        print(caractere, end='', flush=True)
                        time.sleep(0.01)
                    texte14 = f"    -Longitude : {g.lng}\n"
                    for caractere in texte14:
                        print(caractere, end='', flush=True)
                        time.sleep(0.01)
                else:
                    texte15 = "IP not found.\n"
                    for caractere in texte15:
                        print(caractere, end='', flush=True)
                        time.sleep(0.01)

        adresse_ip = input("ip> ")
        localiser_ip(adresse_ip)



    #-- SHERLOCK HELP    
    elif choice == "sherlock help":
        texte8 = "    -search\n"
        for caractere in texte8:
            print(caractere, end='', flush=True)
            time.sleep(0.01)

    #-- SHERLOCK SEARCH
    elif choice == "sherlock search":
        def search_name_on_web(name):
            query = f'"{name}"'
            url = f"https://www.google.com/search?q={query}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.select('.tF2Cxc')
            for result in search_results:
                link = result.a['href']
                texte16 = f"         -{link}\n"
                for caractere in texte16:
                    print(caractere, end='', flush=True)
                    time.sleep(0.01)
        full_name = input("Name> ")
        search_name_on_web(full_name)
     

    #-- ALARM HELP    
    elif choice == "alarm help":
        texte9 = """    -disable\n"""
        for caractere in texte9:
            print(caractere, end='', flush=True)
            time.sleep(0.01)

    #-- ALARM DISABLE    
    elif choice == "alarm disable":
        print("You are not connected to any network\n") 


    #-- BLACKOUT HELP  
    elif choice == "blackout help":
        texte10 = "    -start\n"
        for caractere in texte10:
            print(caractere, end='', flush=True)
            time.sleep(0.01)

    #-- BLACKOUT START
    elif choice == "blackout start":
        print("soon...")


    #-- WIFI
    elif choice == "wifi help":
        texte23 = "    -show ip\n"
        for caractere in texte23:
            print(caractere, end='', flush=True)
            time.sleep(0.01)
        texte28 = "    -show network\n"
        for caractere in texte28:
            print(caractere, end='', flush=True)
            time.sleep(0.01)
        texte29 = "    -bruteforce\n"
        for caractere in texte29:
            print(caractere, end='', flush=True)
            time.sleep(0.01)  

    #-- WIFI SHOW IP   
    elif choice == "wifi show ip":
        def get_hostname(ip):
            try:
                hostname = socket.gethostbyaddr(ip)[0]
                return hostname
            except socket.herror:
                return "NONE"
        def scan_wifi_network():
            active_ips = []
            interfaces = psutil.net_if_addrs()
            for interface_name, interface_addresses in interfaces.items():
                for address in interface_addresses:
                    if address.family == socket.AF_INET and not address.address.startswith("127."):
                        ip = address.address
                        hostname = get_hostname(ip)
                        active_ips.append((ip, hostname))
            return active_ips
        active_ips = scan_wifi_network()
        texte24 = "> Active IP addresses : \n"
        for caractere in texte24:
            print(caractere, end='', flush=True)
            time.sleep(0.01)
        for ip, hostname in active_ips:
            texte25 = f"    -{ip} {hostname}\n"
            for caractere in texte25:
                print(caractere, end='', flush=True)
                time.sleep(0.01)

    #-- WIFI SHOW NETWORK
    elif choice == "wifi show network":
        texte30 = "> Active network :\n"
        for caractere in texte30:
                print(caractere, end='', flush=True)
                time.sleep(0.01)
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        if iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
            iface.disconnect()
            iface.activate()
        iface.scan()
        results = iface.scan_results()
        for result in results:
            texte31 = f"                 {result.ssid}\n"
            for caractere in texte31:
                print(caractere, end='', flush=True)
                time.sleep(0.01)


    #-- WIFI BRUTEFORCE
    elif choice == "wifi bruteforce":
        wifi = pywifi.PyWiFi()
        adapter = wifi.interfaces()[0]
        ssid = input('Name> ')
        characters = string.ascii_letters + string.digits
        password = ''.join(random.sample(characters, 22))
        def print_same_line(text):
            print(text, end='\r')
        connected = False
        while not connected:
            print_same_line(f"                                              |{password}|")
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = password
            adapter.remove_all_network_profiles()
            tmp_profile = adapter.add_network_profile(profile)
            adapter.connect(tmp_profile)
            if adapter.status() == const.IFACE_CONNECTED:
                connected = True
                print_same_line("Connecté au réseau : " + ssid)
            else:
                password = ''.join(random.sample(characters, 22))
    

    #-- CLEAR
    elif choice == "clear":
        os.system('clear' if os.name == 'nt' else 'clear')
        #-- HACKING RE TEXT
        texte3 = "X-SOCIETY :\n"
        for caractere in texte3:
            print(caractere, end='', flush=True)
            time.sleep(0.1)
        print()      

        #-- HELP RE TEXT
        texte4 = """> Type 'help' to get list of commands."""
        for caractere in texte4:
            print(caractere, end='', flush=True)
            time.sleep(0.01)  
        print()


    #-- RESTART
    elif choice == "restart":
        texte32 = "restarting ..."
        for caractere in texte32:
            print(caractere, end='', flush=True)
            time.sleep(0.01)  
        print()
        os.system('python main.py')    


    #-- EXIT
    elif choice == "exit":
        os.system('clear')    
        texte18 = """Thank you for using X-SOCIETY ."""
        for caractere in texte18:
            print(caractere, end='', flush=True)
            time.sleep(0.01)
        os.system('clear')    
        break

        
    #-- COMMAND NOT FOUND
    else: 
        texte26 = "Command is not found.\n"
        for caractere in texte26:
            print(caractere, end='', flush=True)
            time.sleep(0.01)  
    
