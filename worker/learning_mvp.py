def evaluate(before, after, regression_limit=0.0):
    if before["benchmark_id"] != after["benchmark_id"]:
        raise ValueError("benchmark mismatch")
    b=before["score"]; a=after["score"]
    delta=a-b
    regressions=[k for k,v in after.get("secondary",{}).items() if k in before.get("secondary",{}) and v < before["secondary"][k]-regression_limit]
    ablation=bool(after.get("ablation_passed",False))
    accept=delta>0 and not regressions and ablation
    return {"benchmark_id":before["benchmark_id"],"before":b,"after":a,"delta":delta,"regressions":regressions,"ablation_passed":ablation,"decision":"ACCEPT" if accept else "ROLLBACK","evidence_level":"E2","status":"PRELIMINARY"}

if __name__=="__main__":
    b={"benchmark_id":"demo-v1","score":0.70,"secondary":{"robustness":0.80}}
    a={"benchmark_id":"demo-v1","score":0.76,"secondary":{"robustness":0.81},"ablation_passed":True}
    print(evaluate(b,a))
