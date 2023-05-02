#include <iostream>
#include <string>
using namespace std;

int de = 0, n;
string loai ;

int main(){
    cout << "nhap vao gia tri: ";
    cin >> n;
    for (int i =1; i <= n; i++){
        if (n%i==0){
            de += 1;
        }
    }
    if (de == 2){
        loai = "la so nguyen to";
    } else if ((n==0) || (n==1)){
        loai = "khong la so nguyen to va cung khong la hop so";
    } else {
        loai = "la hop so";
    }
    cout << "so vua nhap " << loai << endl;
}
