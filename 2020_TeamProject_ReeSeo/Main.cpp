#include <filesystem>
#include <iostream>
#include <string>

namespace fs = std::filesystem;
using namespace std;

// �׽�Ʈ �ּ� �߰�

int main() {
	if (!fs::exists("./user")) {
		cout << "������ ���� ����ðڽ��ϱ�? (yes or no) : ";

		string ans;
		cin >> ans;

		if (ans == "yes") {
			fs::create_directory("./user");
		}
	}
	else {
		cout << "1. ���� �ʱ�ȭ\n";
		cout << "2. ���� ���� ����ϱ�\n";

		string ans;
		cin >> ans;

		if (ans == "1") {
			fs::remove("./user");
		}
		else if (ans == "2") {

		}
	}

}