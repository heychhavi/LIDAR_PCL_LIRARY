from __future__ import print_function
import numpy as np
import xml.etree.ElementTree as ET
import math
import json
tree = ET.parse('firstfile.xml')
epsilon=1e-6


w1 = [2, 3, 4, 6, 7, 8]
wsum = [-9.5, -5.75, -2.0, 2.0, 5.75, 9.5]
xyz=[]
d1 = ['1.5707963267949010e+00']
t = [0.06, 0.06, 0.06, 0.06, 0.06, 0.06]
a = 0.1
b = 0.625
p = math.sin(float(d1[0]))
q = math.cos(float(d1[0]))
T = 45.6666

#for T in range(50):

n = -730
m = -39
    
for i in range(len(w1)):
        #for n in range(-730,0):
        while n<= 720 :
            n=n+0.1
            for m in range(-39,24):
                r = math.sqrt(1+(math.tan((math.radians(n*a + 0.5)) + (float(d1[0]))))*(math.tan((math.radians(n*a + 0.5)) + (float(d1[0])))))
                s = math.sqrt(1 + ((math.tan(math.radians(m*b)))*(math.tan(math.radians(m*b)))))
                I = (q/(r*s)) + ((math.tan((math.radians(n*a + 0.5)) + (float(d1[0])))*p)/(r*s))
                J = (p/(r*s)) + (q*(math.tan((math.radians(n*a + 0.5)) + (float(d1[0])))/(r*s)))
                K = math.tan(math.radians(m*b))/(s)

                #print (I,J,K)
        
                planeNormal = np.array([0, 0, 1])
                planePoint = np.array([0, 0, 0.02]) #Any point on the plane

                #Define ray
                rayDirection = np.array([I, J, K])
                rayPoint = np.array([3.875, ((0.6)*(T)) , 0.5]) #Any point along the ray

                ndotu = planeNormal.dot(rayDirection) 

                if abs(ndotu) < epsilon:
                    #print ("no intersection or line is within plane")
                    continue;
                w = rayPoint - planePoint
                si = -planeNormal.dot(w) / ndotu
                Psi = w + si * rayDirection + planePoint
                G = math.sqrt(((Psi[0] - (3.875))*(Psi[0] - (3.875)))+((Psi[1]-((0.6)*(T)))*(Psi[1]-((0.6)*(T)))) + ((0.02-0.5)*(0.02-0.5)))
                if Psi[0] >= wsum[i]-t[i] and Psi[0] <= wsum[i]+t[i] and Psi[1]>=(0.6)*(T) and Psi[1]<=1000 :
                    if G <= 120:
                        xyz.append({'Pos_x':((Psi[0])+(9.5)) ,'Pos_y':Psi[1],'Pos_z':Psi[2], 'ValidFlag': 'True'})
                        
                
                        #print ("intersection at", Psi)



b = json.dumps({'timestamp':[{'VehiclePosition': [{'Pos_X':-13.875,'Pos_Y':((0.6)*(T))}],'Lidar':[{'Point Cloud':xyz}]}]})
print(b)

