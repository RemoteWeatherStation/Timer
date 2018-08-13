import pyenergy
import time

# Specifying the serial number of the board
em = pyenergy.EnergyMonitor("EE00")

# Use measurement point 1
em.enableMeasurementPoint(1)
em.start(1)
   
time.sleep (120)

em.stop(1)
m = em.getMeasurement(1)
print "{m.energy}, {m.time}, {m.avg_power}, {m.avg_current},{m.avg_voltage}".format(m=m)
