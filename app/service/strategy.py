from app.models.request_body import CreateNewStrategy, QueryMyStrategy, QueryMyResult
from app.service.db_service import Database
from app.models.db_model import Strategy as StrategyModel, Result as ResultModel
from app.models.response import Strategy as StrategyResponse, StrategyList
import uuid

class StrategyService():
    def __init__(self, url):
        self.db_engine = Database(url)

    def handle_create_strategy(self, strategy: CreateNewStrategy):
        print("strategy post got ", strategy)
        with self.db_engine.get_db() as db:
            new_strategy = StrategyModel(
                id=uuid.uuid4(),
                creater_id=strategy.creater_id,
                created_date=strategy.created_date,
                assignemnt=strategy.assignemnt
            )
            print(new_strategy)
            db.add(new_strategy)
            db.flush()
            return StrategyResponse(
                creater_id=new_strategy.creater_id,
                created_date=new_strategy.created_date,
                assignemnt=new_strategy.assignemnt
            )

    def handle_query_strategy(self, strategy: QueryMyStrategy):
        with self.db_engine.get_db() as db:
            start_date = strategy.from_date
            end_date = strategy.to_date
            try:
                q = db.query(StrategyModel).filter(StrategyModel.creater_id == strategy.user_id)
                if start_date:
                    q = q.filter(StrategyModel.created_date >= start_date)
                if end_date:
                    q = q.filter(StrategyModel.created_date <= end_date)
            except Exception as e:
                print(e)
                raise
            strategies = [StrategyResponse(
                creater_id=strategy.creater_id,
                created_date=strategy.created_date,
                assignemnt=strategy.assignemnt
                ) for strategy in q.all()]
            
            return StrategyList(strategies=strategies)
        
    def handle_query_result(self, result: QueryMyResult):
        with self.db_engine.get_db() as db:
            try:
                last_strategy_id = db.query(StrategyModel.id).filter(StrategyModel.creater_id == result.user_id).order_by(StrategyModel.created_date.desc()).first()
                q = db.query(ResultModel).filter(
                    or_(ResultModel.strategy1_id == last_strategy_id, ResultModel.strategy2_id == last_strategy_id))

            except Exception as e:
                print(e)
                raise
            return q.all()