CC = g++

default: kmeans

kmeans: kmeans.cpp
	${CC} -O0 -g  -std=c++11 -Wall -Wextra -Wno-unused-parameter -fopenmp -o $@ kmeans.cpp

kmeans_parallel: kmeans_parallel.cpp
	${CC} -O0 -g  -std=c++11 -Wall -Wextra -Wno-unused-parameter -fopenmp -o $@ kmeans_parallel.cpp

kmeans_serial: kmeans_serial.cpp
	${CC} -O0 -g  -std=c++11 -Wall -Wextra -Wno-unused-parameter -fopenmp -o $@ kmeans_serial.cpp

clean:
	-rm -vf kmeans
