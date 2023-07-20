import os
import base64
import requests
from dotenv import load_dotenv
from github import Github, Auth

from updater import get_config, push_changes

load_dotenv("secret.env")
# load_dotenv("github.env")

# TODO: fix config encoding/decoding

github_api_url = os.environ.get("GITHUB_API_URL")
username = os.environ.get("GITHUB_USER_NAME")
access_token = os.environ.get("GITHUB_TOKEN")

auth = Auth.Token(access_token)
g = Github(access_token)

branch_name = "test-b"
remote_config_path = "config.json"
docker_version = "9.99.99"

repos = g.get_user().get_repos()
for repo in repos:
    if repo.name.startswith("my-custom-nn-detection-model"):
        # create new branch
        try:
            default_branch = repo.get_branch(repo.default_branch)
            branch_ref = repo.create_git_ref(
                ref=f"refs/heads/{branch_name}", sha=default_branch.commit.sha
            )
            branch = repo.get_branch(branch_name)
        except:
            branch = repo.get_branch(branch_name)

        data = get_config(repo.full_name, remote_config_path, access_token)
        push_changes(repo, remote_config_path, data, docker_version, branch)
        print(f"Docker image for {repo.name} has been updated")
