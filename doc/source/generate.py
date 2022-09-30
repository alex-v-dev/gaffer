#! /bin/bash
# BuildTarget: _static/GafferLogo.svg
# BuildTarget: _static/GafferLogoMini.svg

import shutil

shutil.copy2("../../resources/GafferLogo.svg",  "_static")
shutil.copy2("../../resources/GafferLogoMini.svg", "_static")
