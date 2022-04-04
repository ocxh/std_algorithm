#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable : 4996)

typedef struct Node
{
    int value;
    struct Node *next;
} Node;

void makeNode(Node **start, int data);
void prtNode(Node **start);
void freeNode(Node **start);

void main()
{
    Node *start = NULL;

    int option = 0;
    int data = 0;

    while (1)
    {
        printf("option: 노드생성(1) 노드출력(2) 종료(0): ");
        scanf("%d", &option);

        switch (option)
        {
        case 1:
            printf("데이터 입력: ");
            scanf("%d", &data);
            makeNode(&start, data);
            break;
        case 2:
            prtNode(&start);
            break;
        case 0:
            freeNode(&start);
            return;
        default:
            break;
        }
    }
}

void makeNode(Node **start, int data)
{
    Node *new = (Node *)malloc(sizeof(Node));
    Node *now = *start;

    new->value = data;
    new->next = NULL;
    if (now == NULL)
        *start = new;
    else
    {
        while (now->next != NULL)
        {
            now = now->next;
        }
        now->next = new;
    }
    printf("노드 생성 완료!\n");
}

void prtNode(Node **start)
{
    Node *now = *start;
    while (now != NULL)
    {
        printf("%d ", now->value);
        now = now->next;
    }
    printf("\n출력 완료!\n");
}

void freeNode(Node **start)
{
    Node *now = *start;
    Node *next_node = NULL;
    while (now != NULL)
    {
        next_node = now->next;
        free(now);
        now = next_node;
    }
    printf("초기화 완료!\n");
}