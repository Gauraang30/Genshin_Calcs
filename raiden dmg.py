er=float(input("enter your er "))
edmg=(er-100)*0.4
burst_dmg=er/4
catch=float(input("are you using r5 catch? if yes enter 1 else enter anything else "))
kazuha=float(input("if you have kazuha enter 1 else enter anything else "))
if kazuha==1:
    em=float(input("enter em "))  

    edmg_1=(em*0.04) 
    edmg_2=edmg+edmg_1
else:
    edmg_2=edmg
if catch==1:
    burst_dmg+=32
    burst_dmg_1=burst_dmg+27
else:
    burst_dmg_1=burst_dmg+27
print("your edmg is",edmg_2)
edmg_3=(edmg_2+100)/100
burst_dmg_2=(burst_dmg_1+100)/100
print("your burst dmg is maybe(if the e multiplier counts)",burst_dmg_1)
attack=int(input("enter your attack "))
cdmg=float(input("enter your cdmg "))
cdmg_1=(cdmg+100)/100
stacks=int(input("enter no of stacks "))
dmg=attack*cdmg_1*edmg_3
base_musou=(7.21+(0.07*stacks))*burst_dmg_2*dmg
hit_1=(0.798+(0.0131*stacks))*burst_dmg_2*dmg
hit_2=(0.784+(0.0131*stacks))*burst_dmg_2*dmg
hit_3=(0.96+(0.0131*stacks))*burst_dmg_2*dmg
hit_4=(1.104+(0.0131*stacks))*burst_dmg_2*dmg
hit_5=(1.319+(0.0131*stacks))*burst_dmg_2*dmg
charged=(2.426+(0.0131*stacks))*burst_dmg_2*dmg
res_reduced=0.4
x=0.1-res_reduced
y=abs (x/2)
res_reduced_1=1-y
base_musou_1=base_musou/res_reduced_1
hit_1_1=hit_1/res_reduced_1
hit_2_1=hit_2/res_reduced_1
hit_3_1=hit_3/res_reduced_1
hit_4_1=hit_4/res_reduced_1
hit_5_1=hit_4/res_reduced_1
charged_1=charged/res_reduced_1
base_musou_2=base_musou_1/2
hit_1_2=hit_1_1/2
hit_2_2=hit_2_1/2
hit_3_2=hit_3_1/2
hit_4_2=hit_4_1/2
hit_5_2=hit_5_1/2
charged_2=charged_1/2
combo=(hit_1_2+hit_2_2+hit_3_2+charged_2)*3+(hit_1_2+charged_2)
total=base_musou_2+combo
print("base dmg is ",base_musou_2)
print("hit 1 dmg is ",hit_1_2)
print("hit 2 dmg is  ",hit_2_2)
print("hit 3 dmg is ",hit_3_2)
print("hit 4 dmg is ",hit_4_2)
print("hit 5 dmg is ",hit_5_2)
print("ca dmg is ",charged_2)
print("combo dmg is ",combo)
print("total dmg is ",total)