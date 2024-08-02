#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.size()) {
            return s;
        }

        int i = 0, d = 1;
        string rows[numRows];
        for (char c : s) {
            rows[i] += c;
            if (i == 0) {
                d = 1;
            } else if (i == numRows - 1) {
                d = -1;
            }
            i += d;
        }  

        string result;
        for (string row : rows) {
            result += row;
        }
        return result;
    }
};