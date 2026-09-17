# Google Ads Transparency API

> Query Google Ads Transparency data: advertiser suggestions, creatives, and ad history.

Part of the **DataLeads** API suite (Advertising category). Requests render in a real browser with anti-bot handling and protected-page support built in - no proxies to manage, no infrastructure to run.

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/ads/google/suggestions` | V1 Ads Google Suggestions |
| POST | `/ads/google/advertiser` | V1 Ads Google Advertiser |
| POST | `/ads/google/creative` | V1 Ads Google Creative |
| POST | `/ads/google/advertiser/history` | V1 Ads Google Advertiser History |

## Quick start

```bash
curl -X POST https://data.dataleads.pro/v1/ads/google/suggestions \
  -H 'Content-Type: application/json' \
  -d '{"clientKey": "YOUR_CLIENT_KEY", "keyword": "meal kit"}'
```

Replace `YOUR_CLIENT_KEY` with your key. Get one at [https://data.dataleads.pro](https://data.dataleads.pro) - free tier included.

## MCP server

- **Remote (Streamable HTTP):** `https://data.dataleads.pro/mcp/google-ads-transparency`
- **Stdio (Docker):** `docker run -e DATALEADS_API_KEY=yourkey ghcr.io/dataleads/google-ads-transparency-mcp:latest`

## Pricing

| Tier | Price | Requests |
|---|---|---|
| Free | $0 | 500/mo |
| Starter | $9/mo | 5,000 |
| Pro | $29/mo | 25,000 |
| Business | $99/mo | 100,000 |
| Enterprise | custom | custom |

Full plan details at [https://data.dataleads.pro](https://data.dataleads.pro).

## License

MIT - see [LICENSE](LICENSE).
