#include <iostream>
using namespace std;

int ways = 0;
bool chees_table[12][12];

bool check(int row, int collum, int size)
{ // ham nam ben trong vong lap de kiem tra cac dieu kien de bai
	bool result = true;

	if (row != 0) // hang dang xet co phai hang
	{
		for (int i = row; i >= 0; i--)
		{ // kiem tra xem co quan hau cung cot khong
			if (chees_table[i][collum] == 1)
			{
				return false;
			}
		}


		int pr = row, pc = collum;
		while (pr > 0 && pc < size - 1) // xet cheo phai
		{
			pr--;
			pc++;
			if (chees_table[pr][pc] == 1)
			{
				return false;
			}
		}


		int tr = row, tc = collum;
		while (tr > 0 && tc > 0) // xet cheo trai
		{
			tr--;
			tc--;
			if (chees_table[tr][tc] == 1)
			{
				return false;
			}
		}
	}
	return true;
}

void queen(int step, int n)
{
	if (step > n)
	{
		ways++;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				cout << chees_table[i][j] << " ";
			}
			cout << endl;
		}
		cout << endl;
		return;
	}
	for (int collum = 0; collum < n; collum++)
	{
		if(check(step-1, collum, n)){
			chees_table[step-1][collum] = 1;
			queen(step + 1, n);
			chees_table[step-1][collum] = 0;
		}
	}
}

int main()
{
	int n;
	cin >> n;
	queen(1, n);
	cout << ways;
}