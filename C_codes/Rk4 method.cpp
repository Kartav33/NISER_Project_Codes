#include<bits/stdc++.h>
#include<math.h>
using namespace std;
double func(double x, double y )
{
    double a = log(x+y);
    return a;
}
int main()
{
    double x0, y0, x1, y1, t, h, k1, k2, k3, k4;
    cout<<"Enter the initial values of x and y \n";
    cin>>x0 >>y0;
    cout<<"Enter the width of bins \n";
    cin>>h;
    cout<<"Enter the value of t where f(t) has to be found \n";
    cin>>t;
    while(x0<t)
    {
        k1=h*func(x0,y0);
        k2=h*func(x0+(h/2),y0+(k1/2));
        k3=h*func(x0+(h/2),y0+(k2/2));
        k4=h*func(x0+h,y0+k3);
        x0=x0+h;
        y0=y0+(k1 + 2*k2 + 2*k3 +k4)/6;
    }
    cout<< y0;
    return 0;
}
