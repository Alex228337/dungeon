l = []
day_l = []

f = open('travels.txt','r')

for i in f:
    l = i.split()
    print(i)
    for element in l:
        day_l.append(l[6])
        day_l[0] = int(day_l[0])
        dm = max(day_l)
    
print(dm)

