#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int a, b, c, d, e, f;
	cin >> a >> b >> c >> d >> e >> f;
	long long tx, ty, tz;
	double x, y;
	tx = (long)-f*b+(long)e*c;
	ty = (long)-c*d+(long)f*a;
	tz = (long)a*e-(long)d*b;

	cout << "tx: " << tx << "  ty: " << ty << "  tz: " << tz << endl;

	if(tz == 0){
		if(tx == 0 && ty == 0) cout << "VOSONGHIEM";
		else cout << "VONGHIEM";
	} else {
		x = (double)tx/tz;
		y = (double)ty/tz;
		cout << fixed << setprecision(2) << x << " " << y;
	}
}