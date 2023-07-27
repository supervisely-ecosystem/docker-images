#!/bin/bash

# The input parameter determines which part of the version to increment (major, minor, or patch)
increment_type=$1

# Replace 'your-docker-repo' and 'your-docker-image' with your Docker repository and image names
DOCKER_REPO=$DOCKER_REPO
DOCKER_IMAGE_NAME=$DOCKER_IMAGE_NAME

# Get the latest tag using Docker Hub API
latest_tag=$(curl -s "https://registry.hub.docker.com/v2/repositories/${DOCKER_REPO}/${DOCKER_IMAGE_NAME}/tags/?page_size=1" | jq -r '.results[0].name')

# Extract the version number from the tag
version=$(echo "$latest_tag" | sed -E 's/^v([0-9]+\.[0-9]+\.[0-9]+)$/\1/')

# Increment the version based on the selected type (major, minor, or patch)
IFS='.' read -r -a version_parts <<< "$version"
new_major=${version_parts[0]}
new_minor=${version_parts[1]}
new_patch=${version_parts[2]}

if [[ "$increment_type" == "Major" ]]; then
  ((new_major++))
  new_minor=0
  new_patch=0
elif [[ "$increment_type" == "Minor" ]]; then
  ((new_minor++))
  new_patch=0
elif [[ "$increment_type" == "Patch" ]]; then
  ((new_patch++))
fi

# Assemble the new tag
new_tag="v${new_major}.${new_minor}.${new_patch}"

echo "$new_tag"
