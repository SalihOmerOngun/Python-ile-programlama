# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 09:08:04 2021

@author: Salih Ömer Ongün
"""

my_name = "Salih Omer Ongun"
my_id = "200102002003"
my_email = "s.ongun2020@gtu.edu.tr"


def problem1(a,b):
    if b<0:
        return None
    elif b>len(a)-1:
        return None
    else:
        return a[b]

    
def problem2(a,b):
    if b<0:
        return a
    elif b>len(a)-1:
        return a
    else:
        a.pop(b)
        return a
    
    
def problem3(a,b):
    if b==False:
        a.sort(reverse=True)
        return a
    elif b==True:
        a.sort()
        return a    
    
    
def problem4(a,b):
    s=[]
    for i in a:
        for n in b:
            if i==n:
                s.append(i)
                for k in s:
                    if s.count(k)>1:
                        s.remove(k)
    return len(s)


def problem5(x,w):
    a=0
    b=0
    for n in range(len(w)):
        a+=w[n]*x[n]
        b+=w[n]
    return float(a/b)    



def problem6(m):
    if len(m)==1:
        return float(m[0][0])
    elif len(m)==2:
        if len(m[0])!=len(m[1]):
            return None
        else:
            if len(m[0])!=2:
                return None
            else:
                a=0
                for n in range(len(m)):
                    a+=(1 if n%2==0 else -1)*m[0][n]*problem6([o[:n]+o[n+1:] for o in m[1:]])
                return float(a)    
    elif len(m)==3:
        if len(m[0])!=len(m[1]):
            return None
        elif len(m[0])!=len(m[2]):
            return None
        elif len(m[1])!=len(m[2]):
            return None             
        else:
            if len(m[0])!=3:
                return None
            else:
                a=0
                for n in range(len(m)):
                    a+=(1 if n%2==0 else -1)*m[0][n]*problem6([o[:n]+o[n+1:] for o in m[1:]])
                return float(a)             
    elif len(m)==4:
        if len(m[0])!=len(m[1]):
            return None
        elif len(m[0])!=len(m[2]):
            return None
        elif len(m[1])!=len(m[2]):
            return None
        elif len(m[0])!=len(m[3]):
            return None
        elif len(m[1])!=len(m[3]):
            return None
        elif len(m[2])!=len(m[3]):
            return None
        else:
            if len(m[0])!=4:
                return None
            else:
                a=0
                for n in range(len(m)):
                    a+=(1 if n%2==0 else -1)*m[0][n]*problem6([o[:n]+o[n+1:] for o in m[1:]])
                return float(a)                                                  



def problem7(accounts, source, lira, kurus):
    if source<0:
        return accounts
    elif source>len(accounts)-1:
        return accounts
    else:
        a=accounts[source]
        if float(a)-(lira+kurus/100)<0:
            return accounts
        else:
            a=accounts[source]
            b=float(a)-(lira+kurus/100)
            d=round(b,2)
            accounts.pop(source)
            if str(d)[-3]!=".":
                if str(d)[-1]=="0":
                    accounts.insert(source,str(d))
                else:
                    accounts.insert(source,str(d)+"0") 
            else:    
               accounts.insert(source,str(d))
            return accounts

                 
        


def problem8(accounts, source, destination, lira, kurus,fee=False):
    a=accounts[source]
    a1=accounts[destination] 
    if source<0:
        return accounts
    elif source==destination:
        return accounts
    elif destination<0:
        return accounts
    elif source>len(accounts)-1:
        return accounts
    elif destination>len(accounts)-1:
        return accounts
    else:
        if float(a)-(lira+kurus/100)<0:
            return accounts        
        else:
            if fee==False:    
                a=accounts[source]
                b=float(a)-(lira+kurus/100)
                d=round(b,2)
                accounts.pop(source)
                if str(d)[-3]!=".":
                    if str(d)[-1]=="0":
                        accounts.insert(source,str(d))
                    else:
                            accounts.insert(source,str(d)+"0") 
                else:    
                    accounts.insert(source,str(d))
                a1=accounts[destination]
                b1=float(a1)+(lira+kurus/100)
                d1=round(b1,2)
                accounts.pop(destination)
                if str(d1)[-3]!=".":
                    if str(d1)[-1]=="0":
                        accounts.insert(destination,str(d1))
                    else:
                        accounts.insert(destination,str(d1)+"0") 
                else:    
                    accounts.insert(destination,str(d1))
                return accounts
            elif fee==True:
                if (lira+kurus/100)>=10:
                    if (float(a)-(lira+kurus/100)-((lira+kurus/100)/100))>0:
                        a=accounts[source]
                        b=float(a)-(lira+kurus/100)-int(((lira+kurus/100)/100)*100)/100
                        d=round(b,2)
                        accounts.pop(source)
                        if str(d)[-3]!=".":
                            if str(d)[-1]=="0":
                                accounts.insert(source,str(d))
                            else:
                                accounts.insert(source,str(d)+"0") 
                        else:    
                            accounts.insert(source,str(d))
                        a1=accounts[destination]
                        b1=float(a1)+(lira+kurus/100)
                        d1=round(b1,2)
                        accounts.pop(destination)
                        if str(d1)[-3]!=".":
                            if str(d1)[-1]=="0":
                                accounts.insert(destination,str(d1))
                            else:
                                accounts.insert(destination,str(d1)+"0") 
                        else:    
                            accounts.insert(destination,str(d1))
                        return accounts     
                    else:
                        return accounts
                elif lira+kurus/100<10:
                    if (float(a)-(lira+kurus/100)-int((lira+kurus/100)/100))>0:    
                        a=accounts[source]
                        b=float(a)-(lira+kurus/100)-0.1
                        d=round(b,2)
                        accounts.pop(source)
                        if str(d)[-3]!=".":
                            if str(d)[-1]=="0":
                                accounts.insert(source,str(d))
                            else:
                                accounts.insert(source,str(d)+"0") 
                        else:    
                            accounts.insert(source,str(d))
                        a1=accounts[destination]
                        b1=float(a1)+(lira+kurus/100)
                        d1=round(b1,2)
                        accounts.pop(destination)
                        if str(d1)[-3]!=".":
                            if str(d1)[-1]=="0":
                                accounts.insert(destination,str(d1))
                            else:
                                accounts.insert(destination,str(d1)+"0") 
                        else:    
                            accounts.insert(destination,str(d1))
                        return accounts
                    else:
                        return accounts
               
def problem9():
    pass


def problem10(x):
    for n in x:
        if x.count(n)>1:
            return str(n)


if __name__ == "__main__":
    print("problem1 running")
    print(problem1([1, 2, 3], 3))
    
    print("problem2 running")
    print(problem2([1, 2, 3], 4))
    
    print("problem3 running")
    print(problem3([2, 1, 3], True))
    
    print("problem4 running")
    print(problem4([], [3, 5, 2]))
    
    print("problem5 running")
    print(problem5([1, 2, 3], [.2, .5, .7]))
    
    print("problem6 running")
    print(problem6([[3, 7], [1, 2, 3]]))
    
    print("problem7 running")
    print(problem7(accounts=["11.23", "10.43", "100.63", "0.10"], source=3, lira=10, kurus=13))
    
    print("problem8 running")
    print(problem8(accounts=["11.23", "10.43", "100.63", "0.10"], source=0, destination=1, lira=10, kurus=11, fee=False))
    
    print("problem9 running")
    print(problem9())
    
    print("problem10 running")
    print(problem10(['aba']))
    
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")



    