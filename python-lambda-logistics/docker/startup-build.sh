#!/usr/bin/env bash
# Used to initiate a build and package process

APP_HOME='/app'
APP_TMP='/tmp/app'
APP_VENV="$APP_TMP/venv"
APP_PACKAGES="$APP_TMP/build/site-packages"
APP_CACHE="$APP_TMP/build/pip-cache"
ZIP="$APP_TMP/dist/docker.zip"

# Install venv and packages
pip install --upgrade pip virtualenv
virtualenv --python=python3.6 "$APP_VENV"
"$APP_VENV/bin/pip" install --no-deps -t "$APP_PACKAGES" --cache-dir "$APP_CACHE" -r "$APP_HOME/requirements.txt"

# Zip up everything for distribution
cd "$APP_HOME" && zip -r "$ZIP" * .env --exclude "build/*" --exclude "dist/*" && cd "$APP_PACKAGES" && zip -ur "$ZIP" *