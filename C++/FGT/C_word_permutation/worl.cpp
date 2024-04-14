#include <bits/stdc++.h>
using namespace std;

int ok = 0;
char a[10] = {0}, kq[400006][10] = {0};

void sinh(int n)
{
	int i = n - 1;
	while (i >= 1 && a[i] >= a[i + 1])
	{
		--i;
	}
	if (i == 0)
		ok = 1;
	else
	{
		int l = n;
		while (a[l] <= a[i])
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
	string n;
	getline(cin, n);
	int le = n.length();
	for (int i = 1; i <= le; i++)
	{
		a[i] = n[i - 1];
	}
	sort(a + 1, a + le + 1);
	int cou = 0;
	while (ok != 1)
	{		
		for (int i = 1; i <= le; i++)
		{
			kq[cou][i-1] = a[i];
		}
		sinh(le);
		cou ++;
	}
	cout << cou << "\n";
	int z = cou;
	for(cou; cou > 0; cou --){
		for(int j = 0; j < le; j++) cout << kq[z-cou][j];
		cout << '\n';
	}
}
