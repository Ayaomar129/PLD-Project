# Generated from MyLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete listener for a parse tree produced by MyLangParser.
class MyLangListener(ParseTreeListener):

    # Enter a parse tree produced by MyLangParser#program.
    def enterProgram(self, ctx:MyLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLangParser#program.
    def exitProgram(self, ctx:MyLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLangParser#stmts.
    def enterStmts(self, ctx:MyLangParser.StmtsContext):
        pass

    # Exit a parse tree produced by MyLangParser#stmts.
    def exitStmts(self, ctx:MyLangParser.StmtsContext):
        pass


    # Enter a parse tree produced by MyLangParser#stmt.
    def enterStmt(self, ctx:MyLangParser.StmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#stmt.
    def exitStmt(self, ctx:MyLangParser.StmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#operation.
    def enterOperation(self, ctx:MyLangParser.OperationContext):
        pass

    # Exit a parse tree produced by MyLangParser#operation.
    def exitOperation(self, ctx:MyLangParser.OperationContext):
        pass


    # Enter a parse tree produced by MyLangParser#var.
    def enterVar(self, ctx:MyLangParser.VarContext):
        pass

    # Exit a parse tree produced by MyLangParser#var.
    def exitVar(self, ctx:MyLangParser.VarContext):
        pass


    # Enter a parse tree produced by MyLangParser#opr.
    def enterOpr(self, ctx:MyLangParser.OprContext):
        pass

    # Exit a parse tree produced by MyLangParser#opr.
    def exitOpr(self, ctx:MyLangParser.OprContext):
        pass


    # Enter a parse tree produced by MyLangParser#operand.
    def enterOperand(self, ctx:MyLangParser.OperandContext):
        pass

    # Exit a parse tree produced by MyLangParser#operand.
    def exitOperand(self, ctx:MyLangParser.OperandContext):
        pass


    # Enter a parse tree produced by MyLangParser#conditionStmt.
    def enterConditionStmt(self, ctx:MyLangParser.ConditionStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#conditionStmt.
    def exitConditionStmt(self, ctx:MyLangParser.ConditionStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#cond.
    def enterCond(self, ctx:MyLangParser.CondContext):
        pass

    # Exit a parse tree produced by MyLangParser#cond.
    def exitCond(self, ctx:MyLangParser.CondContext):
        pass


    # Enter a parse tree produced by MyLangParser#compOp.
    def enterCompOp(self, ctx:MyLangParser.CompOpContext):
        pass

    # Exit a parse tree produced by MyLangParser#compOp.
    def exitCompOp(self, ctx:MyLangParser.CompOpContext):
        pass


    # Enter a parse tree produced by MyLangParser#expr.
    def enterExpr(self, ctx:MyLangParser.ExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#expr.
    def exitExpr(self, ctx:MyLangParser.ExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#forStmt.
    def enterForStmt(self, ctx:MyLangParser.ForStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#forStmt.
    def exitForStmt(self, ctx:MyLangParser.ForStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#step.
    def enterStep(self, ctx:MyLangParser.StepContext):
        pass

    # Exit a parse tree produced by MyLangParser#step.
    def exitStep(self, ctx:MyLangParser.StepContext):
        pass


    # Enter a parse tree produced by MyLangParser#block.
    def enterBlock(self, ctx:MyLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MyLangParser#block.
    def exitBlock(self, ctx:MyLangParser.BlockContext):
        pass



del MyLangParser