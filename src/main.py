from globals import (
    REPOS,
    BRANCH_NAME,
    CONFIG_PATH,
    DOCKER_IMAGE,
    DOCKER_VERSION,
    PULL_REQUEST_TITLE,
    PULL_REQUEST_BODY,
    RELEASE_TITLE,
    RELEASE_BODY,
)

from utils import update_config, merge, release

todo_repos = ["import-images-in-sly-format"]
completed_repos = []

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
        contents = repo.get_contents(CONFIG_PATH, ref=branch.name)
        data, sha = update_config(contents, DOCKER_IMAGE, DOCKER_VERSION)
    except Exception as e:
        print(f"Couldn't update '{CONFIG_PATH}' in {repo.name}. Repo is skipped. Reason: {e}")
        completed_repos.append(repo)
        continue

    repo.update_file(
        path=CONFIG_PATH,
        message=PULL_REQUEST_TITLE,
        content=data,
        sha=sha,
        branch=branch.name,
    )
    print(f"Docker image for {repo.name} has been updated")
    completed_repos.append(repo)
    if len(completed_repos) == len(todo_repos):
        break


for repo in completed_repos:
    merge(repo, BRANCH_NAME, PULL_REQUEST_TITLE, PULL_REQUEST_BODY)
    release(repo, RELEASE_TITLE, RELEASE_BODY)
