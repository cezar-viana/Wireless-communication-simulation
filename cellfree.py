#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:34:49 2024

@author: student
"""

# -*- coding: utf-8 -*-
"""simulador2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RCyosBueWp6kudauQidCa8H8jpf5voEp
"""

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

class Coord: #coord class to define ue and ap positions
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
      self.propagation_model = [] #power received by the ap
      self.snr = [] #power noise ratio
      self.sinr = [] #power interference noise ratio
      self.mbps = 0 #link capacity
      self.channel = 0 #channel object that was allocated to ue
      self.AP_associated = [] #AP object to be associated
      self.energy_efficiency = 0

      self.amount = 0
      self.angle = 0
      self.direction = 0
      self.movement_finished = 0
      self.limit_axis = 0
   def state(self):
       if self.amount <= 0:
          self.movement_finished = True
       else:
          self.movement_finished = False
   def define_amount_x(self):
         n = np.random.randint(3,size=1)
         if n == 0:
            total_amount = 0-self.coord_ue[0]
            self.amount_x = -np.random.randint((-1)*(total_amount-1),size=1)
            self.direction = 'negative'
         elif n == 1:
            total_amount = 1000-self.coord_ue[0]
            self.amount_x = np.random.randint(total_amount+1,size=1)
            self.direction = 'positive'
         elif n == 2:
            self.amount_x = 0
            self.direction = 'stopped'

         if self.amount_x != 0:
            self.movement_finished = False
         else:
            self.movement_finished = True
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

class Channel:
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
       self.__UeList = [] #list of all ues
       self.__ApList = [] #list of all aps
       self.__ChList = [] #list of all channels
       self.sinr_list = [[],[],[],[],[]] #list of all sinr data
       self.mbps_list = [[],[],[],[],[]] #list of all link capacity data
       self.snr_list = [[],[],[],[],[]]  #list of all snr data
       self.energy_efficiency_list = [[],[],[],[],[]]
       self.blabla2 = []
       #could exist a list of aps here and then calculate the distance using a for and making association


   def add_ch(self, n_ch): #add a channel
       count = 0
       while count<n_ch:
           obj = Channel()
           self.__ChList.append(obj)
           count = count+1

   def add_ue(self,group_number): #add an ue
     c = UE()
     #c.define_amount_x()
     num = 1
     l = self.__ApList.copy()
     count = 0
     while count<group_number:
       aux = -inf
       for a in l:
         ### this is important, pay attention
         if self.distance_to_ap(c,a)<1:
            self.add_ue(group_number)
            print('FUNCTION CALLED','\n')
            num = 0
            obj = a
            aux = 0
            break

         else:

            pr = np.random.lognormal(0,2)*((10**(-4))/(self.distance_to_ap(c,a)**4))
            #print('pr ue:',pr)
            #print('ap ue:',a)
            #print('distance ue:',self.distance_to_ap(c,a),'\n')
         if pr>aux:
           obj = a
           aux = pr
       #print('aux ue:',aux)
       #print('ap associated ue:',obj)
       #print('distance final ue:',self.distance_to_ap(c,obj))
       c.propagation_model.append(aux)
       l.remove(obj)

       if obj not in c.AP_associated:
          c.AP_associated.append(obj)

       count = count+1

     x = np.random.randint(len(self.__ChList),size=1) #random variable to allocate each ue in a channel
     x = int(x)
     c.channel = self.__ChList[x]

     if num == 1:
         #print('ue: ',c)
         self.__UeList.append(c)
         #print('ap associated: ', len(c.AP_associated))



   def is_higher_than_1(self,ue,ap):
       dist = sqrt((ap.coord_ap[0]-int(ue.coord_ue[0]))**2+(ap.coord_ap[1]-int(ue.coord_ue[1]))**2)
       if dist>=1:
          return True
       else:
         return False

   def add_ap(self, n_APS, edge_x=950, edge_y=950, start_x=50, start_y=50): #add an AP
       #a and b are the amount of aps in (x,y) coordinates
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
       interval = (edge_x-start_x)/(a-1)
       while count<b: #It defines coordinates
         for i in range(a):


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
       c = 10**(-4)
       n = 4
       d_0 = 1
       power = 1

       for u in self.__UeList: #varre a lista de UES, neste caso há somente 1
        u.propagation_model.clear()
        for a in u.AP_associated: #varre a lista de APS associadas
           #print('distance is: ',self.distance_to_ap(u,a),'\n')
           #print('ue in function', u)


           if self.distance_to_ap(u,a)>=d_0: #a distancia da UE para cada ap deve ser >= a 1
              p = np.random.lognormal(0,2)*power*(c/self.distance_to_ap(u,a)**n)
              u.propagation_model.append(p)

           else:
             raise ValueError('distance must be higher than d_0')



   def calcule_snr(self):
       band = 100000000


       for u in self.__UeList:
         for f in u.propagation_model:
            n_power = ((10**-17)*(10**-3))*(band/len(self.__ChList))
            snr = f/n_power
            u.snr.append(snr)

   def alocate_ch(self, c): #inutilized by now
       x = np.random.randint(len(self.__ChList),size=1) #random variable to allocate each ue in a channel
       x = int(x)
       c.channel = self.__ChList[x]
       print(self.__ChList[x])

   def power_to_ap(self, ue, ap): #function to define the power received in specific AP
       dist = sqrt((ap.coord_ap[0]-int(ue.coord_ue[0]))**2+(ap.coord_ap[1]-int(ue.coord_ue[1]))**2)
       power = 10**-4/dist**4
       return power

   def distance_to_ap(self,ue,ap):
       dist = sqrt((ap.coord_ap[0]-int(ue.coord_ue[0]))**2+(ap.coord_ap[1]-int(ue.coord_ue[1]))**2)
       return dist

   def calculate_sinr(self): #outdated, needs new model
       s = 0
       x = 0
       band = 100000000


       while x<len(self.__UeList): #selector of UE to have sinr calculated
         ap = self.__UeList[x].AP_associated
         for u in self.__UeList: #sum all the interference
           if self.__UeList[x].channel == u.channel and u != self.__UeList[x]:
               s = s + self.power_to_ap(u,ap)

         n_power = ((10**-17)*(10**-3))*(band/len(self.__ChList))
         sinr = self.__UeList[x].propagation_model/(s+n_power)
         self.__UeList[x].sinr = sinr
         s = 0
         x = x+1


   def calcule_link_capacity(self):
       band = 100000000
       bc = band/len(self.__ChList)
       s = 0
       for u in self.__UeList:
         for w in u.snr:
           s = s+w
         cap = bc*log2(1+s)
         u.mbps = cap
         s=0

   def plot_propagation_model(self):
       for u in self.__UeList:

           print('power received:',u.get_propagation_model())

   def plot_snr(self):
       for u in self.__UeList:
          print(u.get_snr())

   def plot_sinr(self):
       for u in self.__UeList:
          print('sinr: ',u.sinr)

   def plot_link_capacity(self):
       for u in self.__UeList:
          print('cap: ',u.mbps)

   def vector_sinr(self,n): #CDF

       l = self.sinr_list[n]

       l.sort()
       p = 1. * np.arange(len(l)) / (len(l) - 1)
       return [p,l]


   def vector_mbps(self,n): #CDF
       l = self.mbps_list[n]

       l.sort()
       p = 1. * np.arange(len(l)) / (len(l) - 1)
       return [p,l]

   def vector_snr(self,n): #CDF
       l = self.snr_list[n]
       l.sort()
       p = 1. * np.arange(len(l)) / (len(l) - 1)
       return [p,l]
   def vector_energy_efficiency(self,n): #CDF
       l = self.energy_efficiency_list[n]

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
       l2 = []
       for u in self.__UeList:
        for j in u.AP_associated:
         for a in self.__ApList:
            if a == j:
              l2.append(a.coord_ap[0])
            else:
              l.append(a.coord_ap[0])
       return [l,l2]
   def get_pts_y_AP(self):
       l = []
       l2 = []
       for u in self.__UeList:
        for j in u.AP_associated:
         for a in self.__ApList:
            if a == j:
              l2.append(a.coord_ap[1])
            else:
              l.append(a.coord_ap[1])
       return [l,l2]
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


   def add_sinr(self,n):
       for u in self.__UeList:
         self.sinr_list[n].append(u.get_sinr())
   def add_mbps(self, n):
       for u in self.__UeList:
         self.mbps_list[n].append(u.get_mbps())
   def add_snr(self, n):
       for u in self.__UeList:
        self.snr_list[n].append(u.get_snr())
   def add_energy_efficiency(self,n):
       for u in self.__UeList:
         self.energy_efficiency_list[n].append(u.energy_efficiency)


   def del_UES(self):
       self.__UeList.clear()

   def get_len_sinr(self):
       return len(self.sinr)
   def check_ap(self):
       for u in self.__UeList:

          if u.dist == sqrt((u.AP_associated.coord_ap[0]-int(u.coord_ue[0]))**2+(u.AP_associated.coord_ap[1]-int(u.coord_ue[1]))**2):
            return True
          else:
            return False
   def get_coordinates(self): #to get coordinates and
       for u in self.__UeList:
        print('coord ap: ',u.AP_associated.coord_ap,'coord ue: ', u.coord_ue)
   def get_list(self):
      return self.sinr_list
   def del_APS(self):
       self.__ApList.clear()

   def calculate_energy_efficiency(self,num_group):
       for u in self.__UeList:
         power_transmitted = 1*num_group
         ee = u.mbps/power_transmitted
         u.energy_efficiency = ee

   def define_amount_movement(self):
       for u in self.__UeList:
         n = np.random.randint(7,size=1) #defines types of movements
         u.angle = np.random.randint(2*np.pi,size=1)
         if n == 0: #move only at x negative
            total_amount = 0-u.coord_ue[0]
            u.amount = np.random.randint((-1)*(total_amount-1),size=1)
            u.direction = 'negative x'

         elif n == 1: #move only at x positive
            total_amount = 1000-u.coord_ue[0]
            u.amount = np.random.randint(total_amount+1,size=1)
            u.direction = 'positive x'
         elif n == 2 or n == 6: #no movement
            u.amount = 0
            u.direction = 'stopped'
         elif n == 3: #move only at y negative
            total_amount = 0-u.coord_ue[1]
            u.amount = np.random.randint((-1)*(total_amount-1),size=1)
            u.direction = 'negative y'
         elif n == 4: #move only at y positive
            total_amount = 1000-u.coord_ue[1]
            u.amount = np.random.randint(total_amount+1,size=1)
            u.direction = 'positive y'
         elif n == 5: #move x and y

            if 0<=u.angle<=np.pi/2:
               total_amount = [1000-u.coord_ue[0], 1000-u.coord_ue[1]]

            elif np.pi/2<=u.angle<=np.pi:
               total_amount = [abs(0-u.coord_ue[0]), 1000-u.coord_ue[1]]


            elif np.pi<=u.angle<=(3/2)*np.pi:
               total_amount = [abs(0-u.coord_ue[0]), abs(0-u.coord_ue[1])]


            elif (3/2)*np.pi<=u.angle<=2*np.pi:
               total_amount = [1000-u.coord_ue[0], abs(0-u.coord_ue[1])]


            limit = min(total_amount)
            if limit == total_amount[0]:
               if np.cos(u.angle)!=0:
                  u.limit_axis = 'x'
               else:
                  u.limit_axis = 'y'
            else:
               if np.sin(u.angle)!=0:
                 u.limit_axis = 'y'
               else:
                 u.limit_axis='x'
            u.amount = np.random.randint(min(total_amount)+1,size=1)
            u.direction = 'both'

         if u.amount != 0:
            u.movement_finished = False
         else:
            u.movement_finished = True

   def all_finished(self):
       for u in self.__UeList:
           if u.movement_finished == True:
              return True
           if u.movement_finished == False:
              return False

   def move_ue(self,move_from_AP = False):

      for u in self.__UeList:
        if u.movement_finished == False:
          if u.direction == 'negative x':
            u.coord_ue[0] = u.coord_ue[0]-1
            u.amount = u.amount-1
            u.state()
          elif u.direction == 'positive x':
            u.coord_ue[0] = u.coord_ue[0]+1
            u.amount = u.amount-1
            u.state()
          elif u.direction == 'negative y':
            u.coord_ue[0] = u.coord_ue[1]-1
            u.amount = u.amount-1
            u.state()
          elif u.direction == 'positive y':
            u.coord_ue[0] = u.coord_ue[1]+1
            u.amount = u.amount-1
            u.state()
          elif u.direction == 'both':
            u.coord_ue = [u.coord_ue[0]+1*np.cos(u.angle),u.coord_ue[1]+1*np.sin(u.angle)]
            if u.limit_axis =='x':
               u.amount = u.amount-abs(1*np.cos(u.angle))
            else:
               u.amount = u.amount-abs(1*np.sin(u.angle))

            u.state()
        for j in u.AP_associated:
           if self.distance_to_ap(u,j)<1:
             u.coord_ue[0] = u.coord_ue[0]+1
             u.coord_ue[1] = u.coord_ue[1]+1

   def handover(self,group_number):
      for u in self.__UeList:
          aa = u.AP_associated.copy()
          u.AP_associated.clear()
          count = 0
          l = self.__ApList.copy()
          u.propagation_model.clear()
          while count<group_number:
            aux = -inf
            for a in l: #set distance to AP
              ### this is important, pay attention
              #print(self.distance_to_ap(u,a))
              pr = np.random.lognormal(0,2)*((10**(-4)/(self.distance_to_ap(u,a)**4)))
              #print('pr handover:',pr)
              #print('ap handover:',a)
              #print('distance handover:',self.distance_to_ap(u,a),'\n')
              if pr>aux:
                obj = a
                aux = pr
            #print('aux handover:',aux)
            #print('ap associated handover:',obj)
            #print('distance final handover:',self.distance_to_ap(u,obj),'\n')
            l.remove(obj)
            u.propagation_model.append(aux)
            if obj not in u.AP_associated:
              u.AP_associated.append(obj)

            count = count+1

   def blabla(self):
      aux = inf
      obj = 0
      for u in self.__UeList:
          for j in u.propagation_model:
             if j<aux:
               aux = j
               obj = u
      self.blabla2.append(obj)
   def blabla3(self):
      aux = inf
      obj = 0
      for i in self.blabla2:
        for j in i.propagation_model:
          if j<aux:
            aux = j
            obj = i
      print('power:',aux)

      for k in obj.AP_associated:

          print('distances:',self.distance_to_ap(obj,k))
if __name__ == "__main__":
   system = System()
   ch = 1
   ap = 64
   count = 0
   list_=[1,3,4,5,64]
   system.add_ap(ap)
   system.add_ch(ch)

   while count<=4:

     #print(system.get_CH())


     for i in range(7000): #number of runs


      #print(system.get_APS())
      n = 1 #number of ues
      c = 0
      while c<n:
        system.add_ue(list_[count])
        c = c+1


      system.define_amount_movement()
      state = system.all_finished()
      while state==False:

        #calculating data
        system.calcule_snr()

        system.calcule_link_capacity()
        system.calculate_energy_efficiency(list_[count])
        #appending data

        system.add_mbps(count)
        system.add_energy_efficiency(count)
        #moving ue
        system.move_ue()

        system.handover(list_[count])
        state = system.all_finished()


      #deleting objects
      system.del_UES()



     count = count+1
     print('count iwjadikajhslkdhjkawhdjhaujwdhgwua:',count,'\n')
   dados_x1 = system.get_pts_x_AP()
   dados_y1 = system.get_pts_y_AP()
   dados_x2 = system.get_pts_x_UE()
   dados_y2 = system.get_pts_y_UE()

   print(len(system.get_list()[0]))

   print(system.get_UES())
   print('--------------','\n')

   #x1 = system.vector_sinr(0)
   #x2 = system.vector_sinr(1)
   #x3 = system.vector_sinr(2)
   #plt.plot(x1[1],x1[0], color ='blue',label='1 CH')
   #plt.plot(x2[1],x2[0], color = 'red',label='2 CH')
   #plt.plot(x3[1],x3[0], color = 'green',label='3 CH')
   #plt.suptitle('SINR CDF', y=1.0, fontsize=18)
   #plt.title('UEs=13 / APs=64 / CH=2', fontsize=10)
   #plt.xlabel('db')
   #plt.legend()
   #plt.grid()
   #plt.show()


   y1 = system.vector_mbps(0)
   y2 = system.vector_mbps(1)
   y3 = system.vector_mbps(2)
   y4 = system.vector_mbps(3)
   y5 = system.vector_mbps(4)
   percentile_index = int(0.1*len(y1[1]))
   valor = y1[1][percentile_index]
   percentile_index2 = int(0.1*len(y2[1]))
   valor2 = y2[1][percentile_index2]
   percentile_index3 = int(0.1*len(y3[1]))
   valor3 = y3[1][percentile_index3]
   percentile_index4 = int(0.1*len(y4[1]))
   valor4 = y4[1][percentile_index4]
   percentile_index5 = int(0.1*len(y5[1]))
   valor5 = y5[1][percentile_index5]

   plt.plot(y1[1],y1[0], color = 'blue',label='Cellular')
   plt.plot(y2[1],y2[0],color='red',label='Cell-free: 3 APs',linestyle=':')
   plt.plot(y3[1],y3[0],color='green',label='Cell-free: 4 APs',alpha=0.6)
   plt.plot(y4[1],y4[0],color='black',label='Cell-free: 5 APs')
   plt.plot(y5[1],y5[0],color='aqua',label='Cell-free: 64 APs',linestyle='--')
   #plt.suptitle('LINK CAPACITY CDF', y=1.0, fontsize=18)
   #plt.title('UE=1 / APs=64 / CH=1', fontsize=10)
   plt.axhline(y=0.05, color='black', linestyle='--',label= '95% likely',alpha=0.3)
   #plt.axvline(valor, color = 'red', linestyle = '--', alpha = 0.5)
   plt.xlabel('Mbit/s')
   plt.ylabel('Cumulative Distribution')
   plt.legend()
   plt.grid()
   plt.savefig("link capacity.pdf")    
   plt.show()
  
   #print(y1)
   print(valor,valor2,valor3,valor4,valor5)

   z1 = system.vector_energy_efficiency(0)
   z2 = system.vector_energy_efficiency(1)
   z3 = system.vector_energy_efficiency(2)
   z4 = system.vector_energy_efficiency(3)
   z5 = system.vector_energy_efficiency(4)
   plt.plot(z1[1],z1[0], color = 'blue',label='Cellular')
   plt.plot(z2[1],z2[0],color='red',label='Cell-free: 3 APs',linestyle=':')
   plt.plot(z3[1],z3[0],color='green',label='Cell-free: 4 APs',linestyle='--',alpha=0.6)
   plt.plot(z4[1],z4[0],color='black',label='Cell-free: 5 APs')
   plt.plot(z5[1],z5[0],color='aqua',label='Cell-free: 64 APs',linestyle = '-',alpha=0.6)
   #plt.suptitle('ENERGY EFFICIENCY CDF', y=1.0, fontsize=18)
   #plt.title('UE=1 / APs=64 / CH=1', fontsize=10)
   plt.xlabel('bit/joule')
   plt.ylabel('Cumulative Distribution')
   plt.legend()
   plt.grid()
   plt.savefig("energy efficiency.pdf")
   plt.show()

   #x1 = a[0]
   #y1 = a[1]

   #plt.plot(x1,y1)
   #plt.xlabel('distance')
   #plt.ylabel('capacity')
   #plt.title('Capacity x Distance')
   #plt.grid()
   #plt.show()


   plt.scatter(dados_x1, dados_y1, color='blue', marker='o', label='Pontos Tipo 1')
   plt.scatter(dados_x2, dados_y2, color='red', marker='^', label='Pontos Tipo 2')
   plt.xlabel('Eixo X')
   plt.ylabel('Eixo Y')
   plt.show()