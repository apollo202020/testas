import pickle

# a = 1024
#
# with open("a.pkl", "wb") as file:
#     pickle.dump(a, file)

# with open("a.pkl", "rb") as file:
#     print(pickle.load(file))
# def nuskaityti_zmones():


zmones = []

while True:
    veiksmas = int(input("1 - perziuret\n2 - irasas\n3 - iseiti\n"))
    match veiksmas:
        case 1:
            with open("zmones.pkl", "rb") as file:
                print(pickle.load(file))

        case 2:
            vardas = input("ivesti varda: ")
            zmones.append(vardas)
            with open("zmones.pkl", "wb") as file:
                pickle.dump(zmones, file)

        case 3:
            print("viso gero")
            break