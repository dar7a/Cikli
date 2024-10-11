print("Sveiki!")

zetoni=0

while zetoni<15:
    print(f"{zetoni} žetoni!")
    met=int(input("Iemet žetonus: "))
    zetoni+=met #zetoni=zetoni+met

zetoni=zetoni-15
print("Paņem kafiju!  Tavs atlikums ir {zetoni} žetoni")