#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	short a, b;
	cin >> a >> b;
	if(a == b && a == 0) cout << "INF";
	else if(a == 0 && b != 0) cout << "NO";
	else cout << fixed << setprecision(2) << float(-b)/float(a);
}