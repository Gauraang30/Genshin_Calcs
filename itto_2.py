atk=int(input("enter your atk% "))
atk_1=atk/100
atk_a=int(input("enter your base atk "))
atk_2=atk_a*(1+atk_1)
c_dmg=2.5
def_percent=float(input("enter your def % "))
gorou=int(input("are you using gorou press 1 else press anything "))
if gorou==1:
    def_1=def_percent+0.25    
    def_2=(708*def_1)+330
    geo_dmg=1.856
else:
    geo_dmg=1.706
    def_1=def_percent
    def_2=708*def_1

atk_3=1.14*(def_2)
atk_4=atk_2+atk_3+311
dmg=atk_4*geo_dmg*c_dmg
aa_1=(1.6744*dmg)*1.15/1.75
aa_2=(1.5525*dmg)*1.15/1.75
aa_3=(1.8255*dmg)*1.15/1.75
aa_4=(2.4006*dmg)*1.15/1.75
c_3=(1.0738*dmg)*1.15/1.75
c_4=(1.9146*dmg)*1.15/1.75
print("aa_1 dmg is ",aa_1)
print("aa_2 dmg is ",aa_2)
print("aa_3 dmg is ",aa_3)
print("aa_4 dmg is ",aa_4)
print("c_3 dmg is ",c_3)
print("c_4 dmg is ",c_4)