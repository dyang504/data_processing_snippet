# The file contains common functions and usage cases 
# in python and pandas data processing

# dependency : pandas numpy xlsxwriter datetime

# 1. read large file
def read_large_csv(path,chunksize=2000000,encoding='gb18030'):
    reader = pd.read_csv(path,chunksize=chunksize,encoding=encoding,na_values=[' '])
    chunks = [chunk for chunk in reader]
    return pd.concat(chunks,ignore_index=True)

# solve encoding problem
# set encoding to 'gb18030', avoid encode problem

# move files
def move_file(data_source_folder,data_source_files):
    if not os.path.exists(data_source_folder):
        os.mkdir(data_source_folder)
    for file in data_source_files:
        shutil.move(file,os.path.join(os.getcwd(),data_source_folder))

# 2. handle datetime
# get Today's date
datetime.datetime.today().date()

# get Yestoday automaticly
yestoday_date = datetime.datetime.today().date() - datetime.timedelta(1)

# Combine dataframe
def combine_df(datasource_path_list):
    df_list = []
    for path in datasource_path_list:
        df.append(pd.read_csv(folder+path1,engine="python"))
    return pd.concat(df_list)

# 3. write multiple dataframes to excel
def write_dfs_to_excel():
    pass

# generate variable by condition
# Two results
df['散团'] = np.where(df['销售子舱位'] == 'G','团','散') 
# Three or more results

# filter columns function

# add total

# write title and string to dataframe