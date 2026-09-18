import json
for p in ["config/farm_policy_v1.json","config/engine_registry.json","schemas/job.schema.json","schemas/artifact.schema.json","schemas/evidence.schema.json"]:
    with open(p,encoding="utf-8") as f: json.load(f)
print("CONFIG_VALID")
