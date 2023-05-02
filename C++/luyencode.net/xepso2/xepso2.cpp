#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

int quecoban(long a){
	switch (a)
	{
	case 1:
		return 2;
		break;
	case 2:
		return 5;
		break;
	case 3:
		return 5;
		break;
	case 4:
		return 4;
		break;
	case 5:
		return 5;
		break;
	case 6:
		return 6;
		break;
	case 7:
		return 3;
		break;
	case 8:
		return 7;
		break;
	case 9:
		return 6;
		break;
	case 0:
		return 6;
		break;
	default:
	return 0;
		break;
	}
}

long tongque(long x){
	if(x != 0){
		long tong = 0;
		while(x > 0){
			short num = x - long(float(x)/10)*10;
			x = long(float(x/10));
			tong += quecoban(num);
		}
		return tong;
	} else return quecoban(0);
}

int main(){
	cout << tongque();
	// cout << quecoban(5);
}