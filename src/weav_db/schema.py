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
                    "model": "text-davinci-003",
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
                    "model": "text-davinci-003",
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
                    "model": "text-davinci-003",
                }
            }
        },
        {
            "class": "EmailUser",
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
                    "model": "text-davinci-003",
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
                    "model": "text-davinci-003",
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
                    "model": "text-davinci-003",
                }
            }
        },
        {
            "class": "EmailAdjMatrix",
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
                    "model": "text-davinci-003",
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
                    "model": "text-davinci-003",
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
                    "model": "text-davinci-003",
                }
            }
        }
    ]
}
