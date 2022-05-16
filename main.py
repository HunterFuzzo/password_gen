import time
import sys
import random
import os
from pystyle import Anime, Colorate, Colors, Center , System, Write
from colorama import Fore, Back, Style

System.Title("Password Generator")
System.Size(70, 20)

ascii = """
        ╔══════════════════════════╗
        ║   ╔═╗╦ ╦╔╦╗  ╔═╗╔═╗╔╗╔   ║
        ║   ╠═╝║║║ ║║  ║ ╦║╣ ║║║   ║
        ║   ╩  ╚╩╝═╩╝  ╚═╝╚═╝╝╚╝   ║
        ╚══════════════════════════╝        
"""
def main():
    print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(ascii)))

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    symbol = "&é'(-è_çà)=^$*ù!:;,?./§%µ£¨+°~#{}[]|`\^@¤"

    ans1 = lower_case + symbol
    ans2 = lower_case + num
    ans3 = lower_case + upper_case
    ans4 = lower_case
    
    print("\n["+ Fore.RED+ "!"+ Style.RESET_ALL +"] Password Generator | Made By Azuka\n")
    a = int(input("What lenght do you want ? >>> "))
    length = a
    
    print("\n["+ Fore.RED+ "!"+ Style.RESET_ALL +"] If you say no at all it result in password just with lower case.")
    print('['+ Fore.RED+ '!'+ Style.RESET_ALL +'] Type "y" for yes or "n" for no.\n')

    b = input("Do you want upper case ? >>> ")
    c = input("Do you want number ? >>> ")
    d = input("Do you want special character ? >>> ")
    print(" ")
    n = int(input("How many password do you want to generate ? >>> "))
    done = False
    i = 0
    print(" ")
    for i in range(random.randint(3,8)):
        sys.stdout.write('\r['+ Fore.RED+ '!'+ Style.RESET_ALL +'] Generating password, please wait '+Fore.GREEN+'|'+Style.RESET_ALL)
        time.sleep(0.1)
        sys.stdout.write('\r['+ Fore.RED+ '!'+ Style.RESET_ALL +'] Generating password, please wait '+Fore.YELLOW+'/'+Style.RESET_ALL)
        time.sleep(0.1)
        sys.stdout.write('\r['+ Fore.RED+ '!'+ Style.RESET_ALL +'] Generating password, please wait '+Fore.RED+'-'+Style.RESET_ALL)
        time.sleep(0.1)
        sys.stdout.write('\r['+ Fore.RED+ '!'+ Style.RESET_ALL +'] Generating password, please wait '+Fore.BLUE+'\\'+Style.RESET_ALL)
        time.sleep(0.1)
        i+=1
    sys.stdout.write('\r['+ Fore.GREEN+ '+'+ Style.RESET_ALL +'] Done!                                                  ')
    print(" ")
    done = True
    print(" ")
    i = 0
    for i in range(n):
        if b == "y":
            password = "".join(random.sample(ans3, length))
        else:
            password = "".join(random.sample(ans4, length))
            if c == "y":
                password = "".join(random.sample(ans2, length))
            else:
                password = "".join(random.sample(ans4, length))
                if d == "y":
                    password = "".join(random.sample(ans1, length))
                else:
                    password = "".join(random.sample(ans4, length))
        time.sleep(0.2)
        print("["+ Fore.GREEN+ "+"+ Style.RESET_ALL +"] Your generated password is :", password)
    
    i+=1

    time.sleep(2)
    new = input("\nDo you want to generate new password ? >>> ")

    if new == "y":
        os.system("cls")
        main()
    else:
        exit()

if __name__ == "__main__":
    main()