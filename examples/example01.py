from    __future__      import print_function
import  os
import  sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from    src.utilFunctions   import checkOAuth, createForm, sectionStart, scaleQuestion, textQuestion, updateForm
from    src.dataFunctions   import getCSVdata, getColumns

###
# 0.
###

form_service = checkOAuth()

###
# 1. 
###

form_descripition =\
"""2022/11/30
Comment sheet about the 2nd midterm presentation
第二回中間発表に関するコメントシート"""

form_title = "第二回中間発表"
form_file_name = "form_22110106"

# Creates the initial form
result = createForm(form_service, form_title, form_file_name)

# Updates the form (Adds description)
updateForm(form_service, form_title, form_file_name, form_descripition, result)

###
# 2. 
###

section_description =\
"""If you are the presenter himself/herself, or if you were not able to attend, please enter 0.
Also, DON'T enter 0 for presentations that you attended.\n
発表者自身の場合、聴講できなかった場合は、0を記入してください。
また、聴講した発表には0を記入しないでください。"""

# get data from csv
csv_name = "information"
column_names = ["名前", "学年", "班"]
columns = getColumns(csv_name, column_names)

presenters = columns[0]
grades = columns[1]
teams = columns[2]

# questions
questions = [
    "Research progress: 研究の進捗",
    "Presentation quality: プレゼンの質",
    "Q&A quality: 質疑応答の質",
    "Resume quality: レジュメの質",
    "Comment: コメント"
    ]

# make questions into the form
idx = 0
for i, (presenter, grade, team) in enumerate(zip(presenters, grades, teams)):

    sectionStart(
        form_service, 
        idx, 
        f'{team}班 {grade} {presenter}さん', 
        section_description,
        result)
    
    # incliment
    idx += 1

    for j, question in enumerate(questions):
        if question==questions[-1]:
            textQuestion(form_service, idx, question, result)
        else:
            scaleQuestion(form_service, idx, question, result)
        
        # incliment
        idx+=1


# Prints the result to show the question has been added
get_result = form_service.forms().get(formId=result["formId"]).execute()
print(get_result)

with open("data/formId.txt", mode='a') as f:
    f.write(get_result)
