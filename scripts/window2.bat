update the script, to be able to 


@echo off
mode 90,45
rem con:cols=90 lines=100
title Llama2Robot-Window2
cls

:: Run the main2.py script
echo Launching Llama2Robot-Window2...
echo.
echo.
@echo on


python main2.py %1 %2
@echo off
echo.
echo.

:: Exiting
echo Llama2Robot-Window2 shutting down...
echo.
echo.
pause
exit /b
