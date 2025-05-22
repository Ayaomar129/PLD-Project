grammar MyLang;

// ===== Parser Rules =====

program : stmts ;

stmts : stmt+ ;

stmt
    : operation
    | conditionStmt
    | forStmt
    ;

operation : var ASSIGN opr ;

var : ID ;

opr
    : operand PLUS operand
    | operand MINUS operand
    | operand MUL operand
    | operand DIV operand
    ;

operand : ID | NUMBER ;

conditionStmt
    : IF cond block
    | IF cond block ELSE stmt
    ;

cond : expr compOp expr ;

compOp : LT | GT | EQ | NEQ ;

expr
    : LPAREN expr RPAREN
    | ID
    | NUMBER
    ;

forStmt
    : FOR operation COMMA cond COMMA step COLON block
    ;

step
    : INCR ID
    | ID INCR
    | DECR ID
    | ID DECR
    | operation
    ;

block : LBRACE stmt+ RBRACE ;

// ===== Lexer Rules =====

ASSIGN  : '=' ;
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;

EQ      : '==' ;
NEQ     : '!=' ;
LT      : '<' ;
GT      : '>' ;

INCR    : '++' ;
DECR    : '--' ;

LBRACE  : '{' ;
RBRACE  : '}' ;
COMMA   : ',' ;
COLON   : ':' ;

IF      : 'if' ;
ELSE    : 'else' ;
FOR     : 'for' ;

LPAREN  : '(' ;
RPAREN  : ')' ;

ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER  : [0-9]+ ('.' [0-9]+)? ;
WS      : [ \t\r\n]+ -> skip ;
