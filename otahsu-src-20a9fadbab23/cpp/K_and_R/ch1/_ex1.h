#ifndef __EX1__
#define __EX1__
#include "wc.h"

/***********************************
* ex1-3 
***********************************/
//TODO: "no declaration & just definition" is OK.
//void print_Fahrenheit_Celsius_table(void);
void print_Fahrenheit_Celsius_table()
{
    float fahr, celsius;
    int lower, upper, step;
    char header[50];
    sprintf(header, "Degree list of\n%s %s\n", "Fahrenheit", "Celsius");
    printf(header); 

    lower = 0;
    upper = 300;
    step = 20;
    fahr = lower;
    while( fahr <= upper )
    {
        celsius = (5. / 9.)*(fahr - 32.);
        printf("%10.0f %7.1f\n", fahr, celsius); //"%6.1f" is at-least 6-char wide and 1 after decimal pt.
        fahr += step;
    }
}
/***********************************
* ex1-5
***********************************/
void print_reverse_Fahrenheit_Celsius_table()
{
    float fahr, celsius;
    int lower, upper, step;
    char header[50];
    
    sprintf(header, "Degree list of\n%s %s\n", "Fahrenheit", "Celsius");
    printf(header); 

    lower = 0; upper = 300; step = 20; fahr = upper;
    for ( ; fahr >= lower ; fahr -= step) //TODO-memo: the second-semicolon indicates the "test-condition".
    {
        celsius = (5. / 9.)*(fahr - 32.);
        printf("%10.0f %7.1f\n", fahr, celsius);
    }
}
/***********************************
* ex1-6~7
***********************************/
//TODO-memo: "Text-stream" is a sequence of lines, characters with ending by '\n'. This definition works both for stdin/out or file. 
//TODO-memo: "int getchar(void)" do get a character from stream. "int putchar(int)" do writea char or a line to stream once a time?
void copy_input_to_output()
{
    char c; //int c //TODO: Both declaration of 'int' or 'char' are OK.
    printf("EOF = %d\n", EOF); //TODO-memo: EOF is -1(integer).
    printf("\\n in interger =  %d\n", '\n'); //TODO-memo: EOF is -1(integer).
    if(EOF)
        printf("non-zero expression of if is treated as True!\n");
    while ((c = getchar()) != EOF ) //TODO: keyboad-enter would signal 'EOF'?
    {    
        putchar(c);
        //exit(0); //TODO: why does the while-loop excute more than once?
    }
}
/***********************************
* ex1-8
***********************************/
void count_chars_from_input()
{
    int c;
    unsigned int nb=0, nt=0;
    while((c = getchar()) != '\n' ) //TODO: Cant't understand the behavior of EOF, so replace with '\n'.
    {
        if ( c == '\t')
            ++nt; 
        if ( c == ' ')
            ++nb;
    }
    printf("blank-char in decimal = %d\n", ' ');
    printf("tab-char in decimal = %d\n", '\t');
    printf( "# of blank, # of tab = %d %d\n", nb, nt);
}
/***********************************
* ex1-9
***********************************/
void copy_input_to_output_reduce_blank()
{
    int c;
    unsigned int nb=0;

    while ((c = getchar()) != '\n' )
    {
        switch (c)
        {
            case ' ':
                ++nb;
                if( nb > 1)
                    ; // do nothing.
                else
                    putchar(c);
                break;
            default:
                nb = 0; // reset the counter.
                putchar(c);
                break;
        }
    }
    printf("\n");
}
/***********************************
* ex1-10
***********************************/
void copy_input_to_output_replace_some()
{
    int c;
    printf("\'\\b\', \'\\\\\' = %d, %d\n", '\b', '\\');
    while ((c = getchar()) != '\n' )
    {
        switch (c)
        {
            case '\t':
                printf("\\t");
                break;
            case '\b': //TODO: backspace is 'enter' of keyboard? It doesn't work.
                printf("\\b");
                break;
            case '\\':
                printf("\\");
                break; 
            default:
                putchar(c);
                break;
        }
    }
    printf("\n");

}
/***********************************
* ex1-13, P.24
***********************************/
void histogram_lengths_of_words()
{
    /* Print a table(histrogram) of the word-length(s) from input stream */
    printf("__func__ = %s\n", __func__);

    unsigned int hist[10]; // It records the length of word from no.0~(Max-1)
    unsigned int max = 10;
    unsigned int i, c, wl;
    State st;
    // Inintialization
    c = wl = 0; //TODO-memo : gcc warning: variable \u2018c\u2019 set but not used [-Wunused-but-set-variable]
    st = OUTWORD;
    for(i = 0 ; i < max ; ++i)
        hist[i] = 0;
    // Loop for reading character(number)
    while ((c = getchar()) != EOF)
    {
        if (c == ' ' || c == '\t' || c == '\n') // Treat each char of these as a 0-length string.
        {    
            hist[wl] += 1; 
            st = OUTWORD; 
            hist[0] += 1;
            wl = 0;
        }
        else if ( st == OUTWORD) // at 1st char of a word.
        {    
            st = INWORD;
            ++wl;
        }
        else // in-word but not at the 1st char. 
        {
            ++wl;
        }
    }
    printf("word-length histogram table =\n0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9\n");
    for (i = 0; i < max ; ++i)
        printf("%2d,", hist[i]);
    printf("\n");
}

#endif
// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=200: