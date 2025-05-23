#ifndef STRINGS
#define STRINGS
extern const char *C_str; extern const char *C_sharp_str; extern const char *D_str; extern const char *D_sharp_str; extern const char *E_str; extern const char *F_str; extern const char *F_sharp_str; extern const char *G_str; extern const char *G_sharp_str; extern const char *A_str; extern const char *A_sharp_str; extern const char *B_str;
// ^^^-- Strings needed for handling NOTEs (the strings contain the note names)

extern const char *half_step_str; extern const char *whole_step_str; extern const char *minor_third_str; extern const char *major_third_str; extern const char *perfect_fourth_str; extern const char *tritone_str; extern const char *perfect_fifth_str; extern const char *minor_sixth_str; extern const char *major_sixth_str; extern const char *minor_seventh_str; extern const char *major_seventh_str;
// ^^^-- Strings needed for handling INTERVALs (the strings contain the interval names)

typedef enum NOTE { C, C_sharp, D, D_sharp, E, F, F_sharp, G, G_sharp, A, A_sharp, B } NOTE;   // <<<-- Contain the 12 equivalence classes as enum
typedef struct NOTE_sequence { enum NOTE content; struct NOTE_sequence *next; } NOTE_sequence; // <<<-- The wrapper needed to use the enum in N_linked lists
// ^^^-- Datatypes needed for handling NOTEs

typedef enum INTERVAL { half_step, whole_step, minor_third, major_third, perfect_fourth, tritone, perfect_fifth, minor_sixth, major_sixth, minor_seventh, major_seventh } INTERVAL;
typedef struct INTERVAL_sequence { enum INTERVAL content; struct INTERVAL_sequence *next; } INTERVAL_sequence;
// ^^^-- Datatypes needed for handling INTERVALs

enum NOTE next_NOTE(enum NOTE input);               // <<<-- Function to find next note (in pitch/chromatic order)
const char *print_NOTE(enum NOTE input);            // <<<-- Function to print NOTE names
const char *print_INTERVAL(enum INTERVAL input);    // <<<-- Function to print INTERVAL names
// ^^^-- Function headers

struct NOTE_sequence *initialize_CHROMATIC_SCALE(); // <<<-- Creates a cyclical linked list to represent the chromatic scale
struct INTERVAL_sequence *initialize_MAJOR_SCALE(); // <<<-- Creates a cyclical linked list to represent the major scale
void initialize_ALL(struct NOTE_sequence **register0, struct INTERVAL_sequence **register1);
#endif
