"""Step 4 (RQ3). Latency overhead of calling retrieval as an MCP tool (stdio) vs in-process.

Outputs: results/mcp_overhead.json, results/mcp_latency.csv
"""
import asyncio
import csv
import json
import random
import statistics
import sys
import time

from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

from common import HERE, RESULTS, load_topics
from search_service import SearchService

N_CALLS, SEED, K = 300, 7, 5


def pct(values, q):
    values = sorted(values)
    return values[min(len(values) - 1, int(round(q * (len(values) - 1))))]


async def via_mcp(queries):
    params = StdioServerParameters(command=sys.executable, args=[str(HERE / "mcp_server.py")], cwd=str(HERE))
    t0 = time.perf_counter()
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            startup = time.perf_counter() - t0
            t1 = time.perf_counter()
            tools = await session.list_tools()
            list_ms = (time.perf_counter() - t1) * 1000
            schema = json.dumps([t.model_dump(mode="json", exclude_none=True) for t in tools.tools],
                                ensure_ascii=False)
            await session.call_tool("search_documents", {"query": queries[0], "k": K})  # warm-up
            lat, sizes = [], []
            for q in queries:
                t = time.perf_counter()
                res = await session.call_tool("search_documents", {"query": q, "k": K})
                lat.append((time.perf_counter() - t) * 1000)
                sizes.append(len(json.dumps(res.model_dump(mode="json"), ensure_ascii=False).encode()))
    return startup, list_ms, schema, lat, sizes


def main():
    topics, _ = load_topics()
    queries = [q for _, q in random.Random(SEED).sample(topics, N_CALLS)]

    t0 = time.perf_counter()
    service = SearchService()
    direct_startup = time.perf_counter() - t0
    service.search(queries[0], K)  # warm-up
    direct = []
    for q in queries:
        t = time.perf_counter()
        service.search(q, K)
        direct.append((time.perf_counter() - t) * 1000)

    startup, list_ms, schema, mcp_lat, sizes = asyncio.run(via_mcp(queries))
    overhead = [m - d for m, d in zip(mcp_lat, direct)]
    summary = {
        "n_calls": N_CALLS, "k": K,
        "direct_ms": {"median": statistics.median(direct), "p95": pct(direct, .95), "mean": statistics.mean(direct)},
        "mcp_ms": {"median": statistics.median(mcp_lat), "p95": pct(mcp_lat, .95), "mean": statistics.mean(mcp_lat)},
        "overhead_ms": {"median": statistics.median(overhead), "p95": pct(overhead, .95),
                        "mean": statistics.mean(overhead)},
        "overhead_share_of_mcp_median": statistics.median(overhead) / statistics.median(mcp_lat),
        "server_startup_s": startup, "direct_startup_s": direct_startup,
        "list_tools_ms": list_ms, "tool_schema_bytes": len(schema.encode()),
        "response_bytes_median": statistics.median(sizes),
        "tool_schema": json.loads(schema),
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "mcp_overhead.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False))
    with open(RESULTS / "mcp_latency.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["call", "direct_ms", "mcp_ms"])
        w.writerows([(i, round(d, 3), round(m, 3)) for i, (d, m) in enumerate(zip(direct, mcp_lat))])
    print(json.dumps({k: v for k, v in summary.items() if k != "tool_schema"}, indent=1))


if __name__ == "__main__":
    main()
