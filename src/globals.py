import os

from dotenv import load_dotenv
from github import Auth, Github
from supervisely.api.api import Api
from utils import get_latest_tag

load_dotenv("secret.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

# load_dotenv("github.env")

API = Api()

GITHUB_API_URL = os.environ.get("GITHUB_API_URL")
GITHUB_USER_NAME = os.environ.get("GITHUB_USER_NAME")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

AUTH = Auth.Token(GITHUB_TOKEN)
GIT = Github(GITHUB_TOKEN)

USER = GIT.get_user()
ORG_NAME = "supervisely-ecosystem"
ORG = GIT.get_organization(ORG_NAME)
# REPOS = USER.get_repos()
REPOS = ORG.get_repos()  # 432 repos

BRANCH_NAME = "update-docker-image"
CONFIG_PATH = "config.json"
REQUIREMENTS_PATH = "requirements.txt"
REQUIREMENTS_DEV_PATH = "dev_requirements.txt"

DOCKER_IMAGE = "supervisely/base-py-sdk"
DOCKER_VERSION = get_latest_tag(DOCKER_IMAGE)  # "6.72.70"

# SLY_VERSION = get_latest_sly_version(GIT)

PULL_REQUEST_TITLE = f"Update docker image in config.json to {DOCKER_IMAGE}/{DOCKER_VERSION}"
PULL_REQUEST_BODY = f"This pull request has been automatically created and merged by [{USER.login}]({USER.html_url})."

RELEASE_TITLE = f"Update docker image to {DOCKER_IMAGE}/{DOCKER_VERSION}"
RELEASE_BODY = f"This release has been automatically created by [{USER.login}]({USER.html_url})."
