#include <iostream>
using namespace std;

int chees_table[1006][1006];

int ways[8][2] = {
	{-2, 1},
	{-1, 2},
	{1, 2},
	{2, 1},
	{2, -1},
	{1, -2},
	{-1, -2},
	{-2, -1}};
int X_ni[1006];
int Y_ni[1006];

bool knight(int length, int width, int step = 1)
{
	if (chees_table[1][1] == 2 || chees_table[length][width] == 2)
	{
		return false;
	}

	if (chees_table[length][width] == 1) return true;

	for (int i = 0; i < 8; i++)
	{
		int x = X_ni[i] + ways[i][0];
		int y = Y_ni[i] + ways[i][1];
		if((x > 0 && x < length) && (y > 0 && y < width) && (chees_table[x][y] != 2) && (chees_table[X_ni[i+1]][Y_ni[i+1]] != 1)){
			X_ni[i + 1] = x;
			Y_ni[i + 1] = y;
			chees_table[X_ni[i+1]][Y_ni[i+1]] = 1;
			knight(length, width, step + 1);
			chees_table[X_ni[i+1]][Y_ni[i+1]] = 0;
		}
	}
}

int main()
{
	int n, m, q;
	cin >> n >> m >> q;
	for (int i = 0; i < q; i++)
	{
		int x, y;
		cin >> x >> y;
		chees_table[x - 1][y - 1] = 2;
	}
	X_ni[0] = 1;
	Y_ni[0] = 1;
	chees_table[0][0] = 1;
	string out = (knight(n-1, m-1)) ? "YES" : "NO";
	cout << out;
}