%{
#include <stdio.h>
#include <math.h>
int ip_count = 0;
int line_count = 1;
int char_count = 1;
%}
ipv4	[0-9]+"."[0-9]+"."[0-9]+"."[0-9]+
%%
{ipv4}	{ip_count++; printf("\nIP found on line %d at character %d\n",line_count,char_count); char_count++;}
\n      {line_count++; char_count = 1;}
.	char_count++;

%%
int yywrap(){}
int main(){
	yylex();
	printf("\nTotal number of ip addresses: %d\n", ip_count);
	return 0;
}