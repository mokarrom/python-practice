#!/bin/bash

printf "\e[1mBootstrap Git for your package.\e[0m\n"
printf "More information at \e[92m\e[4mhttps://python.labs.thomsonreuters.com/get-started/bootstrap-git/\e[24m\e[0m\n\n"
printf "\e[1mExecuting this script will:\e[0m\n"
printf "  \e[36m1.\e[0m Initialize a new Git repository\n"
printf "  \e[36m2.\e[0m Perform an initial commit of your package's files\e[0m\n"
printf "  \e[36m3.\e[0m Install Git hooks\e[0m\n\n"
printf "\e[1mPress ENTER to execute...\e[0m"
read

if [ ! -d .git ]; then
    git init
    git add .
    git commit -m "Initial commit."
    git branch -M main
    git remote add origin https://github.com/mokarrom/python-practice.git
fi;

if [ ! -f .git/hooks/pre-commit ]; then
    poetry run pre-commit install
fi

printf "\e[1mCOMPLETE\e[0m\n"
