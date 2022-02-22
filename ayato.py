def stats (wep_atk,atk_percent,flat_atk,hp_percent,flat_hp,cdmg,hydro_dmg):
    atk=((wep_atk+265)*((atk_percent*0.01)+1))+flat_atk
    hp=(12501*(hp_percent*0.01+1))+flat_hp
    cdmg_1=(cdmg*0.01)+1
    hydro_dmg_1=((hydro_dmg*0.01)+0.3)+1
    dmg=hydro_dmg_1*cdmg_1/(0.85*2)
    hp_dmg=0.0103*hp
    n1=((0.9717*atk)+hp_dmg*2)*dmg+((0.12*atk)*cdmg_1/2)
    n1_1=((0.9717*atk)+hp_dmg*4)*dmg+((0.12*atk)*cdmg_1/2)
    n1_dmg=n1+(n1_1*5)
    n2=(1.0823*atk+hp_dmg*3)*dmg+((0.12*atk)*cdmg_1/2)
    n2_1=(1.0823*atk+hp_dmg*4)*dmg+((0.12*atk)*cdmg_1/2)
    n2_dmg=n2+(n2_1*4)
    n3=(1.1929*atk+hp_dmg*4)*dmg+((0.12*atk)*cdmg_1/2)
    n3_dmg=n3*5
    e_dmg=n1_dmg+n2_dmg+n3_dmg
    print(e_dmg)
    
stats(608,66.6,368,25,5500,175.8,61.6) # atk sands #wep_atk,atk_percent,flat_atk,hp_percent,flat_hp,cdmg,hydro_dmg
stats(608,25,368,66.6,5500,175.8,61.6) # hp sands
