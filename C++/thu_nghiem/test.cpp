#include <iostream>

int aa(int p){
	static int d = 15;
	std::cout << d << " " << p<<"--";
	d+= p;
	std::cout << d<<";";
	return d;
}

int main(){
	int a = 4;
	std::cout <<aa(a-1+ aa(a + aa(a-3)));
}