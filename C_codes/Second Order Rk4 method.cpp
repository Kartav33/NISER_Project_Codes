#include<bits/stdc++.h>
#include<math.h>
using namespace std;
double f(double x0, double y0)
{
    double z = -y0 + 0.5 *x0;
    return z;
}
double g(double x0, double z0)
{
    return z0;
}
int main()
{
    double x0, y0, t, h, z0, y1, z1, k1, k2, k3, k4, k5, k6 , k7, k8;
    cout<<"Enter the initial values of x, y and y' \n";
    cin>>x0 >>y0 >>z0;
    cout<<"Enter the width of bins \n";
    cin>>h;
    cout<<"Enter the value of t where f(t) has to be found \n";
    cin>>t;
    while(x0<t)
    {
        k1=h*g(x0,y0);
        k2=h*g(x0+(h/2),y0+(k1/2));
        k3=h*g(x0+(h/2),y0+(k2/2));
        k4=h*g(x0+h,y0+k3);
        y1=y0+(k1 + 2*k2 + 2*k3 +k4)/6;
        k5=h*f(x0,y0);
        k6=h*f(x0+(h/2),y0+(k1/2));
        k7=h*f(x0+(h/2),y0+(k2/2));
        k8=h*f(x0+h,y0+k3);
        z1=z0+(k5 + 2*k6 + 2*k7 +k8)/6;
        y0=y1;
        z0=z1;
        x0=x0+h;
    }
    cout<<y0;
    return 0;
}
