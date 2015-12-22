
from cyepanet import enopen, ensolveH, ensaveinpfile, ensolveQ, enreport, enclose

import time


start_time = time.time()
start_time_display = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


inpfile = "/Users/markwilson/Dropbox/epanet sample files/Bountiful small model NAD83 State Plane Utah North test source.inp"
rptfile = "/Users/markwilson/Dropbox/epanet sample files/Bountiful small model NAD83 State Plane Utah North test source.rpt"
outfile = "/Users/markwilson/Dropbox/epanet sample files/Bountiful small model NAD83 State Plane Utah North test source.out"

newinpfile = "/Users/markwilson/Dropbox/epanet sample files/new_Bountiful small model NAD83 State Plane Utah North test source.inp"



print enopen(inpfile, rptfile, outfile)
print ensolveH()
print ensaveinpfile(newinpfile)
print ensolveQ()
print enreport()
print enclose()

print
print "*" * 80
stop_time = time.time()
stop_time_display = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
elapsed_time = stop_time - start_time
print "Start Time: ", start_time_display
print "Stop Time: ", stop_time_display
print "Elapsed time = ",round(elapsed_time,2)," seconds"
print "*" * 80