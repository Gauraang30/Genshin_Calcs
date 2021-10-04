x=int(input("enter how many values do you wanna calc perecntage diff of "))
while x>0:
    a=float(input("enter the first no "))
    b=float(input("enter the second no "))
    if a>b:
        c=((a-b)/b)*100
    else:
        c=((b-a)/a)*100
    print(c,"%")    
    x-=1
    

