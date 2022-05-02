grammar Expr;

// per processar el final de l'arxiu
root 
    : expr EOF ;

stmt 
    : ID ASSIGN expr                                            # assignStmt
    | READ ID                                                   # readStmt
    | WRITE (expr | ID | STRING)+                               # writeStmt
    | REPRO ID                                                  # reproStmt
    | IF expr LPAREN stmt* RPAREN (ELSE RPAREN stmt* LPAREN)?   # ifStmt
    | WHILE expr LPAREN stmt* RPAREN                            # whileStmt
    | ID expr*                                                  # procedureStmt
    ;

// per processar cada instrucció
expr 
    : op=(PLUS|MINUS) expr                  
    | expr op=(MUL|DIV|MOD) expr          
    | expr op=(PLUS|MINUS) expr           
    | expr op=(EQ|NEQ|GT|GE|LT|LE) expr
    | NUMBER
    ;

leftExpr 
    : ID
    ;

ASSIGN  : '<-' ;

EQ      : '=' ;
NEQ     : '/=' ;
GT      : '>' ;
LT      : '<' ;
GE      : '>=' ;
LE      : '<=' ;

PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
MOD     : '%' ;

READ    : '<?>' ;
WRITE   : '<!>' ;
REPRO   : '<:>' ;

IF      : 'if' ;
ELSE    : 'else' ;
WHILE   : 'while' ;

CONCAT  : '<<' ;
CUT     : '8<' ;

LPAREN  : '|:' ;
RPAREN  : ':|' ;

DIGIT   : '0'..'9' ;
LETTER  : [a-zA-Z] ;
NUMBER  : (DIGIT)+ ;
ID      : LETTER (LETTER | DIGIT)* ;

fragment
ESC_SEQ : '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;

// Strings (in quotes) with escape sequences
STRING  : '"' ( ESC_SEQ | ~('\\'|'"') )* '"' ;

WS      : [ \t\n]+ -> skip ;