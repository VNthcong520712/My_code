#include <iostream>
#include <string.h>
using namespace std;

int ngay, thang, nam, ngt, tht, nt, ngs, ths, ns;
string loi;

int songay(int a,int b){
    if ((a == 4) || (a == 6) || (a == 9) || (a == 11)){
        return 30;
    } else if ((a == 1) || (a == 3) || (a == 5) || (a == 7) || (a == 8) || (a == 10) || (a == 12)){
        return 31;
    } else {
        if ((a == 2) && (b % 4 == 0)){
            return 29;
        } else if (a == 2) {
            return 28;
        }
    }
}

int tinhngay(int a,int b,int c){
    if (a == 1){
        if (b == 1 ){
            ngt = songay(12, c-1);
            tht = 12;
            nt = c - 1;

            ngs = a + 1;
            ths = b;
            ns = c;
        } else {
            ngt = songay(b-1, c);
            tht = b - 1;
            nt = c;

            ngs = a + 1;
            ths = b; 
            ns = c;
        }
    } else if (a == songay(b, c)){
        if (b == 12){
            ngt = songay(b, c) -1;
            tht = b;
            nt = c;

            ngs = 1;
            ths = 1;
            ns = c + 1;
        } else {
            ngt = songay(b, c)-1;
            tht = b;
            nt = c;

            ngs = 1;
            ths = b + 1 ;
            nt = c;
        }
    } else if ((a > 1) && (a < songay(b, c))){
        ngt = a -1;
        tht = b;
        nt = c;

        ngs = a + 1;
        ths = b;
        ns = c;
    }
}

int main(){
    
    cout << "nhap ngay, thang, nam: ";
    cin >> ngay >> thang >> nam; 
    if ((thang > 0) && (thang < 13)){
        if ((ngay > 0)&&(ngay <= songay(thang, nam))){
            tinhngay(ngay, thang, nam);
            cout << "ngay ban nhap la: " << ngay << "/" << thang << "/" << nam << endl;
            cout << "ngay truoc do la: " << ngt << "/" << tht << "/" << nt << endl;
            cout << "ngay sau do la: " << ngs << "/" << ths << "/" << ns << endl;
        } else {
             loi = "nhap vao loi, vui long thu lai";
        }
    } else {
        loi = "nhap vao loi, vui long thu lai"; 
    }
    cout << loi << endl;
}