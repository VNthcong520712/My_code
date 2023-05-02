#include <iostream>
using namespace std;

int main(){
	short a, b;
	cin >> a >> b;
	if(a % 2 != 0){
		a++;
	}
	if(b % 2 != 0){
		b--;
	}
	long s= 0;
	for(int i = a; i <= b; i+= 2){
		s+=  i;
	}
	cout << s;
}