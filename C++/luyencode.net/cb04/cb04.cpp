#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	short a, b; 
	cin >> a >> b;
	cout << a+b << "\n" << a-b << "\n" << a*b << "\n";
	if(b != 0) cout << fixed << setprecision(2) << float(a)/float(b);
	else cout << "INF";
}