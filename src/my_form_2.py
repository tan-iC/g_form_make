from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import  os
import  sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('data/token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('data/client_secret_221031.json', SCOPES)
    creds = tools.run_flow(flow, store)

form_service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

###
# 1. 
###

form_descripition =\
"""2022/11/30\n
Comment sheet about the 2nd midterm presentation\n
第二回中間発表に関するコメントシート"""

# Request body for creating a form
NEW_FORM = {
    "info": {
        "title": "第二回中間発表",
        "documentTitle": 'form_221101_',
    }
}

# Creates the initial form
result = form_service.forms().create(body=NEW_FORM).execute()

###
# 2. 
###

section_description =\
"""If you are the presenter himself/herself, 
or if you were not able to attend, please enter 0.\n
発表者自身の場合、聴講できなかった場合は、0を記入してください。"""


def sectionStart(form_service, idx, title, description, result):
    NEW_QUESTION = {
        "requests": [{
            "createItem": {
                # item
                "item": {
                    # title
                    "title": title,

                    # description
                    "description": description,

                    # sectionize
                    "pageBreakItem": {},
                },
                "location": {
                    "index": idx
                }
            }
        }]
    }

    # Adds the question to the form
    question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()

def textQuestion(form_service, idx, title, result):
    NEW_QUESTION = {
        "requests": [{
            "createItem": {
                # item
                "item": {
                    # upper title in the question 
                    "title": title,

                    # description
                    # "description": description,

                    # questionItem:=question 
                    "questionItem": {
                        "question": {
                                "required": True,
                                "textQuestion": {
                                    "paragraph": True,
                                }
                        }
                    },
                },
                "location": {
                    "index": idx
                }
            }
        }]
    }
    # Adds the question to the form
    question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()

def scaleQuestion(form_service, idx, title, result):
    NEW_QUESTION = {
        "requests": [{
            "createItem": {
                # item
                "item": {
                    # upper title in the question 
                    "title": title,

                    # description
                    # "description": description,

                    # questionItem:=question 
                    "questionItem": {
                        "question": {
                                "required": True,
                                "scaleQuestion": {
                                    "low": 0,
                                    "high": 5,
                                }
                        }
                    },
                },
                "location": {
                    "index": idx
                }
            }
        }]
    }

    # Adds the question to the form
    question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()


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
