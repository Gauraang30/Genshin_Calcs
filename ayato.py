def stats (wep_atk,atk_percent,flat_atk,hp_percent,flat_hp,cdmg,hydro_dmg):
    atk=((wep_atk+265)*atk_percent)+flat_atk
    hp=(12501*hp_percent)+flat_hp
    cdmg_1=(cdmg*0.01)+1
    hydro_dmg_1=((hydro_dmg*0.01)+0.3)+1
    #hp_dmg_e=1.03*0.01*hp
    a=0
    dmg=hydro_dmg_1*cdmg_1/0.85*2
    #stack=6
    #hp_dmg_e*=stack
    n1_dmg=0
    n2_dmg=0
    n3_dmg=0
    '''for n in range (0,5):
        stack+=1
        n1=(0.9717*atk+hp_dmg_e)*dmg
        n1_dmg+=n1
        stack+=1
        n2=(1.0823*atk+hp_dmg_e)*dmg
        n2_dmg+=n2
        stack+=1
        n3=(1.1929*atk+hp_dmg_e)*dmg
        n3_dmg+=n3
    stack+=1
    n1=(0.9717*atk+hp_dmg_e)*dmg
    n1_dmg+=n1
    stack+=1
    n2=(1.0823*atk+hp_dmg_e)*dmg
    n2_dmg+=n2
    e_dmg=n1_dmg+n2_dmg+n3_dmg'''
    #looping individual nas
    '''for n in range (0,5):
        stack=6
        if stack==6 or stack==9 or stack==12 or stack==15 or stack==18:
            n1=(0.9717*atk+1.03*0.01*hp*stack)*dmg
            n1_dmg+=n1
        else:
            n1_dmg+=0
        stack+=1
    for n in range (0,5):
        stack=6
        if stack==7 or stack==10 or stack==13 or stack==16 or stack==19:
            n2=(1.0823*atk+1.03*0.01*hp*stack)*dmg
            n2_dmg+=n2
        else:
            n2_dmg+=0
        stack+=1
    for n in range (0,4):
        stack=6
        if stack==8 or stack==11 or stack==14 or stack==17:
            n3=(1.1929*atk+1.03*0.01*hp*stack)*dmg
            n3_dmg+=n3
    e_dmg=n1_dmg+n2_dmg+n3_dmg
    print(e_dmg)'''
    hp_dmg=0.0103*hp
    n1=(0.9717*atk+hp_dmg*6)*dmg
    n1_1=(0.9717*atk+hp-dmg*9)*dmg
    n1_2=(0.9717*atk+hp_dmg*12)*dmg
    n1_3=(0.9717*atk+hp_dmg*15)*dmg
    n1_4=(0.9717*atk+hp_dmg*18)*dmg
    n1_dmg=n1+n1_1+n1_2+n1_3+n1_4
    n2=(1.0823*atk+hp_dmg*7)*dmg
    n2_1=(1.0823*atk+hp_dmg*10)*dmg
    n2_2=(1.0823*atk+hp_dmg*13)*dmg
    n2_3=(1.0823*atk+hp_dmg*16)*dmg
    n2_4=(1.0823*atk+hp_dmg*19)*dmg
    n2_dmg=n2+n2_1+n2_2+n2_3+n2_4
    n3=(1.1929*atk+hp_dmg*8)*dmg
    n3_1=(1.1929*atk+hp_dmg*11)*dmg
    n3_2=(1.1929*atk+hp_dmg*14)*dmg
    n3_3=(1.1929*atk+hp_dmg*17)*dmg
    n3_dmg=n3+n3_1+n3_2+n3_3
    e_dmg=n1_dmg+n2_dmg+n3_dmg
    print(e_dmg)


    
stats(608,43,368,66.6,5500,175.8,61.6)
        