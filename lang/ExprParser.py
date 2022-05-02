# Generated from Expr.g by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\6\3\27\n\3\r\3\16\3\30\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\7\3!\n\3\f\3\16\3$\13\3\3\3\3\3")
        buf.write("\3\3\3\3\7\3*\n\3\f\3\16\3-\13\3\3\3\5\3\60\n\3\3\3\3")
        buf.write("\3\3\3\3\3\7\3\66\n\3\f\3\16\39\13\3\3\3\3\3\3\3\3\3\7")
        buf.write("\3?\n\3\f\3\16\3B\13\3\3\3\5\3E\n\3\3\4\3\4\3\4\3\4\5")
        buf.write("\4K\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4V\n\4\f")
        buf.write("\4\16\4Y\13\4\3\5\3\5\3\5\2\3\6\6\2\4\6\b\2\5\3\2\n\13")
        buf.write("\3\2\f\16\3\2\4\t\2k\2\n\3\2\2\2\4D\3\2\2\2\6J\3\2\2\2")
        buf.write("\bZ\3\2\2\2\n\13\5\6\4\2\13\f\7\2\2\3\f\3\3\2\2\2\r\16")
        buf.write("\7\34\2\2\16\17\7\3\2\2\17E\5\6\4\2\20\21\7\17\2\2\21")
        buf.write("E\7\34\2\2\22\26\7\20\2\2\23\27\5\6\4\2\24\27\7\34\2\2")
        buf.write("\25\27\7\35\2\2\26\23\3\2\2\2\26\24\3\2\2\2\26\25\3\2")
        buf.write("\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31E\3\2")
        buf.write("\2\2\32\33\7\21\2\2\33E\7\34\2\2\34\35\7\22\2\2\35\36")
        buf.write("\5\6\4\2\36\"\7\27\2\2\37!\5\4\3\2 \37\3\2\2\2!$\3\2\2")
        buf.write("\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\"\3\2\2\2%/\7\30\2")
        buf.write("\2&\'\7\23\2\2\'+\7\30\2\2(*\5\4\3\2)(\3\2\2\2*-\3\2\2")
        buf.write("\2+)\3\2\2\2+,\3\2\2\2,.\3\2\2\2-+\3\2\2\2.\60\7\27\2")
        buf.write("\2/&\3\2\2\2/\60\3\2\2\2\60E\3\2\2\2\61\62\7\24\2\2\62")
        buf.write("\63\5\6\4\2\63\67\7\27\2\2\64\66\5\4\3\2\65\64\3\2\2\2")
        buf.write("\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28:\3\2\2\29\67\3")
        buf.write("\2\2\2:;\7\30\2\2;E\3\2\2\2<@\7\34\2\2=?\5\6\4\2>=\3\2")
        buf.write("\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2AE\3\2\2\2B@\3\2\2\2")
        buf.write("CE\7\34\2\2D\r\3\2\2\2D\20\3\2\2\2D\22\3\2\2\2D\32\3\2")
        buf.write("\2\2D\34\3\2\2\2D\61\3\2\2\2D<\3\2\2\2DC\3\2\2\2E\5\3")
        buf.write("\2\2\2FG\b\4\1\2GH\t\2\2\2HK\5\6\4\7IK\7\33\2\2JF\3\2")
        buf.write("\2\2JI\3\2\2\2KW\3\2\2\2LM\f\6\2\2MN\t\3\2\2NV\5\6\4\7")
        buf.write("OP\f\5\2\2PQ\t\2\2\2QV\5\6\4\6RS\f\4\2\2ST\t\4\2\2TV\5")
        buf.write("\6\4\5UL\3\2\2\2UO\3\2\2\2UR\3\2\2\2VY\3\2\2\2WU\3\2\2")
        buf.write("\2WX\3\2\2\2X\7\3\2\2\2YW\3\2\2\2Z[\7\34\2\2[\t\3\2\2")
        buf.write("\2\r\26\30\"+/\67@DJUW")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "'='", "'/='", "'>'", "'<'", "'>='", 
                     "'<='", "'+'", "'-'", "'*'", "'/'", "'%'", "'<?>'", 
                     "'<!>'", "'<:>'", "'if'", "'else'", "'while'", "'<<'", 
                     "'8<'", "'|:'", "':|'" ]

    symbolicNames = [ "<INVALID>", "ASSIGN", "EQ", "NEQ", "GT", "LT", "GE", 
                      "LE", "PLUS", "MINUS", "MUL", "DIV", "MOD", "READ", 
                      "WRITE", "REPRO", "IF", "ELSE", "WHILE", "CONCAT", 
                      "CUT", "LPAREN", "RPAREN", "DIGIT", "LETTER", "NUMBER", 
                      "ID", "STRING", "WS" ]

    RULE_root = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_leftExpr = 3

    ruleNames =  [ "root", "stmt", "expr", "leftExpr" ]

    EOF = Token.EOF
    ASSIGN=1
    EQ=2
    NEQ=3
    GT=4
    LT=5
    GE=6
    LE=7
    PLUS=8
    MINUS=9
    MUL=10
    DIV=11
    MOD=12
    READ=13
    WRITE=14
    REPRO=15
    IF=16
    ELSE=17
    WHILE=18
    CONCAT=19
    CUT=20
    LPAREN=21
    RPAREN=22
    DIGIT=23
    LETTER=24
    NUMBER=25
    ID=26
    STRING=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def READ(self):
            return self.getToken(ExprParser.READ, 0)

        def WRITE(self):
            return self.getToken(ExprParser.WRITE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.STRING)
            else:
                return self.getToken(ExprParser.STRING, i)

        def REPRO(self):
            return self.getToken(ExprParser.REPRO, 0)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

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

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_stmt




    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.match(ExprParser.ID)
                self.state = 12
                self.match(ExprParser.ASSIGN)
                self.state = 13
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(ExprParser.READ)
                self.state = 15
                self.match(ExprParser.ID)
                pass

            elif la_ == 3:
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
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(ExprParser.REPRO)
                self.state = 25
                self.match(ExprParser.ID)
                pass

            elif la_ == 5:
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

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 65
                self.match(ExprParser.ID)
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
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def MUL(self):
            return self.getToken(ExprParser.MUL, 0)

        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)

        def MOD(self):
            return self.getToken(ExprParser.MOD, 0)

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

        def getRuleIndex(self):
            return ExprParser.RULE_expr



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
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.PLUS, ExprParser.MINUS]:
                self.state = 69
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ExprParser.PLUS or _la==ExprParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self.expr(5)
                pass
            elif token in [ExprParser.NUMBER]:
                self.state = 71
                self.match(ExprParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 83
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 75
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.MUL) | (1 << ExprParser.DIV) | (1 << ExprParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 76
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 78
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.PLUS or _la==ExprParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 79
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 81
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.EQ) | (1 << ExprParser.NEQ) | (1 << ExprParser.GT) | (1 << ExprParser.LT) | (1 << ExprParser.GE) | (1 << ExprParser.LE))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 82
                        self.expr(3)
                        pass

             
                self.state = 87
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




    def leftExpr(self):

        localctx = ExprParser.LeftExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_leftExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
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
         




