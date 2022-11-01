from Utils import get_tip_cheltuiala,get_suma_cheltuiala,get_total_sum
def rap_total_sum(l,tip):
    """
    functia face suma tuturor cheltuielilor care apartin unui anumit tip
    input: l - lista
           tip - string
    output: suma totala a cheltuielilor din acelasi tip
    """
    sume = 0
    for curr_elem in range(len(l)):
        if get_tip_cheltuiala(l[curr_elem]) == tip:
            sume = sume + get_suma_cheltuiala(l[curr_elem])
    return sume

def rap_sum_zi_max(l):
    """
    functia returneaza ziua in care suma cheltuielilor este cea mai mare
    input: l -lista
    output: zi -int
    """
    maxim = 0
    sume = 0
    zi = 0
    for curr_elem in range(1,32):
        sume = get_total_sum(l,curr_elem)
        if (sume > maxim):
            maxim = sume
            zi = curr_elem
    return zi

def get_cheltuieli_by_sume(l,sume):
    """
    functia retuneaza o lista care contine doar cheltuielile care au suma egala cu cea introdusa de utilizator ca parametru
    input: l -list
           sume - int (suma introdusa de utilizator)
    output: list - lista
    """
    list = []
    for curr_elem in range(len(l)):
        if get_suma_cheltuiala(l[curr_elem]) == sume:
            list.append(l[curr_elem])
    return list

def get_cheltuieli_by_type(l):
    """
    functia returneaza o lista care contine cheltuielile sortate dupa tipul acestora
    input: l -lista
    output: list - lista care contine cheltuielile sortate dupa tip
    """
    list = l
    list.sort(key=get_tip_cheltuiala)
    return list


