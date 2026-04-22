@echo off
title SentinelNode Monitor
echo ====================================================
echo           SENTINEL NODE - INITIALIZING
echo ====================================================

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR]: Python not found. Please install Python 3.
    pause
    exit /b
)

if not exist "venv" (
    echo [1/3] Creating isolated virtual environment...
    python -m venv venv
)

echo [2/3] Installing/Updating required tools...
call venv\Scripts\activate
pip install -r requirements.txt --quiet

echo [3/3] Launching SentinelNode...
echo ----------------------------------------------------
python main.py
pause