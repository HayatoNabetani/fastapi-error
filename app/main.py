from fastapi import BackgroundTasks, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def test222222():
    print("aaaaaaaa")
    print("1 + 2")


@app.get("/ossss")
def root2(background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(test222222)
    except Exception as e:
        print(e)
    return {"message": "ok"}


@app.get("/")
def root():
    return {"message": "Hello, World"}
