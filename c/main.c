#include <stdlib.h>
#include <stdio.h>
#include "lib.h"

struct NOTE_sequence *N_link; struct INTERVAL_sequence *I_link;

int main(int argc, char *argv[]) {
    initialize_ALL(&N_link, &I_link);
    
    for (int i = 1; i < 12; i++) {
        printf("Note %i: %s\n", i, print_NOTE(N_link->content));
        N_link = N_link->next;
    }


    for (int i = 1; i < 7; i++) {
        printf("Interval %i: %s\n", i, print_INTERVAL(I_link->content));
        I_link = I_link->next;
    }
    return 0;
}
