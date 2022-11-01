from Utils import get_ziua_cheltuiala, get_tip_cheltuiala

def sterge_din_lista_1(l,date):
    """
    functia sterge din lista cheltuielile care au data egala cu cea introdusa ca parametru
    input: l - lista
           date - int
    output: l - lista
    """
    n = len(l)
    curr_elem = 0
    while curr_elem<n:
        if(get_ziua_cheltuiala(l[curr_elem]) == date):
            del l[curr_elem]
            n = n - 1
        else:
            curr_elem = curr_elem + 1
    return l

def sterge_din_lista_2(l,date1,date2):
    """
    functia sterge din lista cheltuielile a caror data apartine intervalului [date1, date2]
    input: l - lista
           date1 - int
           date2 - int
    output: l - lista
    """
    n = len(l)
    curr_elem = 0
    while curr_elem < n:
        if(date1 <= get_ziua_cheltuiala(l[curr_elem]) <= date2):
            del l[curr_elem]
            n = n - 1
        else:
            curr_elem = curr_elem + 1
    return l

def sterge_by_type(l,tip):
    """
    functia sterge din lista cheltuielile care au tipul egal cu cel introdus ca parametru
    input: l - lista
           date - int
    output: l - lista
    """
    n = len(l)
    curr_elem = 0
    while curr_elem < n:
        if (get_tip_cheltuiala(l[curr_elem]) == tip):
            del l[curr_elem]
            n = n - 1
        else:
            curr_elem = curr_elem + 1
    return l