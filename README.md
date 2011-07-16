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
> python config.py 
then:
> python conventional.py user_config.json
the contents of /your_project should include the relevant stuff

Current State:
--------------


Dependencies:
-------------
- jinja2
- json

Todo:
-----
- pre-commit hooks
- coding conventions doc
- rewrite quick explanation of what everything is
