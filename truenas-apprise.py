#!/usr/bin/env python3
import os
import sys
from aiohttp import web
from aiohttp import ClientSession

APPRISE_BASEURL = os.environ.get("APPRISE_URL", "http://apprise-api-apprise-api:8000")

APPRISE_CONFIG_ID = os.environ.get(
    "APPRISE_CONFIG_ID",
    "afd284184aa5b9fa83abb296d4889bd774a6b0e27f4b5ec8a5e15a31689f849d",
)

APPRISE_TAG = os.environ.get("APPRISE_TAG", "signal")

APPRISE_NOTIFY_URL = "%s/notify/%s" % (APPRISE_BASEURL, APPRISE_CONFIG_ID)
# The ip address the service should listen on
LISTEN_HOST = os.environ.get("LISTEN_HOST", "127.0.0.1")
LISTEN_PORT = os.environ.get("LISTEN_PORT", 12345)

routes = web.RouteTableDef()


# Listen to post requests on / and /message
@routes.post("/")
@routes.post("/message")
async def on_message(request):
    content = await request.json()
    # The content of the alert message
    message = content["text"]
    print("===== Alert =====")
    print(message)

    resp = await send_message(message)

    # Return the status code to truenas
    return web.Response(status=resp.status)


async def send_message(message):
    # POST body
    json = {"body": message, "tag": APPRISE_TAG}
    headers = {"content-type": "application/json"}

    async with ClientSession() as session:
        async with session.post(APPRISE_NOTIFY_URL, json=json, headers=headers) as resp:
            print(resp)
            return resp


if __name__ == "__main__":
    # Listen on default port
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host=LISTEN_HOST, port=LISTEN_PORT)
