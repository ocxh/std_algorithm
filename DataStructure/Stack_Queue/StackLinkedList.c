#include <stdio.h>
#include <stdlib.h>

typedef int Data;

typedef struct _node
{
    Data data;
    struct _node *next;
} Node;

typedef struct _listStack
{
    Node *head;
} ListStack;

typedef ListStack Stack;

void StackInit(Stack *pstack); //스택 초기화
int SIsEmpty(Stack *pstack);   //스택 비어져있는지 확인

void SPush(Stack *pstack, Data data); //스택에 값 넣기
Data SPop(Stack *pstack);             //스택에 값 빼기
Data SPeek(Stack *pstack);            //스택 현재 값

void main()
{
    Stack stack;
    StackInit(&stack);

    SPush(&stack, 1);
    SPush(&stack, 2);
    SPush(&stack, 3);
    SPush(&stack, 4);
    SPush(&stack, 5);
    while (!SIsEmpty(&stack))
    {
        printf("%d ", SPop(&stack));
    }
}

void StackInit(Stack *pstack)
{
    pstack->head = NULL;
}

int SIsEmpty(Stack *pstack)
{
    if (pstack->head == NULL)
        return 1;
    else
        return 0;
}

void SPush(Stack *pstack, Data data)
{
    Node *newNode = (Node *)malloc(sizeof(Node));

    newNode->data = data;
    newNode->next = pstack->head;

    pstack->head = newNode;
}

Data SPop(Stack *pstack)
{
    Data rdata;
    Node *rnode;

    if (SIsEmpty(pstack))
    {
        printf("Stack Memory Error!");
        exit(-1);
    }

    rdata = pstack->head->data;
    rnode = pstack->head;

    pstack->head = pstack->head->next;
    free(rnode);
    return rdata;
}

Data SPeek(Stack *pstack)
{
    if (SIsEmpty(pstack))
    {
        printf("Stack Memory Error!");
        exit(-1);
    }
    return pstack->head->data;
}