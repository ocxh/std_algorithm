#include<stdio.h>
#include<stdlib.h>
#include<memory.h>

int LBS(int arr[], int size);

int main()
{
	int arr[] = { 1,6,3,11,1,9,5,12,3,14,6,17,3,19,2,19 };
	int ans = LBS(arr, 16);
	printf("result: %d", ans);
	return 1;
}

int LBS(int arr[], int size)
{
	int maxValue = 0;
	int* lis = (int*)malloc(sizeof(int) * size); //최장 증가 부분 수열
	int* lds = (int*)malloc(sizeof(int) * size); //최장 감소 부분 수열
	memset(lis, 0x0, sizeof(int) * size);
	memset(lds, 0x0, sizeof(int) * size);

	//최장 증가 부분 수열
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < i; j++)
		{
			if (arr[j] < arr[i] && lis[i] < lis[j] + 1)
				lis[i] = lis[j] + 1;
		}
	}

	//최장 감소 부분 수열
	for (int i = size - 1; i >= 0; i--)
	{
		for (int j = size - 1; j >= i; j--)
		{
			if (arr[j] < arr[i] && lds[i] < lds[j] + 1)
				lds[i] = lds[j] + 1;
		}
	}

	for (int i = 0; i < size; i++)
	{
		if ((lis[i] + lds[i] + 1) > maxValue) maxValue = lis[i] + lds[i] + 1;
	}

	return maxValue;
}