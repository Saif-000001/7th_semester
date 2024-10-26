// Elimination
#include <bits/stdc++.h>
using namespace std;

bool canEliminate(string& s) {
    stack<char> st;
    for (char c : s) {
        if (!st.empty() && st.top() != c) {
            st.pop();
        } else {
            st.push(c);
        }
    }
    return st.empty();
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        string S;
        cin >> S;

        cout << (canEliminate(S) ? "YES" : "NO") << endl;
    }

    return 0;
}
