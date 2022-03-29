import json
import threading
import time

import aiohttp
import asyncio

import requests
from aiohttp import web

import logging

logging.basicConfig(level=logging.CRITICAL)

app = web.Application()
routes = web.RouteTableDef()


@routes.get('/')
async def hello(request: web.Request):
    print(request)
    body = {
        "message": 'not json'
    }
    if request.can_read_body and request.content_type == 'application/json':
        request_body: dict = await request.json()
        name = request_body.get("name")
        body = {
            'message': f'my Message: {name}'
        }

    response = web.json_response(data=body, status=201, content_type='application/json')

    return response


app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=1277)
