## How to build ?


### Docker

```bash
# pulls up the back-end infra
docker compose up --force-recreate

# pulls it down
docker compose down

# remove the image to force-update the back-end
docker rmi -f main-backend

```


### Locally

```bash
# Run these once

# Create virtual-env
python3 -m venv ~/.local/venv_micro

# Load virtual-env
. ~/.local/venv_micro/bin/activate

# install dependencies
pip install -r requirements.txt

# run the server
python main.py

# Set the FLASK_APP environment variable before using Flask CLI commands
export FLASK_APP=main.py

# Initialize migrations (if not already done):
flask db init

# Create a migration file after modifying models:
flask db migrate -m "migration description"

#Apply the migrations to the database:
flask db upgrade

# To revert a migration (downgrade):
flask db downgrade

```