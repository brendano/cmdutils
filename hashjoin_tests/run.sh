#!/bin/bash
set -eux
(
tsv2fmt < a.txt
tsv2fmt < b.txt
hashjoin --inner a.txt b.txt    | tsv2fmt
hashjoin --left a.txt b.txt     | tsv2fmt
hashjoin --outer a.txt b.txt    | tsv2fmt

echo -------------
tsv2fmt < a.txt
tsv2fmt < c.txt
hashjoin --inner a.txt c.txt    | tsv2fmt
hashjoin --left a.txt c.txt    | tsv2fmt
hashjoin --outer a.txt c.txt    | tsv2fmt

echo -------------
tsv2fmt < a.txt
tsv2fmt < d.txt
hashjoin --inner a.txt d.txt    | tsv2fmt
hashjoin --left a.txt d.txt    | tsv2fmt
hashjoin --outer a.txt d.txt    | tsv2fmt

) 2>&1
