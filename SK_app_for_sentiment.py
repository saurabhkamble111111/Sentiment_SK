from fastapi import FastAPI
from sentiment_on_complete_article import sentiment_on_complete_article
from fastapi.middleware.cors import CORSMiddleware
# import json
from pydantic import BaseModel

origins = ["*",]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    a: str
    article_number: str



@app.post("/items/")
async def create_item(item: Item):
    result=sentiment_on_complete_article(item.a,item.article_number)
    return result
    # return item.a

# @app.post("/items")
# def read_item():
#     # article_number=10
    
#     body = requests.body.read().decode('utf-8')
#     d = json.loads(body)
#     # text=list(d.values())[0]
#     # print(body)
#     # print(d)
#     # print(d["aspects"])
#     # print(type(d["aspects"]))
#     # all_aspect_list = ast.literal_eval(d["aspects"])
#     # xyz=ADAPTIVE_ASPECT_BERT_SENTIMENT_FUNCTION(d["texts"],all_aspect_list)
#     # print(xyz)
#     # print(type(xyz))
#     # return {'input': d}
#     # return {"ArticleID":str(d["id"]),"Output":str(xyz)}
#     # result=sentiment_with_bert_with_three_output_arguments(a,article_number)
#     result=sentiment_with_bert_with_three_output_arguments(d["a"],d["article_number"])
#     return result