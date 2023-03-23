
with open("failas.txt", "w") as file:
    file.write("Sveikas pasauli!")

with open("failas.txt", "r+") as file:
    tektas = file.read()
    file.write("Labas rytas, pasauli!")

print(tektas)

with open("failas.txt", "w", encoding="UTF-8") as file:   # SPECIALIOS RAIDES vietoje w jeigu a tada pridet galima teksta
    tektas = file.read()
    file.write("Øasasas Labas rytas, pasauli!")

print(tektas)

with open("failas.txt", "r", encoding="utf-8") as file:
    print(file.readline()[])

with open("failas.txt", "r", encoding="utf-8") as rfile:
    with open("failas_naujas", "a", encoding="utf-8") as wfile:
        for line in tektas:
            wfile.write("b" + line)


# print("Edvinas", end="") # i viena eilute sumeta end=""
# print("Sudzius", end="")
# print("Mokinys", end="")