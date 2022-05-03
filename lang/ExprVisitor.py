# Generated from Expr.g by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignStmt.
    def visitAssignStmt(self, ctx:ExprParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#readStmt.
    def visitReadStmt(self, ctx:ExprParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#writeStmt.
    def visitWriteStmt(self, ctx:ExprParser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#reproStmt.
    def visitReproStmt(self, ctx:ExprParser.ReproStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifStmt.
    def visitIfStmt(self, ctx:ExprParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#whileStmt.
    def visitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#procedureStmt.
    def visitProcedureStmt(self, ctx:ExprParser.ProcedureStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unaryExpr.
    def visitUnaryExpr(self, ctx:ExprParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#valueExpr.
    def visitValueExpr(self, ctx:ExprParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:ExprParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#relationalExpr.
    def visitRelationalExpr(self, ctx:ExprParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#leftExpr.
    def visitLeftExpr(self, ctx:ExprParser.LeftExprContext):
        return self.visitChildren(ctx)



del ExprParser