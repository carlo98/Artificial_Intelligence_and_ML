#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include "Graph.h"
//Initial Weight of all inputs
#define WEIGHT 2
//Number of neuron-NODES and path between them-EDGES
#define NODES 4
#define EDGES 4

struct Node{
  float *w;
  int in;
  Link next;
  int id;
};
struct Graph{
  Link *ladj;
  int V;
  int E;
};

//Working functions
static Link NEWnode(int in,Link next,int id){
  
  int i;
  Link pNode = malloc(sizeof(struct Node));
  
  pNode->w = malloc(in*sizeof(float));
  if(pNode->w == NULL){printf("Memory allocation error, in Graph.c/NEWnode.\n");exit(EXIT_FAILURE);}
  
  for(i = 0;i < in;i++)
    pNode->w[i] = WEIGHT;
  
  pNode->in = in;
  pNode->next = next;
  pNode->id = id;
  
  return pNode;
}

static void NodeFree(Link *node){
  int i;
  for(i = 0;i < (*node)->in;i++)
    free((*node)->w);

  return;
}

//My functions
//Initializing a new graph with 4 nodes and 4 edges; It's going to be more general
void GRAPHinit(GRAPH *G){
  
  GRAPH new = malloc(sizeof(struct Graph));
  if(new == NULL){printf("Memory allocation error, in Graph.c/GRAPHinit.\n");exit(EXIT_FAILURE);}
  
  new->V = NODES;
  new->E = EDGES;
  new->ladj = malloc(new->V*sizeof(link));
  if(new->ladj == NULL){printf("Memory allocation error, in Graph.c/GRAPHinit.\n");exit(EXIT_FAILURE);}
  
  new->ladj[3] = NEWnode(2,NULL,3);
  new->ladj[2] = NEWnode(2,NULL,2);
  new->ladj[1] = NEWnode(2,new->ladj[3],1);
  new->ladj[0] = NEWnode(2,new->ladj[2],0);

  *G = new;
  return;
}

void GRAPHfree(GRAPH *G){

  NodeFree(&((*G)->ladj[3]));
  NodeFree(&((*G)->ladj[2]));
  NodeFree(&((*G)->ladj[0]));
  NodeFree(&((*G)->ladj[1]));

}

static void NodeTrain(Link pNode,Link parent,float *input,float *tmp,float output,const float FACTOR,const float FACTOR2,const int MINER){

  float error,adjustment[2],guess;
  
  if(pNode->id < 2){

    guess = tmp[pNode->id] = input[0]*(pNode->w[0])+input[1]*(pNode->w[1]);
    error = output-guess;
    adjustment[0] = FACTOR*error*input[0];
    adjustment[1] = FACTOR*error*input[1];
    pNode->w[0] += adjustment[0];
    pNode->w[1] += adjustment[1];
  }
  else{
    guess = input[0]*(pNode->w[0])+input[1]*(pNode->w[1]);
    //Adjusting weights
    error = output-guess;
    adjustment[0] = FACTOR2*error*input[0];
    adjustment[1] = FACTOR2*error*input[1];
    pNode->w[0] += adjustment[0];
    pNode->w[1] += adjustment[1];
  }
}

void GRAPHtrain(GRAPH G,float **inputs,float *outputs,const int NUM,const int N,const float FACTOR,const float FACTOR2,const int MINER){

  int i,j;
  float *tmp = malloc(G->ladj[0]->in*sizeof(float));
  if(tmp == NULL){printf("Memory allocation error, in Graph.c/GRAPHtrain.\n");exit(EXIT_FAILURE);}

  for(i = 0;i < NUM;i++)
    for(j = 0;j < N;j++){
      NodeTrain(G->ladj[0],NULL,inputs[j],tmp,outputs[j],FACTOR,FACTOR2,MINER);
      NodeTrain(G->ladj[1],NULL,inputs[j],tmp,outputs[j],FACTOR,FACTOR2,MINER);
      
      NodeTrain(G->ladj[2],G->ladj[0],tmp,inputs[j],outputs[j],FACTOR,FACTOR2,MINER);
      NodeTrain(G->ladj[3],G->ladj[1],tmp,inputs[j],outputs[j],FACTOR,FACTOR2,MINER);
    }

  return;
}

float GRAPHthink(GRAPH G,float *input){

  int fd[2],fd1[2];
  float newInputs[2],output,output2;
  pipe(fd);
  pipe(fd1);
  
  printf("Neuron's weight 1.1 = %f\nNeuron's weight 1.2 = %f\n",G->ladj[0]->w[0],G->ladj[0]->w[1]);
  printf("Neuron's weight 2.1 = %f\nNeuron's weight 2.2 = %f\n",G->ladj[1]->w[0],G->ladj[1]->w[1]);
  printf("Neuron's weight 3.1 = %f\nNeuron's weight 3.2 = %f\n",G->ladj[2]->w[0],G->ladj[2]->w[1]);
  printf("Neuron's weight 4.1 = %f\nNeuron's weight 4.2 = %f\n",G->ladj[3]->w[0],G->ladj[3]->w[1]);
  
  if(fork()){
    newInputs[0] = input[0]*(G->ladj[0]->w[0])+input[1]*(G->ladj[0]->w[1]);
    //System call read and write are blocking 
    write(fd1[1],&newInputs[0],sizeof(float));
    read(fd[0],&newInputs[1],sizeof(float));
    output = newInputs[0]*(G->ladj[2]->w[0])+newInputs[1]*(G->ladj[2]->w[1]);
  }
  else{
    newInputs[0] = input[0]*(G->ladj[1]->w[0])+input[1]*(G->ladj[1]->w[1]);
    //System call read and write are blocking 
    write(fd[1],&newInputs[0],sizeof(float));
    read(fd1[0],&newInputs[1],sizeof(float));
    output2 = newInputs[0]*(G->ladj[3]->w[0])+newInputs[1]*(G->ladj[3]->w[1]);
    write(fd[1],&output2,sizeof(float));
    //Child process terminated
    exit(EXIT_SUCCESS);
  }
  //Father gives the result
  read(fd[0],&output2,sizeof(float));
  return (output+output2)/2;

}

