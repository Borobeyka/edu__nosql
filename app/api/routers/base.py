import importlib.util
from pathlib import Path

from fastapi import APIRouter

ROUTERS_PATH = Path(__file__).parent.resolve()


tag = ["System"]
router = APIRouter(prefix="/system", tags=tag)


@router.get(
    "/ping",
    description="Доступность сервиса",
)
def system_ping():
    return {"ok": True, "message": "Success"}


def get_all_routers():
    modules = [f for f in ROUTERS_PATH.glob("**/*.py") if f.name != "__init__.py"]

    for router_module in modules:
        spec = importlib.util.spec_from_file_location("module.name", router_module)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        router = getattr(module, "router", None)
        if router:
            yield router
