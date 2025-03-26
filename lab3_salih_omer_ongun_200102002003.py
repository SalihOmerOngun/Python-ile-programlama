# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:36:02 2021

@author: Salih Ömer Ongün
"""

my_name = "Salih Omer Ongun"
my_id = "200102002003"
my_email = "s.ongun2020@gtu.edu.tr"


def problem1(x):
    if "K" in str(x):
        return True 
    else:
        return False  


def problem2(x,y,z,t):
    if x<y and x<z and x<t:
        return float(x)
    elif y<x and y<z and y<t:
        return float(y)
    elif z<x and z<y and z<t:
        return float(z)
    elif t<x and t<y and t<z:
        return float(t)
     
def problem3(x,y):
    if x>y:
        if x<0 and y<0:
            if (y-int(y))*-1<=-0.5:
                return int(x)-1
            else:
                return int(x)
        else:
            if y-int(y)>=0.5:
                return 1+int(x)
            else:
                return int(x) 
    elif y>x: 
        if x<0 and y<0:
            if (x-int(x))*-1<=-0.5:
                return int(x)-1
            else:
                return int(x)       
        else:    
            if x-int(x)>=0.5:
                return 1+int(x)
            else:
                return int(x) 
    elif x==y:
        return int(x)    

    
def problem4(radius,height,pi=3.1415):  
    a=pi*(radius**2)*height
    return a


def problem5(radius,height,pi=3.1415):
    if type(radius)==str:
        a=-1
    elif type(radius)==bool:
        a=-1
    elif radius==None: 
        a=-1
    elif type(height)==str:
        a=-1
    elif type(height)==bool:
        a=-1
    elif height==None: 
        a=-1
    elif type(pi)==str:
        a=-1
    elif type(pi)==bool:
        a=-1
    elif pi==None: 
        a=-1
    else:
        a=pi*(radius**2)*height     
    return a 

def problem6(x):
    for n in str(x):
         if str(x).count(n)==1:
             return str(n)


def problem7(x):
    m=0
    while ord(str(x)[m])<=ord(str(x)[m+1]):
        m+=1
        if m==len(str(x))-2:
            if ord(str(x)[-2])<=ord(str(x)[-1]):
                return True
        else:
            continue
    else:
        return False
    
def problem8(x):
    n=0
    for n in range(0,len(str(x))):
        if str(x).count(str(x)[n])==1:
            if n!=len(str(x))-1:
                continue
            if n==len(str(x))-1:
                if str(x).count(str(x)[len(str(x))-1])==1:
                    return True
                else:
                    return False
        else:
            return False
        
        
def problem9(row,column):
    if row==1 and column==1:
        return 1
    elif row!=1 and column==1:
        return 3
    elif row==column and row>1:
        return 2
    elif row!=column and column>1:
        return problem9(row-1,column-1) + problem9(row-1,column)        




def problem10(x,y):
    a=0        
    if len(str(x))<=len(str(y)):
        for n in range(0,len(str(x))):
            if str(x)[n]==str(y)[n]:
                a+=1
    if len(str(y))<len(str(x)):
        for n in range(0,len(str(y))):
            if str(y)[n]==str(x)[n]:
                a+=1                  
    return a            
        

if __name__ == "__main__":
    print("problem1 running")
    print(problem1("64851LIMNK333"))
    
    print("problem2 running")
    print(problem2(2.3,-0.4,-1,4.3))
    
    print("problem3 running")
    print(problem3(-0.7,-0.6))
    
    print("problem4 running")
    print(problem4(2,height=3,pi=3.1415))
    
    print("problem5 running")
    print(problem5(2, None, 3))
    
    print("problem6 running")
    print(problem6('006315a543146'))
    
    print("problem7 running")
    print(problem7('abcdefzg'))
    
    print("problem8 running")
    print(problem8('abgcdefzg'))
    
    print("problem9 running")
    print(problem9(12,7))
    
    print("problem10 running")
    print(problem10('tela', 'kesa'))
    
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")








    
                 