import pandas as pd
import time

start = time.time()
df2 = pd.read_csv(r'C:\Users\klim\Desktop\example\Гойтх_01_01_2023.csv', 
                  delimiter=';', engine='c', header=1)
end = time.time()
print("Time need: ", str(time.strftime('%M:%S', time.gmtime(end-start))))