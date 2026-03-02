# Program 3: Create date, array of dates, arithmetic operations and sorting on dates

import numpy as np

date = np.datetime64('2025-11-01')
dates_in_month = np.arange('2025-11-01', '2025-12-01', dtype='datetime64[D]')
ten_days_later = date + np.timedelta64(10, 'D')
sorted_dates = np.sort(dates_in_month)

print("Dates in november 2025:", dates_in_month)
print("Sorted Dates:", sorted_dates)
