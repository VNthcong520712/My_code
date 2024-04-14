#include <iostream>
using namespace std;

int line[100006][2];
bool check[1000006] = {0};
int out[100006] = {0};
bool ced = 0;

void tree(int n, int s, int t, int step = 1)
{
	if (step > n - 1)
	{
		if (s == t && ced == 0)
		{
			for (int i = 0; i < step; i++)
			{
				cout << out[i] << " ";
			}
			cout << "\n";
			// ced = 1;
		}
		return;
	}
	for (int i = 0; i < n - 1; i++)
	{
		int k;
		if (line[i][0] == s)
		{
			k = line[i][1];
		}
		else if (line[i][1] == s)
		{
			k = line[i][0];
		}

		if (check[i] == 0)
		{
			out[step] = k;
			check[i] == 1;
			tree(n, k, t, step + 1);
			check[i] = 0;
		}
	}
}

int main()
{
	int n, s, t;
	cin >> n >> s >> t;
	for (int i = 0; i < n - 1; i++)
	{
		cin >> line[i][0] >> line[i][1];
	}
	out[0] = s;
	check[0] = 1;
	tree(n, s, t);
}