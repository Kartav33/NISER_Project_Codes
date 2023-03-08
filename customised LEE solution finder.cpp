#include<bits/stdc++.h>
#include<math.h>
using namespace std;
double
f (double x0, double y0, double z0, double n)
{
  double z = -x0 * x0 * pow (y0, n);
  return z;
}

double
g (double x0, double y0, double z0)
{
  return z0 / pow (x0, 2);
}

int
main ()
{
  double x0, y0, t, h, z0, y1, z1, k1, k2, k3, k4, l1, l2, l3, l4, n, h1, x0p;
  cout << "Enter the polytropic index \n";
  cin >> n;
  cout << "Enter the initial values of x, y(x) and y'(x) \n";
  cin >> x0p >> y0 >> z0;
  cout << "Enter the width of bins \n";
  cin >> h1;
  cout << "Enter the value of t where f(t) has to be found \n";
  cin >> t;
  h = h1/10;
  x0= x0p+ 0.00001;
  while (x0 < t)
    {
        k1 = h * g (x0, y0, z0);
        l1 = h * f (x0, y0, z0, n);
        
        k2 = h * g (x0 + (h/2), y0 + (k1/2), z0 +(l1/2));
        l2 = h * f (x0 + (h/2), y0 + (k1/2), z0 +(l1/2), n);
        
        k3 = h * g (x0 + (h/2), y0 + (k2/2), z0 +(l2/2));
        l3 = h * f (x0 + (h/2), y0 + (k2/2), z0 +(l2/2), n);
        
        k4 = h * g (x0 + (h/2), y0 + (k3), z0 +(l3));
        l4 = h * f (x0 + (h/2), y0 + (k3), z0 +(l3), n);
        
        y1 = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6;
        z1 = z0 + (l1 + 2 * l2 + 2 * l3 + l4) / 6;
        y0 = y1;
        z0 = z1;
        x0 = x0 + h;
        if (y0 < 0)
        {
            break;
            
        }
        
    }
  cout << y0;
  return 0;
}
