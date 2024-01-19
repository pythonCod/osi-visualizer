@echo off
echo.
echo #################################
echo # Building OSI Visualizer
echo #################################
echo.

REM Create a build directory
if not exist build mkdir build
cd build

REM Configure the project with CMake
REM cmake -G "MinGW Makefiles" .. 
REM If using MSVC, replace the above line with:
cmake -G "Visual Studio 16 2019" ..

REM Build the project
REM mingw32-make -j8
REM If using MSVC, replace the above line with:
msbuild OSI-Visualizer.sln /p:Configuration=Release /m
