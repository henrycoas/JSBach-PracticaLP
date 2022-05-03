# Generated from Expr.g by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class BachVisitor(ExprVisitor):
    def __init__(self):
        self.nivell = 0

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        l = list(ctx.getChildren())        
        print(self.visit(l[0]))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#valueExpr.
    def visitValueExpr(self, ctx:ExprParser.ValueExprContext):
        # len(l) == 1
        return int(ctx.NUMBER().getText())


    # Visit a parse tree produced by ExprParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:ExprParser.ArithmeticExprContext):
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

