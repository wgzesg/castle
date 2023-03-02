from flask import Blueprint, make_response, jsonify
from flask_pydantic import validate
from app.models.request_body import CreateNewStrategy, QueryMyStrategy, QueryMyResult
from app.service.strategy import StrategyService
bp = Blueprint('apis', __name__)


strategy_service = StrategyService("sqlite:///./db.sqlite3")

@bp.route('/')
@validate()
def index():
    return "hello!!"

@bp.route('/strategy', methods=['POST'])
@validate()
def create_strategy(body: CreateNewStrategy):
    print("strategy post got ", body)
    try:
        resp = strategy_service.handle_create_strategy(body)
    except Exception as e:
        print("error is ", e)
        return make_response(jsonify({"error": "internal server error"}), 500)
    return make_response(jsonify(resp.dict()), 200)

    

@bp.route('/strategy', methods=['GET'])
@validate()
def retrieve_my_strategy(body: QueryMyStrategy):
    print("I got ", body)
    try:
        resp = strategy_service.handle_query_strategy(body)
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": "internal server error"}), 500)
    return make_response(jsonify(resp.dict()), 200)

@bp.route('/result', methods=['GET'])
@validate()
def get_my_result(body: QueryMyResult):
    print("I got ", body)
    try:
        resp = strategy_service.handle_query_result(body)
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": "internal server error"}), 500)
    return make_response(jsonify(resp.dict()), 200)