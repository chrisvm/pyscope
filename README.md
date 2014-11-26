**pyscope**
==============

Pyscope is a collection of Python tools for understanding Python
scripts/programs. It will include tools for viewing code on the command line,
creating markdown or html of Python code and more.

This project is still on development and it's just
starting.


Usage
-----

It is intended to be a set of command line tools. They can be used as follows:

    pyscope [command] [--options] [arguments]

**Commands**

- html
- markdown
- cat
- ls

ls
==

Using the ls command works just like ls, but with pretty printing.

Input:

    pyscope ls

Output:

    |- main.py
    |- src/
    |---|- lib.py
        |- pyconst.py
        |- module/
        |---|- conf.json
    |- LICENSE
    |- .gitignore

html
====

Outputs styled html with the code and its comments, by its side. It's trying to
replicate the documentation style found at the coffescript documentation
(http://coffeescript.org/documentation/docs/lexer.html).

cat
===

`cat`, just like `ls`, works by replicating some of the functionality of the original program but extending/tweaking it. My goal for cat is for it to do tha normal printing to stdout but with color, and maybe some other tweaks that pop up as I develop this project. 

markdown
========

This purpose of this command is to produce markdown from a python source file. 
While its functionality is somewhat similar to the `html` command, the output `html` produces is completely different in form. The format will be vertical, that of a markdown document, while the `html` command adopts a side-by-side view of code and comments. The output will be valid Markdown, which can then be rendered to html markup. 