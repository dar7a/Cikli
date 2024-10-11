vards=input("Ievadi savu vārdu nominatīvā locijumā (Kas?):")

vards=vards.lower() 
# funkcija .lower()- visus burtus kovertē par mazajiem burtiem.

vards=vards.capitalize()
# funkcija .capitalize()- simbolu virknē pirmo burtu konvertē par lielo.

UzminiVardu1="saies"
minejums=None

while UzminiVardu1!=minejums:
    # !=nav vienāds. 
    minejums=input(f"uzmini vārdu {UzminiVardu1[2]+UzminiVardu1[0]+UzminiVardu1[4]+UzminiVardu1[4]+UzminiVardu1[1]+UzminiVardu1[3]}: ")

print("Pareizi!")

UzminiVardu1="saule"

while True:
    minejums=input(f"uzmini vārdu {UzminiVardu1[2]+UzminiVardu1[0]+UzminiVardu1[4]+UzminiVardu1[4]+UzminiVardu1[1]+UzminiVardu1[3]}: ")

    if UzminiVardu1==minejums:
        print("Pareizi!")
        break

UzminiVardu1="sskola"

reizes=2

for i in range(3):
    minejums=input(f"uzmini vārdu {UzminiVardu1[2]+UzminiVardu1[0]+UzminiVardu1[4]+UzminiVardu1[4]+UzminiVardu1[1]+UzminiVardu1[3]}: ")

    if UzminiVardu1==minejums:
        print("Pareizi!")
        break
    else: 
        if reizes>0:
         print(f"Neuzminēji. Atlikušas {reizes} reizes.")
        reizes-=1
    
    print("Spēles beigas.")