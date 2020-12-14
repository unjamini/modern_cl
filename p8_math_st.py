import pandas as pd


def get_column_mean(frame, col_name):
    return frame[col_name].mean()


#  скачала датасет здесь: https://sdm.lbl.gov/fastbit/data/samples.html (более 2млн строк)

if __name__ == '__main__':
    df_name = './star2000.csv'
    data = pd.read_csv(df_name)
    data_cols = data.columns
    for col in data_cols:
        print(f'Mean for column {col} is: {get_column_mean(data, col)}')
