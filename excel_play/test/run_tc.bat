@echo off
echo Iteration 30
@echo on
@echo off
echo Time Stamp is: %DATE% %TIME%
echo %USERNAME%
echo %USERDOMAIN%
ver
@echo on
@echo off
pushd %~dp0
echo.
echo.
echo.
echo.
echo "cli_read_me_25"

cd ..
cd ..
cd scripts
call activate_vir_env.bat
cd ..
python -m excel_play.main.excelplay "--help" > excel_play\test\logs\cli_read_me_25.log
cd scripts
call deactivate_vir_env.bat
cd ..
echo.
echo.
echo.
echo.
echo "Batch Execution Done"

@echo on