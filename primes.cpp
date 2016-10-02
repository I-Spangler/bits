#include <iostream>
#include<cmath>

using namespace std;

int main(){

    int d;
    cin>>d;
    bool eprimo = true;
    int raiz = sqrt(d);
    for(int i = 2; i <= raiz; i++){
      if(d%i == 0)
        eprimo = false;
    }
    eprimo ? cout<<"sim"<<endl : cout<<"nao"<<endl;

    return 0;
}
