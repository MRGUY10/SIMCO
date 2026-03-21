@echo off

REM Activate Python virtual environment
call .venv\Scripts\activate

REM Start the backend server
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000

REM Wait for user input to close
pause
