import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QTableWidgetItem, QMessageBox, QInputDialog
from PyQt5.QtCore import QTextStream, Qt, QTimer, QThread, pyqtSignal, QSize
from PyQt5.QtGui import QTextCursor, QIcon
from PyQt5.uic import loadUi
import json

from mongo_db.mongo import *
from weav_db.weav import weav_db, is_valid_weaviate, check_batch_result
from mhandlers.dcompose import start_docker_compose, stop_docker_compose

import pickle


def load_pickle(filename):
    print(f"\nLoad binary: {filename}")
    with open(filename, 'rb') as f:
        messages = pickle.load(f)
    return messages

def save_pickle(data, filename):
    print(f"\nSave binary: {filename}")
    with open(filename, 'wb') as f:
        pickle.dump(data, f)



class MyWindow(QMainWindow):
    
    signal_log = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        loadUi("ui/main_window.ui", self)  # Load the .ui file

        self.setWindowTitle("Weaviate.Dev")
        
        app_icon = QIcon('ui/weav_g.png')
        self.setWindowIcon(app_icon)

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
        self.pushButton_populate_documents.clicked.connect(self.weav_populate_documents)
        self.pushButton_populate_templates.clicked.connect(self.weav_populate_templates)

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
        if not self.weav_status:
            QMessageBox.critical(self, 'Error', "Weaviate is offline", QMessageBox.Ok)
            return
        
        from weav_db.schema import schema
        
        classes = []
        class_objects = {}
        for weav_class in schema['classes']:
            classes.append(weav_class['class'])
            class_objects[weav_class['class']] = weav_class

        # Select class in an alert box that lists all classes
        class_name, ok = QInputDialog.getItem(self, "Select class", "Class:", classes, 0, False)
        class_obj = class_objects[class_name]

        question = f"Attempt to delete the class '{class_name}'?"
        reply = QMessageBox.question(self, 'Message', question, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.weavdb.class_delete(class_name)
            QMessageBox.information(self, 'Message', f"Class '{class_name}' deleted", QMessageBox.Ok)

        #Print json
        #print(json.dumps(class_obj, indent=2))

        # Qt alert box for confirmation
        question = f"Are you sure you want to add the class '{class_name}'?"
        reply = QMessageBox.question(self, 'Message', question, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        
        self.weavdb.schema_add_class(class_obj)
        QMessageBox.information(self, 'Message', f"Class '{class_name}' added", QMessageBox.Ok)



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



    def weav_populate_documents(self):
    
        print("Populate documents")
        weav_class = "EmailDocument"

        import os
        import time
        from langchain.document_loaders import PyPDFLoader 
        from langchain.document_loaders import Docx2txtLoader
        from langchain.document_loaders import TextLoader
        from langchain.text_splitter import CharacterTextSplitter

        pdf_dir = "../data/pdf"
        pdfs = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if os.path.isfile(os.path.join(pdf_dir, f))]

        
#        metadatas = load_pickle("../data/pdf/metadata.pickle")
#
#        text_splitter = CharacterTextSplitter(
#            chunk_size=8000, 
#            chunk_overlap=200, 
#            separator="\n"
#        )
#        prepath = "../data/pdf/"
#        self.progressBar.setRange(0, len(metadatas))
#        for i, metadata in enumerate(metadatas):
#            self.progressBar.setValue(i+1)
#            filename = prepath + metadata['file_name']
#
#            try:
#                if filename.lower().endswith('.pdf'):
#                    loader = PyPDFLoader(filename)
#                elif filename.lower().endswith('.docx'):
#                    loader = Docx2txtLoader(filename)
#                elif filename.lower().endswith('.txt'):
#                    loader = TextLoader(filename)
#                else:
#                    print("  File type not supported")
#                    continue
#
#                documents = loader.load()
#                chunks = text_splitter.split_documents(documents)
#
#                document = ""
#                for chunk in chunks:
#                    clean_chunk = chunk.page_content.replace("\n", " ")
#                    document += clean_chunk + "\n"
#                text_chunks = text_splitter.split_text(document)
#                metadatas[i]['chunks'] = text_chunks
#
#                print(f"Filename {filename} has length {len(document)} in {len(chunks)} chunks and {len(text_chunks)} chunks2")
#            except:
#                print(f"  Error loading file {filename}")
#                continue
#
#
#        save_pickle(metadatas, "../data/pdf/metadata_chunks.pickle")

        metadatas = load_pickle("../data/pdf/metadata_chunks.pickle")

        self.progressBar.setRange(0, len(metadatas))

        with self.weavdb.client.batch(
            batch_size=20,
            num_workers=10,
            dynamic=True,
            timeout_retries=5,
            connection_error_retries=5,
            callback=check_batch_result
        ) as batch:
            for d, metadata in enumerate(metadatas):
                self.progressBar.setValue(d+1)

                if 'chunks' not in metadata or len(metadata['chunks']) == 0:
                    print("  No chunks")
                    continue
                else:
                    print(f"  Processing {d+1} of {len(metadatas)}: {len(metadata['chunks'])} chunks")

                for chunk in metadata['chunks']:
                    data_object = {
                        "template": False,
                        "email_id": metadata['email_id'],
                        "user_id": metadata['user_id'],
                        "thread_id": metadata['thread_id'],
                        "user_email": metadata['user_email'],
                        "document_file_name": metadata['file_name'],
                        "document_id": metadata['attachment_id'],
                        "data": chunk,
                    }
                    batch.add_data_object(
                        data_object,
                        class_name=weav_class,
                    )
                    time.sleep(0.015)
        print()







    def weav_populate_templates(self):
    
        print("Populate templates")

        import os
        # List documents in '../data/pdf'
        pdf_dir = "../data/templates"
        pdfs = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if os.path.isfile(os.path.join(pdf_dir, f))]
        #for pdf in pdfs:
        #    print(pdf)


        import time
        from langchain.document_loaders import PyPDFLoader 
        from langchain.document_loaders import Docx2txtLoader
        from langchain.document_loaders import TextLoader
        from langchain.text_splitter import CharacterTextSplitter



        text_splitter = CharacterTextSplitter(
            chunk_size=8000, 
            chunk_overlap=200, 
            separator="\n"
        )
        prepath = "../data/templates/"

        files_in_prepath = [f for f in os.listdir(prepath) if (os.path.isfile(os.path.join(prepath, f)) and f.lower()[-7:] != '.pickle')]

        metadatas = []


        self.progressBar.setRange(0, len(files_in_prepath))
        for i, filename in enumerate(files_in_prepath):
            self.progressBar.setValue(i+1)
            filename = prepath + filename

            try:
                if filename.lower().endswith('.pdf'):
                    loader = PyPDFLoader(filename)
                elif filename.lower().endswith('.docx'):
                    loader = Docx2txtLoader(filename)
                elif filename.lower().endswith('.txt'):
                    loader = TextLoader(filename)
                else:
                    print("  File type not supported")
                    continue


                documents = loader.load()
                chunks = text_splitter.split_documents(documents)


                document = ""
                for chunk in chunks:
                    clean_chunk = chunk.page_content.replace("\n", " ")
                    document += clean_chunk + "\n"
                print("Document lenght:", len(document))
                chunks2 = text_splitter.split_text(document)

                metadata = {
                    "file_name": filename,
                    "chunks": chunks2
                }
                metadatas.append(metadata)

                print(f"Filename {filename} has {len(chunks)} chunks and {len(chunks2)} chunks2")
            except:
                print(f"  Error loading file {filename}")
                continue

   
        save_pickle(metadatas, "../data/templates/metadata_chunks.pickle")

        

        import time


        weav_class = "EmailDocument"

        #metadatas.append({
        #    "file_name": "void",
        #    "chunks": ["aaa"]
        #})

        self.progressBar.setRange(0, len(metadatas))

        # WARNING: Weaviate fails to upload the last document in the batch


        with self.weavdb.client.batch(
            batch_size=20,
            num_workers=10,
            dynamic=True,
            timeout_retries=5,
            connection_error_retries=5,
            callback=check_batch_result
        ) as batch:
            for d, metadata in enumerate(metadatas):
                #print_progress_bar(0, int(100*(d+1)/len(metadatas)), message=f"Processing {d+1} of {len(metadatas)}")
                self.progressBar.setValue(d+1)

                if 'chunks' not in metadata or len(metadata['chunks']) == 0:
                    print("  No chunks")
                    continue
                else:
                    print(f"  Processing {d+1} of {len(metadatas)}: {len(metadata['chunks'])} chunks")


                for chunk in metadata['chunks']:
                    print(f"Add chunk for {metadata['file_name']}")

                    #print()
                    #print("Chunk")
                    #print(chunk)
                    #print()

                    data_object = {
                        "template": True,
                        "document_file_name": metadata['file_name'],
                        "data": chunk,
                    }
                    batch.add_data_object(
                        data_object,
                        class_name=weav_class,
                    )
                    time.sleep(0.015)
        print()






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


    #window.setWindowFlags(Qt.Window)
    #app_icon = QIcon('ui/weav_g.png')
    #app.setWindowIcon(app_icon)
    #window.setIconSize(QSize(35, 35))
    #window.set_icon = app_icon



    window.show()
    sys.exit(app.exec_())
