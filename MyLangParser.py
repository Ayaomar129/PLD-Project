# Generated from MyLang.g4 by ANTLR 4.13.2
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
        4,1,23,121,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,1,4,1,32,8,1,11,1,12,1,33,1,2,1,2,1,2,3,2,39,8,2,1,3,1,
        3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,3,5,63,8,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,3,7,77,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,
        10,1,10,1,10,3,10,91,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,111,8,12,
        1,13,1,13,4,13,115,8,13,11,13,12,13,116,1,13,1,13,1,13,0,0,14,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,0,2,1,0,21,22,1,0,6,9,120,0,28,
        1,0,0,0,2,31,1,0,0,0,4,38,1,0,0,0,6,40,1,0,0,0,8,44,1,0,0,0,10,62,
        1,0,0,0,12,64,1,0,0,0,14,76,1,0,0,0,16,78,1,0,0,0,18,82,1,0,0,0,
        20,90,1,0,0,0,22,92,1,0,0,0,24,110,1,0,0,0,26,112,1,0,0,0,28,29,
        3,2,1,0,29,1,1,0,0,0,30,32,3,4,2,0,31,30,1,0,0,0,32,33,1,0,0,0,33,
        31,1,0,0,0,33,34,1,0,0,0,34,3,1,0,0,0,35,39,3,6,3,0,36,39,3,14,7,
        0,37,39,3,22,11,0,38,35,1,0,0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,5,
        1,0,0,0,40,41,3,8,4,0,41,42,5,1,0,0,42,43,3,10,5,0,43,7,1,0,0,0,
        44,45,5,21,0,0,45,9,1,0,0,0,46,47,3,12,6,0,47,48,5,2,0,0,48,49,3,
        12,6,0,49,63,1,0,0,0,50,51,3,12,6,0,51,52,5,3,0,0,52,53,3,12,6,0,
        53,63,1,0,0,0,54,55,3,12,6,0,55,56,5,4,0,0,56,57,3,12,6,0,57,63,
        1,0,0,0,58,59,3,12,6,0,59,60,5,5,0,0,60,61,3,12,6,0,61,63,1,0,0,
        0,62,46,1,0,0,0,62,50,1,0,0,0,62,54,1,0,0,0,62,58,1,0,0,0,63,11,
        1,0,0,0,64,65,7,0,0,0,65,13,1,0,0,0,66,67,5,16,0,0,67,68,3,16,8,
        0,68,69,3,26,13,0,69,77,1,0,0,0,70,71,5,16,0,0,71,72,3,16,8,0,72,
        73,3,26,13,0,73,74,5,17,0,0,74,75,3,4,2,0,75,77,1,0,0,0,76,66,1,
        0,0,0,76,70,1,0,0,0,77,15,1,0,0,0,78,79,3,20,10,0,79,80,3,18,9,0,
        80,81,3,20,10,0,81,17,1,0,0,0,82,83,7,1,0,0,83,19,1,0,0,0,84,85,
        5,19,0,0,85,86,3,20,10,0,86,87,5,20,0,0,87,91,1,0,0,0,88,91,5,21,
        0,0,89,91,5,22,0,0,90,84,1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,
        21,1,0,0,0,92,93,5,18,0,0,93,94,3,6,3,0,94,95,5,14,0,0,95,96,3,16,
        8,0,96,97,5,14,0,0,97,98,3,24,12,0,98,99,5,15,0,0,99,100,3,26,13,
        0,100,23,1,0,0,0,101,102,5,10,0,0,102,111,5,21,0,0,103,104,5,21,
        0,0,104,111,5,10,0,0,105,106,5,11,0,0,106,111,5,21,0,0,107,108,5,
        21,0,0,108,111,5,11,0,0,109,111,3,6,3,0,110,101,1,0,0,0,110,103,
        1,0,0,0,110,105,1,0,0,0,110,107,1,0,0,0,110,109,1,0,0,0,111,25,1,
        0,0,0,112,114,5,12,0,0,113,115,3,4,2,0,114,113,1,0,0,0,115,116,1,
        0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,5,
        13,0,0,119,27,1,0,0,0,7,33,38,62,76,90,110,116
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "'=='", 
                     "'!='", "'<'", "'>'", "'++'", "'--'", "'{'", "'}'", 
                     "','", "':'", "'if'", "'else'", "'for'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
                      "EQ", "NEQ", "LT", "GT", "INCR", "DECR", "LBRACE", 
                      "RBRACE", "COMMA", "COLON", "IF", "ELSE", "FOR", "LPAREN", 
                      "RPAREN", "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_stmts = 1
    RULE_stmt = 2
    RULE_operation = 3
    RULE_var = 4
    RULE_opr = 5
    RULE_operand = 6
    RULE_conditionStmt = 7
    RULE_cond = 8
    RULE_compOp = 9
    RULE_expr = 10
    RULE_forStmt = 11
    RULE_step = 12
    RULE_block = 13

    ruleNames =  [ "program", "stmts", "stmt", "operation", "var", "opr", 
                   "operand", "conditionStmt", "cond", "compOp", "expr", 
                   "forStmt", "step", "block" ]

    EOF = Token.EOF
    ASSIGN=1
    PLUS=2
    MINUS=3
    MUL=4
    DIV=5
    EQ=6
    NEQ=7
    LT=8
    GT=9
    INCR=10
    DECR=11
    LBRACE=12
    RBRACE=13
    COMMA=14
    COLON=15
    IF=16
    ELSE=17
    FOR=18
    LPAREN=19
    RPAREN=20
    ID=21
    NUMBER=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmts(self):
            return self.getTypedRuleContext(MyLangParser.StmtsContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MyLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.stmts()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StmtContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmts" ):
                listener.enterStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmts" ):
                listener.exitStmts(self)




    def stmts(self):

        localctx = MyLangParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.stmt()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2424832) != 0)):
                    break

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

        def operation(self):
            return self.getTypedRuleContext(MyLangParser.OperationContext,0)


        def conditionStmt(self):
            return self.getTypedRuleContext(MyLangParser.ConditionStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MyLangParser.ForStmtContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = MyLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.operation()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.conditionStmt()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.forStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(MyLangParser.VarContext,0)


        def ASSIGN(self):
            return self.getToken(MyLangParser.ASSIGN, 0)

        def opr(self):
            return self.getTypedRuleContext(MyLangParser.OprContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = MyLangParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.var()
            self.state = 41
            self.match(MyLangParser.ASSIGN)
            self.state = 42
            self.opr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = MyLangParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(MyLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.OperandContext)
            else:
                return self.getTypedRuleContext(MyLangParser.OperandContext,i)


        def PLUS(self):
            return self.getToken(MyLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MyLangParser.MINUS, 0)

        def MUL(self):
            return self.getToken(MyLangParser.MUL, 0)

        def DIV(self):
            return self.getToken(MyLangParser.DIV, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_opr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpr" ):
                listener.enterOpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpr" ):
                listener.exitOpr(self)




    def opr(self):

        localctx = MyLangParser.OprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_opr)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.operand()
                self.state = 47
                self.match(MyLangParser.PLUS)
                self.state = 48
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.operand()
                self.state = 51
                self.match(MyLangParser.MINUS)
                self.state = 52
                self.operand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.operand()
                self.state = 55
                self.match(MyLangParser.MUL)
                self.state = 56
                self.operand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.operand()
                self.state = 59
                self.match(MyLangParser.DIV)
                self.state = 60
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def NUMBER(self):
            return self.getToken(MyLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)




    def operand(self):

        localctx = MyLangParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MyLangParser.IF, 0)

        def cond(self):
            return self.getTypedRuleContext(MyLangParser.CondContext,0)


        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def ELSE(self):
            return self.getToken(MyLangParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(MyLangParser.StmtContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_conditionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionStmt" ):
                listener.enterConditionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionStmt" ):
                listener.exitConditionStmt(self)




    def conditionStmt(self):

        localctx = MyLangParser.ConditionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditionStmt)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(MyLangParser.IF)
                self.state = 67
                self.cond()
                self.state = 68
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(MyLangParser.IF)
                self.state = 71
                self.cond()
                self.state = 72
                self.block()
                self.state = 73
                self.match(MyLangParser.ELSE)
                self.state = 74
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExprContext,i)


        def compOp(self):
            return self.getTypedRuleContext(MyLangParser.CompOpContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = MyLangParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.expr()
            self.state = 79
            self.compOp()
            self.state = 80
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(MyLangParser.LT, 0)

        def GT(self):
            return self.getToken(MyLangParser.GT, 0)

        def EQ(self):
            return self.getToken(MyLangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MyLangParser.NEQ, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_compOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompOp" ):
                listener.enterCompOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompOp" ):
                listener.exitCompOp(self)




    def compOp(self):

        localctx = MyLangParser.CompOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MyLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def NUMBER(self):
            return self.getToken(MyLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = MyLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(MyLangParser.LPAREN)
                self.state = 85
                self.expr()
                self.state = 86
                self.match(MyLangParser.RPAREN)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(MyLangParser.ID)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.match(MyLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MyLangParser.FOR, 0)

        def operation(self):
            return self.getTypedRuleContext(MyLangParser.OperationContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.COMMA)
            else:
                return self.getToken(MyLangParser.COMMA, i)

        def cond(self):
            return self.getTypedRuleContext(MyLangParser.CondContext,0)


        def step(self):
            return self.getTypedRuleContext(MyLangParser.StepContext,0)


        def COLON(self):
            return self.getToken(MyLangParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)




    def forStmt(self):

        localctx = MyLangParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MyLangParser.FOR)
            self.state = 93
            self.operation()
            self.state = 94
            self.match(MyLangParser.COMMA)
            self.state = 95
            self.cond()
            self.state = 96
            self.match(MyLangParser.COMMA)
            self.state = 97
            self.step()
            self.state = 98
            self.match(MyLangParser.COLON)
            self.state = 99
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCR(self):
            return self.getToken(MyLangParser.INCR, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def DECR(self):
            return self.getToken(MyLangParser.DECR, 0)

        def operation(self):
            return self.getTypedRuleContext(MyLangParser.OperationContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_step

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStep" ):
                listener.enterStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStep" ):
                listener.exitStep(self)




    def step(self):

        localctx = MyLangParser.StepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_step)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(MyLangParser.INCR)
                self.state = 102
                self.match(MyLangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(MyLangParser.ID)
                self.state = 104
                self.match(MyLangParser.INCR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.match(MyLangParser.DECR)
                self.state = 106
                self.match(MyLangParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.match(MyLangParser.ID)
                self.state = 108
                self.match(MyLangParser.DECR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 109
                self.operation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MyLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MyLangParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StmtContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = MyLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(MyLangParser.LBRACE)
            self.state = 114 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 113
                self.stmt()
                self.state = 116 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2424832) != 0)):
                    break

            self.state = 118
            self.match(MyLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





