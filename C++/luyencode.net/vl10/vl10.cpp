#include <iostream>
#include <string.h>
using namespace std;

int main(){
	string so;
	getline(cin, so);
	if(so[0] == '-') so = so.substr(1, so.length());
	cout << so.length();
}