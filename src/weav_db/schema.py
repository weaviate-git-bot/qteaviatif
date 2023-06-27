schema = {
    "classes": [{
        "class": "Email",
        "description": "Contains a preprocessed email body, user_id and email_id",
        "properties": [
            {
                "name": "user_id",
                "dataType": ["text"],
                "moduleConfig": {
                    "text2vec-openai": {
                        "skip": True
                    }
                }
            },
            {
                "name": "email_id",
                "dataType": ["text"],
                "moduleConfig": {
                    "text2vec-openai": {
                        "skip": True
                    }
                }
            },
            {
                "name": "body_proc",
                "dataType": ["text"],
            },
            {
                "name": "thread_id",
                "dataType": ["text"],
                "moduleConfig": {
                    "text2vec-openai": {
                        "skip": True
                    }
                }
            }
        ],
        "vectorizer": "text2vec-openai",
        "moduleConfig": {
            "vectorizeClassName": False,
            "model": "ada",
            "modelVersion": "002",
            "type": "text",
            "qna-openai": {
                "model": "text-davinci-003",
            }
        }
    }]
}
