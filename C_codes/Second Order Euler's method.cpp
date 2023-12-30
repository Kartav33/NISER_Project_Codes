#include<bits/stdc++.h>
#include<math.h>
using namespace std;
double f(double y0, double x0)
{
    double z = -y0 + 0.5 *x0;
    return z;
}
double g(double z0, double x0)
{
    return z0;
}
int main()
{
    double x0, y0, t, h, z0, y1, z1;
    cout<<"Enter the initial values of x, y and y' \n";
    cin>>x0 >>y0 >>z0;
    cout<<"Enter the width of bins \n";
    cin>>h;
    cout<<"Enter the value of t where f(t) has to be found \n";
    cin>>t;
    while(x0<t)
    {
        y1= y0 + h*g(z0,x0);
        z1= z0 + h*f(y0,x0);
        y0=y1;
        z0=z1;
        x0=x0+h;
    }
    cout<<y0;
    return 0;
}
