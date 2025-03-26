# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 10:59:45 2021

@author: Salih Ömer Ongün
"""
my_name = "Salih Omer Ongun"
my_id = "200102002003"
my_email = "s.ongun2020@gtu.edu.tr"


def problem1():
    F=float(input("Enter a Fahrenheit:"))
    C=(F-32)/1.8
    return C

def problem2():
    C=float(input("Enter a Celsius:"))
    F=(C*1.8)+32
    return F

def problem3():
    a=int(input("Enter a number:"))
    b=2*(a**2)-a
    return b

def problem4():
    n=int(input("Enter a number:"))
    a=2
    b=1
    count=1
    while True:
        c=a+b
        a=b
        b=c
        count+=1
        if count==n:
            break
        elif n==1:
            return 1
            break
        elif n==0:
            return 2
            break
    return c    


def problem5():
    a=str(input("Enter a string:"))
    return a[::-1]


def problem6():
    k=" "
    b=input("Enter a word:")
    for n in b:
        if n=="a" or n=="e"or n=="i" or n=="u" or n=="o" or n=="A" or n=="E" or n=="I" or n=="U" or n=="O" or n=="Q" or n=="q" or n=="w" or n=="W" or n=="r" or n=="R" or n=="t" or n=="T" or n=="Y" or n=="P" or n=="D" or n=="S" or n=="F" or n=="G" or n=="H" or n=="J" or n=="K" or n=="L" or n=="Z" or n=="X" or n=="C" or n=="V" or n=="B" or n=="N" or n=="M" or n=="y" or n=="p" or n=="s" or n=="d" or n=="f" or n=="g" or n=="h" or n=="k" or n=="l" or n=="z" or n=="x" or n=="c" or n=="v" or n=="b" or n=="n" or n=="m" or n=="1" or n=="2" or n==0 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9:# 1 ve 2 hariç diğer sayıları tırnağa almadığın için okumamış.  
            k +=n
    return k


def problem7():
    target=int(input("enter a number:"))
    a=""
    if target<0:
        b="-"
    else:
        b=""
    while True:
        if target==0:
            break
        elif target<0:
            target=target*(-1)
        if target%4==0:
            target=target//4# sıfırları atman istenmiyormuş o yüzden bu satır boşa yazıldı ve sonuçta hatalı çıktı.
            continue
        a += str(target % 4)
        target = target // 4  
    return b+a[::-1]    
        
def problem8():# buradan puan alamadık.
    a=str(input("enter a string:"))
    b= "{"
    c= "}"       
    d= "[" 
    e= "]"
    if a[0]==b:
        if a[1]==c:
            return True
        elif a[-1]==e:
            return True
        else:
            return False
    elif a[0]==d:
        if a[1]==e:
            return True
        elif a[-1]==e:
            return True
        else:
            return False

def problem9():
    s=str(input("enter a string:"))
    count=0
    for a in s[::-1]:
        if a!=" ":
            count+=1
        elif a==" ":
            break
    return count


def problem10():
    k=str(input("enter a string:"))
    x=0
    y=0
    for i in k:
        if (i=="n"):
            y+=1
        elif (i=="s"):
            y-=1
        elif (i=="w"):
            x+=1
        elif (i=="e"):
            x-=1   
    destination=x**2+y**2        
    guess=destination**(1/2)
    return guess


if __name__ == "__main__":
    print("problem1 running")
    print(problem1())
    
    print("problem2 running")
    print(problem2())
    
    print("problem3 running")
    print(problem3())
    
    print("problem4 running")
    print(problem4())
    
    print("problem5 running")
    print(problem5())
    
    print("problem6 running")
    print(problem6())
    
    print("problem7 running")
    print(problem7())
    
    print("problem8 running")
    print(problem8())
    
    print("problem9 running")
    print(problem9())
    
    print("problem10 running")
    print(problem10())
    
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")




