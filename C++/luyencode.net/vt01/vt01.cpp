#include <iostream>
using namespace std;

int main(){
	int n, a, max;
	cin >> n;
	cin >> a;
	max = a;
	for(n; n > 1; n --){
		cin >> a;
		max = (a > max)?a:max;
	}
	cout << max;
}