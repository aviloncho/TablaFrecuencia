# -*- coding: utf-8 -*-


class TablaFrecuencia:

    def __init__(self, lista):
        self._lista = lista
        self._unique = set(self._lista)
        self.N = len(self._lista)
        self.absoluta = {}
        self.relativa = {}

    def calcular(self):
        self.absoluta.clear()
        self.relativa.clear()

        conteo = 0
        for item in sorted(self._unique):
            cant = self._lista.count(item)
            conteo += cant
            self.absoluta[item] = [cant,conteo]
            self.relativa[item] = [cant/self.N, conteo/self.N]
