grammar ExprRight;

expr
    : term '+' expr   # Add
    | term '-' expr   # Sub
    | term            # ToTerm
    ;

term
    : factor '*' term # Mul
    | factor '/' term # Div
    | factor          # ToFactor
    ;

factor
    : '(' expr ')'
    | NUMBER
    ;

NUMBER : [0-9]+;
WS : [ \t\r\n]+ -> skip;
