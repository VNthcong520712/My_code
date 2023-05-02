#include <iostream>
#include <math.h>
using namespace std;

int main(){
	short a, b;
	cin >> a >> b;
	a = abs(a);
	b = abs(b);
	short td = min(a, b);
	if(td == 0) {
		cout << max(a, b);
		exit(0);
	}
	while(abs(a-b) > 0){
		short c;
		if(a > b){
			c = b;
			b = a-b;
			a = c;
		}else{
			c = a;
			a = b-a;
			b = c;
		}
		td = min(a, b);
	}
	cout << td;
}
