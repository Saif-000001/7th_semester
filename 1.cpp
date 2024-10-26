// Special Queries
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {
    int Q;
    cin >> Q;
    queue<string> q;

    while (Q--) {
        int command;
        cin >> command;

        if (command == 0) {
            string name;
            cin >> name;
            q.push(name);
        } else if (command == 1) {
            if (!q.empty()) {
                cout << q.front() << endl;
                q.pop();
            } else {
                cout << "Invalid" << endl;
            }
        }
    }
    return 0;
}
