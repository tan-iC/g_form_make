import  os
import  sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import  pandas  as pd


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
    """
    - 数値の合計列を追加
    """

    df.loc['Total'] = df.sum()
    return df

def sumCSVdata(df, presenters, commentColumn, questions):
    """
    - 発表者ごとに行を作成
    - columnごとにsum
    - コメントに関しては'- {comment}\n'で結合
    """

    sums = []
    comments = []
    d = {}
    for presenter in presenters:
        d.update({presenter:{}})
    
    i = 0
    for column_name, item in df.iteritems():

        question = column_name
        dot = (column_name.find('.'))

        if dot!=-1:
            column_name = column_name[:dot]

        if column_name not in questions:
            # タイムスタンプを飛ばす
            continue

        # コメントの処理
        if commentColumn in column_name:

            text = ""
            for comment in item:
                text += f'- {comment}\t'
            comments.append(text)
            presenter = presenters[i]
            # print(f'{presenter}: {column_name}::\n{text}')
            d[presenter][column_name]=text
            i += 1
        
        # コメント以外の数値の処理
        else:
            presenter = presenters[i]
            tmp = df[question].sum()
            sums.append(tmp)
            # print(f'{presenter}: {column_name}::{tmp}')
            d[presenter][column_name]=tmp

    # dictからdfへ
    df = pd.DataFrame(d.values(), index=d.keys())

    # Totalの列を追加する
    df = addTotalColumn(df, commentColumn)

    # 結果を保存する
    df.to_csv('result/result.csv', encoding='utf8')

    return df


def addTotalColumn(df, commentColumn):
    """
    - 一旦コメントを除き、評点の合計を追加する
    """
    c_ = df[commentColumn]
    df = df.T.drop(commentColumn)
    df = append_sum_row_label(df).T
    df = pd.concat([df, c_], axis=1)

    return df


def sortEachColumn(df):
    """
    - 要素ごとにdfをソート
    """

    for column_name in df:
        df_s = df.sort_values(column_name, ascending=False)
        # print(f'sorted by:{column_name}\n{df_s}\n')
        df_s.to_csv(f'result/sortedBy{column_name}.csv', encoding='utf8')


def totalling(file_name, row_names, column_names):
    """
    - 一連の集計作業を行う
    """

    df = getCSVdata(file_name)

    df = sumCSVdata(df, row_names, column_names[-1], column_names)

    sortEachColumn(df)
