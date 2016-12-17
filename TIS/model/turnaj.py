'''
Created on Nov 10, 2015

@author: dusky
'''

class Turnaj(object):
    '''
    classdocs
    '''
    idTurnaju = None
    nazov = None
    datumOd = None
    datumDo = None
    vysledkyPole_IdTimov = None
    spirit = None
    mesto = None
    stat = None
    datumZapisu = None
    report = None

    def __init__(self, idTurnaju, nazov, datumOd, datumDo, vysledkyPole_IdTimov, spirit, mesto, stat, datumZapisu, report):
        '''
        Constructor
        '''
        raise Exception("Non implemented")
    
    def parsujVysledky(self):
        raise Exception("Non implemented")