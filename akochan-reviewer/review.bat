@echo off
:a
set /p url=Enter Tenhou / Mahjong Soul replay url= 
set OMP_NUM_THREADS=8
akochan-reviewer.exe --lang en --without-viewer %url%
goto a