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
                    "name": "thread_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "from",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "to",
                    "dataType": ["text[]"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "body_proc",
                    "dataType": ["text"],
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailBkp",
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
                    "name": "thread_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "from",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "to",
                    "dataType": ["text[]"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "body_proc",
                    "dataType": ["text"],
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailBis",
            "description": "Contains a preprocessed email body, user_id and email_id",
            "properties": [
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
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "Email1on1",
            "description": "Contains a preprocessed email body, sender_id and receiver_id",
            "properties": [
                {
                    "name": "sender_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "receiver_id",
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
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "Email1on1Bkp",
            "description": "Contains a preprocessed email body, sender_id and receiver_id",
            "properties": [
                {
                    "name": "sender_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "receiver_id",
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
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailClique",
            "description": "Contains a preprocessed email body, sender_id and receiver_id",
            "properties": [
                {
                    "name": "clique_id",
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
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
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
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },

        {
            "class": "EmailDocument",
            "description": "Contains pdf or docx documents",
            "properties": [
                {
                    "name": "template",
                    "dataType": ["boolean"],
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
                    "name": "user_email",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "document_file_name",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "document_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "data",
                    "dataType": ["text"]
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailUser",
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
                    "name": "body_proc",
                    "dataType": ["text"],
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailUserBkp",
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
                    "name": "body_proc",
                    "dataType": ["text"],
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailUser2",
            "description": "Contains a preprocessed email body, user_id and email_id",
            "properties": [
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
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailUserSent",
            "description": "Contains emails sent by a user",
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
                    "name": "body_proc",
                    "dataType": ["text"],
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },{
            "class": "EmailUserSentBkp",
            "description": "Contains emails sent by a user",
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
                    "name": "body_proc",
                    "dataType": ["text"],
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailUserReceived",
            "description": "Contains emaisl received by a user",
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
                    "name": "body_proc",
                    "dataType": ["text"],
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailUserReceivedBkp",
            "description": "Contains emaisl received by a user",
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
                    "name": "body_proc",
                    "dataType": ["text"],
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailAdjMatrix",
            "description": "Contains emaisl received by a user",
            "properties": [
                {
                    "name": "sender_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "receiver_id",
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
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailAdjMatrixBkp",
            "description": "Contains emaisl received by a user",
            "properties": [
                {
                    "name": "sender_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "receiver_id",
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
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "Email1on1Conversation",
            "description": "Contains a conversation between 2 people",
            "properties": [
                {
                    "name": "sender_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "receiver_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "subject",
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
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "Email1on1ConversationBkp",
            "description": "Contains a conversation between 2 people",
            "properties": [
                {
                    "name": "sender_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "receiver_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },
                {
                    "name": "subject",
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
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        },
        {
            "class": "EmailGroupConversation",
            "description": "Contains a conversation between a group people",
            "properties": [
                {
                    "name": "conversation_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },{
                    "name": "members",
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
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text",
                "qna-openai": {
                    "model": "gpt-3.5-turbo-16k",
                }
            }
        }
    ]
}
