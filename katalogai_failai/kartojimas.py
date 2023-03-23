# TODO                                               KINTAMIEJI IF SALYGA

# a = float(input("Iveskite norima skaiciu: "))
# b = float(input("IVeskite antra norima skaiciu: "))
#
# if a < b:
#     print("A mazesnis uz b")
# elif a > b:
#     print("A didesnis uz b")
# else:
#     print("A yra lygu b")

print("===========================================================================================")

# eilute = "Zen of Python"
#
# print(eilute[-1])
# print(eilute[7])
# print(eilute[:3])
# print(eilute[7:])
# print(eilute[::-1])
# print(eilute.split())
# print(eilute.replace("Python", "Programing"))

print("===========================================================================================")

# a = int(input("IVeskite pirma skaiciu: "))
# b = int(input("Iveskite antra skaiciu: "))
# matematinis_veiksmas = input("Koki matematini veiksma norite atlikt?: ")
#
# if b == 0 or a == 0 and matematinis_veiksmas == "/":
#     print("Dalyba is nulio negalima")
# elif matematinis_veiksmas == "+":
#     print("Skaiciu sudetis", a, "+", b, "=", a + b)
# elif matematinis_veiksmas == "-":
#     print("Skaiciu atimtis", a, "-", b, "=", a - b)
# elif matematinis_veiksmas == "*":
#     print("Skaiciu daugyba", a, "*", b, "=", a * b)
# elif matematinis_veiksmas == "/":
#     print("Skaiciu dalyba", a, "/", b, "=", a / b)
# elif matematinis_veiksmas == "**":
#     print("Skaiciu pakelimas kvadratu", a, "**", b, "=", a ** b)
# elif matematinis_veiksmas == "**1/x":
#     print("Skaiciu saknies traukimas", a, "**1/x", b, "=", a **1/ b)
# else:
#     print("netinkamas simbolis")
print("===========================================================================================")

# a = int(input("Iveskite norima skaiciu: "))
# if a % 2 == 0:
#     print("Skaicius yra lygnis")
# else:
#     print("skaicius yra nelyginis")
#
# if a % 3 == 0:
#     print("SKaicius dalinasi is triju")

# todo                                              MASYVAI CIKLAI

# sarasas = [1, 2, 3, 10, 100, "labas", "kas tu?", 500, 1000]
#
# print(sarasas[6]) # atspausdinti 1 norima yrasa
# sarasas.append(1)  # prideti norima yrasa
# print(sarasas)
# sarasas[5] = "NELABAS" # pakeisti norima yrasa
# print(sarasas)
# sarasas.pop(1)  # istrinti norima yrasa
# print(sarasas)
# print("===========================================================================================")

# suma = 0
# while True:
#     a = int(input("Iveskite norima skaiciu: "))
#     if a < 0:
#         break
#     suma += a
#
# print(suma)

print("===========================================================================================")

# sarasas = []
#
# for i in range(5):
#     sarasas.append(input("Iveskite zodi: "))
#
# for zodis in sarasas:
#     print(sarasas, len(sarasas), sarasas.index(zodis))

print("===========================================================================================")
# import random
#
# skaicius = random.randint(1, 6)
# skaicius2 = random.randint(1, 6)
# skaicius3 = random.randint(1, 6)
# print(skaicius, skaicius2, skaicius3)
# if skaicius == 5 or skaicius2 == 5 or skaicius3 == 5:
#     print("Pralaimejai")
#
# else:
#     print("Laimejai")


print("===========================================================================================")

import datetime
import calendar

# metai = int(input("Iveskite metus formatu - %Y: "))
#
# if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
#     print("Kelemieji metai")
# else:
#     print("Nekeliemji metai")

for metai in range(1900, 2100):
    if metai % 400 == 0:
        print(metai)
    elif metai % 100 == 0:
        continue
    elif metai % 4 == 0:
        print(metai)
    else:
        continue


