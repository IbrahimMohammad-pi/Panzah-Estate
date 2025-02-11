
import finnhub
import pandas as pd 
import time

# Setup client
finnhub_client = finnhub.Client(api_key="culm4s9r01qovv70a3ugculm4s9r01qovv70a3v0")

# Stock stock_candles
#
timer_1=time.perf_counter()
res=finnhub_client.symbol_lookup('apple')
timer_2=time.perf_counter()
#print(res)
data_frame=pd.DataFrame(res)
print(data_frame)
print(timer_2-timer_1)
