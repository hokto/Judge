#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<utility>
#include<string>
#include<initializer_list>
#include<map>
#include<queue>
#include<set>
#define lint long long int
#define rep(i,n) for(int i=0;i<int(n);i++)
#define arep(i,a,n) for(int i=a;i<n;i++)
#define sort(a) sort(a.begin(),a.end())
#define reverse(a) reverse(a.begin(),a.end())
#define fill(a,x) fill(a.begin(),a.end(),x)
#define pb push_back
#define mp make_pair
#define AlphabetNUM 26
#define vint vector<int>
#define F first
#define S second
#define ALL(data) data.begin(),data.end()
using namespace std;
/*
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         fozubaoyou    pass System Test!
*/
template<typename Rast>inline void out(Rast rast){cout<<rast<<"\n";return;}
template<typename Rast>inline void in(Rast& rast){cin>>rast;return;}
template< typename T >istream& operator >> (istream& is, vector<T>& vec){for(T& x: vec) is >> x;return is;}
template< typename First, typename... Rest >void in(First& first, Rest&... rest){cin >> first;in( rest... );return;}
template< typename First, typename... Rest >void out(First first, Rest... rest){cout << first<<" ";out( rest... );return;}
template<typename T>T gcd( T a,T b){if(b==0)return a;return gcd(b,a%b);}
template<typename T>bool chmax(T& a,T b){if(a<b){a=b;return true;}else{return false;}}
template<typename T>bool chmin(T& a,T b){if(a>b){a=b;return false;}else{return true;}}
template<typename T>T lcm(T a, T b){return a * b / gcd(a, b);}

lint MOD=pow(10,9)+7;
int inf=-1+pow(2,31);
int dirx[]={0,1,0,-1};
int diry[]={-1,0,1,0};

int main(){
	int n;
	lint m;
	in(n,m);
	lint ans=0;
	lint a[n];
	lint b[n];
	set< pair<lint,lint> > se;
	rep(i,n){
		cin>>a[i];
		se.insert(mp(a[i],i));
	}
	rep(i,n)cin>>b[i];
	while(1){
		auto now=*se.begin();
		se.erase(now);
		if(m<now.F)break;
		m=m-now.F;
		ans++;
		now.F+=b[now.S];
		se.insert(now);
	}
	out(ans);
	return 0;
}
