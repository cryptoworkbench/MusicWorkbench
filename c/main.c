#include <stdlib.h>
#include <stdio.h>
#include "lib.h"

struct NOTE_sequence *N_link; struct INTERVAL_sequence *I_link;

int main(int argc, char *argv[]) {
    initialize_ALL(&N_link, &I_link);
    
    test_NOTE_sequence(N_link, 13);
    test_INTERVAL_sequence(I_link, 15);
    return 0;
}
