@echo off
call env\Scripts\activate.bat
start /B uvicorn app:app --reload
pause