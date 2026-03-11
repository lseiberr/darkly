import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_url():
	start_url = "http://192.168.64.17/"
	visited = set()
	to_visit = [start_url]
	domain = urlparse(start_url).netloc
	while to_visit:
		url = to_visit.pop()
		if url in visited:
			continue
		visited.add(url)
		try:
			response = requests.get(url, timeout=5)
			soup = BeautifulSoup(response.text, "html.parser")
			for link in soup.find_all("a", href=True):
				href = link["href"]
				full_url = urljoin(url, href)
				if urlparse(full_url).netloc == domain:
					if full_url not in visited:
						to_visit.append(full_url)
		except:
			pass
	return visited

def get_all_urls():
	urls = extract_url()
	with open("urls.txt", "w") as file:
		for url in urls:
			file.write(url + "\n")

def main():
	get_all_urls()

if __name__ == "__main__":
	main()
