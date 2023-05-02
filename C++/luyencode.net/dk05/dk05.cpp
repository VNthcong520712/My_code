#include <iostream>
#include <math.h>
using namespace std;

int main(){
	long a; 
	cin >> a;
	long c = long(sqrt(a));
	if(c*c == a) cout << "YES";
	else cout << "NO";
}