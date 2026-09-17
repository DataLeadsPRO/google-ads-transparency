import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE = os.environ.get('DATALEADS_BASE_URL', 'https://data.dataleads.pro/v1')
KEY = os.environ.get('DATALEADS_API_KEY', '')
mcp = FastMCP('Google Ads Transparency API')

def _call(path, payload):
    body = {'clientKey': KEY}
    body.update(payload or {})
    r = httpx.post(BASE + path, json=body, headers={'Authorization': 'Bearer ' + KEY}, timeout=120)
    r.raise_for_status()
    return r.json()

TOOLS = [
  {
    "name": "ads_google_suggestions",
    "method": "POST",
    "path": "/ads/google/suggestions",
    "description": "V1 Ads Google Suggestions"
  },
  {
    "name": "ads_google_advertiser",
    "method": "POST",
    "path": "/ads/google/advertiser",
    "description": "V1 Ads Google Advertiser"
  },
  {
    "name": "ads_google_creative",
    "method": "POST",
    "path": "/ads/google/creative",
    "description": "V1 Ads Google Creative"
  },
  {
    "name": "ads_google_advertiser_history",
    "method": "POST",
    "path": "/ads/google/advertiser/history",
    "description": "V1 Ads Google Advertiser History"
  }
]

def _register():
    import json as _json
    for t in TOOLS:
        def _make(t=t):
            def _tool(payload: dict) -> dict:
                return _call(t['path'], payload)
            _tool.__name__ = t['name']
            _tool.__doc__ = t['description']
            return _tool
        fn = _make()
        mcp.tool()(fn, name=t['name'], description=t['description'])

_register()


if __name__ == '__main__':
    mcp.run()
