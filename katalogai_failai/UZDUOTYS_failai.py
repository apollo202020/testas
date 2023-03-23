#todo 1 UZDUOTIS

# todo 1.Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
# import this
import datetime

tekstas = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# with open("Tekstas.txt", "w") as file:
#     file.write(tekstas)

# todo 2.Atspausdintų tekstą iš sukurto failo

# with open("Tekstas.txt", "r") as file:
#     print(file.read())



# todo 3.Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką

# with open("Tekstas.txt", "a") as file:
#     file.write(f"\n{datetime.datetime.today()\n}")


# todo 4.Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).

# naujas = ""
#
# with open("Tekstas.txt", 'r') as file:
#     for nr, line in enumerate(file, 1):
#         naujas += f"{nr} {line}"
#
#
# with open("Tekstas.txt", "w") as file:
#     file.write(naujas)

# todo 5.Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."

# with open("Tekstas.txt", "r") as file:
#     pakeitimas = file.read()
#
# pakeitimas = pakeitimas.replace("Beautiful is better than ugly.", "Grazu yra geriau nei bjauru")
#
# with open("Tekstas.txt", "w", encoding="UTF-8") as file:
#     file.write(pakeitimas)

# todo 6.Atspausdintų visą failo tekstą atbulai

# with open("Tekstas.txt", "r") as file:
#     file_tekstas = file.read()
#     print(file_tekstas[::-1])

# todo 7. Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių

# with open('Tekstas.txt', 'r') as file:
#     file_tekstas = file.read()
#     print("Žodžių kiekis:", len(file_tekstas.split()))
#     print("Skaičių kiekis:", sum(c.isdigit() for c in file_tekstas))
#     print("Didžiųjų raidžių:", sum(c.isupper() for c in file_tekstas))
#     print("Mažųjų raidžių:", sum(c.islower() for c in file_tekstas))




# todo 8: Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS

# with open("Tekstas.txt", "r", encoding="UTF-8") as nuskaitomas_failas:
#     with open("failas_naujas", "w", encoding="utf-8") as irasomas_failas:
#         irasomas_failas.write(nuskaitomas_failas.read().upper()






