### Windows Only

## review.py

Basic python script to format input to [akochan-reviewer](https://github.com/Equim-chan/akochan-reviewer). This script saves a very small amount of time spent typing, assuming that the same flags are provided each time. At the moment, the only supported flags are `--lang en` and `--without viewer`.

Directory structure is above akochan-reviewer, hence the `cd akochan-reviewer` in the command line.

**default review.txt**

```
en=true
viewer=true
```

## review.bat

If python is not installed, use this batch file instead. It either needs to sit in the akochan directory, or it needs to cd to it.
