from typing import List
from weaviate import Client
from migrate import *

SOURCE_WEAVIATE_URL = "http://localhost:8080"
TARGET_WEAVIATE_URL = "http://localhost:8080"

source_client = Client(
    url=SOURCE_WEAVIATE_URL,
)

target_client = Client(
    url=TARGET_WEAVIATE_URL,
)

classes: List[str] = [class_schema["class"] for class_schema in source_client.schema.get()["classes"]]

forward = True
classes = ["EmailUser", "EmailUserSent", "EmailUserReceived", "Email1on1Conversation"]
rest_classes = ["Email", "EmailAdjMatrix", "Email1on1"]

for cls in classes:
    if forward:
        SOURCE_WEAVIATE_CLASS = cls
        TARGET_WEAVIATE_CLASS = cls + "Bkp"
    else:
        SOURCE_WEAVIATE_CLASS = cls + "Bkp"
        TARGET_WEAVIATE_CLASS = cls


    print(f"Start migration for class '{SOURCE_WEAVIATE_CLASS}' to '{TARGET_WEAVIATE_CLASS}'")

    migrate_data_from_weaviate_to_weaviate(
            source_wv=source_client,
            target_wv=target_client,
            from_class_name=SOURCE_WEAVIATE_CLASS,
            to_class_name=TARGET_WEAVIATE_CLASS,
        )
    
    print(f"Class migrated: '{SOURCE_WEAVIATE_CLASS}' to '{TARGET_WEAVIATE_CLASS}'")


#for cls in classes:
#    print(f"Start migration for class '{cls}'")
#    migrate_data_from_weaviate_to_weaviate(
#        source_wv=source_client,
#        target_wv=target_client,
#        from_class_name=cls,
#        to_class_name=cls,
#    )
#    print(f"Class '{cls}' migrated to '{TARGET_WEAVIATE_URL}'")



