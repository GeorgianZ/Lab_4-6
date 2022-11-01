from Utils import get_suma_cheltuiala, get_ziua_cheltuiala, get_tip_cheltuiala

def creeaza_cheltuiala(ziua,suma,tip_cheltuiala):
    """
    functia va returna un dictionar care va contine ziua, suma si tipul cheltuielii
    input: ziua - int
           suma - float
           tip_cheltuiala - string
    output: datele unei cheltuieli
    """
    return {
        "ziua":ziua,
        "suma":suma,
        "tip_cheltuiala":tip_cheltuiala
    }

def valideaza_cheltuiala(cheltuiala):
    """
    functie care verifica: -daca ziua este cuprinsa in intervalul [1,31]
                           -daca suma este un numar real pozitiv
                           -daca tipul de cheltuiala este unul din cele specificate in enunt
    input: o cheltuiala
    output: -, daca cheltuiala este valida
    raises: Exception cu textul:
                    - "zi invalida!\n" daca ziua<1 sau ziua>31
                    - "suma invalida!\n" daca suma<0 sau daca suma nu este un numar real
                    - "tip invalid!\n" daca tipul este oricare altul decat cele specificate:(mancare, intretinere, imbracaminte, telefon,altele)
    """
    err = ""
    if(get_ziua_cheltuiala(cheltuiala)>31 or get_ziua_cheltuiala(cheltuiala)<1):
        err += "zi invalida!\n"

    if(isinstance(get_suma_cheltuiala(cheltuiala),float)==False):
        err += "suma invalida!\n"
    elif(get_suma_cheltuiala(cheltuiala)<0):
        err += "suma invalida!\n"

    if(get_tip_cheltuiala(cheltuiala)!="mancare" and get_tip_cheltuiala(cheltuiala)!="intretinere" and get_tip_cheltuiala(cheltuiala)!="imbracaminte" and get_tip_cheltuiala(cheltuiala)!="telefon" and get_tip_cheltuiala(cheltuiala)!="altele" ):
        err += "tip invalid!\n"

    if(len(err)>0):
        raise Exception(err)

def adauga_cheltuiala(l,cheltuiala):
    """
    functie care adauga intr-o lista datele unei cheltuieli introduse de catre utilizator
    input: lista de cheltuieli si o cheltuiala
    output: -, daca cheltuiala a fost adaugata in lista
    """
    l.append(cheltuiala)


def srv_adauga_cheltuiala(l,ziua,suma,tip_cheltuiala):
    """
    functie care creeaza o cheltuiala cu valorile introduse, o valideaza, iar apoi o adauga in lista
    functia va afisa erorile corespunzatoare daca datele introduse nu sunt corecte
    input: l - lista
           ziua - int
           suma - float
           tip_cheltuiala - string
    output: -, daca cheltuiala este adaugata in lista
    """
    cheltuiala = creeaza_cheltuiala(ziua,suma,tip_cheltuiala)
    valideaza_cheltuiala(cheltuiala)
    adauga_cheltuiala(l,cheltuiala)


def srv_modifica_cheltuiala(l,ziua,suma,tip_cheltuiala,elem):
    """
    functie care creeaza o cheltuiala cu valorile introduse, o valideaza, iar apoi modifica valorile elementului
    din lista corespunzator cu valoarea aleasa de utilizator daca datele introduse sunt corecte
    input: l - lista
           ziua -int
           suma - float
           tip_cheltuiala - string
           elem - float
    output: -, daca cheltuiala selectata de utilizator este modificata
    """
    cheltuiala = creeaza_cheltuiala(ziua, suma, tip_cheltuiala)
    valideaza_cheltuiala(cheltuiala)
    l[elem-1] = cheltuiala