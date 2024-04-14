#include <bits/stdc++.h>
using namespace std;

int n, k, a[20] = {0};

void sinh()
{
	int i = n;
	while (i >= 1 && a[i] == 1)
	{
		a[i] = 0;
		--i;
	}
	a[i] = 1;
}

int main()
{
	cin >> n >> k;
	a[n] = 1;
	for (int i = 0; i < k; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			cout << a[j];
		}
		cout << "\n";
		sinh();
	}
}