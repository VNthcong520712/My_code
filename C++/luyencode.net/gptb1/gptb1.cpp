#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	long long a, b, c, d, e, f;
	cin >> a >> b >> c >> d >> e >> f;
	long long tx, ty, tz;
	double x, y;

	tx = (long)-f*b+(long)e*c;
	ty = (long)-c*d+(long)f*a;
	tz = (long)a*e-(long)d*b;

	if(tz == 0){
		if(tx == 0 && ty == 0) cout << "VOSONGHIEM";
		else cout << "VONGHIEM";
	} else {
		x = (double)tx/tz;
		y = (double)ty/tz;

		if(x == 0) x = double(0);
		if(y == 0) y = double(0);

		cout << fixed << setprecision(2) << x << " " << y;
	}
}