import pickle

# todo 1. Leistų vartotojui įvesti norimą eilučių kiekį

# eiluciu_sk = ""
#
# while True:
#     ivedimas = input("Teksto ivedimas?: ")
#     eiluciu_sk += ivedimas + "\n"  # \n visad i nauja eilute nukelia
#     if not ivedimas:
#         break

# todo 2. Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
# failo_pav = input("ivesti failo pavadinimas: ")
#
# with open(f"{failo_pav}.txt", "w") as file:
#     file.write(eiluciu_sk)


# todo 3. Įrašytų įvestą tekstą atskiromis eilutėmis į failą

import os
import datetime
# todo 1
os.chdir("C\\Users\\slapt")
print(os.getcwd())

os.mkdir("Naujas katalogas")
# todo 2
os.chdir("C\\Users\\slapt")
