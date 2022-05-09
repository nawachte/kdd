%option noyywrap
%{
#include <stdio.h>
#include <math.h>
int line_num = 1;
int num_comments = 0;
%}
%x IN_COMMENT
%%

<IN_COMMENT>{
[^*/]+	{printf("\n%d	%s",++num_comments,yytext);}
"*"	{}
"*/"    {BEGIN(INITIAL);}
}
([\"].*[\"])	{}
"/*"    {BEGIN(IN_COMMENT);}
\n	{}
.
%%
int main(){
	yylex();
	printf("\n\n%d comments found.\n", num_comments);
	return 0;
}