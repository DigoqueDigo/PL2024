# Calculator

Implementação de uma calculadora interativa que aceita expressões matemáticas com variáveis.

## Gramática

```
READ : ? VARIABLE

PRINT : ! EXPRESSION

ASSIGN : VARIABLE = EXPRESSION

EXPRESSION : TERM PLUS TERM
        | TERM MINUS TERM
        | TERM

TERM: FACTOR TIMES FACTOR
    | FACTOR DIVIDE FACTOR
    | FACTOR

FACTOR : NUMBER
    | VARIABLE
    | LPAREN EXPRESSION RPAREN
```

## Lookahead's

```
LK(READ) : {?}
LK(PRINT) : {!}
LK(ASSIGN) : {VARIABLE}
LK(EXPRESSION) : {NUMBER,VARIAVLE,LPAREN}
LK(TERM) : {NUMBER,VARIAVLE,LPAREN}
LK(FACTION) :{NUMBER,VARIAVLE,LPAREN}
```
