#include<bits/stdc++.h>
#include<math.h>
using namespace std;
int main()
{
    double xi=0.01, theta=1.0, f1=0.0, N=pow(10,7), dxi=pow(10,-6);
    int n=0;
    for(int i=0; i<N; i++)
    {
        f1 += -xi*xi*dxi*pow(theta,n);
        theta += (f1/(xi*xi))*dxi;
        xi +=dxi;
        if(xi<2.000002 && (xi-dxi)>=2)
        {
            cout<<theta;
        }
    }
}
