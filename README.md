# El llenguatge JSBach

# Introducció

Aquesta és la Pràctica de Llenguatges de Programació del Q2 del curs 2021-2022.

# Compilació i execució

Dins del codi en Python, hi ha diverses crides a ```os.system(command)``` que executen totes les instruccions necessàries per l'execució. 

Dins del codi, ja es compila la gramàtica, es genera la plantilla del visitor, es crea la partitura i es toca per terminal. A l'hora de reproduir la música, fa comprovacions de si el sistema operatiu que s'està utilitzant és Linux o Mac (darwin), a través de ```sys.platform```.

Per tant, només cal executar l'intèrpret amb un fitxer d'entrada i, opcionalment, el primer procediment de l'arxiu d'entrada a ser executat:
```bash
python3 jsbach.py input.jsb
```

Si no es volgués generar la música, es pot comentar la crida a `__generateMusic()` dins del `main` de `jsbach.py`.

# Creació de la gramàtica

Utilitzant ANTLR4. Fitxer `jsbach.g4`.

## Part lèxica

En aquesta secció de la gramàtica, hi he especificat els diferents tokens de la sintaxis del llenguatge.

He utilitzat les construccions `fragment`, que serveixen per simplificar la gramàtica fent-la més llegible.

Alguns exemples:
```
// ---Operacions amb llistes
CONCAT  : '<<' ;
CUT     : '8<' ;
LENGTH  : '#' ;

// ---Altres construccions
fragment
NUMNOTE : '0'..'8' ;
NOTE    : ('A'|'B'|'C'|'D'|'E'|'F'|'G') NUMNOTE?;

COMMENT
    : '~~~' ~( '\r' | '\n' )* '~~~' -> skip
    ;
```

## Part sintàctica

En la part sintàctica, m'he preocupat de posar noms autoexplicatius i de mantenir una estructura neta.

Un exemple complet dels possibles enunciats del llenguatge:
```
// ---Statement
stmt 
    : READ VARID                                                # readStmt
    | WRITE expr+                                               # writeStmt
    | PLAY expr                                                 # playStmt
    | IF expr LPAREN stmts RPAREN (ELSE LPAREN stmts RPAREN)?   # ifStmt
    | WHILE expr LPAREN stmts RPAREN                            # whileStmt
    | PROCID paramsListCall                                     # procCallStmt
    | leftExpr ASSIGN expr                                      # assignStmt
    | VARID CONCAT expr                                         # concatStmt
    | CUT VARID '[' expr ']'                                    # cutStmt
    ;
```

# Implementació dels visitadors

Utilitzant Python3. Fitxer `jsbach.py`.

## Instruccions

La majoria d'instruccions no tenen molt misteri, més enllà de visitar els fills i fer-los-hi el tractament corresponent.

Per exemple, en el cas de les expressions relacionals, aritmètiques i unàries és important tenir en compte qui és el fill que equival a l'operació que s'està fent. Això ho faig consultant si el context actual de l'expressió relacional té el fill `EQ()`, per tal de fer l'operació d'igualtat; si el context és aritmètic, doncs comprovo si s'està sumant o dividint o l'operació que sigui.

## Estructures auxiliars 

Una part molt important són les estructures de dades que he afegit dins de la classe. Totes elles son productes de la reflexió i meditació i considero que ofereixen bones solucions a les necessitats del problema.

- `allScopes`: 
    - **Llista** que simula una pila de **scopes**.
    - L'última llista és l'scope actual.
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
Per fer transformacions entre notes en format string i valors enters, vaig considerar dues possibilitats: consultar el seu valor en un diccionari o bé calcular el seu valor quan es necessités. Vaig descartar la primera opció, no volia haver de crear un diccionari tant gran. Així que per aquesta raó, em vaig posar mans a l'obra per aconseguir la fòrmula.

### Què sabem de música?
De coses tècniques, no massa (almenys ara mateix). Però em vaig estar posant al dia i vaig arribar a què, en la notació anglesa:
```
A0=0    A1=7    A2=14   .
B0=1    B1=8    .       .
C1=2    C2=9    .
D1=3    .
E1=4    .
F1=5
G1=6
```
Dels apunts anteriors i assignant a cada lletra el seu valor inicial (el de més a l'esquerra), vaig derivar-ne una :
```
Si la lletra es A o B:
    Valor d'una nota = Valor base lletra + Octava * Nombre que acompanya la lletra
si no:
    Valor d'una nota = Valor base lletra + Octava * (Nombre que acompanya la lletra-1)
```
Compte: si la lletra era "A" o "B", el Nombre es manté igual; en cas contrari, li resto 1. Es pot veure perquè això és cert perquè el valor base de les lletres de la C a la G és una unitat superior.

Per tant, amb aquesta fòrmula/pseudo-codi ja m'és possible conèixer el valor de qualsevol nota.

### Guardant notes com el seu valor...
Després d'aquesta il·luminació matemàtica, vaig veure com guardar les notes com el seu valor facilita operar amb elles posteriorment. Qualsevol operació com sumar, restar, multiplicar... és tant simple com operar amb dos enters.

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
Seguint amb la mania de fer com si com més llarga l'estructura if més diners em costa, vaig decidir buscar la manera de calcular la manera de passar d'un valor enter a una nota en notació Lilypond.

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