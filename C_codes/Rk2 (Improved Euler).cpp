#include<bits/stdc++.h>
#include<math.h>
using namespace std;
double func(double x, double y )
{
    double a = x + sin(x);
    return a;
}
int main()
{
    double x0, y0, x1, y1, t, h,y1d;
    cout<<"Enter the initial values of x and y \n";
    cin>>x0 >>y0;
    cout<<"Enter the width of bins \n";
    cin>>h;
    cout<<"Enter the value of t where f(t) has to be found \n";
    cin>>t;
    while(x0<t)
    {
        //y1d=y0+(h*func(x0,y0));
        //x1=x0+h;
        y1=y0+h*(func(x0+h,y0+(h*func(x0,y0)))+func(x0,y0))*0.5;
        x0=x1;
        y0=y1;
    }
    cout<< y0;
    return 0;
}
