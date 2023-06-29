import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QTextStream, Qt, QTimer, QThread, pyqtSignal, QSize
from PyQt5.QtGui import QTextCursor, QIcon
from PyQt5.uic import loadUi
import json

from mongo_db.mongo import *
from weav_db.weav import weav_db, is_valid_weaviate, check_batch_result
from mhandlers.dcompose import start_docker_compose, stop_docker_compose





class MyWindow(QMainWindow):
    
    signal_log = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        loadUi("ui/main_window.ui", self)  # Load the .ui file

        self.setWindowTitle("Weaviate.Dev")

        with open("ui/config.json") as f:
            self.config = json.load(f)
        with open("credentials.json") as f:
            self.credentials = json.load(f)
        
            
        self.weav_host = self.lineEdit_host.text()
        self.weav_key = self.lineEdit_key.text()
        self.docker_compose_file_path = self.config['docker_compose_file_path']

        self.mongodb = mongo_db(self.config["mongo_db"]["name"], self.config["mongo_db"]["address"])



        self.pushButton_weav_refresh.setIcon(QIcon('ui/weav_refresh.png'))
        self.pushButton_weav_refresh.setIconSize(QSize(35, 35))
        self.pushButton_weav_refresh.clicked.connect(self.weav_refresh)
        self.pushButton_weav_refresh.setToolTip("Weaviate: Refresh")

        self.weav_status = is_valid_weaviate(self.weav_host)

        if self.weav_status:
            self.weavdb = weav_db(self.weav_host, {'open_ai_api_key': self.credentials['open_ai_api_key']})
            self.pushButton_weav_status.setIcon(QIcon('ui/weav_g.png'))
            self.pushButton_weav_status.setToolTip("Weaviate: Online")
            self.pushButton_weav_refresh.setEnabled(True)
            self.weavdb.link_progress_bar(self.progressBar)

        else:
            self.weavdb = None
            self.pushButton_weav_status.setIcon(QIcon('ui/weav_r.png'))
            self.pushButton_weav_status.setToolTip("Weaviate: Offline")
            self.pushButton_weav_refresh.setEnabled(False)

        # add icon to button pushButton_weav
        self.pushButton_weav_status.setIconSize(QSize(35, 35))
        self.pushButton_weav_status.clicked.connect(self.weav_toggle)


        # set pushbutton_weav_refresh to disabled
        self.pushButton_count.clicked.connect(self.weav_count)
        self.pushButton_count_distinct.clicked.connect(self.weav_count_distinct)
        self.pushButton_schema.clicked.connect(self.weav_schema)
        self.pushButton_schema_add.clicked.connect(self.weav_schema_add)
        self.pushButton_schema_add_class.clicked.connect(self.weav_schema_add_class)
        self.pushButton_get.clicked.connect(self.weav_get)
        self.pushButton_process.clicked.connect(self.weav_process)
        self.pushButton_clear_class.clicked.connect(self.weav_clear_class)

        self.pushButton_populate_thread_id.clicked.connect(self.weav_populate_thread_id)

        self.pushButton_mongo_create_threads_collection.clicked.connect(self.mongo_create_threads_collection)



    #  - Control - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    def weav_toggle(self):
        if self.weav_status:
            question = "Are you sure you want to disconnect from Weaviate?"
            reply = QMessageBox.question(self, 'Message', question, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                print("Shutting down")
                result = stop_docker_compose(self.docker_compose_file_path)
                if result:
                    print("Weaviate is offline")
                    self.weavdb = None
                    self.pushButton_weav_status.setIcon(QIcon('ui/weav_r.png'))
                    self.pushButton_weav_status.setToolTip("Weaviate: Offline")
                    self.pushButton_weav_refresh.setEnabled(False)
                    self.weav_status = False
                else:
                    print("Shutdown failure")
            else:
                return

        else:
            question = "Connect to Weaviate?"
            reply = QMessageBox.question(self, 'Message', question, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                print("Connecting")
                result = start_docker_compose(self.docker_compose_file_path)
                if result:
                    print("Weaviate is online")
                    self.weavdb = weav_db(self.weav_host, {'open_ai_api_key': self.credentials['open_ai_api_key']})
                    self.pushButton_weav_status.setIcon(QIcon('ui/weav_g.png'))
                    self.pushButton_weav_status.setToolTip("Weaviate: Online")
                    self.pushButton_weav_refresh.setEnabled(True)
                    self.weav_status = True
                    self.weavdb.link_progress_bar(self.progressBar)
                else:
                    print("Startup failure")
            else:
                return

    def weav_refresh(self):
        print("Refresh weav")
        pass


    # - Query - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    def get_filter(self):
        filter_where = self.textEdit_filter.toPlainText()
        filter_class = self.lineEdit_class.text()
        filter_enable = self.checkBox_filter.isChecked()
        filter_json = json.loads(filter_where)
        return filter_class, filter_enable, filter_json



    def weav_count(self):
        if not self.weav_status:
            print("Weaviate is offline")
            return
        
        filter_class, filter_enable, filter_json = self.get_filter()
        
        if filter_enable:
            count = self.weavdb.objects_get_count(filter_class, filter_json)
            print("Count filter: ", count)
        else:
            count = self.weavdb.objects_get_count(filter_class)
            print("Count no filter: ", count)

    def weav_count_distinct(self):
        if not self.weav_status:
            print("Weaviate is offline")
            return
        
        filter_class, filter_enable, filter_json = self.get_filter()

        class_to_count = self.lineEdit_class.text()
        field_to_count = self.lineEdit_field.text()

        count = self.weavdb.objects_get_count_distinct(class_to_count, field_to_count, filter_json)
        #print("Count distinct: ", count)

        


    def weav_schema(self):
        if not self.weav_status:
            print("Weaviate is offline")
            return

        schema = self.weavdb.get_schema()
        print("Schema: ", json.dumps(schema, indent=2))


    def weav_get(self):

        properties = ["body_proc"]
        filter_where = json.loads(self.textEdit_filter.toPlainText())

        item_count = self.weavdb.objects_get_count("Email", filter_where)
        print("Item count: ", item_count)

        #res = self.weavdb.objects_get(filter_where, properties, limit=item_count)
        #res = self.weavdb.objects_get(filter_where, properties, total_documents=item_count)
        self.email_bodies, self.email_vectors = self.weavdb.objects_get_pages(filter_where, properties, total_documents=item_count)
        #print(res)
        #self.email_bodies = [body['body_proc'] for body in res['data']['Get']['Email']]
        #self.email_vectors = [body['_additional']['vector'] for body in res['data']['Get']['Email']]

        print("Email bodies retrieved: ", len(self.email_bodies))
        print("Email vectors retrieved: ", len(self.email_vectors))


    def weav_schema_add(self):
        property = {
            "name": "thread_id",
            "dataType": ["text"],
            "moduleConfig": {
                "text2vec-openai": {
                    "skip": True
                }
            }
        }
        self.weavdb.schema_add_property("Email", property)



    def weav_clear_class(self):
        if not self.weav_status:
            print("Weaviate is offline")
            return

        filter_class = self.lineEdit_class.text()
        self.weavdb.clear_class(filter_class)
        print("Cleared class")

    def weav_schema_add_class(self):
        self.weavdb.class_delete("Thread")
        class_obj = {
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
        self.weavdb.schema_add_class(class_obj)


    def weav_process(self):
        import os
        from langchain.embeddings import OpenAIEmbeddings
        from langchain.vectorstores.weaviate import Weaviate
        from langchain.chains import RetrievalQA
        from langchain.llms import OpenAI
        from langchain.chat_models import ChatOpenAI

        from langchain.vectorstores import Chroma
        from langchain.chains.question_answering import load_qa_chain

        from langchain.vectorstores.weaviate import Weaviate
        from langchain.embeddings import OpenAIEmbeddings

        # self.credentials['open_ai_api_key']
        model = "gpt-3.5-turbo-16k"
        model_obj = ChatOpenAI(
            temperature=0,
            openai_api_key=self.credentials['open_ai_api_key'],
            model_name=model
        )


        prompt = f"""
            What are the main functions performed by the writter? \
            On what objects are the products performed? \
            Format your response as a python list of tuples, example: [("Function", "Object"), ("Function", "Object")].
            Limit your response to 10 tuples.
            """
        os.environ["OPENAI_API_KEY"] = self.credentials['open_ai_api_key']
        os.environ["WEAVIATE_URL"] = self.credentials['weaviate']['cluster_url']
        
        embeddings = OpenAIEmbeddings() 

        use_faiss = False

        if use_faiss:
            print(len(self.email_bodies))
            print("Create docsearch")
            from langchain.vectorstores import FAISS
            docsearch = FAISS.from_texts(texts=self.email_bodies, embedding=embeddings)
            
            print("Create qa")        
            chain = load_qa_chain(ChatOpenAI(model=model), chain_type='stuff')
            docs = docsearch.similarity_search(prompt)

            print("query")
            resp = chain.run(input_documents=docs, question=prompt)

            print("resp: ", resp)

        else:
            metadatas = [{"vector_embeddings": vec} for vec in self.email_vectors]

            docsearch = Weaviate.from_texts(texts=self.email_bodies, embedding=embeddings, metadatas=metadatas)
            print("Create qa")
            qa = RetrievalQA.from_chain_type(llm=model_obj, chain_type="stuff", retriever=docsearch.as_retriever())
            print("query")
            resp = qa.run(query=prompt)
            print("resp: ", resp)



    def weav_populate_thread_id(self):
        message_data = self.mongodb.find("emails", {"body_proc": {"$ne": ""}}, {
            "_id": 1, "thread_id": 1
        })

        from aux.aux import print_progress_bar
        from weaviate.util import generate_uuid5

        self.weavdb.client.batch.configure(
            batch_size=1000,
            dynamic=False,
            callback=check_batch_result
        )
        with self.weavdb.client.batch:
            for i in range(len(message_data)):
                print_progress_bar(0, int(100*i/len(message_data)), message=f"Processing {i} of {len(message_data)}")
                self.weavdb.objects_set_property("Email", generate_uuid5(message_data[i]['_id']), "thread_id", message_data[i]['thread_id'])




    def mongo_create_threads_collection(self):

        users = self.mongodb.find("users", {"active": 1}, {"_id": 1, "email": 1})
        
        self.progressBar.setRange(0, len(users))
        for u, user in enumerate(users):
            self.progressBar.setValue(u+1)
            user_id = user['_id']
            weaviate_user_filter = {
                "path": "user_id",
                "operator": "Equal",
                "valueText": user_id
            }

            thread_count = {}
            user_messages = self.mongodb.find("emails", {"user_id": user_id}, {
                "_id": 1, "thread_id": 1
            })

            for message in user_messages:
                if message['thread_id'] not in thread_count:
                    thread_count[message['thread_id']] = 0
                thread_count[message['thread_id']] += 1

            for thread_id in thread_count:
                thread_record = {
                    "user_id": user_id,
                    "thread_id": thread_id,
                    "email_count": thread_count[thread_id],
                    "email_ids": [],
                }

                self.mongodb.insert_one("threads", thread_record)

        self.progressBar.setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
