#include <iostream>
using namespace std;

int main(){
	int n, max;
	cin >> n;
	cin >> max;
	int index = 0;
	for(int i = 1; i < n; i++){
		int z;
		cin >> z;
		if(z >= max){
			max = z; 
			index = i;
		}
	}
	cout << index;
}