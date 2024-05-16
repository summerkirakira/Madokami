from fastapi import APIRouter, HTTPException, Depends
from madokami.drivers.deps import SessionDep, get_client_id
from .models import MikanSearchResponse, MikanSearchPostBody
from urllib.parse import quote
from .mikan_search_engine import MikanSearchEngine
from madokami.drivers.router import register_router

mikan_router = APIRouter(tags=["Mikan"])


@mikan_router.post("/mikan/search", response_model=MikanSearchResponse, dependencies=[Depends(get_client_id)])
def run_engine(search: MikanSearchPostBody):
    try:
        search_results = MikanSearchEngine().search(search.keyword)
        return MikanSearchResponse(data=search_results)
    except Exception as e:
        return MikanSearchResponse(message=f"Failed to search: {e}", success=False)


register_router(mikan_router)

