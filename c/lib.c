#include <stdlib.h>
#include <stdio.h>
#include "lib.h"

const char *C_str = "C";
const char *C_sharp_str = "C#";
const char *D_str = "D";
const char *D_sharp_str = "D#";
const char *E_str= "E";
const char *F_str = "F"; const char *F_sharp_str = "F#"; const char *G_str= "G"; const char *G_sharp_str = "G#"; const char *A_str= "A"; const char *A_sharp_str = "A#"; const char *B_str= "B";
// ^^^-- Strings needed for handling NOTEs (the strings contain the note names)

const char *half_step_str = "half step"; const char *whole_step_str = "whole step"; const char *minor_third_str = "minor third"; const char *major_third_str = "major third"; const char *perfect_fourth_str = "perfect fourth"; const char *tritone_str = "tritone"; const char *perfect_fifth_str = "perfect fifth"; const char *minor_sixth_str = "minor sixth"; const char *major_sixth_str = "major sixth"; const char *minor_seventh_str = "minor seventh"; const char *major_seventh_str = "major seventh";
// ^^^-- Strings needed for handling INTERVALs (the strings contain the interval names)

enum NOTE next_NOTE(enum NOTE input) { switch (input) { case C: return C_sharp; case C_sharp: return D; case D: return D_sharp; case D_sharp: return E; case E: return F; case F: return F_sharp; case F_sharp: return G; case G: return G_sharp; case G_sharp: return A; case A: return A_sharp; case A_sharp: return B; case B: return C; }; }
// ^^^-- Function to find next note (in pitch/chromatic order)

struct NOTE_sequence *initialize_CHROMATIC_SCALE() {
    struct NOTE_sequence *N_link = malloc(sizeof(struct NOTE_sequence)); N_link->content = C; NOTE_sequence *N_link_backup = N_link;
    for (enum NOTE current_note = next_NOTE(N_link->content); current_note != N_link_backup->content; current_note = next_NOTE(N_link->content))
    { N_link->next = malloc(sizeof(struct NOTE_sequence)); N_link->next->content = current_note; N_link = N_link->next; } N_link->next = N_link_backup; N_link = N_link_backup;
    return N_link;
}

struct INTERVAL_sequence *initialize_MAJOR_SCALE() {
    struct INTERVAL_sequence *I_seq = malloc(sizeof(struct INTERVAL_sequence)); I_seq->content = whole_step; INTERVAL_sequence *I_link_backup = I_seq;
    I_seq->next = malloc(sizeof(struct INTERVAL_sequence)); I_seq = I_seq->next; I_seq->content = whole_step;
    I_seq->next = malloc(sizeof(struct INTERVAL_sequence)); I_seq = I_seq->next; I_seq->content = half_step;
    I_seq->next = malloc(sizeof(struct INTERVAL_sequence)); I_seq = I_seq->next; I_seq->content = whole_step;
    I_seq->next = malloc(sizeof(struct INTERVAL_sequence)); I_seq = I_seq->next; I_seq->content = whole_step;
    I_seq->next = malloc(sizeof(struct INTERVAL_sequence)); I_seq = I_seq->next; I_seq->content = whole_step;
    I_seq->next = malloc(sizeof(struct INTERVAL_sequence)); I_seq = I_seq->next; I_seq->content = half_step;
    I_seq->next = I_link_backup; I_seq = I_seq->next;
    return I_seq;
}

void initialize_ALL(struct NOTE_sequence **register0, struct INTERVAL_sequence **register1) { *register0 = initialize_CHROMATIC_SCALE(); *register1 = initialize_MAJOR_SCALE(); }

const char *print_NOTE(enum NOTE input) { switch (input) { case C: return C_str; case C_sharp: return C_sharp_str; case D: return D_str; case D_sharp: return D_sharp_str; case E: return E_str; case F: return F_str; case F_sharp: return F_sharp_str; case G: return G_str; case G_sharp: return G_sharp_str; case A: return A_str; case A_sharp: return A_sharp_str; case B: return B_str; }; }

const char *print_INTERVAL(enum INTERVAL input) { switch (input) { case half_step: return half_step_str; case whole_step: return whole_step_str; case minor_third: return minor_third_str; case major_third: return major_third_str; case perfect_fourth: return perfect_fourth_str; case tritone: return tritone_str; case perfect_fifth: return perfect_fifth_str; case minor_sixth: return minor_sixth_str; case major_sixth: return major_sixth_str; case minor_seventh: return minor_seventh_str; case major_seventh: return major_seventh_str; } }

void test_NOTE_sequence(struct NOTE_sequence *N_sequence, int amount) { for (int i = 1; i <= amount; i++) { printf("Note %i: %s\n", i, print_NOTE(N_sequence->content)); N_sequence = N_sequence->next; } }

void test_INTERVAL_sequence(struct INTERVAL_sequence *I_sequence, int amount) { for (int i = 1; i <= amount; i++) { printf("Interval %i: %s\n", i, print_INTERVAL(I_sequence->content)); I_sequence = I_sequence->next; } }
