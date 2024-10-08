import os
import datetime
path='C:\\Users\\Public\\akki\\tasks'
if os.path.exists(path):
    pass
else:os.mkdir(path)
if not os.path.exists(path+'\\file.txt'):
    date=datetime.datetime.date(datetime.datetime.now())
    with open(path+'\\file.txt','w')as opening:
        opening.write(str([date,False,'set up the account'])+'@')
def add_task(tasks):
    with open(path+'file.txt','a') as lol:
        data=[datetime.datetime.now(),False,tasks]
        lol.write('@'+str(data))
def delete_task(tasks):
    with open(path+'file.txt','r') as lol:
        data=lol.read().split('@')
    data_recreation=''
    for i in data:
        if eval(i)[2]==tasks:pass
        else:data_recreation+=''.join('@'+i)
    with open(path+'file.txt','w') as lol:
        lol.write(data_recreation)
def tasks_show():
    date=datetime.datetime.date(datetime.datetime.now())
    yesterday = date - datetime.timedelta(days=1)
    tomorrow = date + datetime.timedelta(days=1)
    with open(path+'\\file.txt','r') as data:
        data_ectracted=data.read().split('@')
    today_task=[]
    tommarow_task=[]
    yesterday_task=[]
    future_task=[]
    previous_task=[]
    for task in data_ectracted:
        print(task)
        if task[0]==date:today_task.append(task[1:])
        elif task[0]==yesterday:yesterday_task.append(task[1:])
        elif task[0]==tomorrow:tommarow_task.append(task[1:])
        elif task[0]<yesterday:previous_task.append(task[1:])
        elif task[0]>tomorrow:future_task.append(task[1:])
        else:pass
    data_ectracted.clear()
    return today_task,tommarow_task,yesterday_task,future_task,previous_task
def data_show():
    response='add_task'
    date=datetime.datetime.now()
    today_task,tommarow_task,yesterday_task,future_task,previous_task=tasks_show()
    def show(data):
        done=[]
        not_done=[]
        for i in data:
            if not i[0]:done.append(i[1])
            else:not_done.append(i[1])
        print('Tasks Remain'+'='*39)
        for num,i in enumerate(done,start=1):print(str(num)+'.',i)
        print('\n\n\nTasks Compleated'+'='*34)
        for num,i in enumerate(not_done,start=1):print(str(num)+'.',i)
    while True:
        response=input("enter response:- ").split('-')
        if response[1].strip()=='add_task':
            add_task(response[2])
        elif response[1].strip()=='delete_task':
            delete_task(response[2])
        elif response[1].strip()=='today':
            print(f'Today{str(datetime.datetime.date(date))}\n\n'.center(50))
            show(today_task)
        elif response[1].strip()=='tommarow':
            print(f'tommarow{str(datetime.datetime.date(date))}\n\n'.center(50))
            show(tommarow_task)
        elif response[1].strip()=='yesterday':
            print(f'yesterday{str(datetime.datetime.date(date))}\n\n'.center(50))
            show(yesterday_task)
        elif response[1].strip()=='future':
            print(f'futre{str(datetime.datetime.date(date))}\n\n'.center(50))
            show(future_task)
        elif response[1].strip()=='previous':
            print(f'previous{str(datetime.datetime.date(date))}\n\n'.center(50))
            show(previous_task)
        elif response[1].strip()=='help':print('u can use this things here:)\n1.-help --> for seeing what u can do takes no argument\n2. -today --> show today task\n3. -tommarow --> show tommarow tasks\n4. -yesterday --> show yesterday task only \n5. -future --> show future task \n6. -previous --> show previous task \n7. -add_task --> help to add\n    task takes "-task" as argument\n8. -delete_task --> delete a task \n    takes "-task" as argument')
        else:nothing=input('u typed something wrong');os.system('cls')
data_show()