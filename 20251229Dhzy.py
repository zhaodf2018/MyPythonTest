import akshare as ak

# 获取登海种业实时行情
# 002041 对应的是深交所股票
stock_df = ak.stock_zh_a_spot_em()
denghai_info = stock_df[stock_df['代码'] == '002041']

print("登海种业实时行情：")
print(denghai_info[['代码', '名称', '最新价', '涨跌幅', '成交量', '今开']])
