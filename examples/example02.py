from    __future__      import print_function
import  os
import  sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from    src.dataFunctions   import getCSVdata, getColumns, sumCSVdata, sortEachColumn, totalling

file_name = "information"
column_names = ["名前", "学年", "班"]

df = getCSVdata(file_name)

columns = getColumns(file_name, column_names)

presenters = columns[0]
questions = [
    "Research progress: 研究の進捗",
    "Presentation quality: プレゼンの質",
    "Q&A quality: 質疑応答の質",
    "Resume quality: レジュメの質",
    "Comment: コメント"
    ]

totalling("form_22110106", presenters, questions)
