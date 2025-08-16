import requests

GITHUB_USERNAME = "Fanu2"
GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

def get_all_public_repos():
    repos = []
    page = 1
    while True:
        response = requests.get(f"{GITHUB_API_URL}?per_page=100&page={page}")
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

# Usage
all_public_repos = get_all_public_repos()
for repo in all_public_repos:
    print(repo['name'], repo['html_url'])
