import cProfile
import subprocess
from memory_profiler import profile
def lol():
    encoding_types = ["UTF-8","UTF-16","UTF-32","ASCII","ANSI","ISO-8859-1","Windows-1252","Unicode"]
    for i in encoding_types:
            try:data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode(i).split('\n');break
            except Exception:continue
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    password11=[]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:password11.append(results)
        except IndexError:password11.append('_______')
    print(profiles)
    print(password11)





@profile
def lol1():
    encoding_types = ["UTF-8","UTF-16","UTF-32","ASCII","ANSI","ISO-8859-1","Windows-1252","Unicode"]
    data_extracted=''
    for i in encoding_types:
            try:data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode(i).split('\n');break
            except Exception:continue
    for i in data:
        if "All User Profile" in i:
            data_extracted+=''.join(P:=i.split(":")[1][1:-1])
            D=subprocess.check_output(['netsh', 'wlan', 'show', 'profile', P, 'key=clear']).decode('utf-8').split('\n')
            data_extracted+=''.join(b.split(":")[1][1:-1] for b in D if "Key Content" in b)
    print(data_extracted)



# cProfile.run('lol()')
# 0.944  -  1619
# 0.943  -  1619
# 1.036  -  1619
# 1.067  -  1619
# 1.049  -  1619
# cProfile.run('lol1()')
# 0.942  -  1609
# 0.942  -  1609
# 0.947  -  1609
# 1.057  -  1609
# 1.089  -  1609
lol1()