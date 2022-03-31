from crypt import methods
from flask import request
from app import app
import pipeline


@app.route("/run", methods=["POST"])
def call_pipeline():
    params = request.json
    htmls = pipeline.pipeline_runner(params.get("pipeline"))
    import pdb; pdb.set_trace()
    return "Working"