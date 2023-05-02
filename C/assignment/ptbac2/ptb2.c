#include <stdio.h>
#include <math.h>

int a, b, c, denta;
float x1, x2;

int main(){
    printf("ax^2 + bx + c = 0; nhap a b va c : ");
    scanf("%d%d%d", &a, &b, &c);
    if ((a == 0) && (b == 0)){
        printf("phuong trinh vo nghiem");
    } else if ((a == 0) && (b !=0)){
        float r = -c/b;
        printf("phuong trinh co nghiem la x = %f",r);
    } else {
        denta = pow(b,2) - 4*a*c;
        if (denta < 0){
            printf("phuong trinh vo nghiem ");
        } else if(denta >= 0){
            x1 = (float)(-b + (float)sqrt(denta))/(2*a);
            x2 = (float)(-b - (float)sqrt(denta))/(2*a);
            printf("nghiem cua phuong trinh la: x1 = %f, x2 = %f", x1, x2);
        }
    }        
}