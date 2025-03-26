# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 08:17:14 2021

@author: Salih Ömer Ongün
"""

my_name = "Salih Omer Ongun"
my_id = "200102002003"
my_email = "s.ongun2020@gtu.edu.tr"

def problem1():
    my_name= "Salih Omer Ongun"
    return my_name[0]
"""
def problem2(): 
    a=int(input("Enter a number:"))
    b=a%16
    my_name="Salih Omer Ongun"
    c=my_name[b]
    return c

def problem3():
    a=int(input("first number:"))
    b=int(input("second number:"))
    d=a%16
    e=b%16
    my_name="Salih Omer Ongun"
    if d<e:
        my_name[d:e+1]
        return my_name[d:e+1]
    else:
        return my_name[e:d+1]
    
def problem4():
    a=input("Enter a word:")
    vowel=0
    for n in a:
        if (n=="a" or n=="e"or n=="i" or n=="u" or n=="o" or n=="A" or n=="E" or n=="I" or n=="U" or n=="O"):
            vowel+=1
    return(vowel)
          
def problem5():
    my_id = "200102002003"
    toplam=0
    for i in range(0,12):
        toplam=toplam+int(my_id[i])
    return toplam
    

def problem6():# burada def in başında fazladan boşluk olmuş o yuzden tüm ödevden sıfır aldık.
     a=int(input("Enter a number:"))
     c=1
     for n in range(1,a+1):
         c=c*n
     return(c)    


def problem7():
    a=int(input("Enter a number:"))
    if a%3==0 and a%7==0:
        return("True")
    else:
        return("False")
    
def problem8():
    a=int(input("Enter a number:"))
    if a%3==0 and a%7!=0:
        return("1")
    elif a%3!=0 and a%7==0:
        return("2")    
    elif a%3==0 and a%7==0:
        return("3")


def problem9():
    a=int(input("Enter a number:"))
    for number in range(2,a):
        if(a%number==0):
            return("False")
        else:
            return("True")
        
def problem10():
    a=float(input("Enter a number:"))
    x=6
    for i in range(1,13):
        x=((a/x)+x)/2
    return x        
        
        
        
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
    
"""        
        
        
        
    