#RC Voltage Divider
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Cycles of Charge-Discharge
def cycle(a):
    #First Half 
    tc = np.linspace((2*a/(2*f)),((2*a+1)/(2*f)),1000) #Charging time. Time interval of: (1/2f) 
    Vo= Vm*(1-np.exp((-1*T)*t))
    plt.plot(tc,Vo)

    #Second Half
    tc= np.linspace(((2*a+1)/(2*f)),((2*a+2)/(2*f)),1000) #Discharging time
    Vo = Vm*(np.exp((-1*T)*t))
    plt.plot(tc,Vo)

#Input necessary details
f = int(input('Input Frequency: '))
Vm = float(input('Input Vmax:'))
R = float(input('Input R:'))
Cu = float(input('Input Capacitance in uF:'))
C = Cu*10**-6
T= 1/(R*C) #RC constant

t = np.linspace(0, 1, 1000)
x=signal.square(2 * np.pi * f * t)
Vi=x*Vm
plt.plot(t, Vi)

for c in range(0,f):  #Number of cycles is decided by frequency
    cycle(c)


plt.xlabel('t (sec) ->')
plt.ylabel('Amplitude (volts)')
plt.title('RC Circuit Simulation')
plt.show()
