#include <iostream>
using namespace std;

int main(){
	int n, x, count = 0;
	cin >> n >> x;
	for(int i = 0; i < n; i++){
		int z;
		cin >> z;
		if(z == x){
			count ++;
		}
	}
	cout << count;
}