from Add import srv_adauga_cheltuiala
from Utils import get_ziua_cheltuiala, get_suma_cheltuiala, get_tip_cheltuiala
def undo_list(l):
    """
    functie care face undo la ultima operatie care modifica lista
    input: l - lista
    output: aux - lista care contine elementele din l inainte de efectuarea unei operatii
    """
    aux= []
    for curr_elem in range(len(l)):
        srv_adauga_cheltuiala(aux,get_ziua_cheltuiala(l[curr_elem]),get_suma_cheltuiala(l[curr_elem]),get_tip_cheltuiala(l[curr_elem]))
    return aux