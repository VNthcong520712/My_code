#include <iostream>
using namespace std;

int main(){
	double a;
	cin >> a;
	int n = int(a);
	double d = (a > 0)?(a - n):(-a+n);
	if(d >= 0.5) n += (a > 0)?1:-1;
	cout << n;
}