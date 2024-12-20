#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Import data from db.json
python manage.py loaddata db.json

# create superuser if missing
echo "
import os
from django.contrib.auth import get_user_model

User = get_user_model()

User.objects.filter(username=os.environ['DJANGO_SUPERUSER_USERNAME']).exists() or \
    User.objects.create_superuser(os.environ['DJANGO_SUPERUSER_USERNAME'], os.environ['DJANGO_SUPERUSER_EMAIL'], os.environ['DJANGO_SUPERUSER_PASSWORD'])
" | python manage.py shell