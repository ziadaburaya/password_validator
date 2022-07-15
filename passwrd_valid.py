
import sys
import  re
from colorama import Fore, Back, Style
name_file = sys.argv[0]
password=sys.argv[1]

def valid():
        mes=""
        if len(password) < 10:
           mes= "Password length must be greater than 10\n"
        if re.search('[a-z]',password) is None:
           mes=mes+ "Password must contain a small letter [a-z]\n"
        if re.search('[0-9]', password) is None:
           mes=mes+ "Password must contain a number [0-9]\n"
        if re.search('[A-Z]', password) is None:
            mes=mes+"Password must contain a capital letter [A-Z]\n"
        if re.search('[#?!@$%^&*-]',password) is None:
           mes=mes+"Password must contain a  special character [#?!@$%^&*-]\n"
        if mes=="":
           return 1
        print(mes)

def read():
    pword = open("PASSWORD.txt", "r")
    for password1 in pword:
        print(password1)

if name_file=="passwrd_valid.py" and password!="-f" :
    if(valid()==1):
        print(Fore.GREEN + "is a valid password:1")
    else:
       print(Fore.RED + 'is not valid password:0')
elif password=="-f" :
    read()
else: print("wrong command")




