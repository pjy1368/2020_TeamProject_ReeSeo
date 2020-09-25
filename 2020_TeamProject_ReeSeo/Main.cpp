#include <filesystem>
#include <iostream>
#include <string>
#include "Account.h"

namespace fs = std::filesystem;
using namespace std;

int main() {
	string path = "./user";
	Account* account = new Account();
	if (account->isMember(path)) {
		cout << "계정을 새로 만드시겠습니까? yes or no";
		string ans;
		cin >> ans;

		if (ans == "yes") {
			account->create(path);
		}

	}
	else {
		cout << "1. 계정 초기화\n";
		cout << "2. 기존 계정 사용하기\n";

		string ans;
		cin >> ans;

		if (ans == "1") {
			account->clear(path);
		}
		else if (ans == "2") {

		}
	}

}