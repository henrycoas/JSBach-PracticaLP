# El llenguatge JSBach

## Introducció

Aquesta és la Pràctica de Llenguatges de Programació del Q2 del curs 2021-2022.

## Instalació i configuració

Si creus que ja ho tens tot ben muntat o ho saps segur, pots saltar-te aquest pas. En cas contrari, he preparat un fitxer que fa la instalació (en Linux). Pots revisar-lo per després executar-lo amb:
```bash
bash setup.sh
```

Per compilar la gramàtica i generar la plantilla del visitor:
```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor jsbach.g4
```

## Ús
```python
python3 jsbach.py input.jsb
```
