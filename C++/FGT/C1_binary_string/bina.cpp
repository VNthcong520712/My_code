#include <iostream>
using namespace std;

char X[32772];
int count = 0;

void nhiphan(int i, int n, int s = 1, int k = 0){
	for(int j = 0; j < 2; j++){
		X[s-1] = (char) j + 48;
		if (j == 1) k = 1;
		if(s >= n){
			if(k ==1){
				if (count == i) return;
				cout << X ;
				count ++;
				cout << endl;
			}
		}
		else nhiphan(i, n, s+1, k);
	}
}

int main(){
	int n, k;
	cin >> n >> k;
	nhiphan(k, n);
}