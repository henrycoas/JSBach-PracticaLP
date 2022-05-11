grammar jsbach;

/// Parser Rules (part gramàtica)

// per processar el final de l'arxiu
// un arxiu es un conjunt de procediments
root 
    : procedureDef+ EOF ;

procedureDef
    : PROCID paramsListDef LPAREN stmt* RPAREN
    ;

paramsListDef
    : VARID*
    ;

paramsListCall
    : expr*
    ;

stmt 
    : READ VARID                                                # readStmt
    | WRITE expr+                                               # writeStmt
    | REPRO expr                                              # reproStmt
    | IF expr LPAREN stmt* RPAREN (ELSE LPAREN stmt* RPAREN)?   # ifStmt
    | WHILE expr LPAREN stmt* RPAREN                            # whileStmt
    | PROCID paramsListCall                                              # procCallStmt
    | leftExpr ASSIGN expr                                      # assignStmt
    ;

// per processar cada instrucció
expr 
    : '(' expr ')'                              # parenthesesExpr
    | op=(PLUS|MINUS) expr                      # unaryExpr   
    | expr op=(MUL|DIV|MOD) expr                # arithmeticExpr
    | expr op=(PLUS|MINUS) expr                 # arithmeticExpr
    | expr op=(EQ|NEQ|GT|GE|LT|LE) expr         # relationalExpr
    | (NUMBER | STRING | BOOLEAN)               # valueExpr
    | (ident | array)                           # idExpr
    ;

leftExpr 
    : VARID
    ;

ident
    : (VARID | NOTE)
    ;

array
    : '{' (VARID* | NOTE*) '}'
    ;

/// Lexer Rules (part lèxica)

ASSIGN  : '<-' ;

READ    : '<?>' ;
WRITE   : '<!>' ;
REPRO   : '<:>' ;

IF      : 'if' ;
ELSE    : 'else' ;
WHILE   : 'while' ;

// ---Operacions amb llistes
CONCAT  : '<<' ;
CUT     : '8<' ;
LENGTH  : '#' ;

LPAREN  : '|:' ;
RPAREN  : ':|' ;

// ---Operadors relacionals
EQ      : '=' ;
NEQ     : '/=' ;
GT      : '>' ;
LT      : '<' ;
GE      : '>=' ;
LE      : '<=' ;

// ---Operadors aritmètics
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
MOD     : '%' ;

fragment
NUMNOTE : '0'..'8' ;
NOTE    : ('A'|'B'|'C'|'D'|'E'|'F'|'G') NUMNOTE?;

fragment
DIGIT   : '0'..'9' ;
fragment
LETTER  : [a-zA-Z] ;
fragment
LOWERCASE  : [a-z] ;
fragment
UPPERCASE  : [A-Z] ;

NUMBER  : (DIGIT)+ ;
BOOLEAN : ('0' | '1') ;
PROCID  : UPPERCASE (LETTER | DIGIT)* ;
VARID   : LOWERCASE (LETTER | DIGIT)* ;

fragment
ESC_SEQ : '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;

// Strings (in quotes) with escape sequences
STRING  : '"' ( ESC_SEQ | ~('\\'|'"') )* '"' ;

WORD    : [a-zA-Z\u0080-\u00FF]+ ;

WS      : [ \t\n]+ -> skip ;

COMMENT
    : '~~~' ~( '\r' | '\n' )* '~~~' -> skip
    ;