x= "hu tao"
w="eula"
import random

list = [x, w]
n=len(list)
for b in range(1,n) : 
    a=random.choice(list)
    print(a)
    list.remove(a)