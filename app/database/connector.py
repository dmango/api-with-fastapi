import pandas as pd
from pkg_resources import resource_filename


def select_customer(customer_id):

    file_path = resource_filename('app', 'database/customers.csv')
    df = pd.read_csv(file_path, sep=';')
    df.loc[:, 'id'] = df['id'].astype(str)

    return df.loc[df.id == customer_id]


def select_invoices(customer_id):

    file_path = resource_filename('app', 'database/invoices.csv')
    df = pd.read_csv(file_path, sep=';')
    df.loc[:, 'customer_id'] = df['customer_id'].astype(str)

    return {i: f"/invoice/{i}" for i in list(df.loc[df.customer_id == customer_id, 'invoice_id'])}
