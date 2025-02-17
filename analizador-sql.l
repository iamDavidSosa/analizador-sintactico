%{
#include <stdio.h>
#include "parser.tab.h"

int yywrap(void);
void analizarSQL(const char* texto);
%}

DIGIT      [0-9]+
ID         [a-zA-Z_][a-zA-Z0-9_]*
STRING     '\'([^']|'')*'
COMMENT    "--".*
BLOCK_COMMENT  "/\*"([^*]|\*+[^*/])*"\*/"

%%

[ \t\r\n]+      ;

[Ss][Ee][Ll][Ee][Cc][Tt]      { printf("TOKEN: SELECT\n"); return SELECT; }
[Ff][Rr][Oo][Mm]              { printf("TOKEN: FROM\n"); return FROM; }
[Ww][Hh][Ee][Rr][Ee]          { printf("TOKEN: WHERE\n"); return WHERE; }
[Ii][Nn][Ss][Ee][Rr][Tt]      { printf("TOKEN: INSERT\n"); return INSERT; }
[Uu][Pp][Dd][Aa][Tt][Ee]      { printf("TOKEN: UPDATE\n"); return UPDATE; }
[Dd][Ee][Ll][Ee][Tt][Ee]      { printf("TOKEN: DELETE\n"); return DELETE; }

{DIGIT}      { printf("TOKEN: NUMERO (%s)\n", yytext); yylval.num = atoi(yytext); return NUMERO; }
{STRING}     { printf("TOKEN: TEXTO (%s)\n", yytext); yylval.str = strdup(yytext); return TEXTO; }

"="          { printf("TOKEN: IGUAL\n"); return IGUAL; }
"*"          { printf("TOKEN: ALL\n"); return ALL; }
"<>"         { printf("TOKEN: DIFERENTE_DE\n"); return DIFERENTE_DE; }
">"          { printf("TOKEN: MAYOR\n"); return MAYOR; }
"<"          { printf("TOKEN: MENOR\n"); return MENOR; }
[Aa][Nn][Dd] { printf("TOKEN: AND\n"); return AND; }
[Oo][Rr]     { printf("TOKEN: OR\n"); return OR; }
[Ll][Ii][Kk][Ee] { printf("TOKEN: PARECIDO_A\n"); return PARECIDO_A; }

{COMMENT}     ;
{BLOCK_COMMENT} ;

{ID}          { printf("TOKEN: IDENTIFICADOR (%s)\n", yytext); yylval.str = strdup(yytext); return IDENTIFICADOR; }

.             { printf("TOKEN: OTROS (%s)\n", yytext); return yytext[0]; }

%%

int yywrap(void) { return 1; }

void analizarSQL(const char* texto) {
    printf("Iniciando análisis...\n");
    yy_scan_string(texto);
    yylex();
    yy_delete_buffer(YY_CURRENT_BUFFER);
    printf("Análisis completado.\n");
}