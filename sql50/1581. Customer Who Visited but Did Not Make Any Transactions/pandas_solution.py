import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(visits, transactions, on='visit_id', how='left').loc[lambda x : x['transaction_id'].isnull(),['customer_id','visit_id']].groupby(by='customer_id' ,as_index=False).count().rename({'visit_id':'count_no_trans'}, axis=1)