#include<iostream>
#include<stdlib.h>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int main()
{
  long long int n,m,x,y;
  
  cin>>n>>m;
  
  vector<long long int> a(n);
  
  for(int i=0;i<n;i++)
  {
    cin>>a[i];
  }
  
  for(int j=0;j<m;j++)
  {
    cin>>x>>y;
    
    x=x-1;
    
    a[x]=a[x]+y;
  }
  
  for(int k=0;k<n;k++)
  {
    cout<<a[k]<<" ";
  }
  
  cout<<endl;

  return 0;
}