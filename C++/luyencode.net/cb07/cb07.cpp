#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	float r; 
	cin >> r;
	cout << fixed << setprecision(3) << 2*r*3.14 << " " << r*r*3.14;
}