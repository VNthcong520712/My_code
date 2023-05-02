#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
	ifstream vao("vao.inp");
	ofstream ra("ra.out");
	
	string a;
	int i = -1;
	do {
		getline(vao, a);
		i ++;
	}
	while(a != "<EOF>");

	ra << i;
}