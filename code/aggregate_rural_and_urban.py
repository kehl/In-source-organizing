#!/usr/bin/python

# This script takes an input file ("all_cases.csv") that contains location-stratified
# disease time series data, and aggregates the disease incidence based on whether the
# location was rural or urban.
#
# You will be making multiple changes to the code below.  Each time you make a
# substantial change, verify that you have not changed the output from the program.
#
# The Exercise:
#
# 1) Read through, understand, and annotate the code.  If you do not understand a line,
# investigate it by experimenting, checking python references, and talking to others.
#
# 2) If there anything simple that can be done to make the code more readable or
# manageable, go ahead and do that--things like renaming variables or reducing the use
# of "magical" numbers.
#
# 3) Break the code up into functional units, and then turn those units into functions.
#
# 4) Write a class that can represent the input data in a useful way.  Create a parser
# function in the class that takes a line of text from the file and returns structured
# data that is useful and easy to understand.

urban_ts = dict()
rural_ts = dict()
for i in [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]:
    urban_ts[i] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    rural_ts[i] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

header_line = True
for line in file("all_cases.csv"):
    if header_line == True:
        header_line = False
        continue
    parts = line.strip().split(',')
    t = int(parts[0])
    muni_num = parts[4]
    data = map(int, parts[5:])
    if muni_num in ['050','101','041']: # urban municipality codes
        for i in range(0,52):
            urban_ts[t][i] += data[i]
    else:
        for i in range(0,52):
            rural_ts[t][i] += data[i]

header_line = True
print "location total_cases"
for line in file("all_cases.csv"):
    if header_line == True:
        header_line = False
        continue
    parts = line.strip().split(',')
    year = int(parts[0])
    muni_num = parts[4]
    data = map(int, parts[5:])
    print parts[3], parts[4], sum(map(int, parts[5:]))

print
print
print
print "year week urban rural"
for i in [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]:
    for week in range(0,52):
        print i, week+1, urban_ts[i][week], rural_ts[i][week]
