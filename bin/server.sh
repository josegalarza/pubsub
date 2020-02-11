#!/usr/bin/env bash

main() {
    local repo_root
    repo_root=$(git rev-parse --show-toplevel)
    pipenv run python "${repo_root}/src/server.py" "$@"
}

main "$@"
