import random


class Opcion:
    def __init__(self, texto, casa):
        self.texto = texto
        self.casa = casa


class Sombrero:
    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.user = ''
        self.user_resp = []
        self.puntaje = {
            'Gryffindor': 0,
            'Hufflepuff': 0,
            'Ravenclaw': 0,
            'Slytherin': 0,
        }
        random.shuffle(self.preguntas)

    def presentarse(self):
        print(
            '¡Hey tú! ¿Listo para ser seleccionado? Sabes muy bien que Hogwarts tiene cuatro Casas: \n Gryffindor, el hogar de los valientes,\n Hufflepuf, el hogar de los que son justos.\n Ravenclaw, donde se aprecia la inteligencia y sabiduría. \n finalmente Slytherin, donde predominan los ambiciosos. \n\n Te haré algunas preguntas para ver en qué casa perteneces')
        print('Pero antes, debes decirme tu nombre. ')
        self.user = input()

    def evaluar(self):
        for i in range(len(self.preguntas)):
            pregunta = self.preguntas[i]
            casa = pregunta.preguntar()
            self.puntaje[casa] = self.puntaje[casa] + 1

    def asignar_casa(self):
        max_value = max(self.puntaje, key=self.puntaje.get)
        print('Tu casa es:', max_value, '¡Felicidades', self.user, '!')


class Pregunta:
    def __init__(self, texto, opciones):
        self.texto = texto
        self.opciones = opciones

    def preguntar(self):
        print(self.texto)
        for i in range(len(self.opciones)):
            opcion = self.opciones[i]
            print(i + 1, opcion.texto)
        print('\n')
        user_resp = input('Elije una opción: ')
        return self.opciones[int(user_resp) - 1].casa


sombrero = Sombrero([
    Pregunta('¿Cómo te describirías en una palabra?', [
        Opcion('Valiente', 'Gryffindor'),
        Opcion('Leal', 'Hufflepuff'),
        Opcion('Inteligente', 'Ravenclaw'),
        Opcion('Ambicioso', 'Slytherin')
    ]),
    Pregunta('Cuál es tu pensamiento sobre los muggles', [
        Opcion('Me agradan, hay que saber vivir sin magia.', 'Gryffindor'),
        Opcion('Deberíamos respetarlos ', 'Hufflepuff'),
        Opcion('Me da curiosidad su forma de vida sin magia', 'Ravenclaw'),
        Opcion('Los magos somos superiores a ellos', 'Slytherin')
    ]),
    Pregunta('¿Cual de estas materias te gusta más?', [
        Opcion('Defensa contra la artes oscuras', 'Gryffindor'),
        Opcion('Herbología ', 'Hufflepuff'),
        Opcion('Encantamientos', 'Ravenclaw'),
        Opcion('Pociones', 'Slytherin')
    ]),
    Pregunta('Elige una criatura', [
        Opcion('Leon', 'Gryffindor'),
        Opcion('Tejon ', 'Hufflepuff'),
        Opcion('Aguila', 'Ravenclaw'),
        Opcion('Serpiente', 'Slytherin')
    ]),
    Pregunta('¿Qué tipo de trabajo te gustaría hacer?', [
        Opcion('Uno se oriente a la seguridad', 'Gryffindor'),
        Opcion('Uno que ayude al prójimo', 'Hufflepuff'),
        Opcion('uno que me permita adquirir y demostrar conocimiento', 'Ravenclaw'),
        Opcion('uno que me lleve a la cima', 'Slytherin')
    ])
])

sombrero.presentarse()
sombrero.evaluar()
sombrero.asignar_casa()

# sombrero.presentarse()
# print(sombrero.user)
# pregunta_1 = Pregunta('¿Cómo te describirías en una palabra?', [
#         Opcion('Valiente', 'Gryffindor'),
#         Opcion('Leal', 'Hufflepuff'),
#         Opcion('Inteligente', 'Ravenclaw'),
#         Opcion('Ambicioso', 'Slytherin')
#     ])
# print(pregunta_1.preguntar())
# Hacer un programa que respondiendo a ciertas preguntas, haga un sorteo que diga a que casa de Hogwarts pertenece el usuario,
# class, function, methods, list, dicts
