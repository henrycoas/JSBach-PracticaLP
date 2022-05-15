# El llenguatge JSBach

# Introducció

Aquesta és la Pràctica de Llenguatges de Programació del Q2 del curs 2021-2022.

# Compilació i execució

Per compilar la gramàtica i generar la plantilla del visitor:
```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor jsbach.g4
```

Per executar l'intèrpret amb un fitxer d'entrada:
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

## Els valors de les notes i les notes dels valors

## Errors i excepcions
- Divisió entre 0
- Crida a un procediment no definit
- Repetició de procediment ja definit
- Nombre de paràmetres incorrecte
- Noms de paràmetres formals repetits
- Acces a un índex inexistent d'una llista
    - L'excepció especifica quina llista, a quin índex s'ha intentat accedir i quin era el tamany real de la llista

# Generació dels fitxers d'àudio

Utilitzant Lilipond per generar les partitures i Timidity++ i ffmpeg per generar els WAV i MP3.

## El format .ly

## Conversió de l'àudio

# Automatització mitjançant scripts

Per tal d'utilitzar el meu temps de manera més eficient i fer fàcilment reproduïbles els meus resultats, vaig decidir crear alguns scripts en bash per a l'entorn Linux que utilitzava. 

- Script per preparar al complet l'entorn:
```bash

```

- Script per compilar, executar i generar arxius de so: 
```bash

```