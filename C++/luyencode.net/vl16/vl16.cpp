#include <iostream>
#include <math.h>
using namespace std;

int main(){
	short a, b;
	cin >> a >> b;
	a = abs(a);
	b = abs(b);
	int bu = max(a, b);
	int ln = a*b;
	for(int i = bu; i <= ln; i+=bu){
		if(i % a == 0 && i % b == 0){
			cout << i;
			break;
		}
	}
}