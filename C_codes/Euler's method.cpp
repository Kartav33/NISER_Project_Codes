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
    double x0, y0, x, y, t, h;
    cout<<"Enter the initial values of x and y \n";
    cin>>x0 >>y0;
    cout<<"Enter the width of bins \n";
    cin>>h;
    cout<<"Enter the value of t where f(t) has to be found \n";
    cin>>t;
    while(x0<t)
    {
        y=y0+(h*func(x0,y0));
        y0=y;
        x0=x0+h;
    }
    cout<< y0;
    return 0;
}
