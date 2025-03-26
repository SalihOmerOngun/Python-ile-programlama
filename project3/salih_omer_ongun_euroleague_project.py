

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 17:25:00 2021

@author: Salih Ömer Ongün
"""




import random

class Person:
    
    def __init__(self,name, lastname):
        self.a=name
        self.b=lastname
        
    def get_name(self):
        return str(self.a)+" "+str(self.b)
    
    def __str__(self):
        return str(self.a)+" "+str(self.b)
    
    def __lt__(self,another):
        if self.b==another.b:
            if self.a<another.a:
                return True
            else:
                return False
        else:
            if self.b<another.b:
                return True
            else:
                return False
            
            
class Player(Person):
    say=0
    def __init__(self,name, lastname):
         Person.__init__(self, name, lastname)  
         Player.say+=1
         self.id=Player.say
         self.mypower=random.randint(4,8)
         self.team=""
         self.pointlist=[]
         self.point=0
           
    def get_id(self):
        return self.id          
    
    def set_team(self,t):
        self.team=t.__str__()

    def get_team(self):
        return self.team 
    
    def add_to_points(self,x):
        pass
        
    def get_power(self):
        return self.mypower
    
        
    def get_points_detailed(self):
        return self.pointlist
    

    def get_points(self):
        return sum(self.pointlist)

 
    def reset(self):
        self.pointlist=[]

    
        
    def __lt__(self,another):
        if self.get_points()!=another.get_points():
            if self.get_points()<another.get_points():
                return True
            else:
                return False
        else:
            if self.b==another.b:
                if self.a<another.a:
                    return True
                else:
                    return False
            else:
                if self.b<another.b:
                    return True
                else:
                    return False    
        
        
class Manager(Person):
    say=0
    def __init__(self,name, lastname):
        Person.__init__(self, name, lastname)
        Manager.say+=1
        self.id=Manager.say
        self.team=""
        self.inflist=[]
        
    def get_id(self):
        return self.id
        
    def set_team(self,t):
        self.team=t.__str__()
            
    def get_team(self):
        return self.team       
    
    def get_influence_detailed(self): 
        return self.inflist
    
    def get_influence(self):
        return sum(self.inflist)
    
    def reset(self):
        self.inflist=[]
    
    def __lt__(self,another):
        if self.get_influence()!=another.get_influence():
            if self.get_influence()<another.get_influence():
                return True
            else:
                return False
        else:
            if self.b==another.b:
                if self.a<another.a:
                    return True
                else:
                    return False
            else:
                if self.b<another.b:
                    return True
                else:
                    return False
            
        
class Team:
    say=0
    def __init__(self,teamname, manager, players):
        Team.say+=1
        self.id=Team.say
        self.a=teamname
        self.b=manager
        self.c=players
        self.teamscore=0
        self.teamconceded=0
        self.teamwin=0
        self.teamlosses=0
        
    def get_id(self):
        return self.id
     
    def get_name(self):
        return self.a
    
    def reset(self):
        self.b.inflist=[]
        for i in self.c:
            i.pointlist=[]
        self.tl=[]    
        self.teamscore=0
        self.teamconceded=0
        self.teamwin=0
        self.teamlosses=0
        
    def add_to_fixture(self,m):
        pass
    
    def get_roster(self):
        d=[]
        for i in self.c:
            d.append(i)
        return d    
    
    def get_manager(self):
        return self.b
    
    def get_fixture(self):
        self.tl=[]
        for i in range(1,len(Season.fixdict)+1):
            for i in Season.fixdict["week"+str(i)]:
                if i.get_home_team().get_name()==self.a or i.get_away_team().get_name()==self.a:
                    self.tl.append(i)
        return self.tl 

    def add_result(self,s):
        self.teamscore+=s[0]
        self.teamconceded+=s[1]
        if s[0]>s[1]:
            self.teamwin+=1
        elif s[1]<s[0]:
            self.teamlosses+=1
          

    def __str__(self):
        return str(self.a)
    
    def get_scored(self):
        return self.teamscore
    
    def get_conceded(self):
        return self.teamconceded
    
    def get_wins(self):
        return self.teamwin
    
    def get_losses(self):
        return self.teamlosses
  
    def __lt__(self,another):
        if self.teamwin!= another.teamwin:
              if self.teamwin< another.teamwin:
                  return True
              else:
                  return False
        elif self.teamwin== another.teamwin:
           if  (int(self.teamscore)-int(self.teamconceded))<(int(another.teamscore)-int(another.teamconceded)):
               return True
           else:
               return False
        else:
            return True
        
    
class Match:
    
    def __init__(self,home_team, away_team, week_no):
        self.home=home_team
        self.away=away_team
        self.week=week_no
        self.played="not finished"
    
    def is_played(self):
        if self.played=="finished":
            return True
        else:
            return False
    
    def play(self):
        self.played="finished"
        self.away_point=0
        self.home_point=0
        k=random.randint(-10, 10)
        home_manager_point =k
        self.home.get_manager().inflist.append(k)
        k=random.randint(-10, 10)
        away_manager_point =k            
        self.away.get_manager().inflist.append(k)
        self.home_point += home_manager_point
        self.away_point += away_manager_point
        for i in range(1,5):
            for i in self.home.get_roster():
                k=random.randint(-5, 5)+i.get_power()
                self.home_point+=k
                i.point+=k
            for i in self.away.get_roster():
                k=random.randint(-5, 5)+i.get_power()
                self.away_point+=k  
                i.point+=k
        while self.home_point==self.away_point:
            for i in self.home.get_roster():
                k=random.randint(-5, 5)
                self.home_point+=k
                i.point+=k
            for i in self.away.get_roster(): 
                k=random.randint(-5, 5)
                self.away_point+=k      
                i.point+=k
        for i in self.home.get_roster():
            i.pointlist.append(i.point)
            i.point=0
        for i in self.away.get_roster():
            i.pointlist.append(i.point)
            i.point=0
        self.gen_teamdict()    
   
        
    def gen_teamdict(self):    
       self.home.teamscore+=self.home_point    
       self.away.teamscore+=self.away_point
       self.home.teamconceded+=self.away_point
       self.away.teamconceded+=self.home_point      
       if self.home_point>self.away_point:
           self.home.teamwin+=1
           self.away.teamlosses+=1
       else:    
           self.away.teamwin+=1
           self.home.teamlosses+=1
           
        
    def get_match_score(self):
         return (self.home_point,self.away_point)

    def get_teams(self):
        return (self.home,self.away)           
    
    def get_home_team(self):
        return self.home    
    
    def get_away_team(self):
        return self.away
    
    def __str__(self):
        if self.is_played() is True:
            return str(self.home)+" "+"("+str(self.home_point)+")"+" vs. "+"("+str(self.away_point)+")"+" "+str(self.away)
        else:
            return str(self.home)+" "+" vs. "+" "+str(self.away)
    
    def get_winner(self):
        if self.is_played() is True:
            if self.home_point>self.away_point:
                return self.home
            else:
                return self.away
        else:
            return None
                
class Season:
    teamlist=[]
    fixdict={}
    mycount=0
    player=[]
    manager=[]
    bestteam=[]
    def __init__(self,teams, managers, players):
        Season.teamlist=[]
        Season.bestteam=[]
        Season.manager=[]
        Season.player=[]
        Season.mycount=0
        self.a=[]
        self.a1=[]
        self.a2=[]
        playerslist=[]
        with open(players,"r") as f:
            for i in f:
                b=i.strip("\n").split()
                self.a.append(Player(b[0],b[1]))
        with open(managers,"r") as f:
            for i in f:
                b=i.strip("\n").split()
                self.a1.append(Manager(b[0],b[1]))
        with open(teams,"r") as f:
            for i in f:
                b=i.strip("\n")
                self.a2.append(b) 
        for i in range(0,len(self.a2)):
            for j in range(i*5,(i+1)*5):
                playerslist.append(self.a[j])
            teami_players=playerslist
            playerslist=[]
            teami_manager=self.a1[i]
            teami=Team(self.a2[i],teami_manager,teami_players)
            Season.teamlist.append(teami)
        self.build_fixture()    
    
    def reset(self):
        Season.bestteam=[]
        Season.manager=[]
        Season.player=[]
        Season.mycount=0
        for i in Season.teamlist:
            i.reset()
        self.control="not build"    
    def build_fixture(self):   
        self.reset()
        self.control="build"
        Season.mycount=0
        Season.fixdict={}
        random.shuffle(Season.teamlist)
        first=[]
        last=[]
        liste=[]
        liste1=[]
        for i in range(0,int(len(Season.teamlist)/2)):
            first.append(Season.teamlist[i]) 
        for i in range(int(len(Season.teamlist)/2),len(Season.teamlist)):
            last.append(Season.teamlist[i])
        last.reverse()    
        for i in range(0,len(Season.teamlist)-1):
            for j in range(0,len(first)):
                liste.append(Match(first[j],last[j],i+1))
                liste1.append(Match(last[j],first[j],i+1+int(len(Season.teamlist))-1))
            Season.fixdict["week"+str(i+1)]=liste
            Season.fixdict["week"+str(i+int(len(Season.teamlist)))]=liste1
            liste1=[]
            liste=[]    
            if i!=len(Season.teamlist)-2:    
                first.insert(1,last[0])
                last.pop(0)
                last.append(first[-1])
                first.pop(-1) 
               
        
    def get_week_fixture(self,week_no):
        if week_no<1 or week_no>len(Season.fixdict):
            return None
        else:
            return Season.fixdict["week"+str(week_no)] 
     
    def get_week_no(self):
        return int(Season.mycount+1)
        
    def play_week(self):
        Season.mycount+=1
        if Season.mycount<=len(Season.fixdict):
            for i in Season.fixdict["week"+str(Season.mycount)]:
                i.play()
        else:
            pass
        x2=[]
        x3=[]
        if len(Season.player)==0:
            for i in self.a:
                Season.player.append(0)
        x1=Season.player.copy()
        Season.player=[]
        for i in self.a:
            Season.player.append(i.get_points())  
        for i in range(0,len(x1)):
            x2.append(int(Season.player[i])-int(x1[i]))
        for i in range(0,len(x2)):
            if x2[i]==max(x2):
                x3.append(self.a[i])
        self.bestplayer=max(x3)
        x22=[]
        x33=[]
        if len(Season.manager)==0:
            for i in self.a1:
                Season.manager.append(0)
        x11=Season.manager.copy()
        Season.manager=[]
        for i in self.a1:
            Season.manager.append(i.get_influence())  
        for i in range(0,len(x11)):
            x22.append(int(Season.manager[i])-int(x11[i]))
        for i in range(0,len(x22)):
            if x22[i]==max(x22):
                x33.append(self.a1[i])
        self.bestmanager=max(x33)
        x222=[]
        x333=[]
        if len(Season.bestteam)==0:
            for i in self.a2:
                 Season.bestteam.append(0)
        x111=Season.bestteam.copy()         
        Season.bestteam=[]
        for i in Season.teamlist:
            Season.bestteam.append(i.get_scored())
        for i in range(0,len(x111)):
            x222.append(int(Season.bestteam[i])-int(x111[i]))
        for i in range(0,len(x222)):
            if x222[i]==max(x222):
                x333.append(Season.teamlist[i])
        self.mostteam=max(x333)

                 
    def get_players(self):
        return self.a
    
    def get_managers(self):
        return self.a1
        
    def get_teams(self):
        return Season.teamlist
    
    def get_season_length(self):
        return len(Season.fixdict)
    
    def get_best_player(self):
        if self.control=="build":
            return self.bestplayer
        else:
            pass
    
    def get_best_manager(self):
        if self.control=="build":
            return self.bestmanager
        else:
            pass
    
    def get_most_scoring_team(self):
        if self.control=="build":
            return self.mostteam
        else:
            pass

    def get_champion(self):
        if Season.mycount>=len(Season.fixdict):
            x3=[]
            x4=[]
            for i in Season.teamlist:
                x3.append(i.get_wins())
            for i in range(0,len(x3)):
                if x3[i]==max(x3):
                    x4.append(Season.teamlist[i])
            return max(x4)
        else:
            return None
    
        