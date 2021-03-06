#!/bin/bash

    
# Update apt-get
sudo apt-get update

# Install pyenv prerequisites
echo "--- Installing PYENV Prerequisites---"
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git 

# Cloning Pyenv 
if [ -d "$HOME/.pyenv" ] ;then
echo "PYENV already Cloned" 
else
echo "--- Cloning PYENV ---"
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
fi


# Initializing PYENV
if grep -q PYENV_ROOT "$HOME/.profile" ;then
    echo "PYENV already on PATH"
else
    echo "Adding PYENV to path"
    echo 'PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    echo 'PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.profile
fi

source ~/.profile

# Set Python 3.8.5 as Global Python Version

if grep 3.8.5 <<< "$(python -V 2>&1)" ;then
    echo "Correct Python Version Already Installed"
else
    echo "--- Using PYENV to install Python 3.8.5 ---"
    pyenv install 3.8.5
    pyenv global 3.8.5
fi

# Install Poetry
echo "--- Installing Poetry ---"
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python