#include <iostream>
using namespace std;

int main(){
	int a, b , c;
	cin >> a >> b >> c;
	int i = (a>b)?a:b;
	int ii = (i>c)?i:c;
	cout << ii;
}