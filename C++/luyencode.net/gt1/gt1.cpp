#include <iostream>
using namespace std;

int main(){
	short n;
	cin >> n;
	unsigned long long gt = 1;
	for(int i = 1; i <= n; i++){
		gt *= i;
	}
	cout << gt;
}