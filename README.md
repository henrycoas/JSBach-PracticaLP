# El llenguatge JSBach

# Introducció

Aquesta és la Pràctica de Llenguatges de Programació del Q2 del curs 2021-2022.

En paraules de l'enunciat, l'objectiu d'aquesta pràctica és implementar un doble intèrpret per a un llenguatge de programació musical anomenat JSBach. La sortida d'aquest doble intèrpret és una partitura i uns fitxers de so que reproduiràn la melodia descrita pel compositor.

És un doble intèrpret perquè funciona en el sentit informàtic (interpreta un programa) i en el sentit musical (interpreta una peça de música).

# Compilació i execució

Dins del codi en Python, hi ha diverses crides a ```os.system()``` que executen totes les instruccions necessàries per l'execució: 

- Compilar la gramàtica, 
- Generar la plantilla del visitor, 
- Generar un fitxer en notació lilypond,
- Crear la partitura en format pdf,
- Tocar la melodia de la partitura per terminal. 

Tot ja es fa desde el codi. A l'hora de reproduir la música, fa comprovacions de si el sistema operatiu que s'està utilitzant és Linux o Mac (darwin), a través de ```sys.platform```.

Per tant, només cal executar l'intèrpret amb un fitxer d'entrada i, opcionalment, el primer procediment de l'arxiu d'entrada a ser executat:
```bash
python3 jsbach.py input.jsb [FirstProc]
```

Si no es volgués generar la partitura per acabar tocant la música, es pot comentar la crida a `__generateMusic()` dins del `main` de `jsbach.py`.

# Creació de la gramàtica

Utilitzant ANTLR4. Fitxer `jsbach.g4`.

## Part lèxica

En aquesta secció de la gramàtica, hi he especificat els diferents tokens de la sintaxis del llenguatge.

He utilitzat les construccions `fragment`, que serveixen per simplificar la gramàtica fent-la més llegible.

Adjunto aquí alguns exemples, com els operadors de llistes, les variables de les notes musicals i els comentaris:
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

Un exemple complet dels possibles enunciats (en anglès, statements) del llenguatge:
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

En el cas de les expressions relacionals, aritmètiques i unàries, per exemple, és important tenir en compte qui és el fill que equival a l'operació que s'està fent. Per saber si en un context d'expressió relacional he d'aplicar l'operació d'igualtat, comprovo si existeix el fill `EQ()`, i el mateix amb l'operadors de desigualtat, menor o igual, etc.

## Estructures auxiliars 

Una part molt important són les estructures de dades que he afegit dins de la classe. Totes elles son productes de la reflexió i meditació i considero que ofereixen bones solucions a les necessitats del problema.

- `allScopes`: 
    - **Llista** que simula una pila de **scopes**.
    - L'última llista és l'scope actual.
    - Un scope conté les variables actives en aquell moment de l'execució.
- `procsStmtsContexts`:
    - **Diccionari** de tots els **procediments** amb el context del seu conjunt de **statements**.
    - Permet visitar tots els procediments quan sigui.
- `procsParameters`:
    - **Diccionari** de tots els **procediments** amb el nom de tots els seus **paràmetres**.
    - Molt útil per assignar valor a les variables d'un nou scope i comprovar ràpidament que el nombre de paràmetres passats és el correcte.
- ~~`musicSheet`~~:
    - **Llista** de les **notes** afegides per la instrucció de reproducció.
    - Quan s'acaba el programa, és el que es converteix en partitura.
- `canonSheet`:
    - Substitueix a `musicSheet` després d'haver fet una extensió de les funcionalitats de JSBach.
    - Diccionari de totes les veus del cànon en format llistes de notes indexades per el seu número de veu.
    - Quan s'acaba el programa, és el que es converteix en les diferents veus de la partitura.

## Sobre notes i els seus valors
Per fer transformacions entre notes en format string i valors enters, vaig considerar dues possibilitats: consultar el seu valor en un diccionari o bé calcular el seu valor quan es necessités. Vaig descartar la primera opció, doncs no volia haver de crear un diccionari tant gran. Així que per aquesta raó, em vaig posar mans a l'obra per aconseguir la fòrmula.

### Què sé de música?
De coses tècniques, no massa (almenys ara mateix). Però em vaig estar posant al dia i vaig arribar a què, en la notació anglesa:
```
A0=0    A1=7    A2=14   .       .
B0=1    B1=8    B2=15   .
C1=2    C2=9    .
D1=3    .       .
E1=4    .
F1=5
G1=6
```
Dels apunts anteriors, assignant a cada lletra el seu valor inicial (el de més a l'esquerra) i sabent que a música una octava = 7, vaig derivar-ne que:
```
Si la lletra es A o B:
    Valor nota = Valor base lletra + Octava * Nombre que acompanya la lletra
si no:
    Valor nota = Valor base lletra + Octava * (Nombre que acompanya la lletra-1)
```
Compte: si la lletra és "A" o "B", el Nombre es manté igual; en cas contrari, li resto 1. Es pot veure perquè això és cert perquè el valor base de les lletres de la C a la G és una unitat superior que el de l'A i la B.

Per tant, amb aquesta fòrmula/pseudo-codi ja m'és possible conèixer el valor de qualsevol nota i aïllant certs operands, fer la conversió de notes a enters (procediment `__noteValueEnglishNotation`) i a la inversa (procediment `__note2lilypond`).

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
- Nota fora del rang existent

# Generació dels fitxers d'àudio

Utilitzant Lilipond per generar les partitures i Timidity++ i ffmpeg per generar els WAV i MP3. Aquest procés es realitza dins de la funció `__generateMusic()`.

# Extensions
## Instrucció de reproducció en cànon
La instrucció de reproducció `<:>` afegeix la nota o la llista de notes donades a la partitura. La instrucció de reproducció en cànon `<::N>`fa exactament el mateix però afegeix les notes a una de les veus de la composició. Benvinguts al món dels cànons!

La instrucció de reproducció `<:>` segueix funcionant, el que ara afegeix les notes a la partitura de la primera veu (la número zero), per tant, el seu equivalent en instrucció de reproducció en cànon seria `<::0>`.
```
~~~ Cànon "Escala de Hanoi" ~~~
Main |:
    Hanoi
    Alle_Schlüssel
:|

~~~ Notes de Hanoi ~~~
Hanoi |:
    src <- {C D E F G}
    dst <- {}
    aux <- {}
    HanoiRec #src src dst aux
:|

HanoiRec n src dst aux |:
    if n > 0 |:
        HanoiRec (n - 1) src aux dst
        note <- src[#src]
        8< src[#src]
        dst << note
        <:1> note
        HanoiRec (n - 1) aux dst src
    :|
:|

~~~ Escala musical ~~~
Alle_Schlüssel |:
    note <- A0
    while note <= C8 |:
        <:2> note
        note <- note + 1
    :|
:|
```
La melodia no té perquè ser la mateixa per les diferents veus. La veu N+1 comença un silenci de negra+corxera més tard que la veu N.