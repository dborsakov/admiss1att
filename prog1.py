import pylab
import numpy as np
import math
import pylab
import matplotlib.pyplot as plt

f_oe = open('Borsyakov_close_eye.asc','r')
f_oe2 = open('Borsyakov_open_eye.asc', 'r')
arr = []
a = 0
n = 0
for line in f_oe:
    a += 1
    #print(line, end='')
    if (a>4):
        arr.append(int(line))
        n+=1
    if (a==n): break


#for i in arr:
#    print(str(i))

pylab.figure(1)
pylab.plot(arr,  'r')
arr2 = []

#---преобраз
Re = np.zeros(n, dtype=np.float) #массив действительных чисел
Im = np.zeros(n, dtype=np.float) #массив мнимых чисел
Result = np.zeros(n, dtype=np.float) #массив результата
ResultNew = np.zeros(50, dtype=np.float) #массив результата
st = 1/(math.sqrt(n))

for m in range(n):
    sumRe = 0
    sumIm = 0
    for k in range(n):
        sumRe += arr[k]*math.cos(2*math.pi/n*k*m)
        sumIm += arr[k]*math.sin(2*math.pi/n*k*m)
        #print(math.sin(((2*math.pi)/n)*k*m),'test')
        #print('m='+str(m)+' k='+str(k)+' sin(((2*math.pi)/n)*k*m)='+str(math.sin(2*math.pi/n*k*m))+' 2*math.pi/n='+str(2*math.pi/n))
    Re[m] = st*sumRe
    Im[m] = st*sumIm

for i in range(50):
    Result[i] = math.log10((Re[i]**2)+(Im[i]**2))
    ResultNew[i] = Result[i]


pylab.figure(2)
pylab.plot(ResultNew, 'b')

#-----------------------------------------------------open eye------
a=0
n=0
for line in f_oe2:
    a += 1
    #print(line, end='')
    if (a>4):
        arr.append(int(line))
        n+=1
    if (a==n): break

pylab.figure(3)
pylab.plot(arr,  'r')
arr2 = []

Re = np.zeros(n, dtype=np.float) #массив действительных чисел
Im = np.zeros(n, dtype=np.float) #массив мнимых чисел
Result = np.zeros(n, dtype=np.float) #массив результата
ResultNew = np.zeros(50, dtype=np.float) #массив результата
st = 1/(math.sqrt(n))


for m in range(n):
    sumRe = 0
    sumIm = 0
    for k in range(n):
        sumRe += arr[k]*math.cos(2*math.pi/n*k*m)
        sumIm += arr[k]*math.sin(2*math.pi/n*k*m)
        #print(math.sin(((2*math.pi)/n)*k*m),'test')
        #print('m='+str(m)+' k='+str(k)+' sin(((2*math.pi)/n)*k*m)='+str(math.sin(2*math.pi/n*k*m))+' 2*math.pi/n='+str(2*math.pi/n))
    Re[m] = st*sumRe
    Im[m] = st*sumIm

for i in range(50):
    Result[i] = math.log10((Re[i]**2)+(Im[i]**2))
    ResultNew[i] = Result[i]

pylab.figure(4)
pylab.plot(ResultNew, 'b')


pylab.show()
