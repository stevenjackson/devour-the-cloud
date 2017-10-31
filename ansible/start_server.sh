export ALLOWED_HOSTS=$(curl -s http://169.254.169.254/latest/meta-data/public-hostname)
export SECRET_KEY=codemash2018
SALEOR_ADDR="${ALLOWED_HOSTS}:8000"

echo "STARTING ON ${SALEOR_ADDR}"
python manage.py runserver $SALEOR_ADDR
