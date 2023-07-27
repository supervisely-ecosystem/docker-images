import json
from github import ContentFile, Github, Repository
import requests


def get_latest_tag(docker_image: str) -> str:
    url = f"https://hub.docker.com/v2/repositories/{docker_image}/tags/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            # API returns tags in descending order of creation date
            # data["results"][0]["name"] - "latest" tag
            return data["results"][1]["name"]
        else:
            return None
    else:
        print(
            f"Failed to fetch tags for repository '{docker_image}'. "
            f"Status code: {response.status_code}"
        )
        return None


def get_latest_sly_version(git: Github) -> str:
    repo = git.get_repo("supervisely/supervisely")
    latest_release = repo.get_latest_release()
    if latest_release:
        return latest_release.tag_name.lstrip("v")
    else:
        print("No releases found for the repository.")
        return None


def increment_release_tag(tag_name):
    parts = tag_name.split(".")
    major, minor, patch = int(parts[0][1:]), int(parts[1]), int(parts[2])
    patch += 1
    updated_tag = f"v{major}.{minor}.{patch}"
    return updated_tag


def validate_docker_version(git: Github, docker_image: str) -> None:
    docker_version = get_latest_tag(docker_image)
    sly_version = get_latest_sly_version(git)
    if docker_version != sly_version:
        raise Exception(
            (
                f"Latest version of Supervisely is {sly_version}, "
                f"but latest version of '{docker_image}' is {docker_version}. "
                "Please update DOCKER_VERSION in globals.py"
            )
        )


def update_config(
    repo: Repository,
    branch_name: str,
    config_path: str,
    commit_message: str,
    docker_image: str,
    version: str,
) -> None:
    # Check if config.json in main branch already has the same docker image
    default_contents = repo.get_contents(config_path, ref=repo.default_branch)
    default_json_content = default_contents.decoded_content.decode("utf-8")
    default_data = json.loads(default_json_content)
    if default_data["docker_image"] == f"{docker_image}:{version}":
        raise ValueError(
            f"docker image in config.json is already updated in main branch: '{docker_image}:{version}'"
        )

    contents = repo.get_contents(config_path, ref=branch_name)
    json_content = contents.decoded_content.decode("utf-8")
    data = json.loads(json_content)

    if not data["docker_image"].startswith(docker_image):
        raise ValueError("docker image in config.json doesn't match the one in globals.py")

    # if data["docker_image"] == f"{docker_image}:{version}":
    #     raise ValueError(
    #         f"docker image in config.json is already updated: '{docker_image}:{version}'"
    #     )

    data["docker_image"] = f"{docker_image}:{version}"
    updated_json_content = json.dumps(data, indent=4)

    repo.update_file(
        path=config_path,
        message=commit_message,
        content=updated_json_content,
        sha=contents.sha,
        branch=branch_name,
    )
    print(f"Docker image for {repo.name} has been updated")


def update_requirements(
    repo: Repository, branch_name, requirements_path: str, dev_requirements_path: str, version: str
) -> None:
    try:
        contents = repo.get_contents(dev_requirements_path, ref=branch_name)
        return
    except:
        contents = repo.get_contents(requirements_path, ref=branch_name)
        requirements = contents.decoded_content.decode("utf-8")
        repo.delete_file(
            requirements_path,
            message="delete requirements.txt",
            sha=contents.sha,
            branch=branch_name,
        )
        repo.create_file(
            dev_requirements_path,
            message="update and rename requirements.txt to dev_requirements.txt",
            content=requirements,
            branch=branch_name,
        )


def merge(repo: Repository, branch_name: str, title: str, body: str):
    try:
        default_branch = repo.get_branch(repo.default_branch)
        head_branch = repo.get_branch(branch_name)
    except Exception as e:
        print(f"Error: {e}")
        return None

    try:
        pull_request = None
        for pr in repo.get_pulls(state="open"):
            if pr.base.ref == default_branch.name and pr.head.ref == head_branch.name:
                pull_request = pr
                break

        if pull_request is None:
            pull_request = repo.create_pull(
                title=title, body=body, base=default_branch.name, head=head_branch.name
            )
            print(f"Pull request created successfully: {pull_request.html_url}")

        # Merge the pull request
        merge_result = pull_request.merge()

        # Delete the branch
        ref = repo.get_git_ref(f"heads/{branch_name}")
        ref.delete()
        print(
            f"Pull request merged successfully for '{repo.name}'. Branch: '{branch_name}' has been deleted."
        )

    except Exception as e:
        print(f"Error: {e}")
        return None


def release(repo: Repository, title: str, body: str) -> None:
    try:
        tag_name = increment_release_tag(repo.get_latest_release().tag_name)
    except:
        tag_name = "v1.0.0"
    repo.create_git_release(tag=tag_name, name=title, message=body)
    print(f"Release: '{tag_name}' created successfully for '{repo.name}'.")
