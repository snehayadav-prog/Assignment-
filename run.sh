#!/bin/bash
echo "==================================================="
echo "Starting ShopEase Django E-Commerce Web Server..."
echo "==================================================="

if [ -f "../venv/bin/python" ]; then
    PYTHON="../venv/bin/python"
elif [ -f "venv/bin/python" ]; then
    PYTHON="venv/bin/python"
else
    PYTHON="python3"
fi

$PYTHON manage.py migrate --no-input
$PYTHON populate_data.py
echo "Starting development server on http://127.0.0.1:8080/"
$PYTHON manage.py runserver 127.0.0.1:8080
