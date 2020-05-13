import pathlib

import click
import pandas as pd


def paser_file(file):
    path_class = pathlib.Path(file)
    return path_class.parent, path_class.name


def read_to_df(file, data_type):
    if data_type == "stata":
        return pd.read_stata(file)
    elif data_type == "excel":
        return pd.read_excel(file)
    else:
        raise Exception('Formato não suportado.\n Tente: stata ou excel')


def save_df(df, path, file, sep):
    save_to = f"{path}/{file.split('.')[0]}.csv"
    print(f'Salvando em {save_to}')
    df.to_csv(save_to, sep=sep, index=False)
    return None


@click.command()
@click.option('--file', help='file: path+name+ext')
@click.option('--data_type', help='data type support: stata & excel')
@click.option('--sep', default=";", help='data type support: stata & excel')
def main(file, data_type, sep=';'):
    df = read_to_df(file, data_type)
    path, file_name = paser_file(file)
    save_df(df, str(path), file_name, sep)
    print('Concluído com sucesso')
    return None


if __name__ == "__main__":
    main()
