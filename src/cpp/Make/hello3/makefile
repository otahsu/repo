# variables.
LIBS = -lm
OBJS = main.o foo.o

# targets:
main: ${OBJS}
	g++ -o $@ ${OBJS} ${LIBS}
clean:
	rm -f main.exe ${OBJS}
show: #show shell var.
	echo ${var} 
