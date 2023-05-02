#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	short n; 
	cin >> n;
	double s = 0;
	for(short x = 2; x <= n; x++){
		s += (double)1/x;
	}
	cout << fixed << setprecision(4) << s;
}