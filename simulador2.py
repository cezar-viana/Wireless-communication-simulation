#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:16:23 2024

@author: aluno
"""
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
         
        
        
class AP:
  
   def __init__(self):
       
      self.coord_ap = 0 #ap coordinate
      
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
       self.__ChList = []
       
       #could exist a list of aps here and then calculate the distance using a for and making association
      
   def add_ch(self, n_ch):
       count = 0
       while count<n_ch:
           obj = Channel()
           self.__ChList.append(obj)
           count = count+1
           
   def add_ue(self): 
       c = UE()
       
       aux = inf     
       for a in self.__ApList: #set distance to AP
         ### this is important, pay attention  
         dist = sqrt((a.coord_ap[0]-int(c.coord_ue[0]))**2+(a.coord_ap[1]-int(c.coord_ue[1]))**2) #calculates the distance from the ap
        
         if dist<aux:
           c.AP_associated = a
           aux = dist
         
       
       c.dist = aux
       print(aux)  
       x = np.random.randint(len(self.__ChList),size=1) #random variable to allocate each ue in a channel
       x = int(x)
       c.channel = self.__ChList[x]
       print(self.__ChList[x])
       
       self.__UeList.append(c)
      
   def add_ap(self, n_APS, edge_x=950, edge_y=950, start_x=50, start_y=50):
       a = int(sqrt(n_APS))
       b = int(sqrt(n_APS))-1
      
       while a*b<n_APS:
          b = b+1
       if a*b>n_APS:
          b = b-1        
       if a*b != n_APS:
           c = n_APS-a*b
           for k in range(c):
               ap = AP()
               obj = Coord()
               ap.coord_ap = obj.coord
               self.__ApList.append(ap)
               del ap
               del obj
       coordinates = []       
       j = 0
       count = 0
       while count<b:   
         for i in range(a):
              interval = (edge_x-start_x)/(a-1)
              
              point = [start_x+i*interval,start_y+j]
              coordinates.append(point)
         count = count+1
         j = j+interval
            
       
       
       for n in range(a*b):  
          A = AP()
          A.coord_ap = coordinates[n]
          self.__ApList.append(A)
          del A
    
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
           
            n_power = ((10**-17)*(10**-3))*(band/len(self.__ChList))           
            snr = u.propagation_model/n_power 
            u.snr = snr
   
   def alocate_ch(self, c): #inutilized by now
       x = np.random.randint(len(self.__ChList),size=1) #random variable to allocate each ue in a channel
       x = int(x)
       c.channel = self.__ChList[x]
       print(self.__ChList[x])
   
   def calculate_sinr(self):
       s = 0      
       x = 0
       band = 100000000
      
        
       while x<len(self.__UeList): 
         for u in self.__UeList: #sum all the interference 
           if self.__UeList[x].channel == u.channel and u != self.__UeList[x]:
               s = s +u.propagation_model
            
         n_power = ((10**-17)*(10**-3))*(band/len(self.__ChList))   
         sinr = self.__UeList[x].propagation_model/(s+n_power)
         self.__UeList[x].sinr = sinr
         s = 0
         x = x+1
         n_power = 0
         
   def calcule_link_capacity(self):
       band = 100000000
       
   
       for u in self.__UeList:
           bc = band/len(self.__ChList)
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
   def get_APS(self):  
       return len(self.__ApList)
   def get_CH(self):  
       return len(self.__ChList)
   
    
   def get_pts_x_AP(self):
       l = []
       for a in self.__ApList:
          l.append(a.coord_ap[0])
       return l
   def get_pts_y_AP(self):
       l = []
       for a in self.__ApList:
          l.append(a.coord_ap[1])
       return l
   def get_pts_x_UE(self):
       l = []
       for a in self.__UeList:
          l.append(a.coord_ue[0])
       return l   
   def get_pts_y_UE(self):
       l = []
       for a in self.__UeList:
          l.append(a.coord_ue[1])
       return l
   def get_coordUE(self):
       l = []
       for a in self.__UeList:
         print(a.coord_ue)
         
if __name__ == "__main__":
   system = System()
   system.add_ch(3)
   print(system.get_CH())
   system.add_ap(64)
   print(system.get_APS())
   
   for i in range(1): #number of runs
     n = 10 #number of ues
     c = 0 #counting
     while c<n: #adding UES
       system.add_ue()
       c = c+1
   
     system.comunicate() 
     system.calcule_snr()
     system.calculate_sinr()
     system.calcule_link_capacity()
     
   dados_x1 = system.get_pts_x_AP()
   dados_y1 = system.get_pts_y_AP()
   dados_x2 = system.get_pts_x_UE()
   dados_y2 = system.get_pts_y_UE()
   
   print(system.get_UES())
   print('--------------','\n')
   
   x = system.vector_sinr()
   
   plt.plot(x[1],x[0])
   plt.title('SINR CDF')
   plt.grid()
   plt.show()
   
   y = system.vector_mbps()
  
   plt.plot(y[1],y[0])
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
   
   
   plt.scatter(dados_x1, dados_y1, color='blue', marker='o', label='Pontos Tipo 1')  
   plt.scatter(dados_x2, dados_y2, color='red', marker='^', label='Pontos Tipo 2')
   plt.xlabel('Eixo X')
   plt.ylabel('Eixo Y')
   plt.show()
   
   
   