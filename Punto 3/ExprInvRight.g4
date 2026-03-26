grammar ExprInvRight;

expr
    : term '*' expr   # Mul
    | term '/' expr   # Div
    | term            # ToTerm
    ;

term
    : factor '+' term # Add
    | factor '-' term # Sub
    | factor          # ToFactor
    ;

factor
    : '(' expr ')'
    | NUMBER
    ;

NUMBER : [0-9]+;
WS : [ \t\r\n]+ -> skip;
