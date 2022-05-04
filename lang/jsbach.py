import sys
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

    dictionary = {}

    def __init__(self):
        self.nivell = 0

    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        l = list(ctx.getChildren())
        print(self.visit(l[0]))

    # Visit a parse tree produced by jsbachParser#assignStmt.
    def visitAssignStmt(self, ctx:jsbachParser.AssignStmtContext):
        expr = self.visit(ctx.expr())
        leftExpr = self.visit(ctx.leftExpr())
        dictionary[leftExpr] = expr

    # Visit a parse tree produced by jsbachParser#writeStmt.
    def visitWriteStmt(self, ctx:jsbachParser.WriteStmtContext):
        l = list(ctx.getChildren())
        print(43)
        for expr in l[1:]:
            print(self.visit(expr).getText())


    # Visit a parse tree produced by jsbachParser#valueExpr.
    def visitValueExpr(self, ctx:jsbachParser.ValueExprContext):
        # len(l) == 1
        return int(ctx.NUMBER().getText())


    # Visit a parse tree produced by jsbachParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:jsbachParser.ArithmeticExprContext):
        expr1, op, expr2 = list(ctx.getChildren())
        # len(list) == 3
        if ctx.PLUS():
            return self.visit(expr1) + self.visit(expr2)
        elif ctx.MINUS():
            return self.visit(expr1) - self.visit(expr2)
        elif ctx.MUL():
            return self.visit(expr1) * self.visit(expr2)
        elif ctx.DIV():
            valueExpr2 = self.visit(expr2)
            if valueExpr2 == 0:
                print("Division durch Null (divisió entre 0, pels que no saben alemà)")
                return 0
            return self.visit(expr1) / valueExpr2


    # Visit a parse tree produced by jsbachParser#idExpr.
    def visitIdExpr(self, ctx:jsbachParser.IdExprContext):
        id = ctx.ID().getText()
        print(id)
        return dictionary[id]


    # Visit a parse tree produced by jsbachParser#LeftExprId.
    def visitLeftExprId(self, ctx:jsbachParser.LeftExprIdContext):
        id = ctx.ID().getText()
        print(id)
        return dictionary[id]



input_stream = FileStream(sys.argv[1])

lexer = jsbachLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = jsbachParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))

visitor = BachVisitor()
visitor.visit(tree)