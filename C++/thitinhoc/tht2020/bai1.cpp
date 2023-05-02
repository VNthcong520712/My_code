#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main(){
	ifstream inp("bai1.inp");
	ofstream out("bai1.out");

	long n;
	int k,m, X, V;
	float h, T;

	inp >> n >> k >> m;

	h = (float) k*2/3;

	if(n % 2 == 0){
		V = (n - m)/2;
	}else {
		V = (n - m - 1)/2;
	}
	X = n - V;

	T = round(V*k + h*X);
	if(V != 0 && X != 0){
		out << V << " " << X << " " << T;
	} else out << 0;
}