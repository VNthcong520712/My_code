#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int n, sum = 0, t = 0;
	cin >> n;
	for(int i = 0; i < n; i++){
		int z;
		cin >> z;
		if(z % 2 != 0){
			sum += z;
			t ++;
		}
	}
	cout << fixed << setprecision(4) << (float)sum/t;
}