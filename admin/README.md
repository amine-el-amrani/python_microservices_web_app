## How to build ?


### Docker

```bash
# pulls up the back-end infra
docker compose up --force-recreate

# pulls it down
docker compose down

# remove the image to force-update the back-end
docker rmi -f admin-backend

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
python manage.py runserver
