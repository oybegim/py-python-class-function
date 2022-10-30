birinchi = int(input("birinchi sonni kiriting: "))
ikkinchi = int(input("ikkinchi sonni kiriting: "))
def sanash(birinchi, ikkinchi):
    while birinchi<ikkinchi:
        ikkinchi -= 1
        print(ikkinchi)
sanash(birinchi, ikkinchi)