@ECHO OFF

SET PARAMS=

:_PARAMS_LOOP

REM There is a trailing space in the next line; it is there for formatting.
SET PARAMS=%PARAMS% "%~1"
ECHO %~1
SHIFT

IF NOT "%~1"=="" GOTO _PARAMS_LOOP

ECHO %PARAMS%
python addMargin_Symmetric.py %PARAMS%
REM move test.pdf "C:\Users\William\Desktop\test.pdf"

pause