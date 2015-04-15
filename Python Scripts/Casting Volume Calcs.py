
# coding: utf-8

# In[5]:

'''Code for Volume and weight calculations for Tagets
Code by Scott Gleason, University of New South Wales (UNSW), Australia 
S.Gleason@student.unsw.edu.au, April 2015'''


# In[6]:

'imports numpy and matplotlib libaries into code'
import numpy as np
import matplotlib.pyplot as plt


# In[7]:

'Volume of cylindar is given by V = pi * t * R^2 '
R = 25.4 #mm, Radius
t = 4 #mm, Length
V = np.pi * t * R*R #mm^3
Vcc = V / 1000 #cc #(1000mm^3 per cm^3)
print 'Radius R is', R, 'mm'
print 'Thickness t is', t, 'mm'
print 'Volume of cylinder is', round(V, 3), 'mm^3'
print 'Volume of cylinder is', round(Vcc, 3), 'cc'


# In[8]:

'''Convert wt% to at%
C1' = C1*A2*A3 / (C1*A2*A3 + C2*A1*A3 + C3*A1*A2)

Convert at% to wt% 
C1 = C1'*A1 / (C1'*A1 + ... + Cn'*An)

Where Cn = wt%, Cn' = at%, An = atomic weight'''


# In[9]:

'Mg65Zn30Ca5 atomic precent alloy'
'Mg45.727 Zn56.773 Ca5.8 weight precent alloy'
MgD = 1.738 #g/cm^3
ZnD = 7.14 #g/cm^3
CaD = 1.55 #g/cm^3


# In[10]:

'''Stores periodic elements as an array 
containings an object of each element'''
elements = [
    {name: 'Mg', 
    atomicPercent: 65, #alloy atomic percent
    atomicWeight: 24.305, #amu
    density: 1.738}, #g/cm3
    
    {name: 'Zn', 
    atomicPercent: 30, #alloy atomic percent
    atomicWeight: 65.382, #amu
    density: 7.14}, #g/cm3
    
    {name: 'Ca', 
    atomicPercent: 5, #alloy atomic percent
    atomicWeight: 40.078, #amu
    density: 1.55} #g/cm3
]


# In[ ]:



