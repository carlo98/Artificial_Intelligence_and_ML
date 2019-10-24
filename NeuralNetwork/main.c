/*
 * This network is able to determine the relationship between two inputs and an output, it works well with linear functions.
 * You can change the relationship between data in "Data.c"--"DATAtrainingSet".
 * In "Data.c"--"DATAtrainingSet" you can also change the input set.
 * NUM determines the number of training cycle.
 * FACTOR & FACTOR2 are the coefficient of learning of the first and second layer, respectively.
 * MINER is a working in progress.
 * EXIT determines the number used to end the program.
 */
#include <stdio.h>
#include <stdlib.h>
#include "Graph.h"
#include "Data.h"

#define NUM 1000000
#define FACTOR 0.000001
#define FACTOR2 0.0001
#define MINER 0.001
#define EXIT -1

int main(){

  int N;
  float **inputs = {NULL};
  float *outputs = {NULL};
  float input[2];
  float output=-1;
  GRAPH G = NULL;

  GRAPHinit(&G);
  
  //Inizializing training set, using DATA module
  DATAtrainingSet(&inputs,&outputs,&N);

  //Training neuralNetwork
  GRAPHtrain(G,inputs,outputs,NUM,N,FACTOR,FACTOR2,MINER);

  //Testing with unknown inputs
  while(1){
    printf("First input (%d to exit): ",EXIT); scanf("%f",&input[0]);
    if(input[0] == EXIT)
      break;
    printf("Second input: ");scanf("%f",&input[1]);
    output = GRAPHthink(G,input);
    printf("Output: %f\n",output);
  }

  printf("\nThe end.\n");

  GRAPHfree(&G);
  DATAfree(&inputs,&outputs);

  return 0;
}
    

  
  
  