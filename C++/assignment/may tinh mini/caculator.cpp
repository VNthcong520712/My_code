#include <iostream>
#include <iomanip>
using namespace std;

float a, b;
char tt;
float S = 0;

float tuyetdoi(float a){
    if (a < 0){
        a = -a;
    } 
    return a;
}

int main(){
    cin >> a >> tt >> b; // nhập vào biểu thức

    // kiểm tra dữ liệu đầu vào
    if ((tuyetdoi(a) > 10000) || (tuyetdoi(b) > 10000) || ((tt != '+') && (tt != '-') && (tt != '*') && (tt != '/'))){
        cout << "ERROR"<< endl;
    } else {
            // thực hiện tính toán
        if (tt == '+'){
            S = a + b;
        } else if (tt == '-'){
            S = a - b;              
        } else if (tt == '*'){
            S = a*b;
        } else if (tt == '/'){
            if (b == 0){
                cout << "Math Error" << endl;
            } else{
                S =a/b;
            }
        }
        if (tt == '/'){
            if (b != 0){
            cout << setprecision(2) <<fixed << S << endl;
         }
        }else {
            cout << setprecision(2) <<fixed << S << endl;
     }
    }  
    
}