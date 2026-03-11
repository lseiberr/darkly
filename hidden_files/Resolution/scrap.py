import requests
import time

def check_readme_in_hidden_files(url):
	response = requests.get(url)
	if response.status_code == 200 and "README" in response.text:
		return True
	else:
		return False

def download_readme(url):
	response = requests.get(url+ "README")
	if response.status_code == 200:
		with open("README.txt", "w") as file:
			file.write(response.text)


def check_values_in_readme():
	with open("README.txt", "r") as file:
		content = file.read()
		if "flag" in content.lower():
			print("Flag found in README!")
			return True
		else:
			return False

def delete_readme():
	import os
	if os.path.exists("README.txt"):
		os.remove("README.txt")

def get_all_links(url):
	response = requests.get(url)
	if response.status_code == 200:
		links = []
		for line in response.text.splitlines():
			if "href" in line and "../" not in line and "css" not in line:
				start = line.find("href=") + 6
				end = line.find('"', start)
				links.append(line[start:end])
		return links
	else:
		return []

def loop_links(links, url):
	for link in links:
		print(f"Checking link: {url + link}")
		check_readme_in_hidden_files(url)
		download_readme(url)
		if check_values_in_readme():
			print("Flag found! Ending search.")
			return True
		else:
			delete_readme()
			return False

def recursive_search(url):
	links = get_all_links(url)
	if loop_links(links, url):
		return True
	for link in links:
		if recursive_search(url + link + "/"):
			return True
	return False

def main():
	url = "http://192.168.64.17/.hidden/"
	recursive_search(url)



if __name__ == "__main__":
	main()
