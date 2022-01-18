#include<stdio.h>
#include<math.h>

int intlen(int num)
{
	int f = 10;
	int cnt = 1;
	while (1)
	{
		if (num - f < 0)
		{
			return cnt;
		}
		f *= 10;
		cnt += 1;
	}
}

void refill(int* arr)
{
	for (int i = 0; i < 9; i++)
	{
		arr[i] += 1;
	}
	arr[6] += 1;
}

int main()
{
	int N = 0; //입력값
	int arr[9] = { 1,1,1,1,1,1,2,1,1}; //한 세트(0~8),9는 6에 +1
	int length = 0; //입력값 정수의 길이
	int cnt = 1; //세트 수
	int now = 0;
	int npow = 0;
	scanf("%d", &N);
	length = intlen(N);
	npow = pow(10, length - 1);

	if (length == 1)
	{
		printf("%d", cnt);
	}
	else {
		for (int i = 0; i < length; i++)
		{
			now = N / npow; 
			N -= now * npow;
			if (now == 9) now = 6;
			if (arr[now] <= 0) {
				refill(arr);
				cnt++;
			}
			arr[now]--;
			npow /= 10;
		}
		printf("%d", cnt);
	}
	
	return 0;
}