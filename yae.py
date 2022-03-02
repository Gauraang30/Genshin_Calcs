def stats(atk,flat_atk,chara_base_atk,cdmg,wep_atk,dmg_mul,elemental_dmg):             #atk percentage
    cdmg_1=(cdmg*0.01)+1                                        #cdmg percentage
    dmg_mul_1=(dmg_mul*0.01+1)
    kazuha=int(input('if u have kazu press 1 else press 0 \n'))
    if kazuha==1:
        elemental_dmg+=1.616+0.394
        elemental_res=0.85
    else:
        elemental_dmg+=1.616
        elemental_res=1.1
    raiden=int(input('if u have raiden press 1 else press 0 \n'))
    if raiden==1:
        burst_dmg=0.27
    else:
        burst_dmg=0
    sara=int(input('if u have sara press 1 else press 0 \n'))
    if sara==1:
        flat_atk+=484.617
    else:
        flat_atk+=0
    atk_tot=(((atk*0.01)+1)*(chara_base_atk+wep_atk))+flat_atk
    dmg=atk_tot*cdmg_1*(elemental_dmg)/(2*elemental_res)
    dmg_e_1=(1.0314)*dmg
    dmg_e_2=(1.2893)*dmg
    dmg_e_3=(1.6116)*dmg
    dmg_q=(4.42+5.6749*3)*atk_tot*cdmg_1*(elemental_dmg+burst_dmg)/(2*elemental_res)
    print(dmg_e_1)
    print(dmg_e_2)
    print(dmg_e_3)
    print(dmg_q)
widsith=int(input('0 if no buff 1 if atk 2 if elemental dmg'))
if widsith==0:                      #e stack 1=8688.171322289774 e stack 2=10860.635336269348 e stack 3=13575.583578633119 q=204908.51869489334                                                  
    stats(79.8,358,316,221.2,449,0,0)
elif widsith==1:                    #e stack 1=12283.946093009778 e stack 2=15355.52811490935 e stack 3=19194.11239431312 q=289714.0381185734
    stats(199.8,358,316,221.2,449,0,0)
elif widsith==2:                    #e stack 1=12837.745685174443 e stack 2=16047.804452099483 e stack 3=20059.444392308636 q=291185.7897243221
    stats(79.8,358,316,221.2,449,0,0.96)
