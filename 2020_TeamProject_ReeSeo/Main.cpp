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
		cout << "������ ���� ����ðڽ��ϱ�? yes or no";
		string ans;
		cin >> ans;

		if (ans == "yes") {
			account->create(path);
		}

	}
	else {
		cout << "1. ���� �ʱ�ȭ\n";
		cout << "2. ���� ���� ����ϱ�\n";

		string ans;
		cin >> ans;

		if (ans == "1") {
			account->clear(path);
		}
		else if (ans == "2") {

		}
	}

}