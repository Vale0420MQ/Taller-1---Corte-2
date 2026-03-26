grammar ExprInvLeft;

expr
    : expr '*' term   # Mul
    | expr '/' term   # Div
    | term            # ToTerm
    ;

term
    : term '+' factor # Add
    | term '-' factor # Sub
    | factor          # ToFactor
    ;

factor
    : '(' expr ')'
    | NUMBER
    ;

NUMBER : [0-9]+;
WS : [ \t\r\n]+ -> skip;
