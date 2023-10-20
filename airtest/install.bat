adb devices
set /p var=input apk name : 
echo %var%
adb -s R58M66VY68Y uninstall com.bingo.cruise.free.best.top.game
adb -s R58M66VY68Y install d:/Downloads/%var%
pause