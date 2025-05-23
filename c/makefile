main.o: main.c
	gcc -c main.c

lib.o: lib.c lib.h
	gcc -c lib.c

main: lib.o main.o
	gcc lib.o main.o -o main
