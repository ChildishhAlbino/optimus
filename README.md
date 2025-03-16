# Optimus
Orchestrate & Automate file transformations. WIP

## Goals
- dynamically add and remove jobs that automate repeated tasks
- use folder names to determine which automation needs to be run
- Installed deps:
    - ffmpeg
    - MKVToolNix
    - python

## Design

- The app will run in a docker container
- The container will have two volumes required - /files and /jobs
    - /files is a volume containing files that must be acted upon
    - /jobs is a volume containing the associated scripts that act upon files
- The files directory will contain subdirectories that follow the pattern of `{<job-name>_<positional args>}`
    - i.e. `split-on-chapters_6`
- The jobs directory will contain shell scripts with the pattern of `<job-name>.sh`
    - i.e. `split-on-chapters.sh`
    - These shell files can perform the operation themselves or pass it off to a python script.