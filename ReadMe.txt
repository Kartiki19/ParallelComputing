// generate random data 

// compile 
g++ -o gen_data gen_data.cpp

// execute 
./gen_data <output_file_name> <rec_count> <low rang1> <high range1> <low rang2> <high range2>
example : ./gen_data input_1000.csv 1000 50 400 10 150


###############################

//Compile 

make kmeans_parallel
make kmeans_serial

//execute 

./kmeans_parallel <Input Data Filename> <Output Filename> <Number of Iterations> <Number of Clusters> [-t <num_threads>]
./kmeans_serial <Input Data Filename> <Output Filename> <Number of Iterations> <Number of Clusters> [-t <num_threads>]

example : ./kmeans_parallel input_1000.csv out_1000 10000 5 -t8
./kmeans_serial input_1000.csv out_1000 10000 5 -t8


###################################

module load OpenMPI
 For serial:
 g++ -std=c++11 -fopenmp Kmeans_serial_mpi_1.cpp
 ./a.out input_1000.csv 5 log_mpi_serial_5.csv
 
 For Parallel:
 mpic++ -o Kmeans_parallel_mpi Kmeans_parallel_mpi.cpp
 mpirun -n 2 Kmeans_parallel_mpi input_1000.csv 5 Kmeans_mpi_parallel_2_1000_5.csv



######################################

creating cluttered images 
python3 plotParallel.py <dir of csv file > < input csv file > <number of clusters > <output_img_name>
python3 plotSerial.py <dir of csv file > < input csv file > <number of clusters > <output_img_name>

