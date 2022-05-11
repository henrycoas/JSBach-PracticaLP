# Generated from jsbach.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
else:
    from jsbachParser import jsbachParser

# This class defines a complete generic visitor for a parse tree produced by jsbachParser.

class jsbachVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#procedureDef.
    def visitProcedureDef(self, ctx:jsbachParser.ProcedureDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#paramsListDef.
    def visitParamsListDef(self, ctx:jsbachParser.ParamsListDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#paramsListCall.
    def visitParamsListCall(self, ctx:jsbachParser.ParamsListCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#readStmt.
    def visitReadStmt(self, ctx:jsbachParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#writeStmt.
    def visitWriteStmt(self, ctx:jsbachParser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#reproStmt.
    def visitReproStmt(self, ctx:jsbachParser.ReproStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#ifStmt.
    def visitIfStmt(self, ctx:jsbachParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#whileStmt.
    def visitWhileStmt(self, ctx:jsbachParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#procCallStmt.
    def visitProcCallStmt(self, ctx:jsbachParser.ProcCallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#assignStmt.
    def visitAssignStmt(self, ctx:jsbachParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#unaryExpr.
    def visitUnaryExpr(self, ctx:jsbachParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#valueExpr.
    def visitValueExpr(self, ctx:jsbachParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:jsbachParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#relationalExpr.
    def visitRelationalExpr(self, ctx:jsbachParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#parenthesesExpr.
    def visitParenthesesExpr(self, ctx:jsbachParser.ParenthesesExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#idExpr.
    def visitIdExpr(self, ctx:jsbachParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#leftExpr.
    def visitLeftExpr(self, ctx:jsbachParser.LeftExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#ident.
    def visitIdent(self, ctx:jsbachParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#array.
    def visitArray(self, ctx:jsbachParser.ArrayContext):
        return self.visitChildren(ctx)



del jsbachParser