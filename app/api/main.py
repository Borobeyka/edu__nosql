import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache
from sqlalchemy.orm import Session
from starlette.middleware.base import BaseHTTPMiddleware

from app.api.routers.base import get_all_routers
from app.config.secrets import ENV

app = FastAPI(title=ENV.get("FA_TITLE"), description=ENV.get("FA_DESC"))

for router in get_all_routers():
    app.include_router(router)


class RemoveContentLengthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        if "content-length" in response.headers.keys():
            del response.headers["content-length"]
        return response


app.add_middleware(RemoveContentLengthMiddleware)


@app.on_event("startup")
def startup():
    FastApiRedisCache().init(
        host_url=ENV["REDIS_HOST"],
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, Session],
    )


def main():
    uvicorn.run(
        "app.api.main:app",
        host="0.0.0.0",
        port=int(ENV.get("FA_PORT")),
        timeout_keep_alive=10000,
        reload=ENV.get("FA_RELOAD") == "1",
        debug=ENV.get("FA_DEBUG") == "1",
    )


if __name__ == "__main__":
    main()
