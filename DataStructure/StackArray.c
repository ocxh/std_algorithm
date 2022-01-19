#include<stdio.h>
#include<stdlib.h>

#define TRUE 1
#define FALSE 0
#define STACK_LEN 100

typedef int Data;

typedef struct _arrayStack
{
	Data stackArr[STACK_LEN];
	int topIndex;
}ArrayStack;

typedef ArrayStack Stack;

void StackInit(Stack* pstack); //스택 초기화
int SIsEmpty(Stack* pstack); //스택이 비어있는지 체크
void SPush(Stack* pstack, Data data); //스택에 값 push
Data SPop(Stack* pstack); //스택에서 값 pop
Data SPeek(Stack* pstack); //스택의 마지막 값

int main()
{
	//스택 생성 및 초기화
	Stack stack;
	StackInit(&stack);

	//데이터 넣기
	SPush(&stack, 1); SPush(&stack, 2); SPush(&stack, 3); SPush(&stack, 4); SPush(&stack, 5);

	//데이터 꺼내기
	while (!SIsEmpty(&stack)) printf("%d ", SPop(&stack));

	return 0;

}

void StackInit(Stack* pstack)
{
	pstack->topIndex = -1;
}

int SIsEmpty(Stack* pstack)
{
	if (pstack->topIndex == -1) return TRUE;
	else return FALSE;
}

void SPush(Stack* pstack, int data)
{
	pstack->topIndex += 1;
	pstack->stackArr[pstack->topIndex] = data;
}

Data SPop(Stack* pstack)
{
	int rIdx;
	if (SIsEmpty(pstack))
	{
		printf("Stack Memory Error!");
		exit(-1);
	}
	rIdx = pstack->topIndex;
	pstack->topIndex -= 1;

	return pstack->stackArr[rIdx];
}

Data SPeek(Stack* pstack)
{
	if (SIsEmpty(pstack))
	{
		printf("Stack Memory Error!");
		exit(-1);
	}
	return pstack->stackArr[pstack->topIndex];
}