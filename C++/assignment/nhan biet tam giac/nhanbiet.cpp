#include <iostream>
#include <math.h>
#include <string>
using namespace std;

double a, b, c;
string loai;

int main(){
    cout << "nhap vao 3 canh cua tam giac: ";
    cin >> a >> b >> c;
    if ((a + b <= c) || (a + c <= b) || (b + b <= a) || (a <= 0) || (b <= 0) || (c <= 0)){
        cout << "chi so nhap vao khong dung !!!!!!" << endl;
    } else {
        if ((a*a + b*b == c*c) || (a*a + c*c == b*b) || (c*c + b*b == a*a)){
            if ((a == b)||(b == c)||(c == a)){
                loai = "tam giac la tam giac vuong can";
            } else loai = "tam giac la tam giac vuong";
        } else if ((a == b)||(b == c)||(c == a)){
            if (a == b == c){
                loai = "tam giac la tam giac deu";
            } else loai = "tam giac la tam giac can";
        } else loai = "tam giac la tam giac thuong";
    }
    cout << loai << endl;
}