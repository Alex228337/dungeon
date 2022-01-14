l = []
with open('Perepis.txt', 'r') as f:
    l = f.read().splitlines()
print(l)
count = 0
for i in l:
    l = i.split('.')
    l[2] = int(l[2])
    if l[2]<1978:
        count = count+1
        l = i.split()
        print(l[0])
print(count)  

f.close()

l2 = []

y1 = int(input())
y2 = int(input())
with open('Perepis.txt', 'r') as f:
    l2 = f.read().splitlines()
for i in l2:
    l2 = i.split('.')
    l2[2] = int(l2[2])
    if y1<=l2[2]<=y2:
        print(l2[2])
        l = i.split()
        print(l[0],l[1],l[2],)
    
  
