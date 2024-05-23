from .models import DanmakuStorage
from sqlmodel import Session, select, delete, and_


def get_danmaku_storage(session: Session) -> list[DanmakuStorage]:
    return [r for r in session.exec(select(DanmakuStorage)).all()]


def add_danmaku_storage(session: Session, danmaku_link: str):
    storage = DanmakuStorage(name="B站视频下载", link=danmaku_link)
    session.add(storage)
    session.commit()


def remove_danmaku_storage(session: Session, storage_id: str):
    result = session.exec(select(DanmakuStorage).where(DanmakuStorage.id == storage_id)).first()
    if result is None:
        return None
    session.delete(result)
    session.commit()


def get_danmaku_storage_by_url(session: Session, url: str) -> DanmakuStorage:
    return session.exec(select(DanmakuStorage).where(DanmakuStorage.link == url)).first()