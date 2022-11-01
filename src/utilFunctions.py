from    __future__      import print_function

from    apiclient       import discovery
from    httplib2        import Http
from    oauth2client    import client, file, tools
import  pandas          as pd
import  os
import  sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

###
# 0.
###

def checkOAuth():
    """
    - OAuth認証
    - サーバへアクセス
    """
    SCOPES = "https://www.googleapis.com/auth/forms.body"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    store = file.Storage('data/token.json')
    creds = None
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('data/client_secret_221031.json', SCOPES)
        creds = tools.run_flow(flow, store)

    form_service = discovery.build('forms', 'v1', http=creds.authorize(
        Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)
    return form_service

###
# 1. 
###

def createForm(form_service, title, file_name):
    """
    - フォームの先頭部分を作成
    """
    # Request body for creating a form
    NEW_FORM = {
        "info": {
            "title": title,
            "documentTitle": file_name,
        }
    }
    # Creates the initial form
    result = form_service.forms().create(body=NEW_FORM).execute()
    return result


###
# 2. 
###

def sectionStart(form_service, idx, title, description, result):
    """
    - セクションを作成
    - その他のItemと同じ扱い
    """
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
    """
    - 記述回答を求める質問を作成
    """
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
    """
    - 均等目盛りの質問を作成
    """
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


