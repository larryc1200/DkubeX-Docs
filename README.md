﻿This repository contains the source and build files to create the DKubeX guides.  

- The batch files run under Windows
- The following packages must be installed
  - `sphinx` as described at https://www.sphinx-doc.org/en/master/usage/installation.html
  - `sphinx materials theme` as described at https://pypi.org/project/sphinx-material/
  - `tabs` as described at https://sphinx-tabs.readthedocs.io/en/latest/
  - `linuxdoc` as described at https://pypi.org/project/linuxdoc/ 
  - `pip install sphinx-autobuild` - This will automatically rebuild on changes and show the page
 
The following folder contains the source and HTML files for the installation guide:

- X-auto.bat
  - Build the html files from scratch, removing and recreating the output folder
  - Sets up the local server and automatically rebulds on changes
  - This needs to be rerun when any config or css file changes

- X-build.bat
  - Build the html files without creating a local server or automatically rebuilding

- /source
  - Source file folder to create the user guide

  - index.rst - List of RST files to use
  - conf.py - Material theme configuration file
  - *.rst - Source RST files used to build the output HTML files

  - /images - Folder contains the images used in the guide
  - /_static/css - Folder that contains the CSS files to customize the output
    - custom.css - Primary CSS file for output customization

  - /DKubeX
     - Output HTML files for user guide

















