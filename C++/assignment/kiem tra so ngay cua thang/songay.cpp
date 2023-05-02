#include <iostream>
using namespace std;

int nam, thang, ngay;

int main(){ 
    while (true){
        cout << "nhap vao nam va thang: ";
        cin >> nam >> thang;
        if ((thang > 12) || (thang < 1)){
            cout << "\n!!! ban da nhap sai thang, vui long nhap lai !!!\n" <<endl;
            continue;
        } else {
            if (thang == 2){
                if (nam % 4 == 0){
                ngay = 29;
                } else ngay = 28;
            } else if ((thang == 1) || (thang == 3) || (thang == 5) || (thang == 7) || (thang == 8) || (thang == 10) || (thang == 12)){
                ngay = 31;
            } else ngay = 30;
        } 
        break;
    }
    cout << "thang " << thang << " nam " << nam << " co " << ngay << " ngay" << endl;
}