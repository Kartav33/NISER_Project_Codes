#include<bits/stdc++.h>
using namespace std;
double fun( double x)
{
    return (x*x)/2 + 3*x - 1/x;
}
double sumDoubleItegral (double lb1, double lb2, int n, double dy)
{
    double cumBigsum = 0;
    for(int i=0; i<n; i++)
    {
        double yi = lb1 +i*dy;
        double dx = (double)(yi - lb2)/n;
        double cumSmallsum=0;

        for ( int j=0; j<n; j++)
        {
            double xi = lb2 +dx*j;
            double rectanglearea = fun(xi)*dx;
            cumSmallsum+=rectanglearea;
        }
        double secondrectanglearea = cumSmallsum*dy;
        cumBigsum+=secondrectanglearea;
    }
    return cumBigsum;
}
int main()
{
    double lb1=3, lb2=1, ub1=5;
    int n=10000;
    double dy = (double)(ub1-lb1)/n;
    double result=sumDoubleItegral(lb1, lb2, n, dy);
    cout<<result;
    return 0;
}
