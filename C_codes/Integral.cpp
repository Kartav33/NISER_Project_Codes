#include<bits/stdc++.h>
using namespace std;
double fun(double x)
{
    return x;
}
double sumIntegral(double lb, int n, double dx)
{

    double cumsum=0;
    for(int i=0; i<n; i++)
    {
        double xi=lb + i*dx;
        double rectanglearea= fun(xi)*dx;
        cumsum=cumsum+rectanglearea;
    }
    return cumsum;
}
int main()
{
    double lb=4, ub=7;
    int n=10;
    double dx = (double)(ub-lb)/n;
    double result=sumIntegral(lb, n, dx);
    cout<<result;
    return 0;
}
