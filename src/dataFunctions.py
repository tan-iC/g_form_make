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
