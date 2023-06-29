schema = {
    "classes": 
    [
        {
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
        },
        {
            "class": "Thread",
            "description": "Contains a thread_id, list of emails, and a concatenation of email bodies",
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
                    "name": "thread_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "emails",
                    "dataType": ["text[]"]
                },
                {
                    "name": "messages",
                    "dataType": ["text[]"]
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
        }
    ]
}
