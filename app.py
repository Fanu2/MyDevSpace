import streamlit as st
import requests

GITHUB_USERNAME = "Fanu2"
GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

def get_repos():
    response = requests.get(GITHUB_API_URL)
    return response.json()

st.title("My Projects and Repos")

st.header("GitHub Repositories")
repos = get_repos()
for repo in repos:
    st.markdown(f"- [{repo['name']}]({repo['html_url']})")

st.header("Deployed Projects")
st.markdown("- [My Streamlit App](https://your-streamlit-app-url)")
st.markdown("- [My Vercel Project](https://your-vercel-project-url)")
