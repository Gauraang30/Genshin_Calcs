def stats(atk,flat_atk,cdmg,defence,flat_def,wep_atk,dmg_mul):
    atk_tot=(((atk*0.01)+1)*(227+wep_atk))+flat_atk             #atk percentage
    cdmg_1=(cdmg*0.01)+1                                        #cdmg percentage
    dmg_mul_1=(dmg_mul*0.01+1)                                  #from skyward pride passive
    gorou=int(input("are you using gorou press 1 else press anything "))
    if gorou==1:    
        defence_tot=(((defence*0.01)+1.25)*959)+flat_def
        geo_dmg=1.856
    else:
        defence_tot=(((defence*0.01)+1)*959)+flat_def
        geo_dmg=1.706
    def_atk=0.9792*defence_tot                                  #defence to atk lv 9 q
    atk_q=atk_tot+def_atk                                       #total atk in q
    dmg_1=(atk_q*1.6748+0.35*defence_tot)*(geo_dmg+dmg_mul_1+0.15)*cdmg_1     #dmg for first 4 kesaragi slashes at aa lv 9
    dmg_2=(atk_q*3.5076+0.35*defence_tot)*(geo_dmg+dmg_mul_1+0.15)*cdmg_1      #dmg for final kesaragi slash at aa lv 9 (0.15 dmg increase is due to geo resonance)
    dmg_1_rel=(dmg_1)/(2*0.85)                                                 #2 is enemy def 0.85 is res geo res due to zl shield and resonance
    dmg_2_rel=(dmg_2)/(2*0.85)
    print('1-4 slashes dmg is ',dmg_1_rel)
    print('final slash dmg is ',dmg_2_rel)
    '''vaccum_dmg=((atk_q*0.8)*cdmg_1*dmg_mul_1)/(2*0.95)
    print(vaccum_dmg)'''                                        #skyward pride vaccum blades dmg
wep=input('enter "whiteblind" or "sky"')
if wep=='whiteblind':
    stats(29.3,340,160,173.3,23,510,0)
elif wep=='sky':
    stats(5.3,340,160,97.6,23,674,8)
else:
    print('ERROR')
