#!/bin/bash

# kill all tmux sessions
# tmux kill-server

# enter repository
cd dancing-ducks-lucy

# make sure repository is up to date
git fetch && git reset origin/main --hard

# install requirements into the virtualenv
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
# deactivate
# echo "deactivate successful? $?"

# start new detached tmux session to run the website
# use tmux send-keys function to send commands to detached tmux session
# NAME=portfolio
# tmux new -d -s $NAME
# tmux send-keys -t $NAME 'source python3-virtualenv/bin/activate' ENTER
# tmux send-keys -t $NAME 'flask run --host=0.0.0.0' ENTER
systemctl restart myportfolio
