#include<iostream>
#include<stdlib.h>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int main()
{
  int n;
  int max=-1;
  
  cin>>n;
  
  vector<long long int> a(n);
  
  for(int i=0;i<n;i++)   
  {
    cin>>a[i];
    if(max<a[i])
    {
      max=a[i];
    }
  }
  
  cout<<max<<endl;
  
  return 0;
}