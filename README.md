
printers
===
Scripts used in the "Visualizing printer activity at Princeton University" project at http://www.princeton.edu/~saha/printers/

SCRIPTS
---
- background.py collects data over time
- compounder.py takes column name by command line arguments and outputs all the values that column takes over time
- categorizer.py goes down data.csv and keeps a running record of the number of printers of each type at each data point.
- likelihood.py computes likelihood of printers being available

USAGE
---
python compounder.py data.csv -status > statusValues.txt
python categorizer.py data.csv -datetime > datetimeValues.txt
python graph1.py datetimeValues.txt
