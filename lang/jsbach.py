import sys
import pdb
import os
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
    from .jsbachVisitor import jsbachVisitor
    from .jsbachLexer import jsbachLexer
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor
    from jsbachLexer import jsbachLexer

# This class defines a complete generic visitor for a parse tree produced
# by jsbachParser.


class BachVisitor(jsbachVisitor):

    # llista (stack) de scopes,
    # l'última llista és l'actual
    allScopes = []
    # diccionari de tots els procediments
    # amb el seu context stmts
    procsStmtsContexts = {}
    # diccionari de tots els procediments
    # amb el nom de tots els seus paràmetres
    procsParameters = {}
    # llista de les notes afegides per PLAY
    musicSheet = []
    # diccionari de les llistes de notes afegides per PLAY i CANONPLAY
    canonSheet = {}

    def __init__(self):
        self.nivell = 0

    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx: jsbachParser.RootContext):
        self.visitChildren(ctx)

        # Making sure Main is the last thing to visit
        if len(sys.argv) == 2:
            self.allScopes.append({})
            try:
                for stmt in self.procsStmtsContexts['Main']:
                    self.visit(stmt)
            except KeyError:
                raise Exception('On està el Main, que jo el vegui?')
        else:
            procId = sys.argv[2]
            paramsInput = sys.argv[3:]

            try:
                # EXC: #params passed != #params needed
                if len(self.procsParameters[procId]) != len(paramsInput):
                    raise Exception('La crida a ' +
                                    procId +
                                    ' requereix ' +
                                    str(len(self.procsParameters[procId])) +
                                    ' paràmetres, no ' +
                                    str(len(paramsInput)) +
                                    '.')

                newScope = {}
                for i in range(len(paramsInput)):
                    newScope[self.procsParameters[procId][i]] = paramsInput[i]
            except KeyError:
                raise Exception('El procediment ' + procId + ' no existeix.')

            self.allScopes.append(newScope)

            for stmt in self.procsStmtsContexts[procId]:
                self.visit(stmt)

        self.__createMusicSheet()

    def __note2lilypond(self, noteNum):
        # cada lletra te un residu entre 7 diferent
        # el de l'A es 0, el de la B es 1...
        baseValue = noteNum % 7
        # el codi ascii de la lletra a minúscula es 97
        baseLetter = chr(baseValue + 97)

        # revertim la fòrmula
        offsetNum = int((noteNum - baseValue) / 7)
        if baseLetter != 'a' and baseLetter != 'b':
            offsetNum = offsetNum + 1

        # en notació lilypond,
        # per cada desviació de l'octava central (la 4a) es posa un símbol
        lilyPostfixOffset = 4 - offsetNum - 1

        # depenent si desviació positiva o negativa,
        # octava més alta o més baixa
        if lilyPostfixOffset >= 0:
            lilyPostfix = ',' * lilyPostfixOffset
        else:
            lilyPostfix = '\'' * -lilyPostfixOffset

        # retornem lletra + postfix de lilypond
        return baseLetter + lilyPostfix

    def __createMusicSheet(self):
        fileName = "musica.ly"
        file = open(fileName, "w")

        header = '\\version "2.20.0" \n\\score { \n\t\\new StaffGroup <<'
        file.write(header)

        voicesIds = list(self.canonSheet.keys())
        currentVoice = 0
        # for every voice
        for voice in self.canonSheet:
            file.write(
                '\n\t\t\\new Staff \\absolute { \n\t\t\t\\tempo 4 = 120 \n\t\t\t')
            file.write('r8 ' * int(voicesIds[currentVoice]))
            file.write('r4 ' * int(voicesIds[currentVoice]))

            for note in self.canonSheet[voice]:
                # write all lily notes in one line
                file.write(self.__note2lilypond(note) + ' ')

            file.write('\n\t\t}')
            currentVoice = currentVoice + 1

        footer = '\n\t>> \n\t\\layout { } \n\t\\midi { } \n}'
        file.write(footer)

    # Visit a parse tree produced by jsbachParser#procedureDef.
    def visitProcedureDef(self, ctx: jsbachParser.ProcedureDefContext):
        procId = ctx.PROCID().getText()
        paramList = self.visit(ctx.paramsListDef())

        if procId in self.procsStmtsContexts:
            raise Exception('El procediment ' + procId + ' ja està definit.')

        self.procsStmtsContexts[procId] = ctx.stmts().stmt()
        self.procsParameters[procId] = paramList

    # Visit a parse tree produced by jsbachParser#paramsListDef.
    def visitParamsListDef(self, ctx: jsbachParser.ParamsListDefContext):
        params = []
        for p in ctx.VARID():
            pTxt = p.getText()
            if pTxt in params:
                raise Exception(
                    'Paràmetres formals repetits amb el nom ' + pTxt + '.')
            params.append(pTxt)
        return params

    # Visit a parse tree produced by jsbachParser#assignStmt.
    def visitAssignStmt(self, ctx: jsbachParser.AssignStmtContext):
        expr = self.visit(ctx.expr())
        leftExpr = self.visit(ctx.leftExpr())
        self.allScopes[-1][leftExpr] = expr

    # Visit a parse tree produced by jsbachParser#writeStmt.
    def visitWriteStmt(self, ctx: jsbachParser.WriteStmtContext):
        l = list(ctx.getChildren())
        # l[0] is WRITE token
        for out in l[1:]:
            print(self.visit(out), end=" ")
        print()

    # Visit a parse tree produced by jsbachParser#readStmt.
    def visitReadStmt(self, ctx: jsbachParser.ReadStmtContext):
        id = ctx.VARID().getText()
        inputValue = int(input())
        self.allScopes[-1][id] = inputValue

    # Visit a parse tree produced by jsbachParser#canonPlayStmt.
    def visitCanonPlayStmt(self, ctx: jsbachParser.CanonPlayStmtContext):
        note = self.visit(ctx.expr())
        voice = ctx.NUMBER().getText()
        try:
            if not isinstance(note, list):
                note = [note]
            self.canonSheet[voice].extend(note)
        except KeyError:
            self.canonSheet[voice] = note

    # Visit a parse tree produced by jsbachParser#playStmt.
    def visitPlayStmt(self, ctx: jsbachParser.PlayStmtContext):
        note = self.visit(ctx.expr())
        try:
            if not isinstance(note, list):
                note = [note]
            self.canonSheet['0'].extend(note)
        except KeyError:
            self.canonSheet['0'] = note

    # Visit a parse tree produced by jsbachParser#ifStmt.
    def visitIfStmt(self, ctx: jsbachParser.IfStmtContext):
        boolExpr = self.visit(ctx.expr())
        if boolExpr == 1:
            self.visit(ctx.stmts(0))
        else:
            if ctx.ELSE():
                self.visit(ctx.stmts(1))

    # Visit a parse tree produced by jsbachParser#whileStmt.
    def visitWhileStmt(self, ctx: jsbachParser.WhileStmtContext):
        while self.visit(ctx.expr()):
            self.visit(ctx.stmts())

    # Visit a parse tree produced by jsbachParser#paramsListCall.
    def visitParamsListCall(self, ctx: jsbachParser.ParamsListCallContext):
        paramsCtx = list(ctx.getChildren())
        params = []
        for p in paramsCtx:
            params.append(self.visit(p))
        return params

    # Visit a parse tree produced by jsbachParser#procCallStmt.
    def visitProcCallStmt(self, ctx: jsbachParser.ProcCallStmtContext):
        procId = ctx.PROCID().getText()
        procStmtsCtx = self.procsStmtsContexts[procId]
        # EXC: procedureName does not exist
        procParams = self.procsParameters[procId]
        myParams = self.visit(ctx.paramsListCall())
        # EXC: #params passed != #params needed
        if len(procParams) != len(myParams):
            raise Exception(
                'La crida a ' +
                procId +
                ' requereix ' +
                len(procParams) +
                ', no ' +
                len(myParams) +
                '.')

        newScope = {}
        for i in range(len(myParams)):
            newScope[procParams[i]] = myParams[i]
        # "push" new vars
        self.allScopes.append(newScope)

        for stmt in procStmtsCtx:
            self.visit(stmt)

        # "pop" new vars
        self.allScopes.pop()

    # Visit a parse tree produced by jsbachParser#concatStmt.
    def visitConcatStmt(self, ctx: jsbachParser.ConcatStmtContext):
        varId = ctx.VARID().getText()
        newElem = self.visit(ctx.expr())
        try:
            self.allScopes[-1][varId].append(newElem)
        except KeyError:
            raise Exception('La llista ' + varId + ' no existeix.')

    # Visit a parse tree produced by jsbachParser#cutStmt.
    def visitCutStmt(self, ctx: jsbachParser.CutStmtContext):
        varId = ctx.VARID().getText()
        index = self.visit(ctx.expr())
        try:
            del self.allScopes[-1][varId][index - 1]
        except KeyError:
            raise Exception('La llista ' + varId + ' no existeix.')
        except IndexError:
            raise Exception('Accés a índex inexistent ' + str(index) + ' de la llista ' +
                            varId + ', de tamany ' + str(len(self.allScopes[-1][varId])) + '.')

    # Visit a parse tree produced by jsbachParser#arrayLengthExpr.
    def visitArrayLengthExpr(self, ctx: jsbachParser.ArrayLengthExprContext):
        varId = ctx.VARID().getText()
        try:
            return len(self.allScopes[-1][varId])
        except KeyError:
            raise Exception('La llista ' + varId + ' no existeix.')

    # Visit a parse tree produced by jsbachParser#unaryExpr.
    def visitUnaryExpr(self, ctx: jsbachParser.UnaryExprContext):
        expr = self.visit(ctx.expr())
        if ctx.PLUS():
            return expr
        elif ctx.MINUS():
            return -expr

    # Visit a parse tree produced by jsbachParser#valueExpr.
    def visitValueExpr(self, ctx: jsbachParser.ValueExprContext):
        # len(l) == 1
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText().replace('"', '')
        elif ctx.BOOLEAN():
            return int(ctx.BOOLEAN().getText())

    # Visit a parse tree produced by jsbachParser#relationalExpr.
    def visitRelationalExpr(self, ctx: jsbachParser.RelationalExprContext):
        expr1, op, expr2 = list(ctx.getChildren())
        if ctx.EQ():
            retValue = self.visit(expr1) == self.visit(expr2)
        elif ctx.NEQ():
            retValue = self.visit(expr1) != self.visit(expr2)
        elif ctx.GT():
            retValue = self.visit(expr1) > self.visit(expr2)
        elif ctx.GE():
            retValue = self.visit(expr1) >= self.visit(expr2)
        elif ctx.LT():
            retValue = self.visit(expr1) <= self.visit(expr2)
        elif ctx.LE():
            retValue = self.visit(expr1) < self.visit(expr2)
        return 1 if retValue else 0

    # Visit a parse tree produced by jsbachParser#parenthesesExpr.
    def visitParenthesesExpr(self, ctx: jsbachParser.ParenthesesExprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by jsbachParser#arrayAccessExpr.
    def visitArrayAccessExpr(self, ctx: jsbachParser.ArrayAccessExprContext):
        varId = ctx.VARID().getText()
        index = self.visit(ctx.expr())
        try:
            return self.allScopes[-1][varId][index - 1]
        except KeyError:
            raise Exception('La llista ' + varId + ' no existeix.')
        except IndexError:
            raise Exception('Accés a índex inexistent ' + str(index) + ' de la llista ' +
                            varId + ', de tamany ' + str(len(self.allScopes[-1][varId])) + '.')

    # Visit a parse tree produced by jsbachParser#arrayExpr.

    def visitArrayExpr(self, ctx: jsbachParser.ArrayExprContext):
        return self.visit(ctx.array())

    # Visit a parse tree produced by jsbachParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx: jsbachParser.ArithmeticExprContext):
        # len(list) == 3
        expr1, op, expr2 = list(ctx.getChildren())

        if ctx.PLUS():
            return self.visit(expr1) + self.visit(expr2)
        elif ctx.MINUS():
            return self.visit(expr1) - self.visit(expr2)
        elif ctx.MUL():
            return self.visit(expr1) * self.visit(expr2)
        elif ctx.DIV():
            try:
                return self.visit(expr1) / self.visit(expr2)
            except ZeroDivisionError:
                raise Exception(
                    "Division durch Null (divisió entre 0, pels que no saben alemà)")
        elif ctx.MOD():
            return self.visit(expr1) % self.visit(expr2)

    # Visit a parse tree produced by jsbachParser#LeftExprId.
    def visitLeftExpr(self, ctx: jsbachParser.LeftExprContext):
        varId = ctx.VARID().getText()
        return varId

    def __noteValueEnglishNotation(self, noteId):
        # extraiem la lletra de la nota
        letter = noteId[0]
        # extraiem el nombre de la nota
        if len(noteId) > 1:
            number = int(noteId[1])
        # si no té nombre, segons normes de notació musical, li posem un 4
        else:
            number = 4

        # ord(A) retorna el codi ascii per la lletra A majúscula
        # com és 65, li restem aquest nombre per tal que en el nostre cas la
        # lletra A retorni 0
        baseValueFromLetter = ord(letter) - 65
        # sí, una octava musical equival al nombre 7
        octave = 7

        # cas especial, si la lletra no és ni A ni B,
        # l'operació la fem amb --nombre
        if letter not in ['A', 'B']:
            number = number - 1

        # fem el càlcul, com si fos una recta amb pendent
        value = baseValueFromLetter + octave * number

        # possible excepció per limitar les notes [A0-C8]
        if value > 51 or value < 0:
            raise Exception('La nota ' + noteId + ' no existeix.')
        return value

    # Visit a parse tree produced by jsbachParser#ident.
    def visitIdent(self, ctx: jsbachParser.IdentContext):
        if ctx.VARID():
            varId = ctx.VARID().getText()
            try:
                return self.allScopes[-1][varId]
            except KeyError:
                self.allScopes[-1][varId] = 0
                return 0
        elif ctx.NOTE():
            noteId = ctx.NOTE().getText()
            return self.__noteValueEnglishNotation(noteId)

    # Visit a parse tree produced by jsbachParser#array.
    def visitArray(self, ctx: jsbachParser.ArrayContext):
        elems = []
        if ctx.NUMBER():
            for num in ctx.NUMBER():
                elems.append(int(num.getText()))
        elif ctx.NOTE():
            for note in ctx.NOTE():
                elems.append(self.__noteValueEnglishNotation(note.getText()))
        return elems


def __generateMusic():
    # Lilypond
    if os.system('lilypond musica.ly') == 0:
        print('---Lilypond: OK')
    else:
        print("---Lilypond: NO")
        return 1

    # Timidity++
    if os.system('timidity -Ow -o musica.wav musica.midi') == 0:
        print('---Timidity: OK')
    else:
        print('---Timidity: NO')
        return 2

    # ffmpeg
    if os.system(
            'ffmpeg -y -i musica.wav -codec:a libmp3lame -qscale:a 2 musica.mp3') == 0:
        print('---ffmpeg: OK')
    else:
        print('---ffmpeg: NO')
        return 3

    # Operative system check + play
    myOS = sys.platform
    print("---D'acord, el teu sistema utilitza l'OS:", myOS)
    print("---Reproduint l'obra mestra creada.")

    if myOS == "linux":
        if os.system('ffplay -autoexit -showmode 1 musica.mp3') == 0:
            print('---ffplay: OK')
        else:
            print('---ffplay: NO')
            return 4
    elif myOS == "darwin":
        if os.system('afplay musica.mp3') == 0:
            print('---afplay: OK')
        else:
            print('---afplay: NO')
            return 4
    else:
        return 5


if __name__ == "__main__":
    if os.system(
            'antlr4 -Dlanguage=Python3 -no-listener -visitor jsbach.g4') == 0:
        print('---Compilació de la gramàtica i generació de la plantilla del visitor: OK')
    else:
        print('---Compilació de la gramàtica i generació de la plantilla del visitor: NO')

    input_stream = FileStream(sys.argv[1], encoding='utf-8')

    lexer = jsbachLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = jsbachParser(token_stream)
    tree = parser.root()
    print(tree.toStringTree(recog=parser))

    visitor = BachVisitor()
    visitor.visit(tree)

    if __generateMusic():
        print('---Execució interrompuda o acabada amb errors.')
    else:
        print('---Execució acabada amb èxit.')
