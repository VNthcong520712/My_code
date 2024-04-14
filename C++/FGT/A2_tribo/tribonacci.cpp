#include <iostream>
using namespace std;

unsigned long long T[10000006];
const int mod = 1000000007;

unsigned long long tribo(int g)
{
	if (g <= 3) return g;
	if (T[g] != 0) return T[g];
	T[g] = ((tribo(g - 1) + tribo(g - 2)) % mod + tribo(g - 3)) % mod;
	return T[g];
}

int main()
{
	int t;
	cin >> t;
	int inp[t];
	for (int i = 0; i < t; i++)
	{
		cin >> inp[i];
	}

	for (int j = 0; j < t; j++)
	{
		cout << tribo(inp[j]) << "\n";
	}
}

/*
phep mod (a+b+c) int thi ((a+b) % mod + c)%mod
/n giam thoi gian hon endl
tao mang rong gan tat ca gia tri cung so
*/