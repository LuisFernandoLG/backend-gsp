import json
import uuid


class JsonDB():
    def __init__(self):
        self.appforms = []
        self.fileName = "data.json"

    def insert(self, appForm: dict):
        self.loadData()
        appForm = self.insert_id(appForm)
        self.appforms.append(appForm)
        with open(self.fileName, "w") as outFile:
            json.dump(self.appforms, outFile)

    def loadData(self):
        with open(self.fileName) as jsonFile:
            self.appforms = json.load(jsonFile)

    def get_all_appforms(self):
        self.loadData()
        return self.appforms

    def delete(self):
        pass

    def get_random_id(self):
        return uuid.uuid1()

    def insert_id(self, appForm: dict):
        id = str(uuid.uuid4())
        newAppForm = {**appForm, "id": id}
        return newAppForm
