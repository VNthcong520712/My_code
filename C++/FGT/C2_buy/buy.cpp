#include <bits/stdc++.h>
using namespace std;

long bou[21];
bool check[21];
int _count = 0;
int leng = 0;

void buy(int quantity, int list[], int financial, int step = 0, int expend = 0, int st = 0){
	for(int i = st; i < quantity; i++){
		int sup = expend;
		if (check[i] == 0 && sup + list[i] <= financial){
			bou[step] = list[i];
			sup += list[i];
			check[i] = 1;
			buy(quantity, list, financial, step+1, sup, i);
			check[i] = 0;
		}
	}
	// for(int j = 0; j < step; j++){
	// 	cout << bou[j];
	// }
	// cout << endl;
	if (step > leng) leng = step;
	_count ++;
	return;
}

int main(){
	int a, b;
	cin >> a >> b;
	int list[a];
	for(int i = 0; i < a; i++){
		cin >> list[i];
	}
	buy(a, list, b);
	cout << _count << " " << leng;
}