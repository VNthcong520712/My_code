#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	double a, b;
	double k;
	char t;
	cin >> a >> t >> b;
	switch (t){
		case '+':
			k = a+b;
			break;
		case '-':
			k = a-b;
			break;
		case '*':
			k = a*b;
			break;
		case '/':
			if(b == 0){
				cout << "Math Error";
				exit(0);
			}
			else k = (double)a/b;
			break;
	}
	cout << fixed << setprecision(2) << k;
}