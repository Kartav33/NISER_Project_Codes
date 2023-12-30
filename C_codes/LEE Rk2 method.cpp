#include<bits/stdc++.h>
#include<math.h>
using namespace std;

double f(double y0, double x0, double z0, double n)
{
    double z = -pow(y0, n) - z0;
    return z;
}
double g(double z0, double x0)
{
    return z0*x0*0.5;
}
int main()
{
    double x0, y0, t, h, z0, y1p, z1p, y1c, z1c, n;
    cout<<"Enter the polytropic index \n";
    cin>>n;
    cout<<"Enter the initial values of x, y(x) and y'(x) \n";
    cin>>x0 >>y0 >>z0;
    cout<<"Enter the width of bins \n";
    cin>>h;
    cout<<"Enter the value of t where f(t) has to be found \n";
    cin>>t;
    while(x0<t)
    {
        y1p= y0 + h*g(z0,x0);
        z1p= z0 + h*f(y0,x0,z0,n);
        y1c= y0 + h*(g(z1p,x0+h) + g(z0,x0))*0.5;
        z1c= z0 + h*(f(y1p,x0+h,z1p, n) + f(y0,x0,z0,n))*0.5;
        y0=y1c;
        z0=z1c;
        x0=x0+h;
        if (y0 < 0)
        {
            break;
        }
    }
    cout<<y0;
    return 0;
}
