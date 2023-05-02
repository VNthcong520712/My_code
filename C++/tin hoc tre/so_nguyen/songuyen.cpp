#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
	ifstream inp("vao.inp");
	ofstream out("ra.out");

	int vao, tong = 0;
	while (!inp.eof()){
		inp >> vao;
		if(vao % 2 == 0){
			tong+= vao;
		}
	}
	ra << tong;
	inp.close();
}
