# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 16:04:21 2021

@author: Salih Ömer Ongün
"""

my_name = "Salih Omer Ongun"
my_id = "200102002003"
my_email = "s.ongun2020@gtu.edu.tr"


import random

def problem0():
    pass

def problem1():
    class p1:
        
        def __init__(self,x):
            if type(x)==int:
                self.a=x
            else:
                self.a=0
        
        def set_value(self,x):
            if type(x)==int:
                self.a=x
            
                
        def get_value(self):
            return self.a        
    return p1  



def problem2():
    class p1:
        
        def __init__(self,x,y):
            self.a=x
            self.b=y
           
        def get_area(self):
            return self.a*self.b
        def get_perimeter(self):
            return (self.a+self.b)*2
    return p1 
        

def problem3():
    class Grades:

        def __init__(self):
            self.a=[0.0]
            
        def add_grade(self,x):
            self.a.append(x)
            if 0.0 in self.a:
                self.a.remove(0.0)
            
        def remove_grade(self,x):
            if x in self.a:
                self.a.remove(x)
            else:
                pass
                
        def get_min(self):
            return float(min(self.a))
         
        def get_max(self):
            return float(max(self.a))
        
        def get_mean(self):
            return float(sum(self.a)/len(self.a)) 
        
        def get_median(self):
            self.a.sort()
            if len(self.a)%2!=0:
                return float(self.a[len(self.a)//2])
            else:
                return float((self.a[int((len(self.a)/2)-1)]+self.a[int(len(self.a)/2)])/2)
    return Grades        
            
         

def problem4():
    class Movie:
    
        def __init__(self, movie_name, director, year, rating=0.0, length=0):        
            self.a=movie_name
            self.a1=director
            self.a2=year
            self.a3=rating
            self.a4=length
            
        def get_movie_name(self):
            return self.a
        
        def get_director(self):
            return self.a1
            
        def get_year(self):
            return self.a2
        
        def get_rating(self):
            return self.a3
        
        def get_length(self):
            return self.a4
        
        def set_rating(self,x):
            if type(x)==float and x>=0.0 and x<=10.0:
                self.a3=x
                
        def set_length(self,x):
            if type(x)==int and x>=0 and x<=500:
                self.a4=x
    return Movie            
         
            
def problem5():
    class MovieCatalog:
        
        def __init__(self,x):
            self.a=[]
            with open(x,"r") as f:
                for i in f:
                    b=i.strip("\n")
                    c=b.split(",")
                    self.a.append(c)
                    
        def add_movie(self,movie_name, director, year, rating=0.0, length=0):
            l=[]
            self.b=movie_name
            self.b1=director
            self.b2=str(year)
            self.b3=str(rating)
            self.b4=str(length)
            l.append(self.b)
            l.append(self.b1)
            l.append(self.b2)
            l.append(self.b3)
            l.append(self.b4)
            if l not in self.a:
                self.a.append(l)
            l=[]
        
        def remove_movie(self,movie_name):
            for i in self.a:
                if i[0]==movie_name:
                    self.a.remove(i)
            return self.a        
        def get_oldest(self):
            x=[]
            for i in self.a:
                x.append(int(i[2]))
            for k in self.a:
                if int(k[2])==min(x):    
                    return k[0]
                
        def get_lowest_ranking(self):
            x=[]
            for i in self.a:
                x.append(float(i[3]))
            for k in self.a:
                if float(k[3])==min(x):    
                    return k[0]
                
        def get_highest_ranking(self):
            x=[]
            for i in self.a:
                x.append(float(i[3]))
            for k in self.a:
                if float(k[3])==max(x):    
                    return k[0]    
        def get_by_director(self,director):
            x=[]
            for i in self.a:
                if i[1]==director:
                    x.append(i[0])
            return x        
            
            
    return MovieCatalog            

    
def problem6():
    class Node:
        
        def __init__(self,x,y,z):
            self.a=x
            self.b=y
            self.c=z
            
        def get_node(self):
            return (self.a,self.b,self.c)
            
        def get_distance(self):
            return (self.a**2+self.b**2+self.c**2)**0.5
        
        def __add__(self,another):
            xeksen=self.a+another.a
            yeksen=self.b+another.b
            zeksen=self.c+another.c
            return Node(xeksen,yeksen,zeksen)
            
        def __str__(self):
            return "<"+str(self.a)+", "+str(self.b)+ ", "+str(self.c)+">"  
        
        def __gt__(self,another):
            if self.get_distance()>another.get_distance():
                return True
            else:
                return False
            
        def __ge__(self,another):
            if self.get_distance()>=another.get_distance():
                return True
            else:
                return False    
            
        def __lt__(self,another):
            if self.get_distance()<another.get_distance():
                return True
            else:
                return False    
            
        def __le__(self,another):
            if self.get_distance()<=another.get_distance():
                return True
            else:
                return False    
            
        def __eq__(self,another):
            if self.a==another.a and self.b==another.b and self.c==another.c:
                return True
            else:
                return False    
    return Node       
            

def problem7():
    class NodeCloud:
        
        
        def __init__(self,n):
            self.a=[]
            for i in range(0,n):
                k=random.randint(-20,20)
                a=k
                k1=random.randint(-20,20)
                b=k1
                k2=random.randint(-20,20)
                c=k2
                self.a.append((a,b,c))
                
        def get_nodes(self):
            return self.a
            
        def get_outermost(self):
            x=[]
            for i in self.a:
                y=(i[0]**2+i[1]**2+i[2]**2)**0.5   
                x.append(y)
            for i in range(0,len(x)):
                if x[i]==max(x):
                    return self.a[i]
                
        def add_node(self,x, y, z):
            c=(x,y,z)
            if c not in self.a:
                self.a.append(c)
                
        def get_sum(self):
            x=0
            y=0
            z=0
            for i in self.a:
                x+=i[0]
                y+=i[1]
                z+=i[2]
            return problem6()(x,y,z)    
    return NodeCloud    
                
            
def problem8():
    class Encoder:
        
        def __init__(self,x):
            self.a=x
            text=["a","b","c","d","e","f","g","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            b=""
            for i in self.a:
                if i in text:
                    b+=str(i)
                else:
                    continue
            self.a=b
            
        def __str__(self):
            return self.a
    
        def binary(self):
            b1=""
            for i in self.a:
                b1+='{:b}'.format(ord(str(i)))
            return b1
        
        def hex(self):
            b2=""
            for i in self.a:
                b2+='{:x}'.format(ord(str(i)))
            return b2    
        
        def morse(self):
            l={"A":".-","a":".-","b": "-...","B":"-...","C":"-.-.","c":"-.-.","d":"-..","D":"-..","E":".","e":".","F":"..-.","f":"..-.","g":"--.","G":"--.","H":"....","h":"....","I":"..","i":"..","j":".---","J":".---","K":"-.-","k":"-.-","l":".-..","L":".-..","M":"--","m":"--","N":"-.","n":"-.","O":"---","o":"---","P":".--.","p":".--.","Q":"--.-","q":"--.-","R":".-.","r":".-.","s":"...","S":"...","T":"-","t":"-","U":"..-","u":"..-","v":"...-","V":"...-","W":".--","w":".--","X":"-..-","x":"-..-","Y":"-.--","y":"-.--","Z":"--..","z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}
            b3=[]
            for i in self.a:
                b3.append(l[str(i)])
            return b3    
                                                                          
        
    return Encoder    
            



