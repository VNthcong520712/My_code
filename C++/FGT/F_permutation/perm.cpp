#include <iostream>
using namespace std;

bool check[10];
int out[10];

void perm(int a, int step = 1){
	if(step > a){
		for(int i = 1; i <= a; i++){
			cout << out[i] << " ";
		}
		cout << "\n";
		return;
	}

	for(int i = 1; i <= a; i++){
		if(check[i] == 0){
			out[step] = i;
			check[i] = 1;
			perm(a, step + 1);
			check[i] = 0;
		}
	}
}

int main(){
	int n;
	cin >> n;
	perm(n);
}