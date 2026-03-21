@echo off

REM Ensure script runs from repository root
cd /d "%~dp0"

REM Move to SIMCO Logic project folder
cd /d "e:\quiz\SIMCO Logic"

REM Start SIMCO Logic API
e:\quiz\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8010

REM Wait for user input to close
pause
