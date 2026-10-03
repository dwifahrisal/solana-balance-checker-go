#!/usr/bin/env python3
"""Fetch a Solana wallet's SOL balance from a public RPC endpoint."""

import json
import sys
import urllib.request

RPC_URL = "https://api.mainnet-beta.solana.com"


def rpc_call(method: str, params: list) -> dict:
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    req = urllib.request.Request(RPC_URL, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 sol.py <solana-address>", file=sys.stderr)
        return 1
    address = sys.argv[1]
    if len(address) < 32:
        print("invalid solana address", file=sys.stderr)
        return 1

    result = rpc_call("getBalance", [address])
    if "result" not in result:
        print(f"error: {result}", file=sys.stderr)
        return 1

    lamports = result["result"]["value"]
    print(f"address : {address}")
    print(f"balance : {lamports / 1e9:.6f} SOL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
