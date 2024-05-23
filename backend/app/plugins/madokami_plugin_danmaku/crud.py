from .models import DanmakuStorage
from sqlmodel import Session, select, delete


def get_danmaku_storage(session: Session) -> list[DanmakuStorage]:
    return [r for r in session.exec(select(DanmakuStorage)).all()]


def add_danmaku_storage(session: Session, danmaku_link: str):
    storage = DanmakuStorage(name="B站视频下载", link=danmaku_link)
    session.add(storage)
    session.commit()


def remove_danmaku_storage(session: Session, storage_id: str):
    result = session.exec(select(DanmakuStorage).where(DanmakuStorage.id == storage_id))
    if result is None:
        return None
    session.delete(result)
    session.commit()