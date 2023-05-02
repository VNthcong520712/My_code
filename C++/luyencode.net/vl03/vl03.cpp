#include <iostream>
using namespace std;

int main(){
	short n;
	cin >> n;
	int s = 0;
	for(int x = 2; x <= n; x++){
		s += x;
	}
	cout << s+2*n;
}