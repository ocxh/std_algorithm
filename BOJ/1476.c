#include<stdio.h>

int main()
{
	int E, S, M;
	int e=0, s=0, m = 0;
	int cnt = 0;
	scanf("%d %d %d", &E, &S, &M);

	while (1)
	{
		e++;
		s++;
		m++;
		cnt++;
		if (e > 15) e = 1;
		if (s > 28) s = 1;
		if (m > 19) m = 1;
		if (e == E && s == S && m == M) {
			break;
		}
	}
	printf("%d", cnt);

	return 0;
}