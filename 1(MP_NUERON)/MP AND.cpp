#include <iostream>
using namespace std;

int MP_AND(int x1, int x2) {
    int w1 = 1, w2 = 1;
    int theta = 2;

    int sum = w1 * x1 + w2 * x2;
    return (sum >= theta) ? 1 : 0;
}

int main() {
    cout << MP_AND(0,0) << endl;
    cout << MP_AND(0,1) << endl;
    cout << MP_AND(1,0) << endl;
    cout << MP_AND(1,1) << endl;
}
