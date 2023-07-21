import json
import os

from dotenv import load_dotenv
from github import Auth, ContentFile, Github


def update_config(contents: ContentFile, version: str):
    json_content = contents.decoded_content.decode("utf-8")
    data = json.loads(json_content)
    data["docker_image"] = f"supervisely/base-py-sdk:{version}"
    updated_json_content = json.dumps(data, indent=4)
    return updated_json_content, contents.sha


load_dotenv("secret.env")
# load_dotenv("github.env")

github_api_url = os.environ.get("GITHUB_API_URL")
username = os.environ.get("GITHUB_USER_NAME")
access_token = os.environ.get("GITHUB_TOKEN")
org_name = "supervisely-ecosystem"

auth = Auth.Token(access_token)
g = Github(access_token)


user = g.get_user()
org = g.get_organization(org_name)
# repos = org.get_repos()
# for repo in repos:  # 432 repos
# print(repo.name)


branch_name = "update-docker-image"
remote_config_path = "config.json"
docker_version = "7.77.76"

repos = user.get_repos()
for repo in repos:
    if not repo.name == "my-custom-nn-detection-model":
        continue

    try:
        # Check if the repository has config.json
        contents = repo.get_contents(remote_config_path)
    except:
        print(f"Couldn't find '{remote_config_path}' in {repo.name}. Repo is skipped")
        continue

    try:
        # create branch if not exists
        default_branch = repo.get_branch(repo.default_branch)
        branch_ref = repo.create_git_ref(
            ref=f"refs/heads/{branch_name}", sha=default_branch.commit.sha
        )
        branch = repo.get_branch(branch_name)
    except:
        branch = repo.get_branch(branch_name)

    try:
        # find and read config.json
        contents = repo.get_contents(remote_config_path, ref=branch.name)
        data, sha = update_config(contents, docker_version)
    except:
        print(f"Couldn't read '{remote_config_path}' in {repo.name}. Repo is skipped")
        continue

    repo.update_file(
        path=remote_config_path,
        message=f"Update docker image in config.json to v{docker_version}",
        content=data,
        sha=sha,
        branch=branch.name,
    )
    print(f"Docker image for {repo.name} has been updated")
    break
