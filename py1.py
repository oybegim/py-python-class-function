a =[["Uzbekistan: ", "Turkey: ", "Russia: ", "USA:  "],
["The capital: Tashkent", "The capital: Ankara", "The capital: Moscow", "The capital: Washington"], 
["language: Uzbek", "language: Turkish", "language: Russian", "language: English"]]
b = input("1.Uzbekistan, 2.Turkey, 3.Russia, 4.USA")
if b == "Uzbekistan":
    print(a[0][0])
    print(a[1][0])
    print(a[2][0])
elif b == "Turkey":
    print(a[0][1])
    print(a[1][1])
    print(a[2][1])
elif b == "Russia":
    print(a[0][2])
    print(a[1][2])
    print(a[2][2])
elif b == "USA":
    print(a[0][3])
    print(a[1][3])
    print(a[2][3])
