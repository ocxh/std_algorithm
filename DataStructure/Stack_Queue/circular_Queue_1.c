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

void QueueInit(Queue* pq); //ť �ʱ�ȭ
int QIsEmpty(Queue* pq); //ť ����ִ��� Ȯ��
int NextPosIdx(int pos); //���� ��ġ�� ���� �ε��� ��ȯ
void Enqueue(Queue* pq, Data data); //value �߰�
Data Dequeue(Queue* pq); //value ����

int main()
{
	Queue q;
	QueueInit(&q);

	Enqueue(&q, 1); Enqueue(&q, 2); Enqueue(&q, 3); Enqueue(&q, 4); Enqueue(&q, 5);

	while (!QIsEmpty(&q))
		printf("%d", Dequeue(&q));

	return 0;
}


void QueueInit(Queue* pq) //�� �� ��� front�� rear�� ���� ��ġ�� ����Ŵ
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
	//ť�� �� ���ִٸ�
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
	//ť�� ���������
	if (QIsEmpty(pq))
	{
		printf("Queue is empty");
		exit(-1);
	}

	pq->front = NextPosIdx(pq->front);
	return pq->queArr[pq->front];
}


