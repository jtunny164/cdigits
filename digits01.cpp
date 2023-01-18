#include <iostream>
#include <cmath>
using namespace std;

int * getDigits(long n) {
    // turn a 10-digit number into an array of its digits
    static int digits[10];
    for (int d=0; n>0; d++) {
        digits[9-d] = n % 10;
        n /= 10;
    }
    return digits;
}

bool usesAllDigits(int* d) {
    // Ugly, probably better ways to do this
    bool used[10];
    for (int i=0; i<10; i++) {
        used[i] = false;
        for (int k=0; k<10; k++) {
            if (d[k] == i) {
                used[i] = true;
            }
        }
    }
    for (int i=0; i<10; i++) {
        if (used[i] == false) {
            return false;   // fail if any not used
        }
    }
    return true;    // all digits 0-9 were used
}

bool testConstraints(int* d) {
    bool result = false;
    if (usesAllDigits(d)) {
        // See if the digits meet the divisibility constraints
        result = true;
        for (int n=0; result && (n<10); n++) {
            long k = 0;
            for (int i=0; i<=n; i++) {
                k += d[i] * std::pow(10, n-i);
                result = k % (n + 1) == 0;  // check for divisibility
            }
            //std::cout << "Number: " << k << endl;
        }
    }
    return result;
}

int main() {
    int * digits;
    long val;
	for (val=3816545000; val < 3816550000; val++) {		// there happens to be a solution in this range
		digits = getDigits(val);
		bool ok = testConstraints(digits);
		if (ok) {
			std::cout << "Value of " << val << " is a solution!" << endl;
		}
	}
    return 0;
}
