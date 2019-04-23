from ast import literal_eval
from collections import defaultdict

import pandas as pd


def main(file_name: str):
    df = pd.read_csv(file_name, index_col=0, header=0)

    rates = defaultdict(int)
    for i, row in df.iterrows():
        data = literal_eval(row['query_last_values'])

        group = data['experimentValue']
        if data['action'] == 'publications_checkout' and data['hasRenewalVP'] == 'true':
            rates[group] += 1

    print(rates)


if __name__ == "__main__":
    main('for_test.csv')
