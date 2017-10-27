@echo off
set p=D:\BingWallpaper\
schtasks /create /tn "BingWallpaperDownloader" /tr "C:\Python36\python.exe '%p%GetWallpaper.py'" /sc daily /st 10:00
copy  /y "%p%config\Startup.bat" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Startup.bat"