@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

set "file_input="
for %%I in (*.json) do (
    if /I not "%%~nxI"=="trimmed.json" (
        set "file_input=%%~nxI"
        goto :found
    )
)

:found
echo File found: %file_input%
goto :input

:endlocal

:input
echo How much context to leave?
echo Default 10000
set /p amount=

if "!amount!"=="" (
    set "amount=10000"
)

goto :start

:start
python .\trimmer.py -i .\%file_input% -o .\trimmed.json -a %amount%
