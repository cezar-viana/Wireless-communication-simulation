# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 20:40:54 2023

@author: CESAR FILHO
"""
import numpy as np
from math import sqrt, log2, log10, inf
import matplotlib.pyplot as plt

class Coord: #coord class for define ue and ap positions
   def __init__(self):
      self.coord = [np.random.randint(1000,size=1),np.random.randint(1000,size=1)] #self.__coord[0] must be the x and [1] the y
           
   @property
   def coord(self):
      return self.__coord
  
   @coord.setter 
   def coord(self, lista_):
      self.__coord = lista_

class UE: 
   def __init__(self):
      c = Coord()
      self.coord_ue = c.coord #ue coordinate 
      self.dist = 0 #setter
      self.propagation_model = 0 #power received by the ap
      self.snr = 0 #power noise ratio
      self.sinr = 0 #power interference noise ratio
      self.mbps = 0 #link capacity
      self.channel = 0 #channel object that was allocated to ue
      self.AP_associated = 0 #AP object to be associated
   
   @property 
   def dist(self):
       return self.__dist
   
   @dist.setter
   def dist(self, dist_):
      self.__dist = dist_ 
   
   #getters 
   def get_dist(self):
       return self.dist
   
   def get_propagation_model(self):
       return self.propagation_model
   
   def get_snr(self):
       return self.snr
   
   def get_sinr(self):
       return (10*log10(self.sinr))
   
   def get_mbps(self):
       return (self.mbps*(10**-6))
   
class Channel: #channel class to be included in the ap class
    def __init__(self):
        band = 100000000
        n_ch = 2 #useless
        self.channel_band = band/n_ch #useless

class AP:
  
   def __init__(self,x,y):
      self.n_ch = 10 #number of channels to be created  
      self.coord_ap = [x,y] #ap coordinate
      c = 0
      self.channels = [] #list of channels
      while c<self.n_ch: #method to create channels objects
          obj = Channel()
          self.channels.append(obj)
          c = c+1
   
      print(self.channels) #print for analyze the system working
   #def set_coordenada(self, lista_):
       
      #self._coord_ap.coord = lista_
    

class System:
   #band = 100000000
   #c = 10**-4
   #n = 4 #propagation model
   #d_0 = 1
   #n_ch = 5
   #n_power = 10**-17*(band/n_ch) 
   #power = 1
   def __init__(self):
       self.__UeList = [] #list for all ues
       self.__ApList = [] #list for all aps 
       #could exist a list of aps here and then calculate the distance using a for and making association
       
   def add_ue(self): 
       c = UE()
       
       aux = inf     
       for a in self.__ApList:
         ### this is important, pay attention  
         dist = sqrt((a.coord_ap[0]-int(c.coord_ue[0]))**2+(a.coord_ap[1]-int(c.coord_ue[1]))**2) #calculates the distance from the ap
         if dist<aux:
             c.AP_associated = a
             c.dist = dist   
         aux = dist
         
         
         x = np.random.randint(len(a.channels),size=1) #random variable to allocate each ue in a channel
         x = int(x)
         c.channel = a.channels[x]
         print(a.channels[x])
       
       self.__UeList.append(c)
      
   def add_ap(self):
       c = AP()          
       self.__ApList.append(c)
    
   def comunicate(self): #every UE comunicates at the same time
       c = 10**-4
       n = 4
       d_0 = 1
       power = 1
       for u in self.__UeList:
           if u.dist>=d_0:
              p = power*(c/u.dist**n)
              u.propagation_model = p
            
           else:
               raise ValueError('distance must be higher than d0')
   
   def calcule_snr(self):
       band = 100000000
       
        
       for u in self.__UeList:          
           
            n_power = ((10**-17)*(10**-3))*(band/u.AP_associated.n_ch)           
            snr = u.propagation_model/n_power 
            u.snr = snr
   
   def alocate_ch(self): #inutilized by now
      for a in self.__Aplist:  #this just works with 1 ap in the system. If there are more aps, this need to be fixed
       for u in self.__UeList:
          x = np.random.randint(len(a.channels),size=1)
          x = int(x)
          u.channel = a.channels[x]
   
   def calculate_sinr(self):
       s = 0      
       x = 0
       band = 100000000
      
        
       while x<len(self.__UeList): 
         for u in self.__UeList: #sum all the interference 
           if self.__UeList[x].channel == u.channel and u != self.__UeList[x]:
               s = s +u.propagation_model
            
         n_power = ((10**-17)*(10**-3))*(band/u.AP_associated.n_ch)   
         sinr = self.__UeList[x].propagation_model/(s+n_power)
         self.__UeList[x].sinr = sinr
         s = 0
         x = x+1
         n_power = 0
         
   def calcule_link_capacity(self):
       band = 100000000
       
   
       for u in self.__UeList:
           bc = band/u.AP_associated.n_ch
           cap = bc*log2(1+u.sinr)
           u.mbps = cap
           bc = 0 #redundancia?
           
   def plot_propagation_model(self):
       for u in self.__UeList:
           print('distance:',u.get_dist())
           print('power received:',u.get_propagation_model())
  
   def plot_snr(self):
       for u in self.__UeList:
          print(u.get_snr()) 
   
   def plot_sinr(self):
       for u in self.__UeList:
          print(u.get_sinr()) 
   
   def plot_link_capacity(self):
       for u in self.__UeList:
          print(u.get_mbps()) 
   
   def vector_sinr(self):
       l = []
       for u in self.__UeList:
           l.append(u.get_sinr())
       
       l.sort()
       p = 1. * np.arange(len(l)) / (len(l) - 1)
       return [p,l]
        
       
   def vector_mbps(self):
       l = []
       for u in self.__UeList:
           l.append(u.get_mbps())
       l.sort()
       p = 1. * np.arange(len(l)) / (len(l) - 1)
       return [p,l]
   
   def ordenate(self):
       l = self.__UeList
       l2 = []
       x = []
       y = []
       
       s = UE() #this s variable could be a simple int
       s.dist = inf
       for i in range(len(self.__UeList)):
         
           for u in l:
             if u.dist<s.dist:
                s = u
           x.append(s.get_dist())
           y.append(s.get_mbps())
           
           l2.append(u)   
           l.remove(s)
           s.dist = inf
       return [x,y]    
   def get_UES(self):  
       return len(self.__UeList)

   
       

if __name__ == "__main__":
   system = System()
   
   system.add_ap()
   
   
   for i in range(1): #number of runs
     n = 5 #number of ues
     c = 0 #counting
     while c<n: #adding UES
       system.add_ue()
       c = c+1
   
     system.comunicate() 
     system.calcule_snr()
     system.calculate_sinr()
     system.calcule_link_capacity()
   
   print('--------------','\n')
   
   x = system.vector_sinr()
   
   plt.plot(x[0],x[1])
   plt.title('SINR CDF')
   plt.grid()
   plt.show()
   
   y = system.vector_mbps()
  
   plt.plot(y[0],y[1])
   plt.title('Link Capacity CDF')
   plt.grid()
   plt.show()
   
   
   a = system.ordenate()
   
   x1 = a[0]
   y1 = a[1]
   
   plt.plot(x1,y1)
   plt.xlabel('distance')
   plt.ylabel('capacity')
   plt.title('Capacity x Distance')
   plt.grid()
   plt.show()
   
   
   