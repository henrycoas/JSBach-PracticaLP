grammar jsbach;

/// Parser Rules (part gramàtica)

// per processar el final de l'arxiu
// un arxiu es un conjunt de procediments
root 
    : procedureDef+ EOF 
    ;

procedureDef
    : PROCID paramsListDef LPAREN stmts RPAREN
    ;

stmts
    : stmt*
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
    | PLAY expr                                                 # playStmt
    | CANONPLAY NUMBER '>' expr                                 # canonPlayStmt
    | IF expr LPAREN stmts RPAREN (ELSE LPAREN stmts RPAREN)?   # ifStmt
    | WHILE expr LPAREN stmts RPAREN                            # whileStmt
    | PROCID paramsListCall                                     # procCallStmt
    | leftExpr ASSIGN expr                                      # assignStmt
    | VARID CONCAT expr                                         # concatStmt
    | CUT VARID '[' expr ']'                                    # cutStmt
    ;

// per processar cada instrucció
expr 
    : '(' expr ')'                              # parenthesesExpr
    | op=(PLUS|MINUS) expr                      # unaryExpr   
    | expr op=(MUL|DIV|MOD) expr                # arithmeticExpr
    | expr op=(PLUS|MINUS) expr                 # arithmeticExpr
    | expr op=(EQ|NEQ|GT|GE|LT|LE) expr         # relationalExpr
    | (NUMBER | STRING | BOOLEAN)               # valueExpr
    | VARID '[' expr ']'                        # arrayAccessExpr
    | ident                                     # idExpr
    | array                                     # arrayExpr
    | LENGTH VARID                              # arrayLengthExpr
    ;

leftExpr 
    : VARID
    ;

ident
    : (VARID | NOTE)
    ;

array
    : '{' (NUMBER | NOTE)* '}'
    ;


/// Lexer Rules (part lèxica)

ASSIGN  : '<-' ;

READ    : '<?>' ;
WRITE   : '<!>' ;
PLAY    : '<:>' ;
CANONPLAY : '<::' ;

// ---Instruccions condicionals i iteratives
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

// ---Altres construccions
fragment
NUMNOTE : '0'..'8' ;
NOTE    : ('A'|'B'|'C'|'D'|'E'|'F'|'G') NUMNOTE?;

fragment
DIGIT   : [0-9] ;
fragment
WORD    : [a-zA-Z\u0080-\u00FF]+ ;
fragment
LOWERCASE  : [a-z] ;
fragment
UPPERCASE  : [A-Z] ;

NUMBER  : (DIGIT)+ ;
BOOLEAN : ('0' | '1') ;
PROCID  : UPPERCASE (WORD | DIGIT | '-' | '_')* ;
VARID   : LOWERCASE (WORD | DIGIT | '-' | '_')* ;

fragment
ESC_SEQ : '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;

// Strings (in quotes) with escape sequences
STRING  : '"' ( ESC_SEQ | ~('\\'|'"') )* '"' ;

WS      : [ \t\n]+ -> skip ;

COMMENT
    : '~~~' ~( '\r' | '\n' )* '~~~' -> skip
    ;