# El llenguatge JSBach

# Introducció

Aquesta és la Pràctica de Llenguatges de Programació del Q2 del curs 2021-2022.

# Compilació i execució

Dins del codi en Python, hi ha diverses crides a ```os.system(command)``` que executen totes les instruccions necessàries per l'execució. 

Dins del codi, ja es compila la gramàtica, es genera la plantilla del visitor, es crea la partitura i es toca per terminal. A l'hora de reproduir la música, fa comprovacions de si el sistema operatiu que s'està utilitzant és linux o darwin, a través de ```sys.platform```.

Per tant, només cal executar l'intèrpret amb un fitxer d'entrada i, opcionalment, el primer procediment de l'arxiu d'entrada a ser executat:
```bash
python3 jsbach.py input.jsb
```

# Creació de la gramàtica

Utilitzant ANTLR4.

## Part lèxica

## Part sintàctica

# Implementació dels visitadors

Utilitzant Python3.

## Instruccions

La majoria d'instruccions no tenen molt misteri, més enllà de visitar els fills i fer-los-hi el tractament corresponent.

## Estructures auxiliars

- `allScopes`: 
    - **Llista** que simula una pila de **scopes**, on l'última llista és l'scope actual.
- `procsStmtsContexts`:
    - **Diccionari** de tots els **procediments** amb el context del seu conjunt de **statements**.
    - Permet visitar tots els procediments quan sigui.
- `procsParameters`:
    - **Diccionari** de tots els **procediments** amb el nom de tots els seus **paràmetres**.
    - Molt útil per assignar valor a les variables d'un nou scope i comprovar ràpidament que el nombre de paràmetres passats és el correcte.
- `musicSheet`:
    - **Llista** de les **notes** afegides per la instrucció de reproducció.
    - Quan s'acaba el programa, és el que es converteix en partitura.

## Sobre notes i els seus valors
En aquest punt

### Què sabem de música?
```
A0=0    A1=7    A2=14   .
B0=1    B1=8    .       .
C1=2    C2=9    .
D1=3    .
E1=4    .
F1=5
G1=6
```
Dels apunts anteriors i assignant a cada lletra el seu valor inicial, vaig derivar-ne una fòrmula:
```
Valor d'una nota = Valor base lletra + Octava * Nombre que acompanya la lletra
```
Si la lletra era "A" o "B", el Nombre es manté igual; en cas contrari, li resto 1. Es pot veure perquè això és cert comprovant alguns valors.

### Guardant notes com el seu valor...
Guardar les notes com el seu valor facilita operar amb elles posteriorment. Qualsevol operació com sumar, restar, multiplicar... és tant simple com operar amb dos enters.

```python
def __noteValueEnglishNotation(self, noteId):
    letter = noteId[0]
    if len(noteId) > 1:
        number = int(noteId[1])
    else:
        number = 4

    # ord(A) = ascii code for letter A = 65
    baseValueFromLetter = ord(letter) - 65
    octave = 7

    if letter not in ['A', 'B']:
        number = number - 1

    value = baseValueFromLetter + octave * number
    if value > 51 or value < 0:
        raise Exception('La nota ' + noteId + ' no existeix.')
    return value
```

### ...per passar-les després a notació Lilypond
Seguint amb la mania de fer com si cada if costés diners de la meva butxaca, vaig decidir buscar la manera de calcular la manera de passar d'un valor enter a una nota en notació Lilypond.
```python
def __num2note(self, noteNum):
    # letter
    baseValue = noteNum % 7
    baseLetter = chr(baseValue + 97)

    # number
    offsetNum = int((noteNum-baseValue)/7)
    if baseLetter != 'a' and baseLetter != 'b':
        offsetNum = offsetNum+1

    # lilypond notation postfix
    lilyPostfixOffset = 4 - offsetNum - 1
        
    if lilyPostfixOffset >= 0:
        lilyPostfix = ',' * lilyPostfixOffset
    else:
        lilyPostfix = '\'' * -lilyPostfixOffset

    return baseLetter + lilyPostfix
```

## Errors i excepcions
- Divisió entre 0
- Crida a un procediment no definit:
    - El nom del procediment no existeix.
- Repetició de procediment ja definit:
    - El nom del procediment ja existeix.
- Nombre de paràmetres incorrecte:
    - L'excepció indica els paràmetres que necessita realment el procediment cridat incorrectament i quants se n'han passat.
- Noms de paràmetres formals repetits:
    - L'excepció indica el nom repetit.
- Accés a un índex inexistent d'una llista
    - L'excepció especifica quina llista, a quin índex s'ha intentat accedir i quin era el tamany real de la llista.
- Execució sense Main ni procediment en primera posició
    - L'excepció pregunta "On és el Main?".
- Accés a una llista inexistent
    - En les instruccions de TALL, CONCATENACIÓ i ACCES.
- Ús de variable inexistent
- Nota fora del rang existent

# Generació dels fitxers d'àudio

Utilitzant Lilipond per generar les partitures i Timidity++ i ffmpeg per generar els WAV i MP3.

# Automatització mitjançant scripts

Per tal d'utilitzar el meu temps de manera més eficient i fer fàcilment reproduïbles els meus resultats, vaig decidir crear alguns scripts en bash per a l'entorn Linux que utilitzava. 

- Script per preparar al complet l'entorn:
```bash

```

- Script per compilar, executar i generar arxius de so: 
```bash

```