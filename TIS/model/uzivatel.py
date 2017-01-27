'''
Created on Nov 10, 2015

@author: dusky
'''

class Uzivatel(object):
    '''
    classdocs
    '''
    idUser = None
    poziciaHrac = None
    poziciaNahoadzovac = None
    poziciaAdminKlubu = None
    poziciaAdmin = None
    login = None
    heslo = None
    idKlubu = None

    def __init__(self, idUser, poziciaHrac, poziciaNahoadzovac, poziciaAdminKlubu, poziciaAdmin, login, heslo, idKlubu = None):
        '''
        Constructor
        '''
        raise Exception("Non implemented")
        