@echo off

set EXE_FILE='R-4.3.1-win.exe'

start "" 'R-4.3.1-win.exe'

:WAIT_LOOP
timeout /t 1 /nobreak >nul
tasklist | find /i 'R-4.3.1-win.exe' >nul
if errorlevel 1 (
    echo File 'R-4.3.1-win.exe' is closed.
    del "%EXE_FILE%"
    echo File 'R-4.3.1-win.exe' has been removed.
    exit /b
)
goto WAIT_LOOP

