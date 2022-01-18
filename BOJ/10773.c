#include <stdio.h>
#define N 1000000

int arrHap(int *arr, int len);
void Insert(int *arr, int num, int len);
void Pop(int *arr, int len);

int main()
{
    int stack[N] = {
        0,
    };
    int k;
    int num = 0;
    int len = 0;
    scanf("%d", &k);

    for (int i = 0; i < k; i++)
    {
        scanf("%d", &num);
        if (num == 0)
        {
            Pop(stack, len);
            len--;
        }
        else
        {
            Insert(stack, num, len);
            len++;
        }
    }

    printf("%d", arrHap(stack, len));

    return 0;
}

int arrHap(int *arr, int len)
{
    int all = 0;
    for (int i = 0; i <= len; i++)
    {
        all += arr[i];
    }
    return all;
}

void Insert(int *arr, int num, int len)
{
    arr[len] = num;
    return;
}

void Pop(int *arr, int len)
{
    if (len <= 0)
        return;
    arr[len - 1] = 0;
    return;
}