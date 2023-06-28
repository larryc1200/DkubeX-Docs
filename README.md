﻿This repository contains the source and build files to create the DKube guides.  

- The source files use Sphinx v3.4.2
- The batch files run under Windows
- The following packages must be installed
  - `tabs` as described at https://sphinx-tabs.readthedocs.io/en/latest/
  - `Linuxdoc` as described at https://devopstutodoc.readthedocs.io/en/stable/documentation/doc_generators/sphinx/contributed_extensions/linux/linux.html
  - `pip install sphinx-autobuild` - this will automatically rebuild on changes and show the page
 
The following folder contains the source and HTML files for the installation guide:

- X-build.bat
  - Batch file to create the user guide

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

















