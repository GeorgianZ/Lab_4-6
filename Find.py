from Utils import get_suma_cheltuiala, get_ziua_cheltuiala, get_tip_cheltuiala

def cheltuieli_mari(l, suma):
    """
    functie care returneaza o lista care contine cheltuielile care au suma mai mare decat cea primita ca parametru
    input: l - lista
           suma -  int
    output: list - lista
    """
    list = []
    for curr_elem in range(len(l)):
        if(get_suma_cheltuiala(l[curr_elem])>suma):
            list.append(l[curr_elem])
    return list

def cheltuieli_mici(l, suma, data):
    """
    functie care returneaza o lista care contine cheltuielile care au suma mai mica decat cea primita ca parametru
    si care au data mai mica decat cea primita ca parametru
    input: l - lista
           suma - float
           data - int
    output: list - lista
    """
    list = []
    for curr_elem in range(len(l)):
        if(get_suma_cheltuiala(l[curr_elem])<suma  and get_ziua_cheltuiala(l[curr_elem])<data):
            list.append(l[curr_elem])
    return list

def afiseaza_by_type(l,tip):
    """
    functie care returneaza o lista care contine cheltuielile care au acelasi tip cu cel primit ca parametru
    input: l - lista
           tip - string
    output: list - lista
    """
    list = []
    for curr_elem in range(len(l)):
        if(get_tip_cheltuiala(l[curr_elem]) == tip):
            list.append(l[curr_elem])
    return list
