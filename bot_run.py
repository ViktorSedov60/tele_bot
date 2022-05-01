@echo off

call %~dp0telegramm_bot\venv\Scripts\activate

cd %1dp0telegramm_bot
set TOKEN-=5321695565:AAFlb2BdS8UfZjNknIKn4sAysymfst8lJag

python bot_telegram.py

pause