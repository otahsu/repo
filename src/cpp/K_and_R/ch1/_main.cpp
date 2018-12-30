#include <stdio.h>
#include <stdlib.h>
#include "ex1.h"
#include "wc.h"
#include "dc.h"
#include "pl.h"
#include "reverse.h"
extern char sLine[MAX];

int main(int argc, char** argv)
{
    extern char sLine[MAX]; //TODO-memo: 'extern' is an adj for the following 'type' in a 'declaration'.
    //printf("hello\0 xxxx"); // C-string is terminated by '\0', so 'xxxx' wouldn't appears
    //printf("world!\n");
    //print_Fahrenheit_Celsius_table();
    //print_reverse_Fahrenheit_Celsius_table();
    //copy_input_to_output();
    //count_chars_from_input();
    //copy_input_to_output_reduce_blank();
    //copy_input_to_output_replace_some();
    //word_count();
    //cat_line_to_word();
    //count_digits();
    //histogram_lengths_of_words();
    //read_stream_print_longest_line();
    reverse_stream_line();
    return 0;
}

// vim: set ft=cpp ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=200: