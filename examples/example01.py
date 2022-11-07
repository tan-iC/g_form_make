from    __future__      import print_function
import  os
import  sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from    src.utilFunctions   import checkOAuth, createForm, sectionStart, scaleQuestion, textQuestion, updateForm

###
# 0.
###

form_service = checkOAuth()

###
# 1. 
###

form_title = "Form Title"
form_file_name = "Form File Name"
form_descripition ="""Form Description"""


# Creates the initial form
result = createForm(form_service, form_title, form_file_name)

# Updates the form (Adds description)
updateForm(form_service, result, form_title, form_file_name, form_descripition)

###
# 2. 
###

section_description ="""Section Description"""

# section num
n = 4

# question num
m = 4

# make questions into the form
idx = 0
for i in range(n):

    sectionStart(
        form_service, 
        idx, 
        result,
        f'Section #{i}', 
        section_description
        )
    
    # incliment
    idx += 1

    for j in range(m):
        if j == (m-1):
            textQuestion(form_service, idx, result, f'Question #{i}-{j}')
        else:
            scaleQuestion(form_service, idx, result, f'Question #{i}-{j}')
        
        # incliment
        idx+=1


# Prints the result to show the question has been added
get_result = form_service.forms().get(formId=result["formId"]).execute()
print(get_result)
