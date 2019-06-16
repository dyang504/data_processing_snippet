import numpy as np
import os
import datetime
import re
import shutil
from typing import List

import pandas as pd
# The file contains common functions and usage cases
# in python and pandas data processing

# dependency : pandas numpy xlsxwriter datetime

# 1. read large file
# A more robust solvtion is use parallel framework like Dask,
# or dump into a database


def read_large_csv(path: str, chunksize: int = 2000000, encoding: str = 'gb18030'):
    """
    Read large csv file to the memory using Pandas,
    Adjust chunksize to enhance perfomance
    """
    reader = pd.read_csv(path, chunksize=chunksize,
                         encoding=encoding, na_values=[' '])
    chunks = [chunk for chunk in reader]
    return pd.concat(chunks, ignore_index=True)


# Search file from the local directory
def search_file(goal_list: List, pattern: str) -> str:
    """search pattern from a goal_list, return the match one"""
    for item in goal_list:
        if re.search(rf"{pattern}", item):
            return item

# solve encoding problem
# set encoding to 'gb18030', avoid encode problem

# move files


def move_file(data_source_folder, data_source_files):
    if not os.path.exists(data_source_folder):
        os.mkdir(data_source_folder)
    for file in data_source_files:
        shutil.move(file, os.path.join(os.getcwd(), data_source_folder))


# 2. handle datetime
# get Today's date
datetime.datetime.today().date()

# get Yestoday automaticly
yestoday_date = datetime.datetime.today().date() - datetime.timedelta(1)

# convert dataframe column to date type, refined for pandas pipe
def convert_to_datetime(df: pd.DataFrame,col: str):
    """
    convert dataframe column to date type
    """
    df[col] = df[col].dt.date
    return df

# Combine dataframe


def combine_df(datasource_path_list: List, folder: str):
    df_list = []
    for path in datasource_path_list:
        path_to_file = os.path.join(folder, path)
        df_list.append(pd.read_csv(path_to_file, engine="python"))
    return pd.concat(df_list)

# 3. write multiple dataframes to excel


def df_to_excel(df: pd.DataFrame, path_to_file: List, sheet_name: str, float_format: str = "%.2f", **to_excel_kwargs):
    """
    Write dataframe to exist Excel file, could be used multiple times
    path_to_file follow the order of [folder,...,filename]
    """
    from openpyxl import load_workbook
    path = os.path.join(*path_to_file)
    if os.path.isfile(path):
        book = load_workbook(path)
        writer = pd.ExcelWriter(path, engine='openpyxl')
        writer.book = book
        writer.sheets = {ws.title: ws for ws in book.worksheets}
        df.to_excel(writer, sheet_name,
                    float_format=float_format, **to_excel_kwargs)
        writer.save()
    else:
        df.to_excel(path, sheet_name, float_format=float_format,
                    **to_excel_kwargs)
    return df.head()


# to_excel, refined for pandas pipe


def to_excel(df, folder, filename, **to_excel_kwargs):
    path = os.path.join(folder, filename)
    df.to_excel(path, **to_excel_kwargs)
    return df.head()


# generate variable by condition
# Two results
dataframe['new column name'] = np.where(
    dataframef['column name'] == 'some value', 'output1', 'output2')
# Three or more results

# filter columns function

# add total

# write title and string to dataframe
