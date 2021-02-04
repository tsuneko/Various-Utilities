## dump.py

Dumped Question and Answer pairs from Open Trivia Database (https://opentdb.com/) into a local text file `dump.txt`.

The dumping process takes approximately two minutes because the API has a maximum call limit of 50 questions at a time. A fresh API token is generated during runtime, so no configuration is required.

It should be a trivial matter from here to adjust this program to retrieve and format other fields of the returned data.
