import pymongo
import aux

class mongo_db:
    def __init__(self, database_name, address="mongodb://localhost:27017/"):
        self.address = address
        self.database = database_name
        self.client = pymongo.MongoClient(self.address)

    def create_database(self):
        mydb = self.client[self.database]
        print("Databases", self.client.list_database_names())

    def create_collection(self, collection_name):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        print("Collections", mydb.list_collection_names())
    
    def collection_empty(self, collection_name):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        return mycol.count_documents({}) == 0
    
    def check_if_ids_exists_in_collection(self, collection_name, data):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        return mycol.count_documents(data) > 0

    def insert_one(self, collection_name, data):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        mycol.insert_one(data)

    def insert_many(self, collection_name, data, ordered=False):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        mycol.insert_many(data, ordered=ordered)



    def find_one(self, collection_name, query, ordered=False):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        return mycol.find_one(query, ordered=ordered)
    
    def find_many(self, collection_name, query):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        cursor = mycol.find({}, query)
        return [document for document in cursor]
    
    def find_all(self, collection_name):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        return mycol.find({})
    
    def find(self, collection_name, filter, projection):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        results = mycol.find(filter, projection)
        return [result for result in results]




    def create_index(self, collection_name, index):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        mycol.create_index(index)

    def drop_collection(self, collection_name):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        mycol.drop()

    def count_documents(self, collection_name, query):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        return mycol.count_documents(query)





    # EVALUATOR PROC

    def insert_many_merge_users(self, collection_name, data, ordered=False):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]

        collection_ids = mycol.distinct('_id')
        data_ids = [datum['_id'] for datum in data]

        for datum in data:
            if datum['_id'] not in collection_ids:
                mycol.insert_one(datum)
            else:
                filter = {'_id': datum['_id']}
                update = {"$set": {"active": datum['active']}}
                #mycol.update_one(datum, {'$set': datum}, upsert=True)
                mycol.update_one(filter, update)

        for id in collection_ids: 
            if id not in data_ids:
                filter = {'_id': id}
                update = {"$set": {"active": 0}}
                mycol.update_one(filter, update)

    def insert_many_merge_email_ids(self, collection_name, data, verbose=False):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]

        print()
        for d, datum in enumerate(data):
            if verbose:
                aux.print_progress_bar(0, int(100*(d+1)/len(data)), message = f"Progress: {d} / {len(data)}")
                #print(f"Progress: {d} / {len(data)}")
            try:
                mycol.insert_one(datum)
            except Exception as e:
                pass
                #print(f"Progress: {d} / {len(data)}, error {e}")


    def insert_many_merge_emails_raw(self, collection_name, data, verbose=False):
        # if type of data == list
        if type(data) == list:
            self.insert_many_merge_emails_raw_list(collection_name, data, verbose=verbose)
        # if type of data == dict
        elif type(data) == dict:
            self.insert_many_merge_emails_raw_dict(collection_name, data, verbose=verbose)


    
    def insert_many_merge_emails_raw_list(self, collection_name, data, verbose=False):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]

        if verbose:
            print()
        errors = []
        for d, datum in enumerate(data):
            if verbose:
                aux.print_progress_bar(0, int(100*(d+1)/len(data)), message = f"Progress: {d} / {len(data)}")
            try:       
                filter = {
                    "user_id": datum['user_id'],
                    "email_id": datum['email_id']
                }
                update = { "$set": {} }
                    
                if 'Date' in datum:
                    update["$set"]["date"] = datum['Date']
                if 'Subject' in datum:
                    update["$set"]["subject"] = datum['Subject']
                if 'From' in datum:
                    update["$set"]["from"] = datum['From']
                if 'To' in datum:
                    update["$set"]["to"] = datum['To']
                if 'Body' in datum:
                    update["$set"]["body_raw"] = datum['Body']
                mycol.update_many(filter, update)

            except Exception as e:
                errors.append({e:datum})
                pass

        if verbose:
            if len(errors) > 0:
                print(f"Errors: {len(errors)}")
                for i in range(min(5, len(errors))):
                    print(errors[i])
        
    


    def insert_many_merge_emails_raw_dict(self, collection_name, data, verbose=False):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]

        if verbose:
            print()
        errors = []
        for u, user_id in enumerate(data):
            print(f"Progress: {u} / {len(data)}")
            for d, datum in enumerate(data[user_id]):
                if verbose:
                    aux.print_progress_bar(0, int(100*(d+1)/len(data[user_id])), message = f"Progress: {d} / {len(data[user_id])} key: {user_id}")
                try:       
                    if 'email_id' not in datum:
                        continue

                    filter = {
                        "user_id": user_id,
                        "email_id": datum['email_id']
                    }
                    update = { "$set": {} }
                    
                    if 'Date' in datum:
                        update["$set"]["date"] = datum['Date']
                    if 'Subject' in datum:
                        update["$set"]["subject"] = datum['Subject']
                    if 'From' in datum:
                        update["$set"]["from"] = datum['From']
                    if 'To' in datum:
                        update["$set"]["to"] = datum['To']
                    if 'Body' in datum:
                        update["$set"]["body_raw"] = datum['Body']
                    mycol.update_many(filter, update)

                except Exception as e:
                    errors.append({e:datum})
                    pass


        if verbose:
            if len(errors) > 0:
                print(f"Errors: {len(errors)}")
                for i in range(min(5, len(errors))):
                    print(errors[i])


    
    def insert_many_merge_emails_proc(self, collection_name, data, verbose=False):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]

        if verbose:
            print()
        errors = []
        for d, datum in enumerate(data):
            if verbose:
                aux.print_progress_bar(0, int(100*(d+1)/len(data)), message = f"Progress: {d} / {len(data)}")
            try:       
                filter = {
                    "user_id": datum['user_id'],
                    "email_id": datum['email_id']
                }
                update = { "$set": {} }
                    
                update["$set"]["body_proc"] = datum['body_proc']

                mycol.update_many(filter, update)

            except Exception as e:
                errors.append({e:datum})
                pass

        if verbose:
            if len(errors) > 0:
                print(f"Errors: {len(errors)}")
                for i in range(min(5, len(errors))):
                    print(errors[i])


    def insert_many_merge_namekeys(self, collection_name, data, verbose=False):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]

        namekey_ids = mycol.distinct('_id')

        errors = []
        for d, key in enumerate(data):
            if verbose:
                aux.print_progress_bar(0, int(100*(d+1)/len(data)), message = f"Progress: {d} / {len(data)}")
            try:     
                if data[key] in namekey_ids:
                    continue  
                datum = {"_id": data[key], "name": key}
                mycol.insert_one(datum)

            except Exception as e:
                errors.append({e:datum})
                pass


    def distinct(self, collection_name, field, query={}, verbose=False):
        mydb = self.client[self.database]
        mycol = mydb[collection_name]
        return mycol.distinct(field, query)



    # EVALUATOR CUSTOM QUERIES

    def users_ready_for_processing(self, verbose=False):
        users_ready = {}

        users = self.find("users", {"active": 1}, {"_id": 1, "email": 1})
        for user in users:
            user_id = user['_id']
            complete = self.count_documents("emails", {"user_id": user_id, "body_proc": {"$ne": ""}})
            total = self.count_documents("emails", {"user_id": user_id})

            if complete / (total+1) > 0.9:
                users_ready[user_id] = user['email']
            
            if verbose:
                try:
                    print(f"{user_id}: {complete} / {total}, {complete/total*100:.2f}%")
                except:
                    print(f"{user_id}: {complete} / {total}")

        return users_ready
