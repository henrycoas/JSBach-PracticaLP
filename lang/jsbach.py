import sys
import pdb
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
    from .jsbachVisitor import jsbachVisitor
    from .jsbachLexer import jsbachLexer
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor
    from jsbachLexer import jsbachLexer

# This class defines a complete generic visitor for a parse tree produced by jsbachParser.

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
    # llista de les notes afegides per REPRO
    musicSheet = []

    def __init__(self):
        self.nivell = 0


    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        self.visitChildren(ctx)
        
        # Making sure Main is the last thing to visit
        if len(sys.argv) == 2:
            self.allScopes.append({})
            for stmt in self.procsStmtsContexts['Main']:
                self.visit(stmt)
        else:
            paramsInput = sys.argv[3:]
            # EXC: #params passed != #params needed
            newScope = {}
            for i in range(len(paramsInput)):
                newScope[self.procsParameters[i]] = paramsInput[i]
            self.allScopes.append(newScope)

            procName = sys.argv[2]
            for stmt in self.procsStmtsContexts[procName]:
                self.visit(stmt)

        print(self.musicSheet)


    # Visit a parse tree produced by jsbachParser#procedureDef.
    def visitProcedureDef(self, ctx:jsbachParser.ProcedureDefContext):
        procId = ctx.PROCID().getText()
        paramList = self.visit(ctx.paramsListDef())

        self.procsStmtsContexts[procId] = ctx.stmts().stmt()
        self.procsParameters[procId] = paramList


    # Visit a parse tree produced by jsbachParser#paramsListDef.
    def visitParamsListDef(self, ctx:jsbachParser.ParamsListDefContext):
        params = []
        for p in ctx.VARID():
            params.append(p.getText())
        return params


    # Visit a parse tree produced by jsbachParser#assignStmt.
    def visitAssignStmt(self, ctx:jsbachParser.AssignStmtContext):
        expr = self.visit(ctx.expr())
        leftExpr = self.visit(ctx.leftExpr())
        self.allScopes[-1][leftExpr] = expr


    # Visit a parse tree produced by jsbachParser#writeStmt.
    def visitWriteStmt(self, ctx:jsbachParser.WriteStmtContext):
        l = list(ctx.getChildren())
        # l[0] is WRITE token
        for out in l[1:]:
            print(self.visit(out), end=" ")
        print()


    # Visit a parse tree produced by jsbachParser#readStmt.
    def visitReadStmt(self, ctx:jsbachParser.ReadStmtContext):
        id = ctx.VARID().getText()
        inputValue = int(input())
        self.allScopes[-1][id] = inputValue


    # Visit a parse tree produced by jsbachParser#playStmt.
    def visitPlayStmt(self, ctx:jsbachParser.PlayStmtContext):
        note = self.visit(ctx.expr())
        if isinstance(note, list):
            self.musicSheet.extend(note)
        else:
            self.musicSheet.append(note)


    # Visit a parse tree produced by jsbachParser#ifStmt.
    def visitIfStmt(self, ctx:jsbachParser.IfStmtContext):
        boolExpr = self.visit(ctx.expr())
        if boolExpr == 1:
            self.visit(ctx.stmts(0))
        else:
            if ctx.ELSE():
                self.visit(ctx.stmts(1))


    # Visit a parse tree produced by jsbachParser#whileStmt.
    def visitWhileStmt(self, ctx:jsbachParser.WhileStmtContext):
        while self.visit(ctx.expr()):
            self.visit(ctx.stmts())

    # Visit a parse tree produced by jsbachParser#paramsListCall.
    def visitParamsListCall(self, ctx:jsbachParser.ParamsListCallContext):
        paramsCtx = list(ctx.getChildren())
        params = []
        for p in paramsCtx:
            params.append(self.visit(p))
        return params


    # Visit a parse tree produced by jsbachParser#procCallStmt.
    def visitProcCallStmt(self, ctx:jsbachParser.ProcCallStmtContext):
        procId = ctx.PROCID().getText()
        procStmtsCtx = self.procsStmtsContexts[procId]
        # EXC: procedureName does not exist
        procParams = self.procsParameters[procId]
        myParams = self.visit(ctx.paramsListCall())
        # EXC: #params passed != #params needed
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
    def visitConcatStmt(self, ctx:jsbachParser.ConcatStmtContext):
        varId = ctx.VARID().getText()
        newElem = self.visit(ctx.expr())
        self.allScopes[-1][varId].append(newElem)


    # Visit a parse tree produced by jsbachParser#cutStmt.
    def visitCutStmt(self, ctx:jsbachParser.CutStmtContext):
        varId = ctx.VARID().getText()
        index = self.visit(ctx.expr())-1
        del self.allScopes[-1][varId][index]

    # Visit a parse tree produced by jsbachParser#arrayLengthExpr.
    def visitArrayLengthExpr(self, ctx:jsbachParser.ArrayLengthExprContext):
        varId = ctx.VARID().getText()
        return len(self.allScopes[-1][varId])


    # Visit a parse tree produced by jsbachParser#unaryExpr.
    def visitUnaryExpr(self, ctx:jsbachParser.UnaryExprContext):
        expr = self.visit(ctx.expr())
        if ctx.PLUS():
            return expr
        elif ctx.MINUS():
            return -expr


    # Visit a parse tree produced by jsbachParser#valueExpr.
    def visitValueExpr(self, ctx:jsbachParser.ValueExprContext):
        # len(l) == 1
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText().replace('"','')
        elif ctx.BOOLEAN():
            return int(ctx.BOOLEAN().getText())


    # Visit a parse tree produced by jsbachParser#relationalExpr.
    def visitRelationalExpr(self, ctx:jsbachParser.RelationalExprContext):
        expr1, op, expr2 =  list(ctx.getChildren())
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
    def visitParenthesesExpr(self, ctx:jsbachParser.ParenthesesExprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by jsbachParser#arrayAccessExpr.
    def visitArrayAccessExpr(self, ctx:jsbachParser.ArrayAccessExprContext):
        varId = ctx.VARID().getText()
        index = self.visit(ctx.expr())-1
        return self.allScopes[-1][varId][index]

    # Visit a parse tree produced by jsbachParser#arrayExpr.
    def visitArrayExpr(self, ctx:jsbachParser.ArrayExprContext):
        return self.visit(ctx.array())


    # Visit a parse tree produced by jsbachParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:jsbachParser.ArithmeticExprContext):
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
            except ZeroDivisionError as zero:
                print("Division durch Null (divisió entre 0, pels que no saben alemà)")
                return None
        elif ctx.MOD():
            return self.visit(expr1) % self.visit(expr2)


    # Visit a parse tree produced by jsbachParser#LeftExprId.
    def visitLeftExpr(self, ctx:jsbachParser.LeftExprContext):
        varId = ctx.VARID().getText()
        return varId


    def __noteValueSpanishNotation(self, noteId):
        return 0


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

        return baseValueFromLetter + octave * number


    # Visit a parse tree produced by jsbachParser#ident.
    def visitIdent(self, ctx:jsbachParser.IdentContext):
        if ctx.VARID():
            varId = ctx.VARID().getText()
            return self.allScopes[-1][varId]
        elif ctx.NOTE():
            noteId = ctx.NOTE().getText()
            return self.__noteValueEnglishNotation(noteId)

    # Visit a parse tree produced by jsbachParser#array.
    def visitArray(self, ctx:jsbachParser.ArrayContext):
        elems = []
        if ctx.NUMBER():
            for num in ctx.NUMBER():
                elems.append(int(num.getText()))
        elif ctx.NOTE():
            for note in ctx.NOTE():
                elems.append(self.__noteValueEnglishNotation(note.getText()))
        return elems
        

input_stream = FileStream(sys.argv[1])

lexer = jsbachLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = jsbachParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))

visitor = BachVisitor()
visitor.visit(tree)
