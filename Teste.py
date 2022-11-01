from Add import creeaza_cheltuiala, valideaza_cheltuiala, adauga_cheltuiala, srv_adauga_cheltuiala, srv_modifica_cheltuiala
from Delete import sterge_din_lista_1, sterge_din_lista_2, sterge_by_type
from Find import *
from Utils import *
from Raports import rap_total_sum, rap_sum_zi_max, get_cheltuieli_by_sume, get_cheltuieli_by_type
from Filter import filter_by_type,filtrare_dupa_suma
from Undo import *

def test_valideaza_cheltuiala():
    """
    functie care testeaza functia valideaza_cheltuiala
    """
    cheltuiala = creeaza_cheltuiala(-12,789.45,"intretinere")
    try:
        valideaza_cheltuiala(cheltuiala)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "zi invalida!\n")

def test_creeaza_cheltuiala():
    """
    functie care testeaza functia creeaza_cheltuiala
    """
    ziua = 23
    suma = 89.14
    tip_cheltuiala = "mancare"
    cheltuiala = creeaza_cheltuiala(ziua,suma,tip_cheltuiala)
    assert (get_ziua_cheltuiala(cheltuiala) == ziua)
    assert (abs(get_suma_cheltuiala(cheltuiala) - suma)<0.00001)
    assert (get_tip_cheltuiala(cheltuiala) == tip_cheltuiala)

def test_adauga_cheltuiala():
    """
    functie care testeaza functia adauga_cheltuiala
    """
    l=[]
    cheltuiala = creeaza_cheltuiala(23,78,"altele")
    adauga_cheltuiala(l,cheltuiala)
    assert(len(l)==1)
    assert(get_ziua_cheltuiala(cheltuiala) == get_ziua_cheltuiala(l[0]))
    assert(abs(get_suma_cheltuiala(cheltuiala)-get_suma_cheltuiala(l[0]))<0.00001)
    assert(get_tip_cheltuiala(cheltuiala) == get_tip_cheltuiala(l[0]))

def test_srv_adauga_cheltuiala():
    """
    functie care testeaza functia srv_adauga_cheltuiala
    """
    l=[]
    srv_adauga_cheltuiala(l,12,20.0,"intretinere")
    assert(len(l)==1)
    try:
        srv_adauga_cheltuiala(l,-20,78.0,"mancare")
        assert(False)
    except Exception as ex:
        assert(str(ex)=="zi invalida!\n")
    try:
        srv_adauga_cheltuiala(l,12,"sdas","sdaf")
        assert(False)
    except Exception as ex:
        assert(str(ex)=="suma invalida!\ntip invalid!\n")
    try:
        srv_adauga_cheltuiala(l,-10,"sadsa","asfdsad")
        assert(False)
    except Exception as ex:
        assert(str(ex)=="zi invalida!\nsuma invalida!\ntip invalid!\n")

def test_srv_modifica_cheltuiala():
    """
    functie care testeaza functia srv_modifica_cheltuiala
    """
    l=[{'ziua': 12, 'suma': 20.0, 'tip_cheltuiala': 'intretinere'}]
    srv_modifica_cheltuiala(l,20,78.0,"altele",1)
    assert(len(l)==1)
    assert(get_ziua_cheltuiala(l[0]) == 20)
    assert(get_suma_cheltuiala(l[0]) == 78.0)
    assert(get_tip_cheltuiala(l[0]) == "altele")

    try:
        srv_modifica_cheltuiala(l,-12,23.4,"mancare",1)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "zi invalida!\n")

def test_filtratre_dupa_suma():
    """
    functie care testeaza functia filtrare_dupa_suma
    """
    list = []
    l=[{'ziua': 12, 'suma': 20.0, 'tip_cheltuiala': 'intretinere'},{'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'mancare'},{'ziua': 10, 'suma': 87.0, 'tip_cheltuiala': 'telefon'}]
    list = filtrare_dupa_suma(l,50)
    assert(len(list) == 2)
    assert(list[0] == {'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'mancare'})
    assert(list[1] == {'ziua': 10, 'suma': 87.0, 'tip_cheltuiala': 'telefon'})


def test_rap_total_sum():
    """
    functie care testeata functia rap_total_sum
    """
    l=[{'ziua': 12, 'suma': 20.0, 'tip_cheltuiala': 'intretinere'},{'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'mancare'},{'ziua': 13, 'suma': 50, 'tip_cheltuiala': 'intretinere'},{'ziua': 10, 'suma': 150, 'tip_cheltuiala': 'mancare'},{'ziua': 5, 'suma': 30, 'tip_cheltuiala': 'altele'}]
    assert rap_total_sum(l,'intretinere') == 70
    assert rap_total_sum(l,'mancare') == 250
    assert rap_total_sum(l,'altele') == 30
    assert rap_total_sum(l,'telefon') == 0

def test_get_total_sume():
    """
    functie care testeaza functia get_total_sum
    """
    l = [{'ziua': 13, 'suma': 20.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'mancare'},
         {'ziua': 13, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    assert get_total_sum(l,13) == 70
    assert get_total_sum(l,25) == 250

def test_rap_suma_zi_max():
    """
    functie care testeaza functia rap_suma_zi_max
    """
    l = [{'ziua': 13, 'suma': 20.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'mancare'},
         {'ziua': 13, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    assert rap_sum_zi_max(l) == 25

    l = [{'ziua': 13, 'suma': 20.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 10, 'suma': 100.0, 'tip_cheltuiala': 'mancare'},
         {'ziua': 13, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 15, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    assert rap_sum_zi_max(l) == 15


def test_get_cheltuieli_by_sume():
    """
    functie care testeaza functia get_cheltuieli_by_sume
    """
    l = [{'ziua': 13, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'mancare'},
         {'ziua': 13, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    assert get_cheltuieli_by_sume(l,100) == [{'ziua': 13, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'mancare'}]
    assert get_cheltuieli_by_sume(l,150) == [{'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]


def test_get_cheltuieli_by_type():
    """
    functie care testeaza functia get_cheltuieli_by_type
    """
    l = [{'ziua': 13, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
         {'ziua': 13, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    list = get_cheltuieli_by_type(l)
    assert list == [{'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
                    {'ziua': 13, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
                    {'ziua': 13, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
                    {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]


def test_filter_by_type():
    """
    functie care testeaza functia filter_by_type
    """
    l = [{'ziua': 13, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
         {'ziua': 13, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    list = filter_by_type(l,'intretinere')
    assert list == [{'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
                   {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    list = filter_by_type(l,'mancare')
    assert list == [{'ziua': 13, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
                    {'ziua': 25, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
                    {'ziua': 13, 'suma': 50, 'tip_cheltuiala': 'intretinere'}]


def test_sterge_din_lista_1():
    """
    functie care testeaza functia sterge_din_lista_1
    """
    l = [{'ziua': 13, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 13, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
         {'ziua': 25, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    list = sterge_din_lista_1(l,13)
    assert list == [{'ziua': 25, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
                    {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]


def test_sterge_din_lista_2():
    """
    functie care testeaza functia sterge_din_lista_2
    """
    l = [{'ziua': 10, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 20, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
         {'ziua': 15, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    list = sterge_din_lista_2(l, 9, 15)
    assert list == [{'ziua': 20, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
                   {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]


def test_afiseaza_by_type():
    """
    functie care testeaza functia afiseaza_by_type
    """
    l = [{'ziua': 10, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 20, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
         {'ziua': 15, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    list = afiseaza_by_type(l,'intretinere')
    assert list == [{'ziua': 10, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
                    {'ziua': 15, 'suma': 50, 'tip_cheltuiala': 'intretinere'}]


def test_sterge_by_type():
    """
    functie care testeaza functia sterge_by_type
    """
    l = [{'ziua': 10, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 20, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
         {'ziua': 15, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    list = sterge_by_type(l,'intretinere')
    assert list == [{'ziua': 20, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
                   {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]


def test_cheltuieli_mari():
    """
    functie care testeaza functia cheltuieli_mari
    """
    l = [{'ziua': 10, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 20, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
         {'ziua': 15, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    list = cheltuieli_mari(l, 100)
    assert list == [{'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]


def test_cheltuieli_mici():
    """
    functie care testeaza functia cheltuieli_mici
    """
    l = [{'ziua': 10, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 20, 'suma': 100.0, 'tip_cheltuiala': 'altele'},
         {'ziua': 15, 'suma': 50, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 25, 'suma': 150, 'tip_cheltuiala': 'mancare'}]
    list = cheltuieli_mici(l, 100, 21)
    assert list == [{'ziua': 15, 'suma': 50, 'tip_cheltuiala': 'intretinere'}]


def test_undo_list():
    """
    functie care testeaza functia undo_list
    """
    l = [{'ziua': 10, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
         {'ziua': 20, 'suma': 100.0, 'tip_cheltuiala': 'altele'}]

    list = undo_list(l)
    srv_adauga_cheltuiala(l, 10, 54.0, 'telefon')
    assert list == [{'ziua': 10, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
                     {'ziua': 20, 'suma': 100.0, 'tip_cheltuiala': 'altele'}]

    l = list
    list = undo_list(l)
    srv_modifica_cheltuiala(l, 20, 10.0, 'mancare', 1)
    assert list == [{'ziua': 10, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
                   {'ziua': 20, 'suma': 100.0, 'tip_cheltuiala': 'altele'}]

    l = list
    list = undo_list(l)
    sterge_din_lista_2(l, 1, 30)
    assert list == [{'ziua': 10, 'suma': 100.0, 'tip_cheltuiala': 'intretinere'},
                    {'ziua': 20, 'suma': 100.0, 'tip_cheltuiala': 'altele'}]


def ui_test_functii():
    test_creeaza_cheltuiala()
    test_valideaza_cheltuiala()
    test_adauga_cheltuiala()
    test_srv_adauga_cheltuiala()
    test_srv_modifica_cheltuiala()
    test_sterge_din_lista_1()
    test_sterge_din_lista_2()
    test_sterge_by_type()
    test_filtratre_dupa_suma()
    test_afiseaza_by_type()
    test_cheltuieli_mari()
    test_cheltuieli_mici()
    test_rap_total_sum()
    test_get_total_sume()
    test_rap_suma_zi_max()
    test_get_cheltuieli_by_sume()
    test_get_cheltuieli_by_type()
    test_filter_by_type()
    test_undo_list()


ui_test_functii()