import numpy as np
date=np.datetime64('2025-11-01')
dm=np.arange('2025-11-01','2025-12-01',dtype='datetime64[D]')
td=date+np.timedelta64(10,'D')
sorted_dates=np.sort(dm)
print("Dates in November 2025:",dm)
print("Sorted Dates:",sorted_dates)
print("Ten Dates Later:",td)
