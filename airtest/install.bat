@echo off
adb devices >1.txt
set /p var1=input apk name : 
for /f %%a in (.\1.txt) do (
if  not '%%a'=='List' (
echo devices : %%a
adb -s %%a uninstall com.bingo.cruise.free.best.top.game
adb -s %%a install d:/Downloads/%var1%
)
)
pause
