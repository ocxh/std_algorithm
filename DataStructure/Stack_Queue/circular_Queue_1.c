#include<stdio.h>
#include<stdlib.h>

#define QUE_LEN 5
typedef int Data;

typedef struct _cQueue
{
	int front;
	int rear;
	Data queArr[QUE_LEN];
}cQueue;

typedef cQueue Queue;

void QueueInit(Queue* pq); //큐 초기화
int QIsEmpty(Queue* pq); //큐 비어있는지 확인
int NextPosIdx(int pos); //현재 위치의 다음 인덱스 반환
void Enqueue(Queue* pq, Data data); //value 추가
Data Dequeue(Queue* pq); //value 삭제

int main()
{
	Queue q;
	QueueInit(&q);

	Enqueue(&q, 1); Enqueue(&q, 2); Enqueue(&q, 3); Enqueue(&q, 4); Enqueue(&q, 5);

	while (!QIsEmpty(&q))
		printf("%d", Dequeue(&q));

	return 0;
}


void QueueInit(Queue* pq) //텅 빈 경우 front와 rear는 같은 위치를 가리킴
{
	pq->front = 0;
	pq->rear = 0;
}

int QIsEmpty(Queue* pq)
{
	return (pq->front == pq->rear) ? true : false;
}

int NextPosIdx(int pos) 
{
	return (pos == QUE_LEN - 1) ? 0 : pos + 1;
}

void Enqueue(Queue* pq, Data data)
{
	//큐가 꽉 차있다면
	if (NextPosIdx(pq->rear) == pq->front)
	{
		printf("Queue is fulled");
		exit(-1);
	}

	pq->rear = NextPosIdx(pq->rear);
	pq->queArr[pq->rear] = data;
}

Data Dequeue(Queue* pq)
{
	//큐가 비어있으면
	if (QIsEmpty(pq))
	{
		printf("Queue is empty");
		exit(-1);
	}

	pq->front = NextPosIdx(pq->front);
	return pq->queArr[pq->front];
}


