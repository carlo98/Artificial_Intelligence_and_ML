#include <stdlib.h>
#include <stdio.h>
#include "Data.h"
//Training set dimension, attection: at the moment only two inputs and one output are supported
#define LEN 16

void DATAtrainingSet(float ***inputs,float **outputs,int *N){

  int i;
  
  *inputs = (float **)malloc(LEN*sizeof(float *));
  *outputs = (float *)malloc(LEN*sizeof(float));
  if(*inputs == NULL || *outputs == NULL){printf("Memory allocation error in Data.c/DATAtrainingSet.\n");exit(EXIT_FAILURE);}
  
  for(i = 0;i < LEN;i++)
      (*inputs)[i] = malloc(2*sizeof(float));
      
  //Input set
  (*inputs)[0][0] = 1; (*inputs)[0][1] = 2; 
  (*inputs)[1][0] = 3; (*inputs)[1][1] = 2; 
  (*inputs)[2][0] = 6; (*inputs)[2][1] = 5; 
  (*inputs)[3][0] = 10; (*inputs)[3][1] = 11; 
  (*inputs)[4][0] = 3; (*inputs)[4][1] = 6; 
  (*inputs)[5][0] = 2; (*inputs)[5][1] = 2; 
  (*inputs)[6][0] = 1; (*inputs)[6][1] = 4; 
  (*inputs)[7][0] = 2; (*inputs)[7][1] = 6;
  (*inputs)[8][0] = 4; (*inputs)[8][1] = 2; 
  (*inputs)[9][0] = 3; (*inputs)[9][1] = 2; 
  (*inputs)[10][0] = 6; (*inputs)[10][1] = 5; 
  (*inputs)[11][0] = 10; (*inputs)[11][1] = 5; 
  (*inputs)[12][0] = 7; (*inputs)[12][1] = 6; 
  (*inputs)[13][0] = 9; (*inputs)[13][1] = 2; 
  (*inputs)[14][0] = 1; (*inputs)[14][1] = 4; 
  (*inputs)[15][0] = 21; (*inputs)[15][1] = 6; 
  
  //Define relationship between data
  for(i = 0;i < LEN;i++)
      (*outputs)[i] = 0.5*((*inputs)[i][0]+(*inputs)[i][1]);
 
  *N = LEN;
  return;
}

void DATAfree(float ***inputs,float **outputs){

  int i;

  for(i = 0;i < LEN;i++)
    free((*inputs)[i]);
  free(*inputs);
  free(*outputs);
  return;
}
