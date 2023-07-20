import requests
import json
import base64
from github import Repository, InputGitTreeElement


def get_config(full_repo_name, file_path, access_token):
    base_url = "https://api.github.com"
    file_url = f"{base_url}/repos/{full_repo_name}/contents/{file_path}"

    try:
        headers = {"Authorization": f"token {access_token}"}
        response = requests.get(file_url, headers=headers)

        if response.status_code == 200:
            file_content = response.json()["content"]
            decoded_content = base64.b64decode(file_content)

            decoded_content_str = decoded_content.decode("utf-8")
            data = json.loads(decoded_content_str)
            data["docker_image"] = "supervisely/base-py-sdk:9.99.99"
            data = json.dumps(data)
            data = base64.b64encode(data.encode("utf-8")).decode("utf-8")
            return data
        else:
            print(f"Failed to read the file: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


def push_changes(repo: Repository, github_file_path, file_content, docker_version, branch=None):
    blob = repo.create_git_blob(content=file_content, encoding="utf-8")
    elements = [
        InputGitTreeElement(path=github_file_path, mode="100644", type="blob", sha=blob.sha)
    ]

    if branch is None:
        branch = repo.get_branch("master")
        head_sha = branch.commit.sha
        base_tree = repo.get_git_tree(sha=head_sha)
        tree = repo.create_git_tree(elements, base_tree)
        parent = repo.get_git_commit(sha=head_sha)

        commit = repo.create_git_commit(
            f"Update docker image in config.json to v{docker_version}", tree, [parent]
        )
        master_ref = repo.get_git_ref(f"heads/{branch.name}")
        master_ref.edit(sha=commit.sha)

    if branch:
        head_sha = branch.commit.sha
        base_tree = repo.get_git_tree(sha=head_sha)
        tree = repo.create_git_tree(elements, base_tree)
        parent = repo.get_git_commit(sha=head_sha)

        commit = repo.create_git_commit(
            f"Update docker image in config.json to v{docker_version}", tree, [parent]
        )
        branch_ref = repo.get_git_ref(ref=f"heads/{branch.name}")
        branch_ref.edit(sha=commit.sha)
