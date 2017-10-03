# git-relations

Get number of times two files are in the same git commit.

## Install

```
pip install git-relations
```

## Usage

Call with a filename from anywhere within a git repository.

Prints number of times the given file is in the same commit as another file.

```
$ git relations <filename>
  3  anotherfile.txt
  3  more.txt
  1  some/other/file
```
