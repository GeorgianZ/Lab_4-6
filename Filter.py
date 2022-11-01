from Utils import get_tip_cheltuiala, get_suma_cheltuiala
def filter_by_type(l,tip):
    """
    functia formeaza o lista care contine elementele care au tipul diferit de cel indicat de utilizator
    input: l - lista
           tip - string
    output: list - lista
    """
    list = []
    for curr_elem in range(len(l)):
        if get_tip_cheltuiala(l[curr_elem]) != tip:
            list.append(l[curr_elem])
    return list

def filtrare_dupa_suma(l,suma):
    """
    functia creeaza o lista care contine elementele mai mari sau egale decat suma pe care o introduce utilizatorul
    input: l -lista
    output: list - lista
    """
    list = []

    for curr_elem in range(len(l)):
        if(get_suma_cheltuiala(l[curr_elem])>=suma):
            list.append(l[curr_elem])
    return list