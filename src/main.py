from globals import (
    REPOS,
    BRANCH_NAME,
    CONFIG_PATH,
    REQUIREMENTS_PATH,
    REQUIREMENTS_DEV_PATH,
    DOCKER_IMAGE,
    DOCKER_VERSION,
    PULL_REQUEST_TITLE,
    PULL_REQUEST_BODY,
    RELEASE_TITLE,
    RELEASE_BODY,
)

from utils import update_config, merge, release, update_requirements

# todo_repos = ["my-custom-nn-detection-model"]
todo_repos = [
    "convert-yolov5-to-supervisely-format",
    "copy-project-between-instances",
]

completed_repos = []
failed_config_repos = []
failed_reqs_repos = []
for repo in REPOS:
    if repo.name not in todo_repos:
        continue

    try:
        # Check if the repository has config.json
        contents = repo.get_contents(CONFIG_PATH)
    except Exception as e:
        print(f"Couldn't process '{CONFIG_PATH}' in {repo.name}. Repo is skipped. Error: {e}")
        continue

    try:
        # create branch if not exists
        default_branch = repo.get_branch(repo.default_branch)
        branch_ref = repo.create_git_ref(
            ref=f"refs/heads/{BRANCH_NAME}", sha=default_branch.commit.sha
        )
        branch = repo.get_branch(BRANCH_NAME)
    except:
        branch = repo.get_branch(BRANCH_NAME)

    try:
        # find and read config.json
        update_config(
            repo, branch.name, CONFIG_PATH, PULL_REQUEST_TITLE, DOCKER_IMAGE, DOCKER_VERSION
        )
    except Exception as e:
        print(f"Couldn't update '{CONFIG_PATH}' in {repo.name}. Repo is skipped. Reason: {e}")
        failed_config_repos.append(repo)
        continue

    try:
        # find and read requirements.txt
        update_requirements(
            repo, branch.name, REQUIREMENTS_PATH, REQUIREMENTS_DEV_PATH, DOCKER_VERSION
        )
    except Exception as e:
        print(f"Couldn't update '{REQUIREMENTS_PATH}' in {repo.name}. Reason: {e}")
        failed_reqs_repos.append(repo)

    completed_repos.append(repo)


for repo in completed_repos:
    merge(repo, BRANCH_NAME, PULL_REQUEST_TITLE, PULL_REQUEST_BODY)
    release(repo, RELEASE_TITLE, RELEASE_BODY)
