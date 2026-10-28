@echo off
echo ===================================================
echo Starting ShopEase Django E-Commerce Web Server...
echo ===================================================

REM Check virtual environment in root or parent
if exist "..\venv\Scripts\python.exe" (
    set PYTHON=..\venv\Scripts\python.exe
) else if exist "venv\Scripts\python.exe" (
    set PYTHON=venv\Scripts\python.exe
) else (
    set PYTHON=python
)

echo Using Python: %PYTHON%
echo Running migrations...
%PYTHON% manage.py migrate --no-input

echo Populating / verifying sample database data...
%PYTHON% populate_data.py

echo Starting development server on http://127.0.0.1:8080/
echo Open http://127.0.0.1:8080/ in your browser.
echo Press CTRL+C to stop.
%PYTHON% manage.py runserver 127.0.0.1:8080
pause
