#!/bin/bash

git push origin main
echo '
check_okay () { if [ $? != 0 ]; then echo "----- $1 -----" ; exit; fi };
echo ----------------- inside server -----------------
cd /var/www/html/orange/
git pull origin main
check_okay "error pulling code"
echo ----------------- done pulling code -----------------
source env/bin/activate
pip install -r requirements.txt
check_okay "error installing requirments"
echo ----------------- done updating requirements -----------------
python manage.py migrate
# python manage.py compilemessages
# python manage.py update_translation_fields
check_okay "error migrating"
echo ----------------- done migration -----------------
sudo  supervisorctl restart orange
check_okay "error restarting"
echo ----------------- done restarting supervisor task -----------------
' | ssh my-server