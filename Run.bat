@echo off
echo Installation in progress
cd /d %~dp0
python -m pip install -r requirements.txt
echo Installation completed
set /p choix=Execute main.py ? (y/n) : 
if /i "%choix%"=="y" (
    python main.py
) else (
    if /i "%choix%"=="n" (
        echo Ok see you later
    ) else (
        echo Invalid choice
    )
)
