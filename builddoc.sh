#!/bin/sh
sphinx-apidoc -F -o docs-sphinx/ japanese/
sphinx-build -b html ./docs-sphinx/ ./docs/