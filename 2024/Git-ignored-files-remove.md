# So, 2024?

ok ok, let's start with, what is git ignored files?

> Git ignore files are files that are ignored by git. LOL.

```bash
> git clean -h     
usage: git clean [-d] [-f] [-i] [-n] [-q] [-e <pattern>] [-x | -X] [--] [<pathspec>...]

    -q, --[no-]quiet      do not print names of files removed
    -n, --[no-]dry-run    dry run
    -f, --[no-]force      force
    -i, --[no-]interactive
                          interactive cleaning
    -d                    remove whole directories
    -e, --exclude <pattern>
                          add <pattern> to ignore rules
    -x                    remove ignored files, too
    -X                    remove only ignored files
```

e git clean -xdn to perform a dry run and see what will be removed.
Then use git clean -xdf to execute it.

Basically, git clean -h or man git-clean(in unix) will give you help.

Be aware that this command will also remove new files that are not in the staging area.
