#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	long t = 0;
	for(int x = 0; x <= n; x++){
		t += x;
	}
	cout << t;
}