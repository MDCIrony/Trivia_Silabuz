#imports
import os
import time
import random

#Declaración de constantes
SECRETPASS = "I KNOW EVERYTHING"
totalPassUsages = 0  #número de veces que se empleó la respuesta secreta
possibleAnswers = ("A", "B", "C", "D", SECRETPASS)
rounds = 1  #numero de rondas jugadas
maxScore = 0  #Tomará al final el escore más alto presente en acumulatedScores
totalQuestions = 10  #total de preguntas de 1 ronda de trivia
acumulatedScores = []  #Es el listado de scores acumulados


########################### FUNCIONES VARIAS ###################################
def inputNumeric(name, waitTime=3):
    #Request: define la cadena para solicitud de datos al usuario
    #Type: define el tipo de numero que debe aceptarse (1: Solo Enteros; 2: Decimales (y enteros, pero siempre retorna un decimal))
    #Incorrecto: define la cadena para mostrar al usuario al ingresar un parámetro invalido
    #MDC Authory
    request = f"Vamos {name}, ingresa tu número (1-6): "
    request2 = f"Vamos {name}, el número ingresado debe estar en el rango 1 a 6, sino es inválido, prueba otra vez: "
    incorrect = "El valor ingresado no es un número correcto, espera unos segundos para intentarlo de nuevo."
    registeredNumber = None  #numero a retornar (dependerá del tipo solicitado)

    while True:
        if registeredNumber == None:
            entry = input(
                request
            )  #Se solicita el ingreso de un valor con la cadena dada como parámetro

            try:
                registeredNumber = int(
                    entry
                )  #Se intenta registrar como entero, de lo contrario pasa al except

            except ValueError:
                print(incorrect + "\n")
                registeredNumber = None
                time.sleep(waitTime)

        elif registeredNumber >= 0 and registeredNumber <= 6:
            break

        else:
            entry = input(
                request2
            )  #Se solicita el ingreso de un valor con la cadena dada como parámetro

            try:
                registeredNumber = int(
                    entry
                )  #Se intenta registrar como entero, de lo contrario pasa al except

            except ValueError:
                print(incorrect + "\n")
                registeredNumber = 8
                time.sleep(waitTime)

    return registeredNumber


def countDown(timing=5):
    for i in range(timing, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    cleanConsole()


def countDownN(timing=5):
    for i in range(timing, 0, -1):
        print(f"{i}...")
        time.sleep(1)


def cleanConsole():  #Función para limpiar consola según so
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def setColour(text, colour):  #Función que retorna texto coloreado
    BLACK = '\033[30m'  #b
    RED = '\033[31m'  #r
    GREEN = '\033[32m'  #g
    YELLOW = '\033[33m'  #y
    BLUE = '\033[34m'  #bl
    MAGENTA = '\033[35m'  #mg
    CYAN = '\033[36m'  #c
    WHITE = '\033[37m'  #w
    RESET = '\033[39m'

    if colour == "b":
        text = BLACK + text + RESET
    elif colour == "r":
        text = RED + text + RESET
    elif colour == "g":
        text = GREEN + text + RESET
    elif colour == "y":
        text = YELLOW + text + RESET
    elif colour == "bl":
        text = BLUE + text + RESET
    elif colour == "mg":
        text = MAGENTA + text + RESET
    elif colour == "c":
        text = CYAN + text + RESET
    elif colour == "w":
        text = WHITE + text + RESET

    return text


def printTitles(
    colour="w",
    *args,
):  #Función para imprimir textos menores a 80char centrados
    BLACK = '\033[30m'  #b
    RED = '\033[31m'  #r
    GREEN = '\033[32m'  #g
    YELLOW = '\033[33m'  #y
    BLUE = '\033[34m'  #bl
    MAGENTA = '\033[35m'  #mg
    CYAN = '\033[36m'  #c
    WHITE = '\033[37m'  #w
    RESET = '\033[39m'

    for i in range(0, len(args)):
        if colour == "b":
            print(BLACK + args[i].center(80, ' ') + RESET)
        elif colour == "r":
            print(RED + args[i].center(80, ' ') + RESET)
        elif colour == "g":
            print(GREEN + args[i].center(80, ' ') + RESET)
        elif colour == "y":
            print(YELLOW + args[i].center(80, ' ') + RESET)
        elif colour == "bl":
            print(BLUE + args[i].center(80, ' ') + RESET)
        elif colour == "mg":
            print(MAGENTA + args[i].center(80, ' ') + RESET)
        elif colour == "c":
            print(CYAN + args[i].center(80, ' ') + RESET)
        elif colour == "w":
            print(WHITE + args[i].center(80, ' ') + RESET)


############################ PREGUNTAS #################################
questions = [  #Hay15Preguntas - [Pregunta, Respuesta Correcta, Otra1, Otra2, Otra3]
    [
        "¿Cuáles son las principales características de Python como lenguaje de programación?",
        "Es un lenguaje interpretado, de tipado dinámico, con buena adaptación a la POO pero de lenta ejecución",
        "Es un lenguaje compilado, de tipado dinámico, con buena adaptación a la POO pero de lenta ejecución",
        "Es un lenguaje compilado, estáticamente tipado, con buena adaptación a la POO pero de lenta ejecución",
        "Es un lenguaje interpretado, de tipado dinámico, con buena adaptación a la POO y de ejecución rápida"
    ],
    [
        "¿Qué es PEP 8?",
        "Son siglas de Python Enhancement Proposal, y corresponden a reglas para darle máxima legibilidad al código en Python",
        "Son siglas de Python Enhancement Proposal, y hace referencia a un módulo específico de la librería estándar de Python",
        "Son siglas de Python Elements Parts, y corresponden a reglas para la creación de clases y objetos dentro de Python",
        "Son siglas de Python Elegant Pants, y corresponde a reglas de vestimenta para los programadores profesionales de Python"
    ],
    [
        "¿Qué son los módulos de Python?",
        "Son archivos que tienen código Python, pudiendo ser variables o clases de funciones ejecutables",
        "Son programas escritos en código Python enfocados a la ciberseguridad",
        "Son complementos de VSCode para poder trabajar en Python",
        "Son carpetas dentro de proyectos desarrollados en Python en donde se almacenan los recursos multimedia (imágenes, videos, audios, etc)"
    ],
    [
        "¿Cuáles de los siguientes SÍ son módulos de Python?",
        "JSON, os, Random, sys, Data Time, Math",
        "JSON, os, aspirine, Data Time, omega",
        "JSON, os, Random, ketchup, Math", "JSON, os, pikachu, Data Time, Math"
    ],
    [
        "¿Qué son las funciones en Python?",
        "Es un bloque de código que se ejecuta únicamente cuando se llama",
        "Es un tipo de condicional dentro de Python",
        "Es otro tipo de ciclos dentro de Python como for y while",
        "Son ejercicios de estiramiento que deben seguir los programadores de Python para evitar dolores"
    ],
    [
        "¿Cuál de los siguientes métodos del módulo random permite aleatorizar los elementos de una lista?",
        "shuffle", "random", "uniform", "choice"
    ],
    [
        "¿Cuál de los siguientes NO es un elemento iterable en Python?",
        "Floats", "Lista", "Tupla", "String"
    ],
    [
        "¿Qué son los diccionarios en Python?",
        "Es un tipo de dato compuesto o contenedor que establece una relación 1 a 1 entre claves y valores asignados. Es mutable",
        "Es un tipo de dato compuesto o contenedor que permite almacenar elementos relacionados del mismo o distinto tipo. Es mutable",
        "Es un tipo de dato compuesto o contenedor que permite almacenar elementos relacionados del mismo o distinto tipo. Es inmutable",
        "Es un tipo de dato comestible que permite llenar el estómago de los programadores en Python. Es supermutable"
    ],
    [
        "De los siguientes, ¿Cuáles SÍ son datos compuestos en Python?",
        "Listas, tuplas, diccionarios y sets",
        "Listas, tuplas, diccionarios y strings",
        "Listas, tuplas diccionarios y Floats",
        "Floats, Strings, Integers y Boolean"
    ],
    [
        "¿Qué hace el método len()?",
        "Determina la longitud de un elemento iterable (listas, tuplas, diccionarios, etc)",
        "Devuelve un elemento aleatorio de un elemento iterable (listas, tuplas, diccionarios, etc)",
        "Aleatoriza los elementos de un elemento iterable (listas, tuplas, diccionarios, etc)",
        "Genera bugs aleatorios en el programa"
    ],
    [
        "¿Python es compatible con la POO?",
        "Sí, lo que significa que cualquier programa puede resolverse creando un modelo de objeto, sin embargo, no es el único enfoque de programación que puede tratar",
        "Sí, la POO es el único enfoque con el que se puede trabajar en Python",
        "¿Qué es POO?",
        "¿Qué tiene que ver Python con una Playa Ortopédica de Osos?"
    ],
    [
        "¿Cómo pueden importarse módulos en Python?", "Todas las anteriores",
        "Con la palabra clave import y el nombre del módulo original: - import array",
        "Con la palabra clave import y un alias: -import array as arr",
        "Importando todo el contenido del módulo: -from array import *"
    ],
    [
        "¿Qué es lo que hace el método upper()?",
        "Devuelve una copia de la cadena/string con todos sus elementos en mayúscula",
        "Devuelve una copia de la cadena/string con todos sus elementos en minúscula",
        "Devuelve una copia de la cadena/string con todos sus elementos en cursiva",
        "Devuelve una copia de la cadena/string con un bigote en todos sus elementos"
    ],
    [
        "¿Es importante la indentación en Python?",
        "Sí es importante, pues especifica un bloque de código",
        "No es importante, nadie hace indentación en Python",
        "Sí es importante, pero solo para que el código se vea guapo",
        "No es importante, yo no indento código y logré ser Senior en Python"
    ],
    [
        "¿Cuál de los siguientes métodos NO sirve para hacer una conversión de datos?",
        "random()",
        "Todos los métodos mencionados sirven para convertir datos", "float()",
        "dict()"
    ]
]
########################### PRESENTACIÓN ###################################
tituloA = "Bienvenido a este juego de TRIVIA"
tituloB = "en donde pondrás a prueba tus conocimientos"
tituloC = "del lenguaje de programación Python"

printTitles("bl", tituloA, tituloB, tituloC)
name = input("\nPor favor, dime cuál es tu nombre: ")

cleanConsole()

########################### INSTRUCCIONES ###################################

insA = f"Muy bien {name}, saldrán en pantalla un total de {totalQuestions} preguntas"
insB = "y tu deberás responder con la letra de aquella respuesta que creas correcta"
insC = "presionando finalmente el botón 'enter' para enviarla, si aciertas, "
insD = "ganarás 5 puntos, sino, perderás puntos de forma aleatoria"
insE = "en un rango de 1 a 5 puntos (influirá mucho tu suerte)\n"
insF = "¡Esfuérzate para demostrar todos tus conocimientos!"

printTitles("bl", insA, insB, insC, insD, insE, insF)
print(
    setColour(
        "\nPD: hay una respuesta secreta que podría ayudarte, intenta probar aleatoriamente a ver si aciertas y ganas muchos puntos extras ;)\n",
        "c"))
input(setColour("\nSi estás listo para jugar, aprieta enter.", "mg"))

cleanConsole()

########################### CÓDIGO MAIN ########################################
while True:
    score = random.randint(0, 10)
    passUsages = 0
    ruptura = False

    #Mensaje personalizado según el puntaje inicial aleatorio obtenido
    if score == 0:
        print(f"Jugarás esta ronda con un Score inicial de {score} puntos.\n")
    elif score <= 5:
        print(
            f"Tienes algo de suerte {name}, iniciarás esta ronda con un Score inicial de {score} puntos, ¡aprovéchalos!\n"
        )
    else:
        print(
            f"Tienes mucha suerte {name}, iniciarás esta ronda con un increíble score inicial de {score} puntos, ¡sácale provecho!\n"
        )

    #Conteo de suspenso inicial
    time.sleep(1.5)
    print("Prepárate, comenzaremos en: ")
    countDown()

    #Tomo el set de preguntas que se jugarán esta ronda:
    questionsSet = random.sample(questions, k=totalQuestions)

    #Ejecuto la presentación y respuesta del usuario para dicha respuesta
    questionNumber = 0
    for questionSelect in questionsSet:
        questionNumber += 1  #numero de pregunta
        answersSet = ["", "", "", ""]
        remainingPlaces = [0, 1, 2, 3]
        truePosition = None  #Ubicación de la respuesta verdadera luego del mixeo
        trueAnswer = None

        #Se plantea el orden aleatorio de respuestas (y se guarda la correcta)
        for i in range(1, 5):
            #Primero ubico la posición de la respuesta correcta
            if i == 1:
                truePosition = random.choice(remainingPlaces)
                answersSet[truePosition] = questionSelect[i]
                remainingPlaces.remove(truePosition)

            #Luego ubico los demás elementos
            else:
                other = random.choice(remainingPlaces)
                answersSet[other] = questionSelect[i]
                remainingPlaces.remove(other)

        #Se establece la condición de respuesta correcta (para comparar con el ingreso del usuario)
        if truePosition == 0:
            trueAnswer = "A"
        elif truePosition == 1:
            trueAnswer = "B"
        elif truePosition == 2:
            trueAnswer = "C"
        elif truePosition == 3:
            trueAnswer = "D"

        #Se imprime para la vista de usuario
        print(
            setColour(
                f"Pregunta #{questionNumber} :  " + questionSelect[0] + "\n",
                "mg"))
        print("a) " + answersSet[0] + "\n")
        print("b) " + answersSet[1] + "\n")
        print("c) " + answersSet[2] + "\n")
        print("d) " + answersSet[3] + "\n")

        #Pedimos respuesta y nos aseguramos que sea una respuesta válida
        reply = input("\nTu respuesta es: ")
        while reply.upper() not in possibleAnswers:
            reply = input(
                f"\nRespuesta invalida, por favor {name}, ingresa una respuesta adecuada: "
            )

        #Evaluamos la certeza de la respuesta
        if reply.upper() == trueAnswer:  #SI LA RESPUESTA ES CORRECTA...
            score += 5
            print(
                setColour(
                    f"\nRespuesta correcta {name}, felicidades, ganaste 5 puntos. Tienes un Score acumulado de {score} puntos.\n",
                    "g"))

            #Si estamos en la última no hacemos el timing
            if questionSelect != questionsSet[len(questionsSet) - 1]:
                time.sleep(1.5)
                print("Prepárate, pasaremos a la siguiente pregunta en: ")

                countDown()
            else:
                print("En unos segundos pasarás a la pantalla final.")
                time.sleep(3)
                cleanConsole()

        elif reply.upper() == SECRETPASS:  #SI SE USÓ EL SECRETPASS...
            if passUsages == 0:
                plusScore = random.randint(35, 78)
                score += plusScore
                print(
                    setColour(
                        f"\n¡Increíble {name}!, veo que conoces la llave secreta del conocimiento, por ello se te han otorgado {plusScore} puntotes, para un total de {score} puntos acumulados. Recuerda no abusar de esto, o podrías tener consecuencias negativas o.o!\n",
                        "y"))
                passUsages += 1
                totalPassUsages += 1

                if questionSelect != questionsSet[len(questionsSet) - 1]:
                    time.sleep(1.5)
                    print("Prepárate, pasaremos a la siguiente pregunta en: ")
                    countDown(8)

                else:
                    print("En unos segundos pasarás a la pantalla final.")
                    time.sleep(8)
                    cleanConsole()

            elif passUsages == 1:
                plusScore = random.randint(50, 106)
                score += plusScore
                print(
                    setColour(
                        f"\n¡Sorprendente {name}!, sigues demostrando ser portador del conocimiento absoluto, por ello los dioses te bendicen con {plusScore} puntotes, para un total de {score} puntos acumulados. Sin embargo, te aconsejo no emplearlo más, o podrías desatar un castigo scorístico sobre ti u-ú. \n",
                        "y"))
                passUsages += 1
                totalPassUsages += 1

                if questionSelect != questionsSet[len(questionsSet) - 1]:
                    time.sleep(1.5)
                    print("Prepárate, pasaremos a la siguiente pregunta en: ")
                    countDown(8)

                else:
                    print("En unos segundos pasarás a la pantalla final.")
                    time.sleep(8)
                    cleanConsole()
            else:
                plusScore = random.randint(-96, -12)
                score += plusScore
                print(
                    setColour(
                        f"\nOh no, lamentablemente has abusado mucho de este poder, y se te ha penalizado con {plusScore} puntos menos :(, quedándote solo {score} puntos. Te advertí de ello {name}. Te aconsejo no usarlo más y seguir solo con tus conocimientos.\n",
                        "r"))
                passUsages += 1
                totalPassUsages += 1

                if questionSelect != questionsSet[len(questionsSet) - 1]:
                    time.sleep(1.5)
                    print("Prepárate, pasaremos a la siguiente pregunta en: ")
                    countDown(8)

                else:
                    print("En unos segundos pasarás a la pantalla final.")
                    time.sleep(8)
                    cleanConsole()

        else:  #SI RESPONDIÓ INCORRECTAMENTE...
            #Si estamos en la última no hacemos el timing
            if questionSelect != questionsSet[len(questionsSet) - 1]:
                subScore = random.randint(-5, -1)
                score -= subScore
                print(
                    setColour(
                        f"\nRespuesta incorrecta {name}, tu Score disminuirá en {subScore} puntos, quedando en un total de  {score} puntos.\n",
                        "r"))
                ####IMPRIMIR RESPUESTA CORRECTA
                print(
                    f"La respuesta correcta era la letra {trueAnswer.lower()}) "
                    + answersSet[truePosition] +
                    ". Mejor suerte en la siguiente :(.\n")

                input("Presiona cualquier tecla para continuar.\n")

                print("Prepárate, pasaremos a la siguiente pregunta en: ")
                countDown()
            else:
                subScore = random.randint(-5, -1)
                score -= subScore
                print(
                    setColour(
                        f"\nRespuesta incorrecta {name}, has perdido {subScore} puntos. No has podido ganar más :(.\n",
                        "r"))
                print(
                    f"La respuesta correcta era la letra {trueAnswer.lower()}) "
                    + answersSet[truePosition] +
                    ". Presiona cualquier tecla para pasar a la pantalla final.\n"
                )
                input()
                cleanConsole()

    #Damos terminada la ronda
    print(
        setColour(
            f"La ronda ha terminado {name}, y has logrado obtener un total de {score} puntos.",
            "c"))

    #APOSTAR PARA GANAR O PERDER MÁS PUNTOS
    casinoPoints = input(
        "\n¡Sin embargo, nos gustaría darte la oportunidad de probar tu suerte e intentar ganar muchos más puntos!... o perderlos cof* cof*. \n\nSi quieres apostar contra nosotros, responde Y, de lo contrario, responde N para quedarte con tus puntos actuales: "
    )
    while True:
        if not (casinoPoints.upper() == "Y" or casinoPoints.upper() == "N"):
            casinoPoints = input(
                f"\nTienes que responde Y o N para poder entenderte correctamente {name}. ¿Deseas probar tu suerte para ganar (cof* o perder cof*) más puntos?: "
            )
        elif casinoPoints.upper() == "Y":
            print(
                "\n¡Está decidido! El juego será lanzar el dado; Nosotros elegiremos un número y tú otro, y luego el dado sacará aleatoriamente un número (el rango de elección será del 1 al 6), gana el que acierte el número del dado, y repetiremos hasta que suceda. Si nosotros ganamos, tu puntaje se dividirá en 2, pero si tú ganas, tu puntaje será multiplicado por 2!. Aprieta enter para continuar."
            )
            input()

            userNumberSelect = inputNumeric(
                name)  #FUERZA AL USUARIO A REGISTRAR UN NUMERO DEL 1 AL 6
            cpuNumberSelect = random.randint(1, 6)  #El valor del cpu
            while True:
                if cpuNumberSelect != userNumberSelect:
                    break
                else:
                    cpuNumberSelect = random.randint(1, 6)

            print(
                f"\nMi elección es el número {cpuNumberSelect}, tu elección {name} es el número {userNumberSelect}. Ahora veamos qué sale en el dado, cruza los dedos:"
            )

            dadoSelect = random.randint(1, 6)

            countDownN()

            print(f"\nEl dado ha sacado el número {dadoSelect}.\n")

            if ((dadoSelect == userNumberSelect)
                    or (dadoSelect == cpuNumberSelect)):
                if dadoSelect == userNumberSelect:
                    score *= 2
                    print(
                        setColour(
                            f"\nEnhorabuena {name}, has tenido mucha suerte esta vez y tu puntaje se ha multiplicado por 2, quedando en un total de {score} puntos.",
                            "g"))
                    break

                elif dadoSelect == cpuNumberSelect:
                    score /= 2
                    print(
                        setColour(
                            f"\nEs una lástima {name}, no has tenido suerte y tu puntaje se ha reducido a la mitad, quedando en un total de {score} puntos. Mejor suerte la próxima :(",
                            "r"))
                    break

            else:
                while True:
                    print(
                        "\nNinguno de los dos ha acertado, ¡hay que volver a intentarlo!"
                    )
                    userNumberSelect = inputNumeric(
                        name
                    )  #FUERZA AL USUARIO A REGISTRAR UN NUMERO DEL 1 AL 6
                    cpuNumberSelect = random.randint(1, 6)  #El valor del cpu
                    while True:
                        if cpuNumberSelect != userNumberSelect:
                            break
                        else:
                            cpuNumberSelect = random.randint(1, 6)

                    print(
                        f"\nMi elección es el número {cpuNumberSelect}, tu elección {name} es el número {userNumberSelect}. Ahora veamos qué sale en el dado, cruza los dedos:"
                    )

                    dadoSelect = random.randint(1, 6)

                    countDownN()

                    print(f"\nEl dado ha sacado el número {dadoSelect}.\n")

                    if ((dadoSelect == userNumberSelect)
                            or (dadoSelect == cpuNumberSelect)):
                        if dadoSelect == userNumberSelect:
                            score *= 2
                            print(
                                setColour(
                                    f"\nEnhorabuena {name}, has tenido mucha suerte esta vez y tu puntaje se ha multiplicado por 2, quedando en un total de {score} puntos.",
                                    "g"))
                            break

                        elif dadoSelect == cpuNumberSelect:
                            score /= 2
                            print(
                                setColour(
                                    f"\nEs una lástima {name}, no has tenido suerte y tu puntaje se ha reducido a la mitad, quedando en un total de {score} puntos. Mejor suerte la próxima :(",
                                    "r"))
                            break
                break
        elif casinoPoints.upper() == "N":
            print(
                f"\nEntendemos que hoy te sientes sin suerte {name}, tu puntaje final esta ronda fue de {score} puntos."
            )
            break

    #Preguntamos si quiere volver a jugar hasta que responda adecuadamente

    acumulatedScores.append(score)  #Guardamos el score obtenido en esta ronda
    decission = input("\n¿Deseas volver a jugar? Y/N: ")
    while True:

        if not (decission.upper() == "Y" or decission.upper() == "N"):
            decission = input(
                f"Tienes que responde Y o N para poder entenderte correctamente {name}. ¿Deseas volver a jugar?: "
            )
        elif decission.upper() == "Y":
            print("¡Está decidido! Volveremos a jugar, prepárate.")
            countDown()
            rounds += 1
            break
        elif decission.upper() == "N":
            ruptura = True
            break

    #Rompemos el ciclo general
    if ruptura == True:
        break

#Limpiamos pantalla y damos el mensaje de despedida, con el puntaje máximo de los acumulados
cleanConsole()
maxScore = max(acumulatedScores)
puntajeAcumulado = sum(acumulatedScores)

if passUsages == 0:

    print(
        f"Muchas gracias por jugar {name}, has completado un total de {rounds} rondas con un score máximo de {maxScore} puntos. Además, el score acumulado de todas las rondas es de {puntajeAcumulado} puntos\n"
    )

    printTitles("bl", "Esperamos verte pronto por aquí :)")
else:
    print(
        f"Muchas gracias por jugar {name}, has completado un total de {rounds} rondas con un puntaje máximo de {maxScore} puntos; además, el score acumulado de todas las rondas jugadas es de {puntajeAcumulado}. Sin embargo, has empleado la respuesta secreta un total de {passUsages} veces, asegurate de confiar solo en tus conocimientos la próxima vez ;). \n"
    )

    printTitles("bl", "Esperamos verte pronto por aquí :)")

input("Aprieta enter para finalizar.")
cleanConsole()
