import re
from typing import Optional
from pathlib import Path
from .models import RssFeed


def get_season(title: str) -> int:
    title = title.lower()
    if 'ova' in title:
        return 0
    if '第一季' in title:
        return 1
    elif '第二季' in title:
        return 2
    elif '第三季' in title:
        return 3
    elif '第四季' in title:
        return 4
    elif '第五季' in title:
        return 5
    elif '第六季' in title:
        return 6
    elif '第七季' in title:
        return 7
    elif '第八季' in title:
        return 8
    elif '第九季' in title:
        return 9
    elif '第十季' in title:
        return 10
    elif '第十一季' in title:
        return 11
    elif '第十二季' in title:
        return 12
    elif '第十三季' in title:
        return 13
    else:
        return 1


def get_episode_by_brackets(filename: str) -> Optional[int]:
    pattern = r'\[(.*?)\]'
    matches = re.findall(pattern, filename)
    if matches:
        for match in matches:
            try:
                return int(match)
            except ValueError:
                pass


def get_episode_by_dash(filename: str) -> Optional[int]:
    pattern = r'- (\d+)'
    match = re.search(pattern, filename)
    if match:
        try:
            return int(match.group(1))
        except ValueError:
            pass


def get_episode(filename: str) -> Optional[int]:
    filename = (filename.lower()
                .replace('v2', '').replace('v3', ''))
    possible_episodes = [
        get_episode_by_brackets(filename),
        get_episode_by_dash(filename)
    ]
    possible_episodes = [episode for episode in possible_episodes if episode]
    if len(set(possible_episodes)) == 1:
        return possible_episodes[0]


def validated_filename(filename) -> str:
    # 文件名中不允许出现的特殊字符
    disallowed_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']

    for char in disallowed_chars:
        filename = filename.replace(char, '')

    return filename


def get_validated_path(path: str) -> Path:
    path = Path(path)
    if not path.is_absolute():
        path = Path.cwd() / path
    return path


def remove_duplicate_items(items: list[RssFeed.Item]) -> list[RssFeed.Item]:
    item_map = {}
    for item in items:
        item_map[f"{item.title} - S{item.season}E{item.episode}"] = item
    return list(item_map.values())


def parse_subtitle_type(title: str) -> Optional[str]:
    pattern = r'\[(.*?)\]'
    matches = re.findall(pattern, title)
    keyword_list = ['简体', '繁体', '中字', '外挂', '内嵌', '双语', '无字', '内封', '繁简', '简日', 'CHT', 'CHS']
    for match in matches:
        if any(keyword in match for keyword in keyword_list):
            return match
    return None
