@echo off
REM Local preview for the academic homepage.
REM Ruby was installed via winget to C:\Ruby33-x64 and is not on the system PATH.
cd /d "%~dp0"
set "PATH=C:\Ruby33-x64\bin;%PATH%"
REM No --incremental: incremental builds do not invalidate pages when
REM _config.yml changes, which silently serves a stale sidebar/nav.
bundle exec jekyll serve --host 127.0.0.1 --port 4000
