import os
from src.globals import API
from tqdm import tqdm

dev_apps_checkbox = False
projects_checkbox = False
not_released_checkbox = False
custom_docker_checkbox = True
private_apps_checkbox = False

app_docker_map = {}
# app name
# repo name
# path to config
# path to dockerfile
# path to gh action
# path to requirements.txt


supervisely_apps = API.app.get_list_ecosystem_modules()
with tqdm(message="Fetching applications", total=len(supervisely_apps)) as pbar:
    for app in supervisely_apps:
        # if app["name"] == "Train YOLOv5":
        # print("yes")

        if app["isPrivate"] is True and not private_apps_checkbox:
            pbar.update(1)
            continue

        if not projects_checkbox and app["type"] == "project":
            pbar.update(1)
            continue

        app_categories = app["config"].get("categories")
        if not dev_apps_checkbox and "development" in app_categories:
            pbar.update(1)
            continue

        app_name = app["name"]
        if not dev_apps_checkbox and app_name.startswith("[dev]"):
            pbar.update(1)
            continue

        app_docker_image = app["config"].get("docker_image")
        if app_docker_image is None:
            app_docker_image = "Not specified"

        if not not_released_checkbox and app_docker_image == "Not specified":
            pbar.update(1)
            continue

        if custom_docker_checkbox and app_docker_image.startswith("supervisely/base-py-sdk"):
            pbar.update(1)
            continue

        app_config_path = f"https://github.com/{app['slug']}"
        app_root_dir = app["pathPrefix"]
        app_docker_map[app_name] = {
            "repo_name": app_docker_image,
            "config_path": f"{app_root_dir}/config.json",
            "action_path": ".github/workflows/build_image.yml",
            "docker_path": "Dockerfile",
            "requirements_path": f"{app_root_dir}/dev_requirements.txt",
        }
        pbar.update(1)


print(app_docker_map)
