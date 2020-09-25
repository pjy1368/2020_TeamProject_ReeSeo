#include <filesystem>
#include <iostream>
#include <string>

namespace fs = std::filesystem;
using namespace std;

// 테스트 주석 추가

int main() {
	if (!fs::exists("./user")) {
		cout << "계정을 새로 만드시겠습니까? (yes or no) : ";

		string ans;
		cin >> ans;

		if (ans == "yes") {
			fs::create_directory("./user");
		}
	}
	else {
		cout << "1. 계정 초기화\n";
		cout << "2. 기존 계정 사용하기\n";

		string ans;
		cin >> ans;

		if (ans == "1") {
			fs::remove("./user");
		}
		else if (ans == "2") {

		}
	}

}