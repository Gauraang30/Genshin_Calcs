atk=int(input("enter your atk% "))
atk_1=atk/100
atk_2=737*(1+atk_1)
c_dmg=2.6

gorou=int(input("are you using gorou press 1 else press anything "))
if gorou==1:
    def_1=2.69+0.25    
    def_2=(930*def_1)+330
    geo_dmg=1.856
else:
    geo_dmg=1.706
    def_1=2.69
    def_2=930*def_1
def_3=0.28*def_2
atk_3=0.9216*(def_2)
atk_4=atk_2+atk_3+311
atk_5=atk_4+def_3
dmg_1=atk_5*c_dmg*geo_dmg
dmg=atk_4*geo_dmg*c_dmg
aa_1=(1.3543*dmg_1)*1.15/1.75
aa_2=(1.3054*dmg_1)*1.15/1.75
aa_3=(1.5664*dmg_1)*1.15/1.75
aa_4=(2.0037*dmg_1)*1.15/1.75
c_1=1.5582*(atk_5+0.35*def_2)*c_dmg*geo_dmg*1.15/1.75
c_2=3.2634*(atk_5+0.35*def_2)*c_dmg*geo_dmg*1.15/1.75
c_3=(1.5464*dmg_1)*1.15/1.75
print("aa_1 dmg is ",aa_1)
print("aa_2 dmg is ",aa_2)
print("aa_3 dmg is ",aa_3)
print("aa_4 dmg is ",aa_4)
print("c_1 dmg is ",c_1)
print("c_2 dmg is ",c_2)
print("c_3 dmg is ",c_3)
