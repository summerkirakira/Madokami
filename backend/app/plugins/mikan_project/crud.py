from sqlmodel import Session
from .models import MikanRssStorage, MikanRssHistory
from sqlmodel import select
from typing import Optional
from datetime import datetime


def get_rss_storages(session: Session) -> list[MikanRssStorage]:
    rss_storages = session.exec(select(MikanRssStorage)).all()
    return [rss_storage for rss_storage in rss_storages]


def get_rss_by_link(session: Session, rss_link: str) -> Optional[MikanRssStorage]:
    rss_storage = session.exec(select(MikanRssStorage).where(MikanRssStorage.rss_link == rss_link)).first()
    return rss_storage


def record_rss_history(session: Session, rss_link: str, success: bool=True) -> Optional[MikanRssStorage]:

    rss_storage = get_rss_by_link(session, rss_link)
    if rss_storage is None:
        return None
    rss_history = MikanRssHistory(success=success, update_time=datetime.now())
    rss_storage.last_updated = datetime.now()
    rss_storage.history.append(rss_history)

    session.add(rss_storage)
    session.commit()
    session.refresh(rss_storage)
    return rss_storage


def add_rss_storage(session: Session, rss_link: str, name: str, preferred_pattern: str, banned_pattern: str) -> MikanRssStorage:
    rss_storage = MikanRssStorage(rss_link=rss_link, name=name, last_updated=datetime.now(), preferred_pattern=preferred_pattern, banned_pattern=banned_pattern)
    session.add(rss_storage)
    session.commit()
    session.refresh(rss_storage)
    return rss_storage


def remove_rss_storage(session: Session, rss_id: str) -> Optional[MikanRssStorage]:
    rss_storage = session.exec(select(MikanRssStorage).where(MikanRssStorage.id == rss_id)).first()
    if rss_storage is None:
        return None
    session.delete(rss_storage)
    session.commit()
    return rss_storage
