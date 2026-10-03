# solana-balance-checker

Fetch a Solana wallet balance from the public RPC — no external dependencies.

## Usage

```bash
python3 sol.py 7EcDhSYgM5p9UgnKZfJq3vQnH1GvhQVz1JvE7rxQxEPE
```

## Notes

- Public RPC endpoints are rate limited; fine for occasional lookups.
- For SPL token balances, extend with `getTokenAccountsByOwner`.
