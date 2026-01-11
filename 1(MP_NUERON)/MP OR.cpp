#include <iostream>
using namespace std;

int MP_OR(int x1, int x2) {
    
    int theta = 1;

    int sum =  x1 +  x2;
    return (sum >= theta) ? 1 : 0;
}

int main() {
    cout << MP_OR(0,0) << endl;
    cout << MP_OR(0,1) << endl;
    cout << MP_OR(1,0) << endl;
    cout << MP_OR(1,1) << endl;
}
