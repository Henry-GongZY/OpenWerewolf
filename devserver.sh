#!/bin/sh
export PATH="$HOME/.local/bin:$PATH"

poetry install
source .venv/bin/activate

if ! grep -q "$PATH" /home/user/.bashrc; then
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> /home/user/.bashrc
fi

if [ -z "$PORT" ]; then
  echo "PORT environment variable not set. Using default port 5000."
  python -m flask --app src/main run -p 5000 --debug
else
  python -m flask --app src/main run -p $PORT --debug
fi