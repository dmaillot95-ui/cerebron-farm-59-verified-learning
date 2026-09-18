from worker.learning_mvp import evaluate

def test_accept():
    b={"benchmark_id":"x","score":0.5,"secondary":{"r":0.7}}
    a={"benchmark_id":"x","score":0.6,"secondary":{"r":0.7},"ablation_passed":True}
    assert evaluate(b,a)["decision"]=="ACCEPT"

def test_rollback_regression():
    b={"benchmark_id":"x","score":0.5,"secondary":{"r":0.7}}
    a={"benchmark_id":"x","score":0.6,"secondary":{"r":0.6},"ablation_passed":True}
    assert evaluate(b,a)["decision"]=="ROLLBACK"
