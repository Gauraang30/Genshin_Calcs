char_name=input("enter character name: ")
char_element=input("enter character element: ")
char_weapon=input("enter character weapon: ")
char_gender=input("enter character gender: ")
char_region=input("enter character region: ")
current_pity=int(input("enter current pity "))
primos=int(input("enter current primogem amt "))
wishes=int(input("enter current no of wishes "))
wishes_1=primos/160
total=current_pity+wishes+wishes_1
welkin=int(input("do you have welkin? if yes press 1 else type 0 "))
days_1=int(input("how many days welkin do you have? "))
days_tot=int(input("no of days till banner end? "))
days_2=days_tot-days_1
if welkin==1:
    daily=150*days_1
else:
    daily=60*days_1

daily_nowelkin=days_2*60
total_1=daily+daily_nowelkin
tot_1=total_1/160
total_fates=total+tot_1
guaranteed=int(input("are you on 50/50? if yes type 1 else type 0 "))
if guaranteed==1:
    no=180-total_fates
else:
    no=90-total_fates
tot_primos=no*160
print("Character Name : ",char_name)
print("Character Element : ",char_element)
print("Character Weapon : ",char_weapon)
print("Character Gender : ",char_gender)
print("Character Region : ",char_region)
if no<=0:
    print("the reqd fates are 0")
    print("the reqd primos are 0")
    print("you'll get",char_name,"easily")
else:
    print("the reqd fates are",no)
    print("the reqd primos are",tot_primos)
    print("you'll need to farm for",char_name)
