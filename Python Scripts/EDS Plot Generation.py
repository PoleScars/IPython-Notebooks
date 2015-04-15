
# coding: utf-8

# In[1]:

"""Code to plot an EDS spectra anaylsis from a master csv file
Code by Scott Gleason, University of New South Wales (UNSW), Australia 
S.Gleason@student.unsw.edu.au, April 2015"""


# In[2]:

'imports numpy and matplotlib libaries into code'
import numpy as np
import matplotlib.pyplot as plt


# In[6]:

'Directs code to head file location on drive'
HeadFile = 'C:\Users\z3492622\Documents\PhD Files\Lab Work'
SubFile = '\SEM\SEM_T1235_070415\EDS Spectra'


# In[7]:

'Directs code to the file to be ploted'
File = '\Python Code Test\TestCodeFile2.csv'

'Assembles full file path as a variable for use within code'
Fname = HeadFile + SubFile + File


# In[8]:

'''Loads full file path as a variable into numpy,
stores it as a as an array and prints it (as a check)'''

'''These variable define the array limits
StartRow is the row data starts on
LastColumn is the column data ends on
(i.e. this cuts unneed instriment data, dates, etc)'''
StartRow = 26
LastColumn = 3

'Creats data variable, should not have to edit this string'
data = np.loadtxt(Fname, delimiter = ',', 
                  skiprows = StartRow - 1, usecols = range(0, LastColumn, 1))
print data


# In[9]:

'Defines function to direct code to specific columns within data'
'First argument is the filename, second argument is the column'
def getColumn(filename, column):
    'This is the array of the filename variable defined above'
    data
    return [result[column] for result in data]


# In[10]:

'Define X & Y axis data to be ploted'
xAxisData = getColumn(Fname, 1)
yAxisData = getColumn(Fname, 2)


# In[11]:

'Generates plot of data, and chart layout'

'Define Plot layout, axis lables, legends, etc'
plt.figure("Counts/keV")
plt.title("Counts/keV", fontsize = 22)
AxisFontSize = 14
plt.xlabel("keV", fontsize = AxisFontSize)
plt.ylabel("Counts", fontsize = AxisFontSize)
LineType = 'g'

'Sets axis upper limit'
xMax = 20
yMax = 7000

'Generates plot'
plt.plot(xAxisData, yAxisData, LineType, linewidth = 1.8)
plt.axis([0, xMax, 0, yMax])
plt.show()


# In[ ]:



