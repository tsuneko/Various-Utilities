Python script to generate commands in order to create and maintain an ordered mymarry list for the discord Mudae Bot. Don't ask why I made this.

Usage:

1. Create a `waifulist.txt` file and populate it with characters from Mudae, in the order you wish to sort them by.

```
Megumi Katou - Saenai Heroine no Sodatekata
Remilia Scarlet - Touhou Project (Windows Canon)
```

2. Use the command `$mms` and copy and paste the output sent to `mms_output.txt`

3. Run `generate_commands.py`

4. From the `commands.txt` file, copy and paste the `$l` commands for likelist, `$note` commands for notes and `$sm note` command for sorting. The notes must be specified for ordering of notes, and so the sort command will only work with two or more claims.
