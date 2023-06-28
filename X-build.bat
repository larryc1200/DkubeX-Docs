@echo off

set path-in=.\source
set path-out=.\DKubeX
set doctype=User Guide

rem rmdir .\DKubeX /S /Q

rem The sphinx-autobuild will rebuild on any changes and show the output
rem sphinx-build -b html -D html_title="%htmltitle%" %path-in% %path-out%
sphinx-autobuild -b html -D html_title="DKubeX User Guide" %path-in% %path-out%


