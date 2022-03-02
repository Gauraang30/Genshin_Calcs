pyrodmg_1_1=float(input("enter your pyrodmg "))
pyrodmg_2_1=(pyrodmg_1_1+100)/100
dmg_1_1=1.32*pyrodmg_2_1
skill=2.14*dmg_1_1
em=int(input("enter your em "))
x=(-0.000505)*em
import math

math.exp( x )

b_1=math.exp(x)*0.189266831*em
z_1=b_1
z_1_1=(z_1+100)*1.15/100
z_2_1=1.5*(z_1_1)
charged_1=z_2_1*skill
burst_1=z_2_1*4.99

pyrodmg_1_2=float(input("enter your pyrodmg "))
pyrodmg_2_2=(pyrodmg_1_2+100)/100
dmg_1_2=1.32*pyrodmg_2_2
skill=2.14*dmg_1_2
em_1=int(input("enter your em "))
x_1=(-0.000505)*em_1

math.exp( x_1 )

b_2=math.exp(x_1)*0.189266831*em_1
z_2=b_2
z_1_2=(z_2+100)/100
z_2_2=1.5*(z_1_2)
charged_2=z_2_2*skill*1.5
burst_2=z_2_2*4.99
print("cw ca",charged_1)
print("cw q",burst_1)
print("sr ca",charged_2)
print("sr q",burst_2)
print(z_1_1)
 
if charged_2>charged_1:
    percent_diff_ca=(charged_2-charged_1)*100/charged_1
    print("percent diff betn ca sr>cw",percent_diff_ca)
else:
    percent_diff_ca=(charged_1-charged_2)*100/charged_2
    print("percent diff betn ca cw>sr",percent_diff_ca)

if burst_2>burst_1:
    percent_diff_q=(burst_2-burst_1)*100/burst_1
    print("percent diff betn q sr>cw",percent_diff_q)
else:
    percent_diff_q=(burst_1-burst_2)*100/burst_2 
    print("percent diff betn q cw>sr",percent_diff_q)         