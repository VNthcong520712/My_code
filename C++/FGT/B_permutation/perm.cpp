#include <bits/stdc++.h>
using namespace std;

/*
so sanh hai phan tu lien ke, neu so truoc nho hon thi co the sinh ra cau hinh tiep theo nho nhat
de sinh ra cau hinh tiep theo nho nhat, phai swap i vua tim duoc voi so nho nhat lon hon a[i]
cac so con lai sap xep tang dan
*/

int ok = 0, a[1010] = {0};

void sinh(int n)
{
	int i = n - 1;
	while (i >= 1 && a[i] > a[i + 1])
	{
		--i;
	}
	if (i == 0)
		ok = 1;
	else
	{
		int l = n;
		while (a[l] < a[i])
			--l;
		swap(a[l], a[i]);
		int sl = i + 1, sr = n;
		while (sl < sr)
		{
			swap(a[sl], a[sr]);
			sl++;
			sr--;
		}
	}
}

int main()
{
	int n, k;
	cin >> n >> k;
	for (int i = 1; i <= n; i++)
	{
		cin >> a[i];
	}
	while (k > 0 && ok != 1)
	{
		sinh(n);
		k--;
	}
	if (ok != 1)
	{
		for (int i = 1; i <= n; i++)
		{
			cout << a[i] << ' ';
		}
	}
	else
		cout << -1;
}

/*
c++ con co ham next_permutation va prev_permutation
*/