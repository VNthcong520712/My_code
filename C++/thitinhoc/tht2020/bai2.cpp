#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

long long lttp(int a){
	long long o = 1;
	for(int i = 0; i < a; i ++){
		o*=10;
	}
	return o;
}

int main(){
	ifstream inp("bai2.inp");
	ofstream out("bai2.out");

	int n, m;
	long long T = 0;
	inp >> n >> m;
	
	int step = 1;
	for(long i = lttp(n)-1; i >= lttp(n - 1); i-= step){
		if(i % n == 0){
			step = n;
			long long z = (m-n >=0)?(i*lttp(m-n)):(i/lttp(n-m));
			T += z;
			out << z;
			if(i - step >= lttp(n-1)){
				out << "+";
			}
		}
	}
	out << "=" << T; 
}