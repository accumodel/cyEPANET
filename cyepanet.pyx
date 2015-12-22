# expose the api to Python

from cpython cimport array
import array

cimport epanet2


def enepanet(char *f1, char *f2, char *f3):
    return epanet2.ENepanet(f1, f2, f3)


def enopen(char *f1, char *f2, char *f3):
    return epanet2.ENopen(f1, f2, f3)


def ensaveinpfile(char *filename):
    return epanet2.ENsaveinpfile(filename)


def enclose():
    return epanet2.ENclose()


def ensolveH():
    return epanet2.ENsolveH()


def ensaveH():
    return epanet2.ENsaveH()


def enopenH():
    return epanet2.ENopenH()


def eninitH(int flag):
    return epanet2.ENinitH(flag)


def enrunH(long t):
    return epanet2.ENrunH(&t)


def ennextH(long tstep):
    return epanet2.ENnextH(&tstep)


def encloseH():
    return epanet2.ENcloseH()


def ensavehydfile(char *filename):
    return epanet2.ENsavehydfile(filename)


def enusehydfile(char *filename):
    return epanet2.ENusehydfile(filename)


def ensolveQ():
    return epanet2.ENsolveQ()


def enopenQ():
    return epanet2.ENopenQ()


def eninitQ(int saveflag):
    return epanet2.ENinitQ(saveflag)


def enrunQ(long t):
    return epanet2.ENrunQ(&t)


def ennextQ(long tstep):
    return epanet2.ENnextQ(&tstep)


def enstepQ(long tleft):
    return epanet2.ENstepQ(&tleft)


def encloseQ():
    return epanet2.ENcloseQ()


def enwriteline(char *line):
    return epanet2.ENwriteline(line)


def enreport():
    return epanet2.ENreport()


cdef extern double *H

cdef printH(int Nnodes, double *H):
    cdef int i
    for i in range(1,Nnodes+1):
        print H[i]


