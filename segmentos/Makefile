CC=gcc
CFLAGS=-c

all: dane1_3.txt main

gen: dane1_3.txt

perf_test: main dane1_3.txt
	time ./main 1>/dev/null

dane1_3.txt:
	python 1.3.gen.py

run:
	./main

main: main.o
	gcc main.o -o main

main.o: main.c
	$(CC) $(CFLAGS) main.c

