#include<iostream>
#include<stdlib.h>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int main()
{
  long long int n,m;
  long long int count=0;
  
  cin>>n>>m;
  
  vector< vector < long long int > > a(n,vector< long long int >(2));
  
  for(int i=0;i<n;i++)
  {
    cin>>a[i][0];
  }
  
  for(int j=0;j<n;j++)
  {
    cin>>a[j][1];
  }
  
  sort(a.begin(),a.end());
  
  while(m>=a[0][0])
  {
    count++;
    m=m-a[0][0];
    a[0][0]=a[0][0]+a[0][1];
    sort(a.begin(),a.end());
  }
  
  cout<<count<<endl;

  return 0;
}