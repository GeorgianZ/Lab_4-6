from Teste import ui_test_functii
from Add import srv_adauga_cheltuiala, srv_modifica_cheltuiala
from Delete import *
from Find import cheltuieli_mari, cheltuieli_mici, afiseaza_by_type
from Raports import *
from Filter import *
from Undo import *

def ui_afiseaza_cheltuieli_mari(l):
    """
    functie care afiseaza cheltuielile care au suma mai mare decat una introdusa de utilizator
    input: l - lista
    output: afiseaza datele cheltuielilor pe care le cautam
    """
    try:
        suma = float(input("Introduceti o suma:"))
    except ValueError:
        print("Introduceti un numar real valid!")
    return cheltuieli_mari(l, suma)

def ui_afiseaza_cheltuieli_mici(l):
    """
    functie care afiseaza cheltuielile care au suma mai mica decat una introdusa de utilizator si care
    s-au realizat inainte de o data specificata
    input: l - lista
    output: afiseaza datele cheltuielilor pe care le cautam
    """
    try:
        suma = float(input("Introduceti o suma:"))
    except ValueError:
        print("Introduceti un numar real valid!")

    try:
        data = int(input("Introduceti o data:"))
    except ValueError and (data>31 or data<1):
        print("Introduceti un numar intreg, mai mare egal decat 1 si mai mic egal decat 31")
    return cheltuieli_mici(l, suma, data)




def ui_modifica_cheltuiala(l):
    """
    functia preia pozitia elementului din lista pe care utilizatorul doreste sa o mofidice,
    apoi citeste noile valori pe care utilizatorul doreste sa le insereze
    input: l - lista
    output: l - lista,
            ziua- int
            suma - float
            tip_cheltuiala - string
            elem - int
    """
    elem = len(l)+1
    while(elem>(len(l))):
        try:
            elem = int(input("Introduceti numarul cheltuielii pe care doriti sa o modificati:"))
        except ValueError:
            print("Introduceti o valoare intreaga si mai mica decat ultimul element din lista!")
    try:
        ziua = int(input("ziua:"))
    except ValueError:
        print("Valoare incorecta!")

    try:
        suma = float(input("suma:"))
    except ValueError:
        print("Valoare incorecta!")

    tip_cheltuiala = input("Tip cheltuiala:")
    srv_modifica_cheltuiala(l,ziua,suma,tip_cheltuiala,elem)

def ui_adauga_in_lista(l):
    """
    functie care adauga in lista o cheltuiala
    input: l -lista
    output: -,daca cheltuiala este adaugata in lista
    """
    try:
        ziua = int(input("ziua:"))
    except ValueError:
        print("Valoare incorecta!")

    try:
        suma = float(input("suma:"))
    except ValueError:
        print("Valoare incorecta!")

    tip_cheltuiala = input("Tip cheltuiala:")

    srv_adauga_cheltuiala(l,ziua,suma,tip_cheltuiala)

def ui_sterge_din_lista_1(l):
    """
    functia ia o valoare introdusa de utilizator si va sterge elementele din lista care au ca parametru
    "ziua" egala cu valoare introdusa
    input: l -lista
    output: -
    """
    elem = 32
    while(elem>31 or elem<0):
        elem = int(input("Introduceti data:"))
    sterge_din_lista_1(l, elem)


def ui_sterge_din_lista_2(l):
    """
    functia ia 2 valori introduse de utilizator si va sterge elementele din lista care au ca parametru
    "ziua" egala o valoare din intervalul celor 2 valori
    input: l -lista
    output: -
    """
    elem1 = 32
    elem2 =32
    while(elem1>31 or elem1<0):
        elem1 = int(input("Introduceti prima data:"))
    while (elem2 > 31 or elem2 < 0):
        elem2 = int(input("Introduceti a doua data:"))
    if(elem1>elem2):
        elem1, elem2 = elem2, elem1
    sterge_din_lista_2(l,elem1,elem2)

def ui_sterge_by_type(l):
    """
    functia sterge din lista elementele care au tipul introdus de utilizator
    input: l - lista
    output: -
    """
    tip = []
    while (
            tip != "mancare" and tip != "intretinere" and tip != "imbracaminte" and tip != "telefon" and tip != "altele"):
        tip = input("Introduceti tipul de cheltuiala pe care doriti sa-l afisati:")
    sterge_by_type(l,tip)


def ui_afiseaza_cheltuieli_tip(l):
    """
    functie care afiseaza cheltuielile care au acelasi tip introdus de utilizator
    input: l - lista
    output: afiseaza elementele din lista care corespund cautarii
    """
    tip=[]
    while(tip!="mancare" and tip!="intretinere" and tip!="imbracaminte" and tip!="telefon" and tip!="altele"):
        tip = input("Introduceti tipul de cheltuiala pe care doriti sa-l stergeti:")
    return afiseaza_by_type(l,tip)



def ui_total_sum(l):
    """
    functie care afiseaza suma totala a aceluiasi tip de cheltuiala care este introdus de catre utilizator
    input: l -lista
    output: sume - int
    """
    tip = []
    while (tip != "mancare" and tip != "intretinere" and tip != "imbracaminte" and tip != "telefon" and tip != "altele"):
        tip = input("Introduceti tipul de cheltuiala pe care doriti sa-l afisati:")
    return rap_total_sum(l,tip)


def ui_find_day_by_sume(l):
    """
    functie care afiseaza ziua in care suma cheltuita a fost maxima
    input: l - lista
    output: zi - int
    """
    return rap_sum_zi_max(l)

def ui_print_cheltuieli_by_sum(l):
    """
    functie returneaza cheltuielile care au suma egala cu cea introdusa de utilizator
    input: l - lista
    output: list - lista
    """
    try:
        sume = float(input("Introduceti suma:"))
    except ValueError:
        print("Introduceti o valoare valida")

    list = get_cheltuieli_by_sume(l,sume)

    return list

def ui_print_cheltuieli_by_type(l):
    """
    functia returneaza o lista care contine cheltuielile sortate dupa tipul acestora
    input: l - lista
    output: list - lista
    """
    list = get_cheltuieli_by_type(l)
    return list

def ui_filter_by_type(l):
    """
    functia returneaza o lista care contine cheltuielile care nu au tipul introdus de utilizator
    input: l - lista
    output: list - lista
    """
    tip = []
    while (
            tip != "mancare" and tip != "intretinere" and tip != "imbracaminte" and tip != "telefon" and tip != "altele"):
        tip = input("Introduceti tipul de cheltuiala pe care doriti sa-l eliminati:")
    list = filter_by_type(l,tip)
    return list

def ui_afiseaza_filtrare_dupa_suma(l):
    """
    functia returneaza o lista filtrata care nu contine cheltuielile mai mici decat suma introdusa de utilizator
    input: l - lista
    output: list - lista
    """
    try:
        suma = float(input("Introduceti o suma:"))
    except ValueError:
        print("Introduceti o valoare reala valida!")
    list = filtrare_dupa_suma(l, suma)
    return list

def Undo(aux):
    """
    functie care face undo la ultima operatie care modifica lista
    input: aux - lista
    output: lista
    """
    n = len(aux)-1
    return aux[n]

def new_interface():
    l = []
    while True:
        command = input("Introduceti comanda:")
        cmd = command.split(" ")
        if cmd[0] == "adauga":
            try:
                srv_adauga_cheltuiala(l, int(cmd[1]), float(cmd[2]), cmd[3])
            except Exception as ex:
                print(ex)

        elif cmd[0] == "modifica":
            if (len(l) == 0):
                print("Aceasta functie poate fi folosita numai dupa ce introduceti cel putin o cheltuiala in lista!")
            else:
                try:
                    srv_modifica_cheltuiala(l, cmd[1], cmd[2], cmd[3], int(cmd[4]))
                except Exception as ex:
                    print(ex)

        elif cmd[0] == "tipareste":
            if (len(l) == 0):
                print("Aceasta functie poate fi folosita numai dupa ce introduceti cel putin o cheltuiala in lista!")
            elif (cmd[1] == "altele" or cmd[1] == "mancare" or cmd[1] == "telefon" or cmd[1] == "intretinere" or cmd[1] == "imbracaminte"):
                print(afiseaza_by_type(l,cmd[1]))
            elif (cmd[1] == "sortare" and cmd[2] == "tip"):
                print(get_cheltuieli_by_type(l))

        elif command == "print":
            print(l)

        elif command == "exit":
            return


def ui_main():
    l=[]
    aux = []
    print("\tGestionarea cheltuielilor de familie realizate intr-o luna\n"
          "1.Adauga o noua cheltuiala\n"
          "2.Modifica o cheltuiala existenta\n"
          "3.Sterge toate cheltuielile pentru o anumita zi\n"
          "4.Sterge toate cheltuielile pentru un anumit interval de zile\n"
          "5.Sterge toate cheltuielile de un anumit tip\n"
          "6.Tipareste cheltuielile mai mari decat o anumita suma\n"
          "7.Tipareste cheltuielile mai mici decat o anumita suma si care s-au realizat inainte de o data specificata\n"
          "8.Tipareste toate cheltuielile de un anumit tip\n"
          "9.Tipareste suma totala pentru un anumit tip de cheltuiala\n"
          "10.Tipareste ziua in care suma cheltuita este maxima\n"
          "11.Tipareste toate cheltuielile ce au o anumita suma\n"
          "12.Tipareste cheltuielile sortate dupa tip\n"
          "13.Filtreaza si elimina cheltuielile de un anumit tip\n"
          "14.Filtreaza si elimina cheltuielile mai mici decat o suma data\n"
          "15.Undo-Afiseaza lista anterioara unei comenzi efectuate care modifica lista\n"
          "16.Tasteaza exit pentru a parasi programul\n")
    while True:
        cmd = input("Introduceti o comanda:")
        if (cmd == "exit"):
            print("Ati parasit programul!\n")
            return

        elif (cmd == "1"):
            aux.append(undo_list(l))
            try:
                ui_adauga_in_lista(l)
            except Exception as ex:
                print(ex)
        elif (cmd == "2"):
            aux.append(undo_list(l))
            if (len(l) == 0):
                print("Aceasta functie poate fi folosita numai dupa ce introduceti cel putin o cheltuiala in lista!")
            else:
                try:
                    ui_modifica_cheltuiala(l)
                except Exception as ex:
                    print(ex)

        elif (cmd == "3"):
            aux.append(undo_list(l))
            if (len(l) == 0):
                print("Aceasta functie poate fi folosita numai dupa ce introduceti cel putin o cheltuiala in lista!")
            else:
                ui_sterge_din_lista_1(l)

        elif (cmd == "4"):
            aux.append(undo_list(l))
            if (len(l) == 0):
                print("Aceasta functie poate fi folosita numai dupa ce introduceti cel putin o cheltuiala in lista!")
            else:
                ui_sterge_din_lista_2(l)

        elif (cmd == "5"):
            aux.append(undo_list(l))
            if (len(l) == 0):
                print("Aceasta functie poate fi folosita numai dupa ce introduceti cel putin o cheltuiala in lista!")
            else:
                ui_sterge_by_type(l)

        elif (cmd == "6"):
            if(len(l) == 0):
                print("Inca nu ati adaugat o cheltuiala!")
            else:
                try:
                    print(ui_afiseaza_cheltuieli_mari(l))
                except Exception as ex:
                    print(ex)
        elif (cmd == "7"):
            if (len(l) == 0):
                print("Inca nu ati adaugat o cheltuiala!")

            else:
                try:
                    print(ui_afiseaza_cheltuieli_mici(l))
                except Exception as ex:
                    print(ex)
        elif (cmd == "8"):
            if (len(l) == 0):
                print("Inca nu ati adaugat o cheltuiala!")

            else:
                print(ui_afiseaza_cheltuieli_tip(l))

        elif (cmd == "9"):
            if (len(l) == 0):
                print("Inca nu ati adaugat o cheltuiala!")
            else:
                print(ui_total_sum(l))

        elif (cmd == "10"):
            if (len(l) == 0):
                print("Inca nu ati adaugat o cheltuiala!")
            else:
                print(ui_find_day_by_sume(l))

        elif (cmd == "11"):

            if (len(l) == 0):
                print("Inca nu ati adaugat o cheltuiala!")
            else:
                list = []
                try:
                    list = ui_print_cheltuieli_by_sum(l)
                except Exception as ex:
                    print(ex)
            if(len(list)):
                print(list)

        elif (cmd == "12"):
            if (len(l) == 0):
                print("Inca nu ati adaugat o cheltuiala!")
            else:
                print(ui_print_cheltuieli_by_type(l))

        elif (cmd == "13"):
            if (len(l) == 0):
                print("Inca nu ati adaugat o cheltuiala!")
            else:
                print(ui_filter_by_type(l))

        elif (cmd == "14"):
            if(len(l) == 0):
                print("Inca nu ati adaugat o cheltuiala!")
            else:
                try:
                    print(ui_afiseaza_filtrare_dupa_suma(l))
                except Exception as ex:
                    print(ex)

        elif (cmd == "Undo"):
                l = Undo(aux)
                print(l)

        else:
            print("Comanda invalida!")

ui_test_functii()
new_interface()
ui_main()