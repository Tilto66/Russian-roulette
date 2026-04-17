@echo off
cd /d %~dp0
echo Installation in progress 
python -m pip install -r requirements.txt
echo Installation completed

:question
set /p comp=Do you want to compile it ? (y/n) : 
if /i "%comp%"=="y" goto yes
if /i "%comp%"=="n" goto no
echo Invalid choice
goto question

:yes
python -m pip install pyinstaller
python -m PyInstaller --onefile Russianroulette.py 
echo Done ! 
pause
goto question

:no
set /p choix=Execute Russianroulette.py ? (y/n) : 
if /i "%choix%"=="y" (
    python Russianroulette.py
) else (
    if /i "%choix%"=="n" (
        echo Ok see you later
    ) else (
        echo Invalid choice
        goto no
    )
)
