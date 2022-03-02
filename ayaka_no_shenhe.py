ayaka_atk=2006
skill_multiplier_1=1.91
skill_multiplier_2=2.86
ayaka_dmg_1=(((skill_multiplier_1*ayaka_atk)*2.1792)*3.143)*19
ayaka_dmg_3=(((skill_multiplier_2*ayaka_atk)*2.1792)*3.143)
dmg=ayaka_dmg_1+ayaka_dmg_3
res_reduced=0.4
x=0.1-res_reduced
y=abs (x/2)
res_reduced_1=1-y
dmg_1=dmg/res_reduced_1
dmg_final=dmg_1/2
print(dmg_final)