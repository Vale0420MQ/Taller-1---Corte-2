grammar ExprLeft;

expr
    : expr '+' term   # Add
    | expr '-' term   # Sub
    | term            # ToTerm
    ;

term
    : term '*' factor # Mul
    | term '/' factor # Div
    | factor          # ToFactor
    ;

factor
    : '(' expr ')'
    | NUMBER
    ;

NUMBER : [0-9]+;
WS : [ \t\r\n]+ -> skip;
