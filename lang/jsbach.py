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
    def __init__(self):
        self.nivell = 0

    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        l = list(ctx.getChildren())        
        print(self.visit(l[0]))
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#assignStmt.
    def visitAssignStmt(self, ctx:jsbachParser.AssignStmtContext):
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#valueExpr.
    def visitValueExpr(self, ctx:jsbachParser.ValueExprContext):
        # len(l) == 1
        return int(ctx.NUMBER().getText())


    # Visit a parse tree produced by jsbachParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:jsbachParser.ArithmeticExprContext):
        expr1, op, expr2 = list(ctx.getChildren())
        # len(list) == 3
        if op.getText() == '+':
            return self.visit(expr1) + self.visit(expr2)
        elif op.getText() == '-':
            return self.visit(expr1) - self.visit(expr2)
        elif op.getText() == '*':
            return self.visit(expr1) * self.visit(expr2)
        elif op.getText() == '/':
            valueExpr2 = self.visit(expr2)
            if valueExpr2 == 0:
                print("Division durch Null (divisió entre 0, pels que no saben alemà)")
                return 0
            return self.visit(expr1) / valueExpr2



input_stream = FileStream(sys.argv[1])

lexer = jsbachLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = jsbachParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))

visitor = BachVisitor()
visitor.visit(tree)