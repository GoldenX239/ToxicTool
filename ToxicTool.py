import os
import sys
import requests
import subprocess
import json

ip_address = requests.get('http://api.ipify.org').text

print(ip_address)

sys.stdout.reconfigure(encoding='utf-8')
os.system("chcp 65001 > nul")

os.system("color 0a")

logo = """

              ▄▄▄█████▓ ▒█████  ▒██   ██▒ ██▓ ▄████▄     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
              ▓  ██▒ ▓▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▒██▀ ▀█     ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
              ▒ ▓██░ ▒░▒██░  ██▒░░  █   ░▒██▒▒▓█    ▄    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
              ░ ▓██▓ ░ ▒██   ██░ ░ █ █ ▒ ░██░▒▓▓▄ ▄██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
                ▒██▒ ░ ░ ████▓▒░▒██▒ ▒██▒░██░▒ ▓███▀ ░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
                ▒ ░░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░ ░▒ ▒  ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
                  ░      ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░  ░  ▒          ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
                ░      ░ ░ ░ ▒   ░    ░   ▒ ░░             ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
                          ░ ░   ░    ░   ░  ░ ░                      ░ ░      ░ ░      ░  ░
                                            ░                                              

"""

menu = """

                                             ___________________
                                            |                   |
                                            | [1] Network Stats |
                                            | [2] Geolocator    |
                                            | [3] Exit          |
                                            |___________________|
"""

running = True

while running == True:
    os.system("title Toxic Tool-GoldenX239")
    os.system("cls")
    print(logo)
    print(menu)
    print("")
    x = int(input("Option: "))

    if x == 1:
        batch_file = "NetworkStats.bat"
        subprocess.run(batch_file, check=True, shell=True)
        print("Batch file executed successfully.")
    elif x == 2:
          ip_address = input("Enter the IP address: ")
          print(ip_address)
          response = requests.get(f'http://ip-api.com/json/{ip_address}').json()
          print(response['city'])
          print(response['country'])
          print(response['zip'])
          input("Press the Enter key to continue: ")

    elif x == 3:
        sys.exit()
    else:
        print("Invalid option, try again.")
