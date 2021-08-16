import math 
import numpy as np
# define constants / initialization 

# define functions
def ran(x):
    x_next=(a*x+c)%K;
    u=x_next/K;
    return [x_next,u]; # ran(x)[0] --> input ; ran(x)[1] -->probablity;

Tao=57; 
alpha = 1/Tao;

def Xgen(x): 
    p = ran(x)[1]  ## generate a new F(x)
    xDistance = math.sqrt(- 2*math.log(-p+1))/alpha
    x = ran(x)[0] #refresh 
    return xDistance;

def Trial(n,x): # n --> size, x --> input
    list = [] 
    sum = 0; 
    x = ran(x)[0]

    for i in range (0, n):
        distance = Xgen(x);
        list.append(distance);
        x = ran(x)[0]; # x refresh; 
     
    return list; 
        
## operation:        
list1 = []
n1=10
trial=110; 
for i in range (0,trial):
    x = ran(x)[0]; # refresh X
    list1.append(np.mean(Trial(10,x))) 
print("n=10:",(list1),"\n")

list2 = []
n2=30
for i in range (0,trial):
    x = ran(x)[0]; # refresh X
    list2.append(np.mean(Trial(n2,x))) 
print("n=30: ",(list2),"\n")
    
    
list3 = []
n3=50
for i in range (0,trial):
    x = ran(x)[0]; # refresh X
    list3.append(np.mean(Trial(n3,x))) 

print("n=50: ",list3,"\n")

list4 = []
n4=100
for i in range (0,trial):
    x = ran(x)[0]; # refresh X
    list4.append(np.mean(Trial(n4,x))) 
print("n=100: ",list4,"\n")

    
list5 = []
n5=250
for i in range (0,trial):
    x = ran(x)[0]; # refresh X
    list5.append(np.mean(Trial(n5,x))) 
print("n=250: ",list5,"\n")

list6 = []
n6=500
for i in range (0,trial):
    x = ran(x)[0]; # refresh X
    list6.append(np.mean(Trial(n6,x))) 
print("n=500: ",list6,"\n")

list7 = []
n7=1000
for i in range (0,trial):
    x = ran(x)[0]; # refresh X
    list7.append(np.mean(Trial(n7,x))) 
print("n=1000: ",list7,"\n")
