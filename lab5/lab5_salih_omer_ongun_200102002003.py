
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 09:27:03 2021

@author: Salih Ömer Ongün
"""

my_name = "Salih Omer Ongun"
my_id = "200102002003"
my_email = "s.ongun2020@gtu.edu.tr"


def problem1(a,b):
    c=[]
    if b<=0:
        return c
    else:
        for n in a:
            if a.count(n)==b:
                c.append(n)       
                for k in c:
                    if c.count(k)>1:
                        c.remove(k)
                        
    return c         
             

def problem2(a):
    b=list(a.values())
    if len(b)%2!=0:
        return b[(len(b)//2)]
    elif len(b)%2==0:
        c=(b[int((len(b)/2)-1)]+b[int(len(b)/2)])/2
        return c 
    
def problem3(x):
    k=[]
    try:
        f=open(x,"r")   
        while True:
            a=f.readline()
            b=a.strip()
            c=b.split(", ")
            if c==['']:
                break
            else:
                l={}
                if len(c)==3:
                    l["name"]=c[0]
                    l["credit"]=int(c[1])
                    l["term"]=int(c[2][0])
                    l["grade"]="NA"
                    k.append(l) 
                if len(c)==4:
                    print(c[3])
                    l["name"]=c[0]
                    l["credit"]=int(c[1])
                    l["term"]=int(c[2])
                    l["grade"]=c[3]
                    k.append(l)
                else:
                    continue
         
    except:
       return k
    else:   
        return k



def problem4(x,y):
    a={"AA":4.0, "BA":3.5, "BB":3.0, "CB":2.5, "CC":2.0, "DC":1.5, "DD":1.0, "FF":0.0}
    b=0
    c=0
    for n in range(0,len(x)):
        if x[n]["term"]==y:
            if x[n]["grade"]=="NA":
                continue
            else:
                b+=x[n]["credit"]
                c+=x[n]["credit"]*a[x[n]["grade"]]
        else:
            continue
    if c==0 and b==0:
        return 0
    if x==[]:
        return 0
    return float(c/b) 


   
def find1(b):    
    r=""
    for i in range(0,b+1):
        r+=str(i)    
    return r.count("1")


def problem5(a,b):
    if a==find1(b):
        return True
    else:
        return False
    
    
def problem7(x,y):
    pass    
    

def problem8(x,y):
    n=0
    m=0
    c=[]
    while True:
        if n!=len(x)-1:   
            if m!=len(x[0])-1:
                i=x[n][m]
                c.append(i)
                m+=1
            else:
                i=x[n][m]
                c.append(i)
                m=0
                n+=1
        else:        
            if m!=len(x[0])-1:
                i=x[n][m]
                c.append(i)
                m+=1
            else:
                i=x[n][m]
                c.append(i)
                break
    for i in y:
        for j in i:
            if j in c:
                continue
            else:
                return False
    for i in range(0,len(y)-1):
        if len(y[i])==len(y[i+1]):
            continue 
        else:
            return False                       
    b=[]
    a=[]
    a1=[]
    b1=[]
    a2=[]
    b2=[]
    for i in y:
        for j in i:
            for m in range(0,len(x)):  
                if j in x[m]:
                    a.append(m)
                    if len(a)==len(y[0]):
                        if len(list(set(a)))==1:
                            a=b.copy()
                            continue
                        else:
                            return False
                        
    for i in y:
        for j in i:
            for m in range(0,len(x)):
                if j in x[m]:    
                    n=x[m].index(j)
                    a2.append(n)
                    if len(a2)==len(y[0]):
                        if a2==sorted(a2):
                            a2=b2.copy()
                            continue
                        else:
                            return False
                            
    for i in range(0,len(y[0])):
        for j in range(0,len(y)):
            for m in range(0,len(x)):
                if y[j][i] in x[m]:
                    n=x[m].index(y[j][i])
                    a1.append(n)
                    if len(a1)==len(y):
                        if len(list(set(a1)))==1:
                            a1=b1.copy()
                            continue
                        else:
                            return False
    return True                   
                

def problem9(s):
    a=""
    for i in s:
        if s.count(i)==1:
            a+=str(i)
        elif s.count(i)>1:
            b=s.count(i)
            if i in a:
                continue
            else:
                a+=str(i)
                a+=str(b)
    b=len(s)        
    c=len(a)      
    d=round(100-(c/b)*100)  
    return a,d



def problem10(x):
    a=min(x)
    b=max(x)
    c=[]
    x.sort()
    for i in range(a,b+1):
        c.append(i)
    if c==x:
        return b+1
    else:
        for i in range(0,len(c)):
            if c[i]==x[i]:
                continue
            else:
                return c[i]


def problem6(s):
    s=s.lower()
    d=s
    b=[]
    b.append(s[0])
    for i in range(1,len(s)):
        b.append(s[0]+s[i])
    for i in range(1,len(s)):
        for i1 in range(1,len(s)):
            if i1==i:
                continue
            else:
                b.append(s[0]+s[i]+s[i1])
    for i in range(1,len(s)):
        for i1 in range(1,len(s)):
            for i2 in range(1,len(s)):
                if i1==i or i2==i1 or i2==i:
                    continue
                else:
                    b.append(s[0]+s[i]+s[i1]+s[i2])
    for i in range(1,len(s)):
        for i1 in range(1,len(s)):
            for i2 in range(1,len(s)):
                for i3 in range(1,len(s)):
                    if i1==i or i2==i1 or i2==i or i3==i2 or i3==i1 or i3==i:
                        continue
                    else:
                        b.append(s[0]+s[i]+s[i1]+s[i2]+s[i3])
   
 
  
    
    for i in range(1,len(s)):
        c=s[i]
        s=str(c)+s[1:i]+s[0]+s[i+1:len(s)]
        b.append(s[0])
        for i in range(1,len(s)):
            b.append(s[0]+s[i])
        for i in range(1,len(s)):
            for i1 in range(1,len(s)):
                if i1==i:
                    continue
                else:
                    b.append(s[0]+s[i]+s[i1])
        for i in range(1,len(s)):
            for i1 in range(1,len(s)):
                for i2 in range(1,len(s)):
                    if i1==i or i2==i1 or i2==i:
                        continue
                    else:
                        b.append(s[0]+s[i]+s[i1]+s[i2])
        for i in range(1,len(s)):
            for i1 in range(1,len(s)):
                for i2 in range(1,len(s)):
                    for i3 in range(1,len(s)):
                        if i1==i or i2==i1 or i2==i or i3==i2 or i3==i1 or i3==i:
                            continue
                        else:
                            b.append(s[0]+s[i]+s[i1]+s[i2]+s[i3])            
        s=d   
    b=sorted(set(b))
    return b           

if __name__ == "__main__":
    print("problem1 running")
    print(problem1([], 1))
    
    print("problem2 running")
    print(problem2({'ahmet': 10, 'ali': 20}))
    
    print("problem3 running")
    print(problem3("transcript3.txt"))
    
    print("problem4 running")
    print(problem4([], 1))
    
    
    print("problem6 running")
    print(problem6("aba"))
    
    print("problem8 running")
    print(problem8([[1,2,3], [4,5,6],[7,8,9]], [[3,1],[6,4],[9,7]]))
    
    print("problem9 running")
    print(problem9('ggoooooooooooollllllllllllll'))
    
    print("problem10 running")
    print(problem10([5,3,4]))
    
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")







       