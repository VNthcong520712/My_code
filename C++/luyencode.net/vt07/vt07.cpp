#include <iostream>
using namespace std;

int main(){
	int a[10], i = 0, x, count = 0;
	for(i; i < 11; i ++){
		cin >> x;
		if(i == 10) break;
		else a[i] = x;
	}
	for(int j = 0; j < 10; j++){
		if(x == a[j]){
			count ++;
			cout << j+1 << " ";
		}
		
		if(j == 9 && count == 0) cout << -1;
	}
}