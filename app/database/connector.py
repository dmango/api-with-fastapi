import pandas as pd
from pkg_resources import resource_filename


def select_customer(customer_id):

    file_path = resource_filename('app', 'database/customers.csv')
    df = pd.read_csv(file_path, sep=';')
    df.loc[:, 'id'] = df['id'].astype(str)

    return df.loc[df.id == customer_id]
