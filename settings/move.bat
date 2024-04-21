@echo off 
:: Define the source folder. 
set "sourcePath=C:\Users\Sarah\AppData\Roaming\talon\user\my-talon-adaptations\settings" 
 
:: Define the destination folder. 
set "destinationPath=C:\Users\Sarah\AppData\Roaming\talon\user\community\settings" 
 
:: Use xcopy to copy the folder. 
xcopy /E /I "%sourcePath%" "%destinationPath%" 