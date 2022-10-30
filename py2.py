birinchi = int(input("1-sonni kiriting: "))
ikkinchi = int(input("2-sonni kiriting: "))
amal = input("amalni kiriting: ")
def kalkulyator(birinchi, ikkinchi):
    if amal =="-":
        print(birinchi-ikkinchi)
    elif amal == "+":
        print(birinchi+ikkinchi)
    elif amal == "/":
        print(birinchi/ikkinchi)
    elif amal == "*":
        print(birinchi*ikkinchi)

kalkulyator(birinchi, ikkinchi)