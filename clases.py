import unittest
#Parametros opcional
class Fecha:
    def __init__(self, año:int=2023, mes:int=5, dia:int=2):
        self.año = año
        self.mes = mes
        self.dia = dia
    def compareTo(self, fecha):
        fecha1 = ((self.año*100)+self.mes)*100 + self.dia
        fecha2 = ((fecha.año*100)+fecha.mes)*100+fecha.dia
        return fecha1 - fecha2
    def __repr__(self):
        return f'{self.dia}/{self.mes}/{self.año}'
class Persona:
    def __init__(self, nombre:str=None, apellido:str=None, nacimiento:Fecha=None):
        if not nombre is None:
            self.nombre = nombre
        if not apellido is None:
            self.apellido = apellido
        if not nacimiento is None:
            self.nacimiento = nacimiento
    def compareTo(self, persona):
        return self.nacimiento.compareTo(persona.nacimiento)
    def __repr__(self):
        return f'Persona --> Nombre = {self.nombre}  Apellido = {self.apellido}  Nacimiento = {self.nacimiento}'
'''class Persona:
    def __init__(self, nombre:str=None, apellido:str=None, diccionario:dict=None, nacimiento:Fecha=None):
        if not diccionario is None:
            self.apellido = diccionario.get('apellido')
            self.nombre = diccionario.get('nombre')
        if not nombre is None:
            self.nombre = nombre
        if not apellido is None:
            self.apellido = apellido
        if not nacimiento is None:
            self.nacimiento = nacimiento
    def __repr__(self):
        return f'Persona --> Nombre = {self.nombre}  Apellido = {self.apellido}  Nacimiento = {self.nacimiento}'''
class Ordenador:
    def porNacimiento(self, entes):
        for i in range(0, len(entes)-1):
            for x in range(1, len(entes)):
                if entes[i].compareTo(entes[x]) > 0:
                    entes[i], entes[x] = entes[x], entes[i]
        return entes
persona_json_1 = {'nombre' : 'Indiana', 'apellido' : 'Jones'}
persona_json_2 = {'nombre' : 'Steve', 'apellido' : 'Rogers'}
'''if __name__ == '__main__':
    persona_1 = Persona(diccionario = persona_json_1)
    persona_2 = Persona(nombre='Tony', apellido='Stark')
    print(persona_1)
    print(persona_2)'''
'''if __name__ == '__main__':
    persona = Persona(nombre='Peter', apellido='Parker', nacimiento= Fecha(año=1999, mes = 12, dia=31))
    print(persona)'''
if __name__ == '__main__':
    ordenador = Ordenador()
    personas = []
    personas.append(Persona('Bruce', 'Wayne', Fecha(1950,3,1)))
    personas.append(Persona('Clark', 'Kent', Fecha(1875,4,7)))
    personas.append(Persona('Arthur', 'Curry', Fecha(1955,12,1)))
    personas = ordenador.porNacimiento(personas)
    print(personas)
