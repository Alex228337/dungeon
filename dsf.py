from math import *

day=[0,0,0]
Lipki=0
october=0

naz={}
viez={}
benz={}



f=open('travels.txt','r')
for i in f:
    l=i.split()

    day[int(l[0])-1]+=int(l[6])  

    if l[2]=='Липки':             
        Lipki+= int(l[6])

    if l[0]=='1':                 
        october+= int(l[4])

    naz[l[2]]= int(l[6]) if  l[2] not in naz else naz[l[2]]+int(l[6])            
    viez[l[3]]= int(l[6]) if  l[3] not in viez else viez[l[3]]+int(l[6])                  
    benz[l[3]]= [1, int(l[5])] if  l[3] not in benz else [benz[l[3]][0]+1, benz[l[3]][1]+int(l[5])]                  



imax=0
for i in range(3):
    if day[i]==max(day):
        imax=i

max_b=0
max_key=''

for i in benz:
    benz[i]=benz[i][1]/benz[i][0]
    if benz[i]>max_b:
        max_b=benz[i]
        max_key=i


print(' дни: ', imax, l[1], ' масса: ', day[imax] )
print(' Липки: ', Lipki)
print(' 1 ', l[1], ' дистант ', october )
print('')
print(naz)
print('раз  ', len(naz))

print('')
print(viez)
print('раз ', len(viez))

print('')
print('расход',max_key, ' знач ' ,round(max_b,2))

f.close()
