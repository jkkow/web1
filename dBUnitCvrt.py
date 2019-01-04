from numpy import log10


def dbtop(dbm):
    power = 10**(dbm / 10)
    return power


def ptodb(power):
    dbm = 10 * log10(power)
    return dbm


def dbsum(*dbms):
    power = 0
    for dbm in dbms:
        power += dbtop(dbm)
    return ptodb(power)
