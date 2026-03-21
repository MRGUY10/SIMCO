@echo off

REM Ensure script runs from repository root
cd /d "%~dp0"

REM Start face classification API
e:\quiz\face_classification\.venv310\Scripts\python.exe -m uvicorn face_classification.src.web.faces:app --host 127.0.0.1 --port 8084

REM Wait for user input to close
pause