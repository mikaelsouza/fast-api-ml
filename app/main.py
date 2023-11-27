import fastapi
from fastapi.responses import JSONResponse


from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForSequenceClassification


app = fastapi.FastAPI()


model_id = "SamLowe/roberta-base-go_emotions-onnx"
file_name = "onnx/model_quantized.onnx"

model = ORTModelForSequenceClassification.from_pretrained(model_id, file_name=file_name)
tokenizer = AutoTokenizer.from_pretrained(model_id)

onnx_classifier = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
    top_k=None,
    function_to_apply="sigmoid",  # optional as is the default for the task
)


@app.get("/")
def hello_world(val: str | None = "Hello world!") -> dict[str, str]:
    return {"message": val}


@app.post("/predict")
def get_prediction(sentence: str = "Hello World!"):
    return JSONResponse(content=onnx_classifier(sentence))
