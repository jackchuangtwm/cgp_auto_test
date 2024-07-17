import pandas as pd
import logging


def process_excel_data(file_name, sheet_name):
    df = pd.read_excel(file_name, sheet_name=sheet_name, dtype=str)
    df.fillna("N/A", inplace=True)

    # 將 DataFrame 轉換為列表格式供 parametrize 使用
    # 這行代碼將一個 Pandas DataFrame 轉換成一個字典列表（list of dictionaries）
    # 每一行 DataFrame 變成列表中的一個字典，每個字典的鍵是列名，值是該行相應列的數據
    data_dicts = df.to_dict(orient='records')

    return data_dicts