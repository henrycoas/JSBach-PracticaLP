grammar Expr;

// per processar el final de l'arxiu
root : expr EOF ;

expr : expr ADD expr
    | NUMBER
    ;

RET     : 'return' ;
LPAREN  : '(' ;
RPAREN  : ')' ;
ADD     : '+' ;
SUB     : '-' ;
MUL     : '*' ;
DIV     : ';' ;
DIGIT   : '0'..'9' ;
LETTER  : [a-zA-Z] ;
NUMBER  : (DIGIT)+ ;
IDENT   : LETTER (LETTER | DIGIT)* ;
WS      : [ \t\n]+ -> skip ;