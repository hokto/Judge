//
//  main.cpp
//  accessories 2.4
//
//  Created by 吉永大翔 on 2020/03/04.
//  Copyright © 2020 吉永大翔. All rights reserved.
//

#include <iostream>
using namespace std;
int main(){
    int n=0,m=0;
    cin>>n;
    int product[n];
    cin>>m;
    int infomationX[m];
    int infomationY[m];
    for(int i=0;i<n;i++){
        cin>>product[i];
    }
    for(int i=0;i<m;i++){
        cin>>infomationX[i];
        cin>>infomationY[i];
    }
    for(int i=0;i<n;i++){
        int sum=0;
        for(int j=0;j<m;j++){
            if(i+1==infomationX[j]){
                sum+=infomationY[j];
            }
        }
        sum=sum+product[i];
        cout<<sum<<" ";
    }
    cout<<endl;
    return 0;
}
