#include <iostream>
using namespace std;

int main(){
	short a, b, kqa, kqb;
	cin >> a >> b;
	short c = abs(a), d = abs(b);
	if(a == 0) cout << 0;
	else if (b == 0) cout << "INVALID";
	else {
		while(c!=d){
			short m;
			if(c > d){
				m = d;
				c = c-d;
				d = m;
			} else {
				m = c;
				d = d-c;
				c = m;
			}
		}
		if(b < 0) {
			kqa = -a/c;
			kqb = -b/c;
		} else {
			kqa = a/c;
			kqb = b/c;
		}

		if(kqb == 1) cout << kqa;
		else cout << kqa << " " << kqb;
	}
}