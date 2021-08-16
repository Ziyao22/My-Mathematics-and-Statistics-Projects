import math
import numpy as np
 
x = 0
 
def nextrandom():
    a = 24693
    c = 1753
    K = 2**15
    x = 1000
    while True:
        x = (a*x+c)%K
        if x == 0:
            continue
        yield x/K
    
r = nextrandom()
 
 
def exponentialRM(rate): #lambda
    x = (math.log(1-next(r)))/(-rate)
    return x
 
def simulate():
    return exponentialRM(1/12)
 
 
def mainFunction(i):
    w=0 
    N=1
    #r = nextrandom()
    number = next(r)
    #p = simulate()
    m = simulate()
 
    while N<5:
        if number < 0.2:
            w += 12
            number = number / 0.2
            if N >= 4:#no one answers
                return w
        elif number > 0.2 and number < 0.5:#busy
            w += 27
            number = (number - 0.2) / 0.3
            if N >= 4:
                return w
        else:#recalculating part 4
            if m > 20:
                w += 27
                number = (number - (0.2+0.3)) / 0.5
                if N >= 4:
                    return w
            else:
                w += m+7
                return w
        N += 1    
 
def repeat(n):
    list = []
    count=0
    while count<1001:
        list.append(mainFunction(count))
        count+=1
    return list
 
    
def W15(list,range):
    count = 0
    for i in list:
        if i <= 15:
            count += 1
    return count
def W20(list,range):
    count = 0
    for i in list:
        if i <= 20:
            count += 1
    return count 
def W30(list,range):
    count = 0
    for i in list:
        if i <= 30:
            count += 1
    return count   
def W40(list,range):
    count = 0
    for i in list:
        if i > 40:
            count += 1
    return count
def W5(list,range):
    count = 0
    for i in list:
        if i > 60:
            count += 1
    return count
def W6(list,range):
    count = 0
    for i in list:
        if i > 80:
            count += 1
    return count
def W7(list,range):
    count = 0
    for i in list:
        if i > 100:
            count += 1
    return count
 
list = repeat(1000)
median = np.median(list)
first_quartile = np.percentile(list, 25)
third_quartile = np.percentile(list, 75)
w15 = W15(list, 15)/1000
w20 = W20(list, 20)/1000
w30 = W30(list, 30)/1000
w40 = W40(list, 40)/1000
w5 = W5(list, 60)/1000
w6 = W6(list, 80)/1000
w7 = W7(list, 100)/1000
    
    
print("The mean value: ",np.mean(list))
print("The first Quartile: ", first_quartile)
print("The median value: ",np.median(list))
print("The third Quartile value: ", third_quartile)
print("W<=15: ",w15)
print("W<=20: ",w20)
print("W<=30: ",w30)
print("W>40: ",w40)
print("W>W5: ",w5)
print("W>W6: ",w6)
print("W>W7: ",w7)
