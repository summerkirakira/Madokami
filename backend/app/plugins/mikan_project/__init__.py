from madokami.models import PluginInfo
from madokami.plugin import register_engine
from .mikan_downloader_engine import MikanDownloaderEngine
from madokami.db import engine, Session, SQLModel


plugin_info = PluginInfo(
    namespace="summerkirakira.mikan_project",
    name="Mikan Project Plugin",
    description="A plugin for Mikan Project",
    is_internal=True,
)

register_engine(plugin_info, MikanDownloaderEngine())


with Session() as session:
    SQLModel.metadata.create_all(engine)