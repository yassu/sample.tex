# sample.tex-by-fab

`sample.tex` is a repository for publish my environment for tex project.

Mainly, use git and fabric command.

I assume that this tex project uses git.
Firtheremore, `tag` is used for virsion.

Usage
=======

step 0
--------

write tex file.

step 1
--------

First, define configures of fabfile.py (AUTHOR, MAIN_BASENAME, LATEX, DVIP or
  VIEW_PDF).

step 2
--------

Compile and view tex file.

```
% fab view
```

Configures
============

Configures in fabfile.py is defined as below:

* Author: author name of tex project. This is used for `submit` task.
* MAIN_BASENAME: basename of main tex file.
* LATEX: used tex name
* DVIP: dvip name (ex: dvipdfm, dvipdfmx)
* VIEW_PDF: command name for viewing pdf file (evince, open e.t.c.)

tasks
=======

fabfile.py provides following tasks by

``` sh
$ fab {task-name}
```

* compile (is equal to comp): compile tex file(means that process latex and dvip
  command)
* view: compile tex file and open compiled pdf
* hand(is equal to submit): compile tex file and copy to {author}-{basefilename}[-{last tag}].pdf
    file

LICENSE
=========

[CC0-1.0](LICENSE)
