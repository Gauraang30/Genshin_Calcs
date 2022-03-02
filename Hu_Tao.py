attack=int(input("enter your attack "))
cdmg=float(input("enter your cdmg "))
pyrodmg=float(input("enter your pyrodmg "))
pyrodmg_1=(pyrodmg+100)/100
cdmg_1=(cdmg+100)/100
dmg=cdmg_1*pyrodmg_1
res_reduced=0.4
x=0.1-res_reduced
y=abs (x/2)
res_reduced_1=1-y
dmg_1=dmg*1.24

skill=2.14*dmg_1
hp=int(input("enter your hp "))
atk_inc=(5.66*hp)/100
atk=attack+atk_inc

em=int(input("enter your em "))
x=(-0.000505)*em
import math

math.exp( x )

b=math.exp(x)*0.189266831*em
z=b+15
z_1=(z+100)/100
z_2=1.5*(z_1)
charged=z_2*atk*skill
charged_1=charged/res_reduced_1
burst=z_2*4.99*atk*dmg_1
burst_1=burst/res_reduced_1
charged_2=charged_1/2
burst_2=burst_1/2

print("your charged dmg is= ",charged_2)
print("your burst dmg is= ",burst_2)
