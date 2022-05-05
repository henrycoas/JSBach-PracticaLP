grammar jsbach;

/// Parser Rules (part gramàtica)

// per processar el final de l'arxiu
// un arxiu es un conjunt de procediments
root 
    : procedureDef+ EOF ;

procedureDef
    : ID paramsListDef LPAREN stmt* RPAREN
    ;

paramsListDef
    : ID*
    ;

stmt 
    : READ ID                                                   # readStmt
    | WRITE expr+                                               # writeStmt
    | REPRO ident                                               # reproStmt
    | IF expr LPAREN stmt* RPAREN (ELSE RPAREN stmt* LPAREN)?   # ifStmt
    | WHILE expr LPAREN stmt* RPAREN                            # whileStmt
    | ID expr*                                                  # procCallStmt
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
    | ID                                        # idExpr
    ;

leftExpr 
    : ID                        #LeftExprId
    ;

ident
    : ID
    ;

/// Lexer Rules (part lèxica)

ASSIGN  : '<-' ;

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

fragment
DIGIT   : '0'..'9' ;
fragment
LETTER  : [a-zA-Z] ;
NUMBER  : (DIGIT)+ ;
BOOLEAN : ('0' | '1') ;
ID      : LETTER (LETTER | DIGIT)* ;

fragment
ESC_SEQ : '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;

// Strings (in quotes) with escape sequences
STRING  : '"' ( ESC_SEQ | ~('\\'|'"') )* '"' ;

WORD    : [a-zA-Z\u0080-\u00FF]+ ;

WS      : [ \t\n]+ -> skip ;