# Generated from Expr.g by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,21,8,1,11,1,12,1,22,1,1,1,1,1,1,1,
        1,1,1,1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,1,1,1,1,1,1,1,5,1,40,8,1,
        10,1,12,1,43,9,1,1,1,3,1,46,8,1,1,1,1,1,1,1,1,1,5,1,52,8,1,10,1,
        12,1,55,9,1,1,1,1,1,1,1,1,1,5,1,61,8,1,10,1,12,1,64,9,1,3,1,66,8,
        1,1,2,1,2,1,2,1,2,3,2,72,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        5,2,83,8,2,10,2,12,2,86,9,2,1,3,1,3,1,3,0,1,4,4,0,2,4,6,0,3,1,0,
        18,19,1,0,20,22,1,0,12,17,103,0,8,1,0,0,0,2,65,1,0,0,0,4,71,1,0,
        0,0,6,87,1,0,0,0,8,9,3,4,2,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,5,26,
        0,0,12,13,5,1,0,0,13,66,3,4,2,0,14,15,5,2,0,0,15,66,5,26,0,0,16,
        20,5,3,0,0,17,21,3,4,2,0,18,21,5,26,0,0,19,21,5,27,0,0,20,17,1,0,
        0,0,20,18,1,0,0,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,
        1,0,0,0,23,66,1,0,0,0,24,25,5,4,0,0,25,66,5,26,0,0,26,27,5,5,0,0,
        27,28,3,4,2,0,28,32,5,10,0,0,29,31,3,2,1,0,30,29,1,0,0,0,31,34,1,
        0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,0,35,
        45,5,11,0,0,36,37,5,6,0,0,37,41,5,11,0,0,38,40,3,2,1,0,39,38,1,0,
        0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,
        1,0,0,0,44,46,5,10,0,0,45,36,1,0,0,0,45,46,1,0,0,0,46,66,1,0,0,0,
        47,48,5,7,0,0,48,49,3,4,2,0,49,53,5,10,0,0,50,52,3,2,1,0,51,50,1,
        0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,
        53,1,0,0,0,56,57,5,11,0,0,57,66,1,0,0,0,58,62,5,26,0,0,59,61,3,4,
        2,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,66,
        1,0,0,0,64,62,1,0,0,0,65,11,1,0,0,0,65,14,1,0,0,0,65,16,1,0,0,0,
        65,24,1,0,0,0,65,26,1,0,0,0,65,47,1,0,0,0,65,58,1,0,0,0,66,3,1,0,
        0,0,67,68,6,2,-1,0,68,69,7,0,0,0,69,72,3,4,2,5,70,72,5,24,0,0,71,
        67,1,0,0,0,71,70,1,0,0,0,72,84,1,0,0,0,73,74,10,4,0,0,74,75,7,1,
        0,0,75,83,3,4,2,5,76,77,10,3,0,0,77,78,7,0,0,0,78,83,3,4,2,4,79,
        80,10,2,0,0,80,81,7,2,0,0,81,83,3,4,2,3,82,73,1,0,0,0,82,76,1,0,
        0,0,82,79,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,5,
        1,0,0,0,86,84,1,0,0,0,87,88,5,26,0,0,88,7,1,0,0,0,11,20,22,32,41,
        45,53,62,65,71,82,84
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "'<?>'", "'<!>'", "'<:>'", "'if'", 
                     "'else'", "'while'", "'<<'", "'8<'", "'|:'", "':|'", 
                     "'='", "'/='", "'>'", "'<'", "'>='", "'<='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "ASSIGN", "READ", "WRITE", "REPRO", "IF", 
                      "ELSE", "WHILE", "CONCAT", "CUT", "LPAREN", "RPAREN", 
                      "EQ", "NEQ", "GT", "LT", "GE", "LE", "PLUS", "MINUS", 
                      "MUL", "DIV", "MOD", "LETTER", "NUMBER", "BOOLEAN", 
                      "ID", "STRING", "WORD", "WS" ]

    RULE_root = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_leftExpr = 3

    ruleNames =  [ "root", "stmt", "expr", "leftExpr" ]

    EOF = Token.EOF
    ASSIGN=1
    READ=2
    WRITE=3
    REPRO=4
    IF=5
    ELSE=6
    WHILE=7
    CONCAT=8
    CUT=9
    LPAREN=10
    RPAREN=11
    EQ=12
    NEQ=13
    GT=14
    LT=15
    GE=16
    LE=17
    PLUS=18
    MINUS=19
    MUL=20
    DIV=21
    MOD=22
    LETTER=23
    NUMBER=24
    BOOLEAN=25
    ID=26
    STRING=27
    WORD=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr(0)
            self.state = 9
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReadStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(ExprParser.READ, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReproStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REPRO(self):
            return self.getToken(ExprParser.REPRO, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReproStmt" ):
                return visitor.visitReproStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LPAREN)
            else:
                return self.getToken(ExprParser.LPAREN, i)
        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RPAREN)
            else:
                return self.getToken(ExprParser.RPAREN, i)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)

        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class ProcedureStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureStmt" ):
                return visitor.visitProcedureStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class WriteStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(ExprParser.WRITE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)
        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.STRING)
            else:
                return self.getToken(ExprParser.STRING, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = ExprParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.match(ExprParser.ID)
                self.state = 12
                self.match(ExprParser.ASSIGN)
                self.state = 13
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.ReadStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(ExprParser.READ)
                self.state = 15
                self.match(ExprParser.ID)
                pass

            elif la_ == 3:
                localctx = ExprParser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.match(ExprParser.WRITE)
                self.state = 20 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 20
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [ExprParser.PLUS, ExprParser.MINUS, ExprParser.NUMBER]:
                            self.state = 17
                            self.expr(0)
                            pass
                        elif token in [ExprParser.ID]:
                            self.state = 18
                            self.match(ExprParser.ID)
                            pass
                        elif token in [ExprParser.STRING]:
                            self.state = 19
                            self.match(ExprParser.STRING)
                            pass
                        else:
                            raise NoViableAltException(self)


                    else:
                        raise NoViableAltException(self)
                    self.state = 22 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass

            elif la_ == 4:
                localctx = ExprParser.ReproStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(ExprParser.REPRO)
                self.state = 25
                self.match(ExprParser.ID)
                pass

            elif la_ == 5:
                localctx = ExprParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.match(ExprParser.IF)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(ExprParser.LPAREN)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.READ) | (1 << ExprParser.WRITE) | (1 << ExprParser.REPRO) | (1 << ExprParser.IF) | (1 << ExprParser.WHILE) | (1 << ExprParser.ID))) != 0):
                    self.state = 29
                    self.stmt()
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 35
                self.match(ExprParser.RPAREN)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ExprParser.ELSE:
                    self.state = 36
                    self.match(ExprParser.ELSE)
                    self.state = 37
                    self.match(ExprParser.RPAREN)
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.READ) | (1 << ExprParser.WRITE) | (1 << ExprParser.REPRO) | (1 << ExprParser.IF) | (1 << ExprParser.WHILE) | (1 << ExprParser.ID))) != 0):
                        self.state = 38
                        self.stmt()
                        self.state = 43
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 44
                    self.match(ExprParser.LPAREN)


                pass

            elif la_ == 6:
                localctx = ExprParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.match(ExprParser.WHILE)
                self.state = 48
                self.expr(0)
                self.state = 49
                self.match(ExprParser.LPAREN)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.READ) | (1 << ExprParser.WRITE) | (1 << ExprParser.REPRO) | (1 << ExprParser.IF) | (1 << ExprParser.WHILE) | (1 << ExprParser.ID))) != 0):
                    self.state = 50
                    self.stmt()
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 56
                self.match(ExprParser.RPAREN)
                pass

            elif la_ == 7:
                localctx = ExprParser.ProcedureStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 58
                self.match(ExprParser.ID)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.PLUS) | (1 << ExprParser.MINUS) | (1 << ExprParser.NUMBER))) != 0):
                    self.state = 59
                    self.expr(0)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class UnaryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class ValueExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueExpr" ):
                return visitor.visitValueExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MUL(self):
            return self.getToken(ExprParser.MUL, 0)
        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)
        def MOD(self):
            return self.getToken(ExprParser.MOD, 0)
        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpr" ):
                return visitor.visitArithmeticExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)
        def NEQ(self):
            return self.getToken(ExprParser.NEQ, 0)
        def GT(self):
            return self.getToken(ExprParser.GT, 0)
        def GE(self):
            return self.getToken(ExprParser.GE, 0)
        def LT(self):
            return self.getToken(ExprParser.LT, 0)
        def LE(self):
            return self.getToken(ExprParser.LE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.PLUS, ExprParser.MINUS]:
                localctx = ExprParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 68
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ExprParser.PLUS or _la==ExprParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 69
                self.expr(5)
                pass
            elif token in [ExprParser.NUMBER]:
                localctx = ExprParser.ValueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70
                self.match(ExprParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 82
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ArithmeticExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 73
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 74
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.MUL) | (1 << ExprParser.DIV) | (1 << ExprParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 75
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ArithmeticExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 76
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 77
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.PLUS or _la==ExprParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 78
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.RelationalExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 79
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 80
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.EQ) | (1 << ExprParser.NEQ) | (1 << ExprParser.GT) | (1 << ExprParser.LT) | (1 << ExprParser.GE) | (1 << ExprParser.LE))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 81
                        self.expr(3)
                        pass

             
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LeftExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_leftExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeftExpr" ):
                return visitor.visitLeftExpr(self)
            else:
                return visitor.visitChildren(self)




    def leftExpr(self):

        localctx = ExprParser.LeftExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_leftExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




