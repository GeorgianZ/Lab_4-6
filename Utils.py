

"""
def creeaza_cheltuiala_lista(ziua, suma, tip_cheltuiala):
    
    functia va returna o lista care va contine ziua, suma si tipul cheltuielii
    input: ziua - int
           suma - float
           tip_cheltuiala - string
    output: list - lista
    
    cheltuiala = [ziua, suma, tip_cheltuiala]
    return cheltuiala
"""

def get_ziua_cheltuiala(cheltuiala):
    """
    functie care extrage ziua in care a fost facuta o cheltuiala
    input: cheltuiala
    output: ziua in care a fost efectuata
    """
    return cheltuiala["ziua"]
    #return cheltuiala[0]

def get_suma_cheltuiala(cheltuiala):
    """
    functie care extrage suma unei cheltuieli
    input: cheltuiala
    output: suma unei cheltuieli
    """
    return cheltuiala["suma"]
    #return cheltuiala[1]

def get_tip_cheltuiala(cheltuiala):
    """
    functie care extrage tipul unei cheltuieli
    input: cheltuiala
    output: tipul unei cheltuieli
    """
    return cheltuiala["tip_cheltuiala"]
    #return cheltuiala[2]


def get_total_sum(l,zi):
    """
    functia face suma totala a cheltuielilor care se realizeaza in aceeasi zi
    input: l - lista
           zi - int
    output: sume - int care este suma totala a cheltuielilor dintr-o zi
    """
    sume = 0
    for curr_elem in range(len(l)):
        if get_ziua_cheltuiala(l[curr_elem]) == zi:
            sume = sume + get_suma_cheltuiala(l[curr_elem])
    return sume



