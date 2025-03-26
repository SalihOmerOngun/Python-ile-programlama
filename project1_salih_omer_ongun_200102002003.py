 # -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 12:14:11 2021

@author: Salih Ömer Ongün
"""
my_name = "Salih Omer Ongun"
my_id = "200102002003"
my_email = "s.ongun2020@gtu.edu.tr"

import random


def generate(row,column):
    c=[]
    d=[]
    while True:
        for k in range(0,row*column):
            c.append(k)
            if len(d)!=row:
                if len(c)==column:
                    d.append(c)
                    c=[]
            elif len(d)==row:
                return d
    
    
def is_valid(board):
    n=0
    m=0
    a=[]
    while True:
        if n!=len(board)-1:   
            if m!=len(board[0])-1:
                i=str(board[n][m])
                a.append(i)
                m+=1
            else:
                i=str(board[n][m])
                a.append(i)
                m=0
                n+=1
        else:        
            if m!=len(board[0])-1:
                i=str(board[n][m])
                a.append(i)
                m+=1
            else:
                i=str(board[n][m])
                a.append(i)
                break    
    for n in a:
        if int(n)>=len(board[0])*len(board):
            
            return False
        if n==a[-1]:
            if int(n)>=len(board[0])*len(board):
                return False    
            else:
                for k in range(0,len(a)):
                    if a.count(a[k])==1:
                       if k==len(a)-1:
                           if a.count(a[k])==1:
                               return True
                           else:
                               return False
                       else:
                           continue
                    else:
                        return False
     
        
def is_solved(board):
    n=0
    m=0
    a=[]
    while True:
        if n!=len(board)-1:   
            if m!=len(board[0])-1:
                i=board[n][m]
                a.append(i)
                m+=1
            else:
                i=board[n][m]
                a.append(i)
                m=0
                n+=1
        else:        
            if m!=len(board[0])-1:
                i=board[n][m]
                a.append(i)
                m+=1
            else:
                i=board[n][m]
                a.append(i)
                break
    b=sorted(a)
    if a==b:
        return True
    else:
        return False  


def get_board_size(board):    
    return (len(board),len(board[0]))


      
def print_board(board):
    s=""
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
             s += str(board[i][j]) + "\t"
        s +='\n'
    return s        

def move_right(board):
    for m in range(0,len(board)):  
        if 0 in board[m]:       
            n=board[m].index(0)
            if n!=len(board[0])-1:
                c=board[m][n+1]
                board[m][n]=c
                board[m][n+1]=0
                return 1
            else:
                return 0  
    

def move_left(board): 
    for m in range(0,len(board)):
        if 0 in board[m]:    
            n=board[m].index(0)
            if n!=0:
                c=board[m][n-1]    
                board[m][n]=c
                board[m][n-1]=0
                return 1
            else:
                return 0
            
def move_up(board):
    for m in range(0,len(board)):        
        if 0 in board[m]:
            if m==0:
                return 0
            else:
                n=board[m].index(0)
                c=board[m-1][n]
                board[m-1][n]=0
                board[m][n]=c
                return 1
            
            
def move_down(board):
    for m in range(0,len(board)):        
        if 0 in board[m]:
            if m==len(board)-1:
                return 0
            else:
                n=board[m].index(0)
                c=board[m+1][n]
                board[m+1][n]=0
                board[m][n]=c
                return 1    


def move_up2(board):
    for m in range(0,len(board)):        
        if 0 in board[m]:
            if m==0:
                return board
            else:
                n=board[m].index(0)
                c=board[m-1][n]
                board[m-1][n]=0
                board[m][n]=c
                return board

def move_right2(board):
    for m in range(0,len(board)):  
        if 0 in board[m]:       
            n=board[m].index(0)
            if n!=len(board[0])-1:
                c=board[m][n+1]
                board[m][n]=c
                board[m][n+1]=0
                return board
            else:
                return board


def move_left2(board): 
    for m in range(0,len(board)):
        if 0 in board[m]:    
            n=board[m].index(0)
            if n!=0:
                c=board[m][n-1]    
                board[m][n]=c
                board[m][n-1]=0
                return board
            else:
                return board


def move_down2(board):
    for m in range(0,len(board)):        
        if 0 in board[m]:
            if m==len(board)-1:
                return board
            else:
                n=board[m].index(0)
                c=board[m+1][n]
                board[m+1][n]=0
                board[m][n]=c
                return board   
            
            
def move_random(board):
    for m in range(0,len(board)):  
        if 0 in board[m]:       
            n=board[m].index(0)
            if n==0 and m==0:
                b=["R","D"]
                c=random.choice(b)
                if c=="R":
                    board=move_right2(board)
                    return c
                if c=="D":
                    board=move_down2(board)
                    return c
            elif n==0 and m!=0 and m!=len(board)-1:
                b1=["U","R","D"]
                c=random.choice(b1)
                if c=="R":
                    board=move_right2(board)
                    return c
                if c=="D":
                    board=move_down2(board)
                    return c
                if c=="U":
                    board=move_up2(board)
                    return c
            elif n==0 and m==len(board)-1:
                b2=["R","U"]
                c=random.choice(b2)
                if c=="R":
                    board=move_right2(board)
                    return c
                if c=="U":
                    board=move_up2(board)
                    return c
            elif n==len(board[0])-1 and m==0:
                b3=["L","D"]
                c=random.choice(b3)
                if c=="L":
                    board=move_left2(board)
                    return c
                if c=="D":
                    board=move_down2(board)
                    return c
            elif n==len(board[0])-1 and m!=len(board)-1 and m!=0:    
                b4=["L","D","U"]    
                c=random.choice(b4)
                if c=="L":
                    board=move_left2(board)
                    return c
                if c=="D":
                    board=move_down2(board)
                    return c
                if c=="U":
                    board=move_up2(board)
                    return c
            elif n==len(board[0])-1 and m==len(board)-1:
                b5=["L","U"]
                c=random.choice(b5)
                if c=="L":
                    board=move_left2(board)
                    return c
                if c=="U":
                    board=move_up2(board)
                    return c
            elif n!=len(board[0])-1 and n!=0 and m==0:
                b6=["L","D","R"]
                c=random.choice(b6)    
                if c=="L":
                    board=move_left2(board)
                    return c
                if c=="D":
                    board=move_down2(board)
                    return c
                if c=="R":
                    board=move_right2(board)
                    return c
            elif n!=len(board[0])-1 and n!=0 and m==len(board)-1:
                b7=["L","U","R"]
                c=random.choice(b7)    
                if c=="L":
                    board=move_left2(board)
                    return c
                if c=="R":
                    board=move_right2(board)
                    return c
                if c=="U":
                    board=move_up2(board)
                    
                    return c
            else:
                b8=["L","U","R","D"]
                c=random.choice(b8)
                if c=="L":
                    board=move_left2(board)
                    return c
                if c=="R":
                    board=move_right2(board)
                    return c
                if c=="U":
                    board=move_up2(board)
                    return c
                if c=="D":
                    board=move_down2(board)
                    return c



def move(board, moves):
    a=0
    for k in moves:
        if k=="L" or k=="l":
            for m in range(0,len(board)):  
                if 0 in board[m]:       
                    n=board[m].index(0)
                    if n==0:
                        continue
                    else:
                        board=move_left2(board)        
                        a+=1
                        break
        elif k=="R" or k=="r":
            for m in range(0,len(board)):
                if 0 in board[m]:
                    n=board[m].index(0)
                    if n==len(board[0])-1:
                        continue
                    else:
                        board=move_right2(board)    
                        a+=1
                        break
        elif k=="D" or k=="d":
            for m in range(0,len(board)):
                if 0 in board[m]:
                    if m==len(board)-1:
                        continue
                    else:
                        board=move_down2(board)
                        a+=1
                        break
        elif k=="U" or k=="u":
            for m in range(0,len(board)):
                if 0 in board[m]:
                    if m==0:
                        continue
                    else:            
                        board=move_up2(board)    
                        a+=1
                        break
    return a  


   

def shuffle(board, times=20):
    a=0
    k=""
    while a<times:
        for m in range(0,len(board)):  
            if 0 in board[m]:       
                n=board[m].index(0)
                if n==0 and m==0:
                    b=["R","D"]
                    c=random.choice(b)
                    if c=="R":
                        board=move_right2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="D":
                        board=move_down2(board)
                        k+=c
                        a+=1
                        continue
                elif n==0 and m!=0 and m!=len(board)-1:
                    b1=["U","R","D"]
                    c=random.choice(b1)
                    if c=="R":
                        board=move_right2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="D":
                        board=move_down2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="U":
                        board=move_up2(board)
                        k+=c
                        a+=1
                        continue
                elif n==0 and m==len(board)-1:
                    b2=["R","U"]
                    c=random.choice(b2)
                    if c=="R":
                        board=move_right2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="U":
                        board=move_up2(board)
                        k+=c
                        a+=1
                        continue
                elif n==len(board[0])-1 and m==0:
                    b3=["L","D"]
                    c=random.choice(b3)
                    if c=="L":
                        board=move_left2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="D":
                        board=move_down2(board)
                        k+=c
                        a+=1
                        continue
                elif n==len(board[0])-1 and m!=len(board)-1 and m!=0:    
                    b4=["L","D","U"]    
                    c=random.choice(b4)
                    if c=="L":
                        board=move_left2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="D":
                        board=move_down2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="U":
                        board=move_up2(board)
                        k+=c
                        a+=1
                        continue
                elif n==len(board[0])-1 and m==len(board)-1:
                    b5=["L","U"]
                    c=random.choice(b5)
                    if c=="L":
                        board=move_left2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="U":
                        board=move_up2(board)
                        k+=c
                        a+=1
                        continue
                elif n!=len(board[0])-1 and n!=0 and m==0:
                    b6=["L","D","R"]
                    c=random.choice(b6)    
                    if c=="L":
                        board=move_left2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="D":
                        board=move_down2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="R":
                        board=move_right2(board)
                        k+=c
                        a+=1
                        continue
                elif n!=len(board[0])-1 and n!=0 and m==len(board)-1:
                    b7=["L","U","R"]
                    c=random.choice(b7)    
                    if c=="L":
                        board=move_left2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="R":
                        board=move_right2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="U":
                        board=move_up2(board)
                        k+=c
                        a+=1
                        continue
                else:
                    b8=["L","U","R","D"]
                    c=random.choice(b8)
                    if c=="L":
                        board=move_left2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="R":
                        board=move_right2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="U":
                        board=move_up2(board)
                        k+=c
                        a+=1
                        continue
                    if c=="D":
                        board=move_down2(board)
                        k+=c
                        a+=1
                        continue
                if is_solved(board)==True:
                      k=""
                      a=0
                      continue
    while a==times:
        return str(k)
    while a>times:
        return str(k[0:10])  
    


def reset(board):
    a=generate(len(board),len(board[0]))
    b=len(board)
    board.clear()
    for k in range(0,b):
        board.append(a[k])
   
def rotate(board):
    a=[]
    b=len(board)
    n=0
    for i in range(b):
        a.append([])
    for i in range(b):
        for j in range(b):
            a[i].insert(0,board[j][n])
            if j==b-1:
                n+=1
            if n==len(board[0]):
                return a
               

def play(board,moves):
    if is_valid(board)==False:
        return -2
    elif is_solved(board)==True:
        return 0
    else:
        a=0
        for k in moves:
            if k!=moves[-1]:
                print(print_board(board))
                if k=="L" or k=="l":
                    for m in range(0,len(board)):  
                        if 0 in board[m]:       
                            n=board[m].index(0)
                            if n==0:
                                continue
                            else:
                                board=move_left2(board)        
                                a+=1
                                if is_solved(board)==True:
                                    return a
                elif k=="R" or k=="r":
                    print(print_board(board))
                    for m in range(0,len(board)):
                        if 0 in board[m]:
                            n=board[m].index(0)
                            if n==len(board[0])-1:
                                continue
                            else:
                                print(print_board(board))
                                board=move_right2(board)    
                                a+=1
                                if is_solved(board)==True:
                                    print(print_board(board))
                                    return a
                elif k=="D" or k=="d":
                    for m in range(0,len(board)):
                        if 0 in board[m]:
                            if m==len(board)-1:
                                continue
                            else:
                                board=move_down2(board)
                                a+=1
                                if is_solved(board)==True:
                                    return a
                elif k=="U" or k=="u":
                    for m in range(0,len(board)):
                        if 0 in board[m]:
                            if m==0:
                                return -1
                            else:            
                                board=move_up2(board)    
                                a+=1
                                if is_solved(board)==True:
                                    return a
            if k==moves[-1]:
                if k=="L" or k=="l":
                    for m in range(0,len(board)):  
                        if 0 in board[m]:       
                            n=board[m].index(0)
                            if n==0:
                                return -1
                            else:
                                board=move_left2(board)        
                                a+=1
                                if is_solved(board)==True:
                                    return a
                                if is_solved(board)==False:
                                    return -1
                elif k=="R" or k=="r":
                    for m in range(0,len(board)):
                        if 0 in board[m]:
                            n=board[m].index(0)
                            if n==len(board[0])-1:
                                return -1
                            else:
                                board=move_right2(board)    
                                a+=1
                                if is_solved(board)==True:
                                    return a
                                if is_solved(board)==False:
                                    return -1
                elif k=="D" or k=="d":
                    for m in range(0,len(board)):
                        if 0 in board[m]:
                            if m==len(board)-1:
                                return -1
                            else:
                                board=move_down2(board)
                                a+=1
                                if is_solved(board)==True:
                                    return a
                                if is_solved(board)==False:
                                    return -1
                elif k=="U" or k=="u":
                    for m in range(0,len(board)):
                        if 0 in board[m]:
                            if m==0:
                                return -1
                            else:            
                                board=move_up2(board)    
                                a+=1
                                if is_solved(board)==True:
                                    return a
                                if is_solved(board)==False:
                                    return -1    
                                
                                
print(play([[1,3],[2,0]],"lrdruulld"))                              

def play_interactive(board=None):
   a=0
   p=""
   if board!=None:
       if is_valid(board)==False:
            return ('', -2)
       elif is_valid(board)==True:
           while is_solved(board)==False:
               k=str(input("Where do you want to move: "))
               if k=="L" or k=="l":
                   for m in range(0,len(board)):  
                       if 0 in board[m]:       
                           n=board[m].index(0)
                           if n==0:
                               continue
                           else:
                               board=move_left2(board)        
                               a+=1
                               p+="L"
               elif k=="R" or k=="r":
                   for m in range(0,len(board)):
                       if 0 in board[m]:
                           n=board[m].index(0)
                           if n==len(board[0])-1:
                               continue
                           else:
                               board=move_right2(board)    
                               a+=1
                               p+="R"
               elif k=="D" or k=="d":
                   for m in range(0,len(board)):
                       if 0 in board[m]:
                           if m==len(board)-1:
                               continue
                           else:
                               board=move_down2(board)
                               a+=1
                               p+="D"
               elif k=="U" or k=="u":
                   for m in range(0,len(board)):
                       if 0 in board[m]:
                           if m==0:
                               continue
                           else:            
                               board=move_up2(board)    
                               a+=1
                               p+="U"
               elif k=="M" or k=="m":
                   for m in range(0,len(board)):  
                       if 0 in board[m]:       
                            n=board[m].index(0)
                            if n==0 and m==0:
                                b=["R","D"]
                                c=random.choice(b)
                                if c=="R":
                                    board=move_right2(board)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board=move_down2(board)
                                    p+=c
                                    a+=1
                            elif n==0 and m!=0 and m!=len(board)-1:
                                b1=["U","R","D"]
                                c=random.choice(b1)
                                if c=="R":
                                    board=move_right2(board)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board=move_down2(board)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board=move_up2(board)
                                    p+=c
                                    a+=1
                            elif n==0 and m==len(board)-1:
                                b2=["R","U"]
                                c=random.choice(b2)
                                if c=="R":
                                    board=move_right2(board)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board=move_up2(board)
                                    p+=c
                                    a+=1
                            elif n==len(board[0])-1 and m==0:
                                b3=["L","D"]
                                c=random.choice(b3)
                                if c=="L":
                                    board=move_left2(board)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board=move_down2(board)
                                    p+=c
                                    a+=1
                            elif n==len(board[0])-1 and m!=len(board)-1 and m!=0:    
                                b4=["L","D","U"]    
                                c=random.choice(b4)
                                if c=="L":
                                    board=move_left2(board)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board=move_down2(board)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board=move_up2(board)
                                    p+=c
                                    a+=1
                            elif n==len(board[0])-1 and m==len(board)-1:
                                b5=["L","U"]
                                c=random.choice(b5)
                                if c=="L":
                                    board=move_left2(board)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board=move_up2(board)
                                    return c
                                    a+=1
                            elif n!=len(board[0])-1 and n!=0 and m==0:
                                b6=["L","D","R"]
                                c=random.choice(b6)    
                                if c=="L":
                                    board=move_left2(board)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board=move_down2(board)
                                    p+=c
                                    a+=1
                                if c=="R":
                                    board=move_right2(board)
                                    p+=c
                                    a+=1
                            elif n!=len(board[0])-1 and n!=0 and m==len(board)-1:
                                b7=["L","U","R"]
                                c=random.choice(b7)    
                                if c=="L":
                                    board=move_left2(board)
                                    p+=c
                                    a+=1
                                if c=="R":
                                    board=move_right2(board)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board=move_up2(board)
                                    p+=c
                                    a+=1
                            else:
                                b8=["L","U","R","D"]
                                c=random.choice(b8)
                                if c=="L":
                                    board=move_left2(board)
                                    p+=c
                                    a+=1
                                if c=="R":
                                    board=move_right2(board)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board=move_up2(board)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board=move_down2(board)
                                    p+=c
                                    a+=1
               elif k=="Q" or k=="q":
                   return (str(p),-1)
               else:
                   print("Wrong move.")
                   continue
           while is_solved(board)==True:
             print(print_board(board))
             print(a)
             return (p,a)
   if board==None:
       a1=str(input("Row number: "))
       b1=str(input("Column number: "))
       board1=generate(int(a1),int(b1))
       y=shuffle(board1)
       while is_solved(board1)==False:
               k=str(input("Where do you want to move: "))
               if k=="L" or k=="l":
                   for m in range(0,len(board1)):  
                       if 0 in board1[m]:       
                           n=board1[m].index(0)
                           if n==0:
                               continue
                           else:
                               board1=move_left2(board1)        
                               a+=1
                               p+="L"
               elif k=="R" or k=="r":
                   for m in range(0,len(board1)):
                       if 0 in board1[m]:
                           n=board1[m].index(0)
                           if n==len(board1[0])-1:
                               continue
                           else:
                               board1=move_right2(board1)    
                               a+=1
                               p+="R"
               elif k=="D" or k=="d":
                   for m in range(0,len(board1)):
                       if 0 in board1[m]:
                           if m==len(board1)-1:
                               continue
                           else:
                               board1=move_down2(board1)
                               a+=1
                               p+="D"
               elif k=="U" or k=="u":
                   for m in range(0,len(board1)):
                       if 0 in board1[m]:
                           if m==0:
                               continue
                           else:            
                               board1=move_up2(board1)    
                               a+=1
                               p+="U"
               elif k=="M" or k=="m":
                   for m in range(0,len(board1)):  
                       if 0 in board1[m]:       
                            n=board1[m].index(0)
                            if n==0 and m==0:
                                b=["R","D"]
                                c=random.choice(b)
                                if c=="R":
                                    board1=move_right2(board1)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board1=move_down2(board1)
                                    p+=c
                                    a+=1
                            elif n==0 and m!=0 and m!=len(board1)-1:
                                b1=["U","R","D"]
                                c=random.choice(b1)
                                if c=="R":
                                    board1=move_right2(board1)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board1=move_down2(board1)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board1=move_up2(board1)
                                    p+=c
                                    a+=1
                            elif n==0 and m==len(board1)-1:
                                b2=["R","U"]
                                c=random.choice(b2)
                                if c=="R":
                                    board1=move_right2(board1)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board1=move_up2(board1)
                                    p+=c
                                    a+=1
                            elif n==len(board1[0])-1 and m==0:
                                b3=["L","D"]
                                c=random.choice(b3)
                                if c=="L":
                                    board1=move_left2(board1)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board1=move_down2(board1)
                                    p+=c
                                    a+=1
                            elif n==len(board1[0])-1 and m!=len(board1)-1 and m!=0:    
                                b4=["L","D","U"]    
                                c=random.choice(b4)
                                if c=="L":
                                    board1=move_left2(board1)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board1=move_down2(board1)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board1=move_up2(board1)
                                    p+=c
                                    a+=1
                            elif n==len(board1[0])-1 and m==len(board1)-1:
                                b5=["L","U"]
                                c=random.choice(b5)
                                if c=="L":
                                    board1=move_left2(board1)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board1=move_up2(board1)
                                    return c
                                    a+=1
                            elif n!=len(board1[0])-1 and n!=0 and m==0:
                                b6=["L","D","R"]
                                c=random.choice(b6)    
                                if c=="L":
                                    board1=move_left2(board1)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board1=move_down2(board1)
                                    p+=c
                                    a+=1
                                if c=="R":
                                    board1=move_right2(board1)
                                    p+=c
                                    a+=1
                            elif n!=len(board1[0])-1 and n!=0 and m==len(board1)-1:
                                b7=["L","U","R"]
                                c=random.choice(b7)    
                                if c=="L":
                                    board1=move_left2(board1)
                                    p+=c
                                    a+=1
                                if c=="R":
                                    board1=move_right2(board1)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board1=move_up2(board1)
                                    p+=c
                                    a+=1
                            else:
                                b8=["L","U","R","D"]
                                c=random.choice(b8)
                                if c=="L":
                                    board1=move_left2(board1)
                                    p+=c
                                    a+=1
                                if c=="R":
                                    board1=move_right2(board1)
                                    p+=c
                                    a+=1
                                if c=="U":
                                    board1=move_up2(board1)
                                    p+=c
                                    a+=1
                                if c=="D":
                                    board1=move_down2(board1)
                                    p+=c
                                    a+=1
               elif k=="Q" or k=="q":
                   return (str(p),-1)
               else:
                   print("Wrong move.")
                   continue
       while is_solved(board1)==True:
           print(print_board(board1))
           print(a)
           return (p,a)                                
                                



