#include <iostream> 
using namespace std;
 
 int thang;

 int main(){
     cout << "nhap vao thang bat ki tu 1 den 12: ";
     cin >> thang;
     if ((thang >= 1)and(thang <=3)){
         cout << "thang " << thang << " thuoc quy I" << endl;
     }else if ((thang >= 4)and(thang <=6)){
         cout << "thang " << thang << " thuoc quy II" << endl;
     }else if ((thang >= 7)and(thang <=9)){
         cout << "thang " << thang << " thuoc quy III" << endl;
     }else if ((thang >= 10)and(thang <=12)){
         cout << "thang " << thang << " thuoc quy IV" << endl;
     } else {
         cout << "thang nhap vao khong ton tai" <<endl;
     }
 }