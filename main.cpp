// #include<iostream>
// #include<algorithm>
// using namespace std;

// int main()
// {    
//     int a,b,c;
//     cin>>a>>b>>c;
//     int m = std::max(a,b);
//     int mm = std::max(m,c);
    
//     if (a == mm)cout<<1<<endl;
//     else if (b == mm)cout<<2<<endl;
//     else cout<<3<<endl;

//     return 0;

// }


#include<iostream>
using namespace std;
 
int main()
{
    int a ,b,k;
    cin>>a>>b>>k;
    if(a%k==0 && b%k==0)cout<<"Both"<<endl;
    else if(a%k==0 && b%k!=0)cout<<"Memo"<<endl;
    else if(a%k!=0 && b%k==0)cout<<"Momo"<<endl;
    else cout<<"No One"<<endl;
    return 0;
}





