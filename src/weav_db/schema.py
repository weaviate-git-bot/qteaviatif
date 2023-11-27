schema = {
    "classes": 
    [
        {
            "class": "Email",
            "description": "Contains a preprocessed email body, user_id and email_id",
            "properties": [
                {
                    "name": "graph_key",
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
                    "name": "signature_available",
                    "dataType": ["boolean"],
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
                    "name": "signature",
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
                    "name": "email_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },{
                    "name": "thread_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },{
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
            "class": "EmailUserSent",
            "description": "Contains emails sent by a user",
            "properties": [
                {
                    "name": "email_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },{
                    "name": "thread_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },{
                    "name": "user_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },{
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
                    "name": "email_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },{
                    "name": "thread_id",
                    "dataType": ["text"],
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": True
                        }
                    }
                },{
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
        }
    ]
}
