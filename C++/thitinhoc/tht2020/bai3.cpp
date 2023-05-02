#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream inp("bai3.inp");
	ofstream out("bai3.out");

	string n, l, c;
	getline(cin, n);
	int tc = 0, tl = 0;
	long N = stoi(n);


	for(int i = 1; i <= n.length(); i ++){
		if(i%2 == 0){
			tc = tc +  (int(n[i-1])-48);
			c += n[i-1];
		} else {
			tl = tl + (int(n[i-1])-48);
			l += n[i-1];
		}
	}
	cout << c << "\n" << l << "\n" << tc << "\n" << tl << "\n" << N ;
}