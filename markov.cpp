#include <iostream>
#include <fstream>
#include <cmath>
#include <stdlib.h>
#include "time.h"
#include <random>
#include <string>
#include <assert.h>
using namespace std;

void update_expectations(int *, int *, int,  int);
void write_expectations_file(int ,int,  int * , int * );

int main(int argc, char* argv[]){
	int MC_samples = 1000000;
	int walk_limit = 1000;
	
	int *walk_displacement = new int [walk_limit+1];
	int *walk_displacement_squared = new int [walk_limit+1];
	for (int i = 1; i <= walk_limit; i++){
		walk_displacement[i] = walk_displacement_squared[i] = 0;
	}
	// Initialize the seed and call the Mersienne algo
	random_device rd;
	mt19937_64 gen(rd());
	uniform_real_distribution<double> RandomNumberGenerator(0.0,1.0);
	int MC_counter = 0;
	for (int m = 0; m < MC_samples; m++){ //MonteCarlo cycle
		int x = 0;
		for (int w = 1; w <= walk_limit; w++){
			double sampling_parameter = RandomNumberGenerator(gen);
			if (sampling_parameter < 0.5){
				x -= 1;
			} else if (sampling_parameter > 0.5) {
				x += 1;
			} else {
				x += 0;
			}
		update_expectations(walk_displacement, walk_displacement_squared, x, w);
		}
		MC_counter++;
	}

	cout <<"MC cycles: "<< MC_counter << endl;
	write_expectations_file(MC_samples, walk_limit, walk_displacement, walk_displacement_squared);

delete [] walk_displacement;
delete [] walk_displacement_squared;
}

void update_expectations(int *walk_displacement, int *walk_displacement_squared, int x, int w){
	int local_displacement = x;  
	walk_displacement_squared[w] += local_displacement*local_displacement;
	walk_displacement[w] += local_displacement;
}

void write_expectations_file(int MC_samples, int walk_limit, int * walk_displacement, int * walk_displacement_squared){
	string filename = "Expectations";
	ofstream e_file;
	e_file.open(filename, std::ios::app);
	for (int i = 0; i < walk_limit; i++){
		double mean_displacement = (double)walk_displacement[i]/MC_samples;
		double mean_displacement_squared = (double)walk_displacement_squared[i]/MC_samples;
		double variance = mean_displacement_squared - mean_displacement*mean_displacement;
		e_file << (double) i << "," << mean_displacement << "," << variance << endl;
	}
}
