#include<stdio.h>
#include<stdlib.h>
#pragma warning (disable: 4326 4996 6031)
#define MAX 5

typedef int Data;

typedef struct _cQueue
{
	int rear;
	int front;
	Data qArr[MAX];
}cQueue;

typedef cQueue Queue;

void InitQueue(Queue* pq);
int IsEmpty(Queue* pq);
int NextIdx(int pos);
void Enqueue1(Queue* pq, Data data);
void Dequeue1(Queue* pq);

void Enqueue2(Queue* pq, Data data);
void Dequeue2(Queue* pq);

void PrtQueue(Queue* pq);

int main()
{
	int option;
	int value;
	Queue pq;
	InitQueue(&pq);
	while (1) {
		printf("1: 종료 2: Enqeue1 3. Dequeue1 4. Enqueue2 5: Dequeue2: ");
		scanf("%d", &option);
		switch (option)
		{
		case 1:
			return 0;
		case 2:
			printf("추가할 값 입력: ");
			scanf("%d", &value);
			Enqueue1(&pq, value);
			break;
		case 3:
			Dequeue1(&pq);
			break;
		case 4:
			printf("추가할 값 입력: ");
			scanf("%d", &value);
			Enqueue2(&pq, value);
			break;
		case 5:
			Dequeue1(&pq);
			break;
		}
		PrtQueue(&pq);
	}
}

void InitQueue(Queue* pq)
{
	pq->rear = 0;
	pq->front = 0;
	for (int i = 0; i < MAX; i++) {
		pq->qArr[i] = 0;
	}
}

int IsEmpty(Queue* pq)
{
	return (pq->rear == pq->front) ? true : false;
}

int NextIdx(int pos)
{
	return (pos == MAX-1) ? 0 : pos + 1;
}

void Enqueue1(Queue* pq, Data data)
{
	pq->qArr[pq->rear = NextIdx(pq->rear)] = data;
}

void Dequeue1(Queue* pq)
{
	pq->qArr[pq->front] = 0;
	pq->front = NextIdx(pq->front);
}

void Enqueue2(Queue* pq, Data data)
{
	pq->qArr[pq->front] = data;
	pq->front = (pq->front + MAX - 1) % MAX;
}

void Dequeue2(Queue* pq)
{
	pq->qArr[pq->rear] = 0;
	pq->rear -= 1;
}

void PrtQueue(Queue* pq)
{
	for (int i = 0; i < MAX; i++) {
		printf("%d ", pq->qArr[i]);
	}
	printf("\n");
}
