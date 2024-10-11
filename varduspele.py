speletajs=input("Ievadi savu vārdu: ")

speletajs=speletajs.lower()

speletajs=speletajs.capitalize()

print(speletajs)

vards1="spindzele"

minejums=input(f"Uzmini vārdu - {vards1[0]}__{vards1[3]}__{vards1[6]}{vards1[7]}{vards1[8]}: ")

minejums=minejums.lower() 

if vards1==minejums:
    print("Uzminēji!")
else:
    print("Neuzminēji!")
print("Spēles beigas!")
