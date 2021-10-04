attack=int(input("enter your attack "))
cdmg=float(input("enter your cdmg "))
cryodmg=float(input("enter your cryodmg "))
cryodmg_1=(cryodmg+100)/100
cdmg_1=(cdmg+100)/100
dmg=attack*cdmg_1*cryodmg_1
skill=(1.7968*19+2.6952)*dmg
skill_3=1.7968*dmg
skill_6=2.6952*dmg
res_reduced=0.4
x=0.1-res_reduced
y=abs (x/2)
res_reduced_1=1-y
skill_1=skill/res_reduced_1
skill_2=skill_1/2
skill_4=skill_3/res_reduced_1
skill_5=skill_4/2
skill_7=skill_6/res_reduced_1
skill_8=skill_7/2
print("your dmg is ",skill_2)
print("cutting dmg is ",skill_5)
print("bloom dmg is ",skill_8)
