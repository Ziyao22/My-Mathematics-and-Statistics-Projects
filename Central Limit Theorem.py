import math 
import numpy as np
import random
x=1000
a=24693
c=3967
K=2**18
start=0
count=1
while start<53:
    x=(a*x+c)%K
    start+=1
    if start>50:
        print("u",count,":",x/K)
    count+=1


def Xgen(x): 
    p = ran(x)[1]  ## generate a new F(x)
    xDistance = math.sqrt(- 2*math.log(-p+1))/alpha
    x = ran(x)[0] #refresh 
    return xDistance;

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
n1=5
trial=550; 
for i in range (0,trial):
    x = ran(x)[0]; # refresh X
    list1.append(np.mean(Trial(n1,x))) 
print("n=5:",(list1),"\n")

list2 = []
n2=10
for i in range (0,trial):
    x = ran(x)[0]; # refresh X
    list2.append(np.mean(Trial(n2,x))) 
print("n=10: ",(list2),"\n")
    
list3 = []
n3=15
for i in range (0,trial):
    x = ran(x)[0]; # refresh X
    list3.append(np.mean(Trial(n3,x))) 

print("n=15: ",list3,"\n")

list4 = []
n4=30
for i in range (0,trial):
    x = ran(x)[0]; # refresh X
    list4.append(np.mean(Trial(n4,x))) 
print("n=30: ",list4,"\n")
