#! /bin/bash
exec 2>error.log
[ -z "${TELEGRAM_TOKEN}" ] && read -p "paste your telegram token here" TE\
LEGRAM_TOKEN && echo -e "TELEGRAM_TOKEN=${TELEGRAM_TOKEN}" >"${HOME}"/.ba\
shrc && source "${HOME}/.bashrc"
[ $? -ne 0 ] && echo "something went wrong, set your token as TELEGRAM_TO\
KEN in your .bashrc, .bash_profile, /etc/environment or /etc/profile and \
try again" && exit 2
source "$PWD"/.venv/bin/activate &&
python3 "$PWD"/terikov.py