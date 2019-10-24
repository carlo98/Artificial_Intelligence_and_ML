#ifndef GRAP
#define GRAP

typedef struct Graph *GRAPH;
typedef struct Node *Link;

void GRAPHinit(GRAPH *G);
void GRAPHfree(GRAPH *G);
void GRAPHtrain(GRAPH G,float **inputs,float *outputs,const int NUM,const int N,const float FACTOR,const float FACTOR2,const int MINER);
float GRAPHthink(GRAPH G,float *input);

#endif
