from    __future__      import print_function
from    utilFunctions   import checkOAuth, createForm, sectionStart, scaleQuestion, textQuestion
from    dataFunctions   import getCSVdata
import  os
import  sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

###
# 0.
###

form_service = checkOAuth()

###
# 1. 
###

form_descripition =\
"""2022/11/30\n
Comment sheet about the 2nd midterm presentation\n
第二回中間発表に関するコメントシート"""

form_title = "第二回中間発表"
form_file_name = "form_22110102"

# Creates the initial form
result = createForm(form_service, form_title, form_file_name)

###
# 2. 
###

section_description =\
"""If you are the presenter himself/herself, 
or if you were not able to attend, please enter 0.\n
発表者自身の場合、聴講できなかった場合は、0を記入してください。"""

# presenters
presenters = [
    "A",
    "B",
    "C"
    ]

# questions
questions = [
    "Research progress: 研究の進捗",
    "Presentation quality: プレゼンの質",
    "Q&A quality: 質疑応答の質",
    "Resume quality: レジュメの質",
    "Comment: コメント"
    ]

idx = 0
for i, person in enumerate(presenters):

    sectionStart(
        form_service, 
        idx, 
        f'{person}さん', 
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
