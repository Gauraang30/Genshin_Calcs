def_percent=float(input("enter def percentage w/o arti passive "))
def_percent_1=def_percent+54
def_percent_2=(def_percent_1+100)/100
def_tot=651*def_percent_2
dmg_increase=0.6296*def_tot
hp_percent=float(input("enter hp percentage "))
hp_percent_1=(0.01*hp_percent)+1
hp=9445*hp_percent_1
hp_flat=float(input("enter flat hp from artis including flower "))
hp_tot=hp+hp_flat
shield=(0.192*hp_tot)+2166
shield_1=shield*1.5
#hp% with hp bot is 236.9
#def% with def bot w/o arti effect is  236.9
#hp% with hybrid (hp/def/def hp wep)is 133.5 def% is 153.8
print("dmg increase is ",dmg_increase)
print("shield strength is ",shield_1)