#include <stdio.h>
#include <math.h>

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
    scanf("%f %c %f", &a, &tt, &b); // nhập vào biểu thức

    // kiểm tra dữ liệu đầu vào
    if ((tuyetdoi(a) > 10000) || (tuyetdoi(b) > 10000) || ((tt != '+') && (tt != '-') && (tt != '*') && (tt != '/'))){
        printf("ERROR");
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
                printf("Math Error");
            } else{
                S =a/b;
            }
        }
        if (tt == '/'){
            if (b != 0){
            printf("%.2f", S);
            }
        }else {
            printf("%.2f", S);
        }
    }  
    
}