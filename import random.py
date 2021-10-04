x= "hu tao"
w="eula"
z="both"
x_1=0
y_1=0
z_1=0
import random

list = [x, w, z]
n=len(list)
for s in range(1,201):
    for b in range(1,n) : 
        a=random.choice(list)
        if a==x:
            x_1+=1
        if a==w:
            y_1+=1  
        if a==z:
            z_1+=1

    if x_1>67 or y_1>67 or z_1>67:
        break    
print("hu tao",x_1)
print("eula",y_1)
print("both",z_1)


    