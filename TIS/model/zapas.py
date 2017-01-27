'''
Created on Nov 10, 2015

@author: dusky
'''

class Zapas(object):
    '''
    classdocs
    '''
    idZapasu = None
    idTurnaja = None
    idTim1 = None
    idTim2 = None
    vysledokTim1 = None
    vysledokTim2 = None

    def __init__(self, idZapasu, idTurnaja, idTim1, idTim2, vysledokTim1, vysledokTim2):
        '''
        Constructor
        '''
        raise Exception("Non implemented")
    
    def vratVysledok(self):
        raise Exception("Non implemented")