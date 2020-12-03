from os import system,listdir
from time import sleep
from getpass import getuser

lines=['']
profile=['']
user=getuser()
save=''
def profile_load():
    global profile
    profiles = listdir(rf'C:\Users\{user}\Documents\Euro Truck Simulator 2\profiles')
    for a in range(len(profiles)):
        print(str(a)+'. '+bytes.fromhex(profiles[a]).decode("ASCII"))
    choice=int(input('Please select Profile'))
    profile=profiles[choice]
    print(profile)
    choose_save_file()

def choose_save_file():
    global save
    saves = listdir(rf'C:\Users\{user}\Documents\Euro Truck Simulator 2\profiles\{profile}\save')
    for a in range(len(saves)):
        print(str(a)+'. '+saves[a])
    choice=int(input('Please select save file'))
    save=saves[choice]
    menu()

def reads():
    global lines
    system(rf'SII_Decrypt.exe "C:\Users\{user}\Documents\Euro Truck Simulator 2\profiles\{profile}\save\{save}\game.sii"')
    sleep(2)
    f=open(rf'C:\Users\{user}\Documents\Euro Truck Simulator 2\profiles\{profile}\save\{save}\game.sii','r')
    lines=f.readlines()
    print(40*'-')
    f.close()

def write(lines):
    f=open(rf'C:\Users\{user}\Documents\Euro Truck Simulator 2\profiles\{profile}\save\{save}\game.sii','w')
    f.writelines(lines)
    f.close()
    print('successfully changed value')

def money():
    system('cls')
    l=0
    for line in lines:
        l+=1
        if 'money_account:' in line:
            print('Current Balance is',line[16:])
            n=int(input('Enter new value -> '))
            lines[l-1]=f' money_account: {n}\n'
            break
    write(lines)
    menu()

def experience():
    system('cls')
    l=0
    for line in lines:
        l+=1
        if 'experience_points:' in line:
            print('Current Exerience is',line[20:])
            n=int(input('Enter new value -> '))
            lines[l-1]=f' experience_points: {n}\n'
            break
    write(lines)
    menu()

def extend():
    system('cls')
    l=0
    f=0
    for line in lines:
        l+=1
        if 'time_upper_limit:' in line:
            f=1
            print('Current Dilevery Time is',line[19:])
            n=int(input('Enter no. of hours to extend -> '))
            n=n*12960000
            v=int(int(line[19:])+n)
            lines[l-1]=f' time_upper_limit: {v}\n'
            break
    if f==0:
        print('TODO this first start a job')
    else:
        write(lines)
    menu()

def menu():
    system('cls')
    reads()
    print('Welcome to ets2 modding tool\tBy Ben24')
    print('Current Profile Selected',bytes.fromhex(profile).decode("ASCII"))
    print('Please select from folowing options\n\n')
    print('0. Exit')
    print('1. Money')
    print('2. Experience')
    print('3. Extend dilevery time limit')
    print('4. Choose other profile')
    print('\tMore options coming soon :P\n')
    choice=input('Enter your choice -> ')
    if int(choice) == 0 or 'exit' in choice.lower():
        print('\nThanks for using me!')
        sleep(2)
        exit()
    elif int(choice) ==1 or 'm' in choice.lower():
        money()
    elif int(choice) ==2 or 'e' in choice.lower():
        experience()
    elif int(choice) ==3 or 'd' in choice.lower():
        extend()
    elif int(choice) ==4 or 'p' in choice.lower():
        profile_load()
    else:
        print('This function is not avaliable, coming soon :P')

profile_load()
