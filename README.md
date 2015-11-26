# PortableInstallationHelper

Quick'n dirty plugin for Sublime Text 3 portable installations (not tested on Sublime Text 2)

## Overview

This plugin alters the editor PATH environment variable during program startup, enabling the use of external binaries usually not reachable through the regular PATH definition.

## Installation

Note with either method, you may need to restart Sublime Text for the plugin to load.

### Package Control

Installation through [package control](http://wbond.net/sublime_packages/package_control) is recommended. It will handle updating your packages as they become available. To install, do the following.

* In the Command Palette, enter `Package Control: Install Package`
* Search for `PortableInstallationHelper`

### Manual

Clone or copy this repository into the packages directory. You will need to rename the folder to `PortableInstallationHelper` if using this method. By default, the Package directory is located at: `<extraction_dir>/Data/Packages/`

### Extra binaries

By default, the plugins prepends the `<extraction_dir>/Data/bin` folder to the PATH environment variable. Your extra binaries should be put here.
