from flask import Blueprint, render_template, request, jsonify
from .qna import get_response, suggest_practice_problems
from .utils import debug_code, format_code

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    question = data.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    response = get_response(question)
    return jsonify({"response": response})

@bp.route("/debug", methods=["POST"])
def debug():
    data = request.json
    code = data.get("code")
    if not code:
        return jsonify({"error": "No code provided"}), 400
    response = debug_code(code)
    return jsonify({"response": format_code(response)})

@bp.route("/practice", methods=["GET"])
def practice():
    topic = request.args.get("topic")
    problems = suggest_practice_problems(topic)
    return jsonify({"problems": problems})
