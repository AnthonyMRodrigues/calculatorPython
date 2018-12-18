import pymongo
import pandas
from sklearn.feature_extraction.text import CountVectorizer

class Analise:
    def startDatabase(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.twitter
        self.collection = self.db.tweets
        return True

    def getItens(self):
        self.items = [{
                "created_at": item["created_at"],
                "text": item["text"],
                "user_name": item["user_name"],
            }
            for item in self.collection.find()]

    def createPandas(self):
        self.items = pandas.DataFrame(self.items)

    def generateSkit(self):
        self.textcv = CountVectorizer()
        self.usercv = CountVectorizer()
        self.text = self.textcv.fit_transform(self.items.text)
        self.user_name = self.usercv.fit_transform(self.items.user_name)

        users = pandas.DataFrame(self.usercv.get_feature_names(), columns=["word"])
        users["count"] = self.user_name.sum(axis=0).tolist()[0]
        users = users.sort_values("count", ascending=False).reset_index(drop=True)

        text = pandas.DataFrame(self.textcv.get_feature_names(), columns=["word"])
        text["count"] = self.text.sum(axis=0).tolist()[0]
        text = text.sort_values("count", ascending=False).reset_index(drop=True)

        print(text)


if __name__ == "__main__":
    analise = Analise()
    analise.startDatabase()
    analise.getItens()
    analise.createPandas()
    analise.generateSkit()
