#include<bits/stdc++.h>
#define lint long long int
using namespace std;
int main() 
{
	lint n=0;
	lint ans=0;
	cin>>n;
	vector<lint> v(n);
	for(int i=0;i<n;i++)
	{
		cin>>v[i];
	}
	for(int i=0;i<n;i++)
	{
		ans=max(ans,v[i]);
	}
	cout<<ans<<endl;
	return 0;
}
