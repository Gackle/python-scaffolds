from fastapi import FastAPI
from pony.orm import Database, db_session  # type: ignore
import uvicorn  # type: ignore

db = Database()
db.bind(
    provider="oracle",
    user="huangjh82",
    password="U41#9_7B",
    dsn="132.98.25.72:1521/gzcent",
)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/item/{item_id}")
@db_session
def read_item(item_id: int, q: str = None):
    result = db.select("TRADE_NO FROM T_WXPAY_ORDER WHERE APP_ID = $item_id")
    print(result)
    return {"item_id": item_id, "q": q, "result": result[0]}


@app.post("/api/system/{key_name}")
def system_demo(key_name: str):
    return {"flag": False, "keyname": key_name}


@app.post("/api/user/{key_name}")
def user_demo(key_name: str):
    return {"flag": False, "keyname": key_name}


@app.post("/api/process/{key_name}")
def process_demo(key_name: str):
    return {"flag": False, "keyname": key_name}


if __name__ == "__main__":
    uvicorn.run(app="example:app", host="127.0.0.1", port=5000, reload=True, debug=True)
