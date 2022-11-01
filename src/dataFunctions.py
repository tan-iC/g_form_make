import  os
import  sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import  pandas  as pd

###
# 0.
###

def getCSVdata(file_name):
    """
    - data/{file_name}.csvを読み込む
    """
    df = pd.read_csv(f"data/{file_name}.csv")
    return df

def getColumns(file_name, column_names):
    """
    - csvを読み込み、columnごとに取得
    - return List[df[name].tolist()]
    """
    df = getCSVdata(file_name)

    columns = []
    for column_name in column_names:
        columns.append(df[column_name].tolist())
    
    return columns

def append_sum_row_label(df):
    df.loc['Total'] = df.sum(numeric_only=True)
    return df

def sumCSVdata(df, presenters, commentColumn):
    """
    - 発表者ごとに行を作成
    - columnごとにsum
    - コメントに関しては'- {comment}\n'で結合
    """
    sums = []
    comments = []
    i = 0
    for column_name, item in df.iteritems():
        if commentColumn in column_name:
            text = ""
            # print(item)
            for comment in item:
                text += f'- {comment}\n'
            comments.append(text)

            presenter = presenters[i]
            print(f'{presenter}: {column_name}::\n{text}')
            i += 1
        else:
            presenter = presenters[i]
            tmp = df[column_name].sum()
            sums.append(tmp)
            print(f'{presenter}: {column_name}::{tmp}')
    # print(sums)
    print(comments)
    
