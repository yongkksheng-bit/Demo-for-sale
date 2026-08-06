@echo off
chcp 65001 >nul
echo ========================================
echo   火山引擎智能方案顾问 - 一键启动
echo ========================================
echo.

echo [1/2] 启动后端服务...
echo.
cd /d "%~dp0backend"
start "火山引擎智能方案顾问-后端" cmd /k "D:\Anaconda\python.exe main.py"

echo [2/2] 等待后端启动...
timeout /t 3 /nobreak >nul

echo.
echo 启动完成！
echo.
echo 后端地址: http://localhost:8000
echo API 文档: http://localhost:8000/docs
echo.
echo 正在打开前端页面...
start "" "%~dp0frontend\index.html"

echo.
echo 按任意键退出...
pause >nul
