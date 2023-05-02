#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

int main(){
	// ax^2+bx+ c = 0
	short a, b, c;
	cin >> a >> b >> c;
	double del = (b*b - 4*a*c);
	if(a == 0){
		if(b == 0 && c == 0) cout << "INF";
		else if(b == 0 && c != 0) cout << "NO";
		// else if(c == 0 && b != 0) cout << 0.00;
		else cout << fixed << setprecision(2) <<(double)-c/b;
	} else {
		if(del < 0) cout << "NO";
		else if(del == 0) cout << fixed << setprecision(2) << (double)-b/(2*a);
		else if(del > 0){
			cout << fixed << setprecision(2) << (double)(-b-sqrt(del))/(2*a) << " " << (double)(-b+sqrt(del))/(2*a);
		}
	}
}