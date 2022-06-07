# Carrera de obstáculos
# Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
# - La función recibirá dos parámetros:
#     - Un array que sólo puede contener String con las palabras "run" o "jump"
#     - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
# - La función imprimirá cómo ha finalizado la carrera:
#     - Si el/a atleta hace "jump" en "_" (suelo) se variará la pista por "x"
#     - Si hace "run" en "|" (valla), se variará la pista por "/"
# - La función retornará un Boolean que indique si ha superado la carrera.
# Para ello tiene que realizar la opción correcta en cada tramo de la pista

# resolución en https://github.com/mouredev
# By Brais Moure Aka. Mouredev
import random
import numpy as np

def random_generator(lenght):
    movements_posibilities = ["run", "jump"]
    track_posibilities = ["_", "|"]
    movements = random.sample(movements_posibilities*lenght, lenght)
    track = random.sample(track_posibilities*lenght, lenght)
    return np.array(movements), np.array(track)

def correct_generator(lenght):
    movements_posibilities = ["run", "jump"]
    track = []
    movements = random.sample(movements_posibilities*lenght, lenght)
    for i in range(len(movements)):
        if movements[i] == "run":
            track.append("_")
        else:
            track.append("|")
    return np.array(movements), np.array(track)

def race(athlete, track):
    results = {}

    if len(track) > len(athlete):
            print("The athlete has not finished")

    elif len(track) == len(athlete):
        for i in range(len(track)):
            if track[i] == '_' and athlete[i] == "run" or track[i] == "|" and athlete[i] == "jump":
                results[i] = "passed"

            else:
                results[i] = "failed"
                
    #Checking the dictionary
    #print(results)
    mark = 0
    for value in results.values():
        if value == "passed":
            mark += 1
    print(f"The athlete has scored {mark}/{len(track)} points (~{mark/len(track)*100}%)")

#Checking auxiliar functions
bad_movements, bad_track = random_generator(10)
random_results = f"Wrong\n\nMovements: {bad_movements}\nTrack: {bad_track}"
#print(random_results)

correct_movements, correct_track = correct_generator(10)
correct_results = f"Correct\n\nMovements: {correct_movements}\nTrack: {correct_track}"
#print(correct_results)

#Checking datatypes returned by the functions
bad_movements, bad_track = random_generator(10)
random_datatypes = f"Wrong\n\nMovements: {type(bad_movements)}\nTrack: {type(bad_track)}"
#print(random_datatypes)

correct_movements, correct_track = correct_generator(10)
correct_datatypes = f"Correct\n\nMovements: {type(correct_movements)}\nTrack: {type(correct_track)}"
#print(correct_datatypes)

#Checking main function
race(correct_movements, correct_track)