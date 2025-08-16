import requests
import streamlit as st

GITHUB_USERNAME = "Fanu2"
GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

def get_all_public_repos():
    repos = []
    page = 1
    while True:
        response = requests.get(f"{GITHUB_API_URL}?per_page=100&page={page}")
        if response.status_code != 200:
            st.error(f"Error: {response.status_code} - {response.text}")
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

st.title("My GitHub Public Repositories")
all_public_repos = get_all_public_repos()
for repo in all_public_repos:
    st.markdown(f"- [{repo['name']}]({repo['html_url']})")
