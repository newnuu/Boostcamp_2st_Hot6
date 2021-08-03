#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct str {
	string s;
	int len;
	str(string ss, int l) {
		s = ss;
		len = l;
	}

	bool operator<(const str &d) {
		return len < d.len;
	}
};

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	int N, res=0;
	cin >> N;
	vector<str> s;
	for (int i = 0; i < N; i++) {
		string tmp;
		cin >> tmp;
		s.push_back(str(tmp, tmp.size()));
	}
	sort(s.begin(), s.end());
	for(int i = 0; i < s.size(); i++) {
		bool hasPrefix = false;
		for(int j = i + 1; j < s.size(); j++) {
			if(s[j].s.find(s[i].s) == 0 ) {
				 hasPrefix = true;
			}
		}
		if(hasPrefix) res++;
	}
	cout << N - res << "\n";
}
