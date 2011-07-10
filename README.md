What this does:
---------------

- makes creating coding conventions for your project suck less
- How it works:
  1.  you make some simple choices on your coding conventions
  2.  We generate:
      - a coding convention doc for newbies
      - appropriate vim/emacs/textmate/etc configs
      - a linter you can use for those conventions
      - a pre-commit hook for github that doesn't let you check in unless the linter passes
  3.  coding conventions don't suck as much anymore.

Example:
--------

python conventional.py your_project.yaml

Current State:
--------------

- Super f-ing rough. 0.01

Dependencies:
-------------

- jinja2
- yaml
