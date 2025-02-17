%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex(void);

extern FILE *yyin;
%}

%token SELECT FROM WHERE INSERT UPDATE DELETE
%token NUMERO TEXTO IDENTIFICADOR
%token IGUAL DIFERENTE_DE MAYOR MENOR AND OR PARECIDO_A ALL

%union {
    int num;
    char *str;
}

%%

query: SELECT column_list FROM IDENTIFICADOR
     {
         printf("Consulta válida: SELECT ... FROM ...\n");
     }
     | INSERT INTO IDENTIFICADOR VALUES '(' value_list ')'
     {
         printf("Consulta válida: INSERT INTO ... VALUES ...\n");
     }
     | UPDATE IDENTIFICADOR SET assignment_list WHERE condition
     {
         printf("Consulta válida: UPDATE ... SET ... WHERE ...\n");
     }
     | DELETE FROM IDENTIFICADOR WHERE condition
     {
         printf("Consulta válida: DELETE FROM ... WHERE ...\n");
     }
     ;

column_list: IDENTIFICADOR
           | column_list ',' IDENTIFICADOR
           ;

value_list: TEXTO
          | NUMERO
          | value_list ',' TEXTO
          | value_list ',' NUMERO
          ;

assignment_list: IDENTIFICADOR '=' TEXTO
               | IDENTIFICADOR '=' NUMERO
               | assignment_list ',' IDENTIFICADOR '=' TEXTO
               | assignment_list ',' IDENTIFICADOR '=' NUMERO
               ;

condition: IDENTIFICADOR IGUAL TEXTO
         | IDENTIFICADOR DIFERENTE_DE TEXTO
         | IDENTIFICADOR MAYOR NUMERO
         | IDENTIFICADOR MENOR NUMERO
         | condition AND condition
         | condition OR condition
         ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error de sintaxis: %s\n", s);
}

int main(int argc, char **argv) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            perror("Error al abrir el archivo");
            return 1;
        }
    }

    yyparse();

    if (argc > 1) {
        fclose(yyin);
    }

    return 0;
}