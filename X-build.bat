@echo off

set path-in=.\source
set path-out=.\DKubeX
set doctype=User Guide

rmdir .\DKubeX /S /Q

sphinx-build -b html -D html_title="%htmltitle%" %path-in% %path-out%
rem sphinx-autobuild -b html -D html_title="DKubeX User Guide" %path-in% %path-out%


