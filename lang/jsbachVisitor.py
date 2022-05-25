# Generated from jsbach.g4 by ANTLR 4.9.2
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


    # Visit a parse tree produced by jsbachParser#stmts.
    def visitStmts(self, ctx:jsbachParser.StmtsContext):
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


    # Visit a parse tree produced by jsbachParser#crabifyStmt.
    def visitCrabifyStmt(self, ctx:jsbachParser.CrabifyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#canonPlayStmt.
    def visitCanonPlayStmt(self, ctx:jsbachParser.CanonPlayStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#playStmt.
    def visitPlayStmt(self, ctx:jsbachParser.PlayStmtContext):
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


    # Visit a parse tree produced by jsbachParser#concatStmt.
    def visitConcatStmt(self, ctx:jsbachParser.ConcatStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#cutStmt.
    def visitCutStmt(self, ctx:jsbachParser.CutStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#arrayLengthExpr.
    def visitArrayLengthExpr(self, ctx:jsbachParser.ArrayLengthExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#unaryExpr.
    def visitUnaryExpr(self, ctx:jsbachParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#valueExpr.
    def visitValueExpr(self, ctx:jsbachParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#arrayAccessExpr.
    def visitArrayAccessExpr(self, ctx:jsbachParser.ArrayAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#arrayExpr.
    def visitArrayExpr(self, ctx:jsbachParser.ArrayExprContext):
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