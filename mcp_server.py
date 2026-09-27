import sys, json
from client import InstinctProactiveIntentReflex

def handle_mcp():
    engine = InstinctProactiveIntentReflex()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(engine.run_benchmark_proactive_reflex(), indent=2))
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            
            if method == "initialize":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {"name": "genpark-instinct-proactive-intent-reflex-skill", "version": "1.0.0"},
                    "capabilities": {"tools": {}}
                }}
            elif method == "tools/list":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [
                    {"name": "analyze_ambient_activity_stream", "description": "Parse window changes and dwell times into attention signals.", "inputSchema": {"type": "object", "properties": {"activity_events": {"type": "array"}}}},
                    {"name": "compute_proactive_confidence", "description": "Formulate Bayesian proactive intent confidence score.", "inputSchema": {"type": "object", "properties": {"context_tokens": {"type": "string"}}}},
                    {"name": "execute_guarded_dry_run", "description": "Simulate proactive micro-actions within reversible sandboxes.", "inputSchema": {"type": "object", "properties": {"intent_candidate": {"type": "string"}}}},
                    {"name": "run_benchmark_proactive_reflex", "description": "Benchmark proactive intention anticipation accuracy.", "inputSchema": {"type": "object"}}
                ]}}
            elif method == "tools/call":
                tname = req.get("params", {}).get("name")
                args = req.get("params", {}).get("arguments", {})
                if tname == "analyze_ambient_activity_stream":
                    res = engine.analyze_ambient_activity_stream(args.get("activity_events", []))
                elif tname == "compute_proactive_confidence":
                    res = engine.compute_proactive_confidence(args.get("context_tokens", ""))
                elif tname == "execute_guarded_dry_run":
                    res = engine.execute_guarded_dry_run(args.get("intent_candidate", ""), args.get("parameters", {}))
                else:
                    res = engine.run_benchmark_proactive_reflex()
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
            else:
                resp = {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}
            
            sys.stdout.write(json.dumps(resp) + "
")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "
")
            sys.stdout.flush()

if __name__ == "__main__":
    handle_mcp()
