#!/usr/bin/env python
# coding: UTF-8
import os
import subprocess
from fabric.api import local, task
from glob import glob
import os.path

AUTHOR = 'yassu'
MAIN_BASENAME = os.path.split(os.getcwd())[-1].split('.')[0]
    # basename of tex file
LATEX = 'latexmk'
DVIP = 'dvipdfmx'
VIEW_PDF = 'evince'


MAKED_EXTENSIONS = [".aux", ".dvi", ".fdb_latexmk", ".fls", ".log", ".pdf",
                    ".synctex.gz"]

if not os.path.isfile(MAIN_BASENAME + '.tex'):
    exit("[Error] {}.tex is not found.".format(MAIN_BASENAME))


class Commands(list):
    def run(self):
        for cmd in self:
            print(cmd)
            local(cmd)


@task
def compile(basename=MAIN_BASENAME):
    " latex and dvip "

    cmds = Commands()
    cmds.append('%s %s' % (LATEX, basename + '.tex'))
    cmds.append('%s %s' % (DVIP, basename + '.dvi'))
    cmds.run()


@task(alias='compile')
def comp(basename=MAIN_BASENAME):
    compile(basename)


@task
def view(basename=MAIN_BASENAME, make=True):
    if make:
        compile()

    cmds = Commands()
    cmds.append('%s %s' % (VIEW_PDF, basename + '.pdf'))
    cmds.run()

def is_using_git():
    try:
        subprocess.check_output(['git', '--version'])
    except FileNotFoundError:
        return False

    return subprocess.check_output(['ls', '.git']) == '\n'


@task
def submit(basename=MAIN_BASENAME, make=True, tag=None, author=AUTHOR):

    if is_using_git() and tag is None:
        tags = subprocess.check_output(['git', 'tag']).split('\n')
        tag = tags[-2] if len(tags) >= 2 else None

    out_basename = '%s-%s' % (AUTHOR, basename)
    if tag is not None:
        out_basename += '-%s' % (tag)

    if make:
        compile()

    local('cp %s %s' % (basename + '.pdf', out_basename + '.pdf'))


@task(alias='submit')
def hand(basename=MAIN_BASENAME, make=True, tag=None, author=AUTHOR):
    submit(basename, make, tag, author)

@task
def clean(basename=MAIN_BASENAME):
    for filename in [basename + ext for ext in MAKED_EXTENSIONS]:
        if os.path.isfile(filename):
            cmd = "rm {}".format(filename)
            print(cmd)
            local("rm {}".format(filename))
