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

    # key: varName, value: variable value
    currentScopeVars = {}
    # key: procName, value: list of the params
    definedProcedures = {}
    # notes added by the REPRO stmt
    musicSheet = []

    def __init__(self):
        self.nivell = 0


    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#procedureDef.
    def visitProcedureDef(self, ctx:jsbachParser.ProcedureDefContext):
        procId = self.visit(ctx.ID())
        params = self.visit(ctx.paramsListDef())
        # save the procedure name with the parameters
        self.definedProcedures[procId] = params
        for stmt in ctx.stmt():
            self.visit(stmt)


    # Visit a parse tree produced by jsbachParser#paramsListDef.
    def visitParamsListDef(self, ctx:jsbachParser.ParamsListDefContext):
        params = list(ctx.getChildren())
        # save each parameter with value 0
        for p in params:
            self.currentScopeVars[p] = 0
        return params


    # Visit a parse tree produced by jsbachParser#assignStmt.
    def visitAssignStmt(self, ctx:jsbachParser.AssignStmtContext):
        expr = self.visit(ctx.expr())
        leftExpr = self.visit(ctx.leftExpr())
        self.currentScopeVars[leftExpr] = expr


    # Visit a parse tree produced by jsbachParser#writeStmt.
    def visitWriteStmt(self, ctx:jsbachParser.WriteStmtContext):
        l = list(ctx.getChildren())
        # l[0] is WRITE
        for out in l[1:]:
            print(self.visit(out), end=" ")
        print()


    # Visit a parse tree produced by jsbachParser#readStmt.
    def visitReadStmt(self, ctx:jsbachParser.ReadStmtContext):
        id = ctx.ID().getText()
        inputValue = input()
        self.currentScopeVars[id] = inputValue


    # Visit a parse tree produced by jsbachParser#ifStmt.
    def visitIfStmt(self, ctx:jsbachParser.IfStmtContext):
        boolExpr = self.visit(ctx.expr())
        if boolExpr == 1:
            self.visit(ctx.stmt(0))
        else:
            if ctx.ELSE():
                self.visit(ctx.stmt(1))


    # Visit a parse tree produced by jsbachParser#whileStmt.
    def visitWhileStmt(self, ctx:jsbachParser.WhileStmtContext):
        while self.visit(ctx.expr()):
            self.visit(ctx.stmt())

    # Visit a parse tree produced by jsbachParser#procCallStmt.
    def visitProcCallStmt(self, ctx:jsbachParser.ProcCallStmtContext):
        l = list(ctx.getChildren())
        procName = l[0]
        # EXC: procedureName does not exist
        # EXC: #params passed != #params needed
        for param in l[1:]:
            # self.definedProcedures[]
            # self.currentScopeVars[]
            return


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
            valueExpr2 = self.visit(expr2)
            if valueExpr2 == 0:
                # EXC: Division durch Null (divisió entre 0, pels que no saben alemà)
                return 0
            return self.visit(expr1) / valueExpr2
        elif ctx.MOD():
            return self.visit(expr1) % self.visit(expr2)


    # Visit a parse tree produced by jsbachParser#idExpr.
    def visitIdExpr(self, ctx:jsbachParser.IdExprContext):
        id = ctx.ID().getText()
        return self.currentScopeVars[id]  


    # Visit a parse tree produced by jsbachParser#LeftExprId.
    def visitLeftExprId(self, ctx:jsbachParser.LeftExprIdContext):
        id = ctx.ID().getText()
        return self.currentScopeVars[id]

input_stream = FileStream(sys.argv[1])

lexer = jsbachLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = jsbachParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))

visitor = BachVisitor()
visitor.visit(tree)
