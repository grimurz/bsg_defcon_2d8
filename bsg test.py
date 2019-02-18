import numpy as np
import matplotlib.pyplot as plt

n = 100000
r = np.zeros(13)

for i in range(n):
    
    d12 = 1
    while True:
        
        roll = np.random.randint(8)+1 + np.random.randint(8)+1
        #roll = np.random.randint(20)+1 
                
        if roll <= np.max([d12,2]):
            r[d12] += 1
            break
    
        if d12 < 12:
            d12 += 1

#r = r[1:]
r = r / n * 100

objects = (range(1,13))
y_pos = np.arange(len(objects))
 
plt.bar(y_pos, r[1:], align='center', alpha=0.8)
plt.xticks(y_pos, objects)
plt.xlabel('turn')
plt.ylabel('%')
 
plt.show()

print("[6,7,8]:",np.round_(r[6]+r[7]+r[8],2))
print("[5,6,7,8,9]:",np.round_(r[5]+r[6]+r[7]+r[8]+r[9],2))
#print("![6,7,8]:",r[1]+r[2]+r[3]+r[4]+r[5]+r[9]+r[10]+r[11]+r[12])
#print("[5,6,8]:",r[5]+r[6]+r[7])
#print("[4,5,6,7,8]:",r[4]+r[5]+r[6]+r[7]+r[8])