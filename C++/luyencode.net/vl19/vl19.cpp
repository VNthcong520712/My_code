#include <iostream>
using namespace std; 

int main(){
	short a, b, dem = 0;
	cin >> a >> b;
	b = b - b%3 - 3;
	for(b; b > a; b -= 3){
		cout << b << " ";
		dem ++;
	}
	if(dem == 0){
		cout << "NOT FOUND";
	}
}