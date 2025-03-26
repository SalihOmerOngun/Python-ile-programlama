# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 12:45:43 2021

@author: Salih Ömer Ongün
"""
my_name = "Salih Omer Ongun"
my_id = "200102002003"
my_email = "s.ongun2020@gtu.edu.tr"


import random

def generate_random(row, column):
    a=[]
    b=[]
    l={}
    while True:
        if len(b)!=row:
            if len(a)!=column:
                k=random.randint(0,255)
                l["red"]=k
                k1=random.randint(0,255)
                l["green"]=k1
                k2=random.randint(0,255)
                l["blue"]=k2
                a.append(l)
                l={}
            if len(a)==column:
                b.append(a)
                a=[]
        if len(b)==row:
            return b
            
         

def is_valid(img):
    for i in img:
        for j in i:
            a=j["red"]
            if a>0 and a<255 and type(a)==int:
                a1=j["green"]
                if a1>0 and a1<255 and type(a1)==int:
                    a2=j["blue"]
                    if a2>0 and a2<255 and type(a2)==int:
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                return False
    return True          



def finddec(x):
    a=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    for i in range(len(a)):
        if x==a[i]:
            return i


def hexdec(y):
    a1=0
    b1=0
    for i in range(len(y),0,-1):
        a1+=(16**b1)*finddec(y[i-1])
        b1+=1
        
    return int(a1)   


def read_from_file(filename):
    x=[]
    l={}
    y=[]
    f=open(filename,"r")
    while True:
        a=f.readline()
        b=a.strip()
        c=b.split(",")
        if c==['']:
            break
        else:
            for i in range(0,len(c)):
                l["red"]=hexdec(c[i][0:2])
                l["green"]=hexdec(c[i][2:4])
                l["blue"]=hexdec(c[i][4:6])
                x.append(l)
                l={}
                if len(x)==len(c):
                    y.append(x)
                    x=[]
                else:
                    continue
    f.close()            
    return y


def clear(img):
    for i in img:
        for j in i:
            j["red"]=0
            j["green"]=0
            j["blue"]=0
    return None        


def set_value(img, value, channel='rgb'):
    if channel=="rgb":
        for i in img:
            for j in i:
                j["red"]=value
                j["green"]=value
                j["blue"]=value
    if channel=="r":             
        for i in img:
            for j in i:
                j["red"]=value
    if channel=="g":            
        for i in img:
            for j in i:
                j["green"]=value  
    if channel=="b":            
        for i in img:
            for j in i:
                j["blue"]=value
    if channel=="rg":            
       for i in img:
           for j in i:
               j["red"]=value
               j["green"]=value           
    if channel=="rb":            
        for i in img:
            for j in i:
                j["red"]=value
                j["blue"]=value                
    if channel=="gb":            
        for i in img:
            for j in i:
                j["green"]=value 
                j["blue"]=value
    return None                

           
def fix(img):
    for i in img:
        for j in i:
            if j["red"]>255:
                j["red"]=255
            elif j["red"]<0:
                j["red"]=0
            elif j["red"]!=int(j["red"]):
                j["red"]=round(j["red"])
            if j["green"]>255:
                j["green"]=255
            elif j["green"]<0:
                j["green"]=0
            elif j["green"]!=int(j["green"]):
               j["green"]=round(j["green"])
            if j["blue"]>255:
                j["blue"]=255
            elif j["blue"]<0:
                j["blue"]=0
            elif j["blue"]!=int(j["blue"]):
                j["blue"]=round(j["blue"])
    return None

    
def rotate90(img):
    a=[]
    b=len(img)
    n=0
    for i in range(len(img[0])):
        a.append([])
    for i in range(len(img[0])):
        for j in range(b):
            a[i].insert(0,img[j][n])
            if j==b-1:
                n+=1
            if n==len(img[0]):
                fix(a)
                return a
  
        
def rotate180(img):
    x=rotate90(img)
    y=rotate90(x)
    fix(y)
    return y


def rotate270(img):
    x=rotate90(img)
    y=rotate90(x)
    z=rotate90(y)
    fix(z)
    return z        
               
        
def mirror_x(img):
    if len(img[0])%2==0:
        for i in range(0,len(img)):
            for j in range(0,int(len(img[0])/2)):
                a=img[i][j]    
                b=img[i][(j*-1)-1]
                img[i][j]=b
                img[i][(j*-1)-1]=a
    if len(img[0])%2!=0:            
        for i in range(0,len(img)):
            for j in range(0,int(len(img[0])/2)):
                a=img[i][j]    
                b=img[i][(j*-1)-1]
                img[i][j]=b
                img[i][(j*-1)-1]=a 
    fix(img)            
    return None   
        
                
def mirror_y(img):    
    if len(img)%2==0:
        for i in range(0,len(img[0])):
            for j in range(0,int(len(img)/2)):
                a=img[j][i]
                b=img[(j*-1)-1][i]
                img[j][i]=b
                img[(j*-1)-1][i]=a
    if len(img)%2!=0:
        for i in range(0,len(img[0])):            
            for j in range(0,int(len(img)/2)):
                a=img[j][i]
                b=img[(j*-1)-1][i]
                img[j][i]=b
                img[(j*-1)-1][i]=a  
    fix(img)            
    return None            
                            
                
                    
def enhance(img, value, channel='rgb'):
    if channel=="rgb":
        for i in img:
            for j in i:
                j["red"]=round(value*j["red"])
                j["green"]=round(value*j["green"])
                j["blue"]=round(value*j["blue"])   
    if channel=="r":             
        for i in img:
            for j in i:
                j["red"]=round(value*j["red"])
    if channel=="g":            
        for i in img:
            for j in i:
                j["green"]=round(value*j["green"])  
    if channel=="b":            
        for i in img:
            for j in i:
                j["blue"]=round(value*j["blue"])
    if channel=="rg":            
       for i in img:
           for j in i:
               j["red"]=round(value*j["red"])
               j["green"]=round(value*j["green"])          
    if channel=="rb":            
        for i in img:
            for j in i:
                j["red"]=round(value*j["red"])
                j["blue"]=round(value*j["blue"])                
    if channel=="gb":            
        for i in img:
            for j in i:
                j["green"]=round(value*j["green"])
                j["blue"]=round(value*j["blue"])                      
    fix(img)            
    return None            


                
def grayscale(img, mode=1):
    if mode==1:    
        for i in img:
            for j in i:
                a=round((j["red"]+j["green"]+j["blue"])/3)
                j["red"]=a
                j["green"]=a
                j["blue"]=a
    if mode==2:
        for i in img:
            for j in i:        
                a=round(0.299*j["red"]+0.587*j["green"]+0.114*j["blue"])    
                j["red"]=a
                j["green"]=a
                j["blue"]=a
    if mode==3:            
        for i in img:
            for j in i:
                a=round(0.2126*j["red"]+0.7152*j["green"]+0.0722*j["blue"])
                j["red"]=a
                j["green"]=a
                j["blue"]=a
    if mode==4:
        for i in img:
            for j in i:
                a=round(0.2627*j["red"]+0.6780*j["green"]+0.0593*j["blue"])                
                j["red"]=a
                j["green"]=a
                j["blue"]=a
    fix(img)                
    return None 

     
               
def scale_down(img, N):
    a1=[]
    b1=[]
    l={}
    a=len(img)
    b=len(img[0])
    c=0
    d=0
    e=0
    f=0
    g=0
    e1=0
    f1=0
    g1=0
    N1=N
    N2=N
    while True:
        if len(b1)==len(img)/N or len(b1)==int(len(img)/N)+1:
            fix(b1)
            return b1
        else:
            if a>=N:
                if b>=N:
                    for i in range(c,N1):
                        for j in range(d,N2):
                            e+=img[i][j]["red"]
                            e1+=1
                            f+=img[i][j]["green"]
                            f1+=1
                            g+=img[i][j]["blue"]
                            g1+=1
                    l["red"]=round(e/e1)    
                    e=0
                    e1=0
                    l["green"]=round(f/f1)
                    f=0
                    f1=0
                    l["blue"]=round(g/g1)
                    g=0
                    g1=0
                    a1.append(l)
                    l={}
                    b=b-N
                    d+=N
                    N2+=N
                    if len(a1)==len(img[0])/N or len(a1)==int(len(img[0])/N)+1:
                        b1.append(a1)
                        a1=[]
                        c+=N
                        N1+=N
                        d=0
                        b=len(img[0])
                        N2=N
                        a=a-N
                    continue
                else:
                    for i in range(c,N1):
                        for j in range(d,len(img[0])):
                            e+=img[i][j]["red"]
                            e1+=1
                            f+=img[i][j]["green"]
                            f1+=1
                            g+=img[i][j]["blue"]
                            g1+=1      
                    l["red"]=round(e/e1)    
                    e=0
                    e1=0
                    l["green"]=round(f/f1)
                    f=0
                    f1=0
                    l["blue"]=round(g/g1)
                    g=0
                    g1=0
                    a1.append(l)
                    l={}
                    b=b-N
                    d+=N
                    if len(a1)==len(img[0])/N or len(a1)==int(len(img[0])/N)+1:
                        b1.append(a1)
                        a1=[]
                        c+=N
                        N1+=N
                        b=len(img[0])
                        d=0
                        N2=N
                        a=a-N
                    continue  
            else:
                if b>=N:
                    for i in range(c,len(img)):
                        for j in range(d,N2):
                            e+=img[i][j]["red"]
                            e1+=1
                            f+=img[i][j]["green"]
                            f1+=1
                            g+=img[i][j]["blue"]
                            g1+=1        
                    l["red"]=round(e/e1)    
                    e=0
                    e1=0
                    l["green"]=round(f/f1)
                    f=0
                    f1=0
                    l["blue"]=round(g/g1)
                    g=0
                    g1=0
                    a1.append(l)
                    l={}
                    b=b-N
                    d+=N
                    N2+=N
                    if len(a1)==len(img[0])/N or len(a1)==int(len(img[0])/N)+1:
                        b1.append(a1)
                        a1=[]
                        c+=N
                        N1+=N
                        d=0
                        b=len(img[0])
                        N2=N
                        a=a-N
                    continue
                else:
                    for i in range(c,len(img)):
                        for j in range(d,len(img[0])):
                            e+=img[i][j]["red"]
                            e1+=1
                            f+=img[i][j]["green"]
                            f1+=1
                            g+=img[i][j]["blue"]
                            g1+=1               
                    l["red"]=round(e/e1)    
                    e=0
                    e1=0
                    l["green"]=round(f/f1)
                    f=0
                    f1=0
                    l["blue"]=round(g/g1)
                    g=0
                    g1=0
                    a1.append(l)
                    l={}
                    b=b-N
                    d+=N
                    if len(a1)==len(img[0])/N or len(a1)==int(len(img[0])/N)+1:
                        b1.append(a1)
                        a1=[]
                        c+=N
                        N1+=N
                        d=0
                        b=len(img[0])
                        N2=N
                        a=a-N
                    continue    
        
def scale_up(img, N):
    p=0
    m=0
    a=[]
    for i in range(0,len(img)):
        a.append([])     
    for i in range(0,len(img)):
        for j in range(0,len(img[0])):
            for k in range(0,N):
                a[p].insert(m,img[i][j])  
                m+=1
        m=0
        for k in range(0,N-1):
            a.insert(p,a[p])    
        p+=N     
    return a      
                        
                

def apply_window(img, window):
    
    a1=0
    b1=0
    c1=0
    b=[[],[],[]]
    a=[]
    l={}
    for i in range(0,len(img)):
        a.append([])
    for i in range(0,len(img)):
        for j in range(0,len(img[0])):
            if i==0 and j==0:
              b[0].append(img[i][j])
              b[0].append(img[i][j])
              b[0].append(img[i][j+1])
              b[1].append(img[i][j])
              b[1].append(img[i][j])
              b[1].append(img[i][j+1])
              b[2].append(img[i+1][j])
              b[2].append(img[i+1][j])
              b[2].append(img[i+1][j+1])
              for i1 in range(0,len(b)):
                  for j1 in range(0,len(b[0])):
                      a1+=window[i1][j1]*b[i1][j1]["red"]
                      b1+=window[i1][j1]*b[i1][j1]["green"]
                      c1+=window[i1][j1]*b[i1][j1]["blue"]
              l["red"]=round(a1)        
              l["green"]=round(b1)
              l["blue"]=round(c1)
              a[0].append(l)
              l={}
              a1=0
              b1=0
              c1=0
              b=[[],[],[]]
              continue
            if i==0 and j==len(img[0])-1:  
              b[0].append(img[i][j-1])
              b[0].append(img[i][j])
              b[0].append(img[i][j])
              b[1].append(img[i][j-1])
              b[1].append(img[i][j])
              b[1].append(img[i][j])
              b[2].append(img[i+1][j-1])
              b[2].append(img[i+1][j])
              b[2].append(img[i+1][j])    
              for i1 in range(0,len(b)):
                  for j1 in range(0,len(b[0])):
                      a1+=window[i1][j1]*b[i1][j1]["red"]
                      b1+=window[i1][j1]*b[i1][j1]["green"]
                      c1+=window[i1][j1]*b[i1][j1]["blue"]
              l["red"]=round(a1)        
              l["green"]=round(b1)
              l["blue"]=round(c1)
              a[0].insert(j,l)
              l={}
              a1=0
              b1=0
              c1=0        
              b=[[],[],[]]
              continue
            elif i==len(img)-1 and j==0:
                b[0].append(img[i-1][j])
                b[0].append(img[i-1][j])
                b[0].append(img[i-1][j+1])
                b[1].append(img[i][j])
                b[1].append(img[i][j])
                b[1].append(img[i][j+1])
                b[2].append(img[i][j])
                b[2].append(img[i][j])
                b[2].append(img[i][j+1])
                for i1 in range(0,len(b)):
                    for j1 in range(0,len(b[0])):
                        a1+=window[i1][j1]*b[i1][j1]["red"]
                        b1+=window[i1][j1]*b[i1][j1]["green"]
                        c1+=window[i1][j1]*b[i1][j1]["blue"]
                l["red"]=round(a1)        
                l["green"]=round(b1)
                l["blue"]=round(c1)
                a[i].insert(j,l)
                l={}
                a1=0
                b1=0
                c1=0
                b=[[],[],[]]
                continue
            elif i==len(img)-1 and j==len(img[0])-1:
               b[0].append(img[i-1][j-1])
               b[0].append(img[i-1][j])
               b[0].append(img[i-1][j])
               b[1].append(img[i][j-1])
               b[1].append(img[i][j])
               b[1].append(img[i][j])
               b[2].append(img[i][j-1])
               b[2].append(img[i][j])
               b[2].append(img[i][j])
               for i1 in range(0,len(b)):
                   for j1 in range(0,len(b[0])):
                       a1+=window[i1][j1]*b[i1][j1]["red"]
                       b1+=window[i1][j1]*b[i1][j1]["green"]
                       c1+=window[i1][j1]*b[i1][j1]["blue"]
               l["red"]=round(a1)        
               l["green"]=round(b1)
               l["blue"]=round(c1)
               a[i].insert(j,l)
               l={}
               a1=0
               b1=0
               c1=0
               b=[[],[],[]] 
               continue
            elif i==0 and j!=0 and j!=len(img[0])-1:
               b[0].append(img[i][j-1])
               b[0].append(img[i][j])
               b[0].append(img[i][j+1])
               b[1].append(img[i][j-1])
               b[1].append(img[i][j])
               b[1].append(img[i][j+1])
               b[2].append(img[i+1][j-1])
               b[2].append(img[i+1][j])
               b[2].append(img[i+1][j+1])
               for i1 in range(0,len(b)):
                   for j1 in range(0,len(b[0])):
                       a1+=window[i1][j1]*b[i1][j1]["red"]
                       b1+=window[i1][j1]*b[i1][j1]["green"]
                       c1+=window[i1][j1]*b[i1][j1]["blue"]
               l["red"]=round(a1)        
               l["green"]=round(b1)
               l["blue"]=round(c1)
               a[i].insert(j,l)
               l={}
               a1=0
               b1=0
               c1=0
               b=[[],[],[]]
               continue
            elif i==len(img)-1 and j!=0 and j!=len(img[0])-1:
               b[0].append(img[i-1][j-1])
               b[0].append(img[i-1][j])
               b[0].append(img[i-1][j+1])
               b[1].append(img[i][j-1])
               b[1].append(img[i][j])
               b[1].append(img[i][j+1])
               b[2].append(img[i][j-1])
               b[2].append(img[i][j])
               b[2].append(img[i][j+1])
               for i1 in range(0,len(b)):
                   for j1 in range(0,len(b[0])):
                       a1+=window[i1][j1]*b[i1][j1]["red"]
                       b1+=window[i1][j1]*b[i1][j1]["green"]
                       c1+=window[i1][j1]*b[i1][j1]["blue"]
               l["red"]=round(a1)        
               l["green"]=round(b1)
               l["blue"]=round(c1)
               a[i].insert(j,l)
               l={}
               a1=0
               b1=0
               c1=0
               b=[[],[],[]]
               continue
            elif i!=0 and i!=len(img)-1 and j==0:
               b[0].append(img[i-1][j])
               b[0].append(img[i-1][j])
               b[0].append(img[i-1][j+1])
               b[1].append(img[i][j])
               b[1].append(img[i][j])
               b[1].append(img[i][j+1])
               b[2].append(img[i+1][j])
               b[2].append(img[i+1][j])
               b[2].append(img[i+1][j+1])
               for i1 in range(0,len(b)):
                   for j1 in range(0,len(b[0])):
                       a1+=window[i1][j1]*b[i1][j1]["red"]
                       b1+=window[i1][j1]*b[i1][j1]["green"]
                       c1+=window[i1][j1]*b[i1][j1]["blue"]
               l["red"]=round(a1)        
               l["green"]=round(b1)
               l["blue"]=round(c1)
               a[i].insert(j,l)
               l={}
               a1=0
               b1=0
               c1=0
               b=[[],[],[]]
               continue
            elif i!=0 and i!=len(img)-1 and j==len(img[0])-1: 
               b[0].append(img[i-1][j-1])
               b[0].append(img[i-1][j])
               b[0].append(img[i-1][j])
               b[1].append(img[i][j-1])
               b[1].append(img[i][j])
               b[1].append(img[i][j])
               b[2].append(img[i+1][j-1])
               b[2].append(img[i+1][j])
               b[2].append(img[i+1][j])
               for i1 in range(0,len(b)):
                   for j1 in range(0,len(b[0])):
                       a1+=window[i1][j1]*b[i1][j1]["red"]
                       b1+=window[i1][j1]*b[i1][j1]["green"]
                       c1+=window[i1][j1]*b[i1][j1]["blue"]
               l["red"]=round(a1)        
               l["green"]=round(b1)
               l["blue"]=round(c1)
               a[i].insert(j,l)
               l={}
               a1=0
               b1=0
               c1=0
               b=[[],[],[]]     
               continue
            else:
                b[0].append(img[i-1][j-1])
                b[0].append(img[i-1][j])
                b[0].append(img[i-1][j+1])
                b[1].append(img[i][j-1])
                b[1].append(img[i][j])
                b[1].append(img[i][j+1])
                b[2].append(img[i+1][j-1])
                b[2].append(img[i+1][j])
                b[2].append(img[i+1][j+1])
                for i1 in range(0,len(b)):
                    for j1 in range(0,len(b[0])):
                        a1+=window[i1][j1]*b[i1][j1]["red"]
                        b1+=window[i1][j1]*b[i1][j1]["green"]
                        c1+=window[i1][j1]*b[i1][j1]["blue"]
                l["red"]=round(a1)        
                l["green"]=round(b1)
                l["blue"]=round(c1)
                a[i].insert(j,l)
                l={}
                a1=0
                b1=0
                c1=0
                b=[[],[],[]]
                continue
    y=fix(a)        
    return a         



def dechex(x):
    if len(hex(x))>3:
        return hex(x)[2:len(hex(x))]
    else:
        return "0"+hex(x)[-1]
    
    

def write_to_file(img, filename):
    with open(filename,"a") as f:
        n=0
        a=""
        for i in img:
            for j in i:
                n+=1
                if n==len(img[0]):
                    a+=str(dechex(j["red"]))
                    a+=str(dechex(j["green"]))
                    a+=str(dechex(j["blue"]))
                    n=0
                else:
                    a+=str(dechex(j["red"]))
                    a+=str(dechex(j["green"]))
                    a+=str(dechex(j["blue"]))+","
            a+="\n"
            f.write(a)
            a=""
        return None
           

def get_freq(img, channel='rgb', bin_size=16):
    red=[]
    red1=[]
    red2=[]
    blue=[]
    blue1=[]
    blue2=[]
    green=[]
    green1=[]
    green2=[]     
    l={}
    l["bin_size"]=bin_size
    if "r" in channel:             
        for i in img:
            for j in i:
                a1=int(j["red"]/bin_size)
                red.append(a1)
        for i in range(0,max(red)+1):
            k=red.count(i)
            if k!=0:
                if i in red2:
                    continue
                else:
                    red2.append(i)
                    red1.insert(i,k)
            else:         
                red1.insert(i,k)        
    if "g" in channel:            
        for i in img:
            for j in i:
                a2=int(j["green"]/bin_size)
                green.append(a2) 
        for i in range(0,max(green)+1):
            k=green.count(i)
            if k!=0:
                if i in green2:
                    continue
                else:
                    green2.append(i)
                    green1.insert(i,k)
            else:         
                green1.insert(i,k)        
    if "b" in channel:            
        for i in img:
            for j in i:
                a3=int(j["blue"]/bin_size)
                blue.append(a3)          
        for i in range(0,max(blue)+1):
            k=blue.count(i)
            if k!=0:
                if i in blue2:
                    continue
                else:
                    blue2.append(i)
                    blue1.insert(i,k)
            else:         
                blue1.insert(i,k)
    if len(red1)!=0:
        for p in range(len(red1),int(255/bin_size)+1):
            red1.append(0)
        l["red"]=red1    
    if len(green1)!=0:
        for p in range(len(green1),int(255/bin_size)+1):
            green1.append(0)
        l["green"]=green1
    if len(blue1)!=0:
        for p in range(len(blue1),int(255/bin_size)+1):
            blue1.append(0)
        l["blue"]=blue1    
    return l                    