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


def apply_banned_pattern(title: str, banned_pattern: str) -> bool:
    if banned_pattern == '':
        return False
    is_searched = re.search(banned_pattern, title)
    if is_searched:
        return True
    else:
        return False


def apply_preferred_pattern(title: str, preferred_pattern: str) -> bool:
    if preferred_pattern == '':
        return False
    is_searched = re.search(preferred_pattern, title)
    if is_searched:
        return True
    else:
        return False


def apply_pattern_filter(items: list[RssFeed.Item], banned_pattern: Optional[str], preferred_pattern: Optional[str]) -> list[RssFeed.Item]:
    if preferred_pattern is None:
        preferred_pattern = ''
    if banned_pattern is None:
        banned_pattern = ''
    banned_items = banned_pattern.split('#')
    preferred_patterns = preferred_pattern.split('#')
    filtered_items = []
    for item in items:
        if any(apply_banned_pattern(item.description, banned_item) for banned_item in banned_items):
            continue
        else:
            filtered_items.append(item)

    filtered_item_map: dict[str, list[RssFeed.Item]] = {}
    for item in filtered_items:
        if f"S{item.season}E{item.episode}" in filtered_item_map:
            filtered_item_map[f"S{item.season}E{item.episode}"].append(item)
        else:
            filtered_item_map[f"S{item.season}E{item.episode}"] = [item]
    filtered_items = []
    for key, value in filtered_item_map.items():
        is_find = False
        for item in value:
            if any(apply_preferred_pattern(item.description, preferred_pattern) for preferred_pattern in preferred_patterns):
                filtered_items.append(item)
                is_find = True
                break
        if not is_find:
            filtered_items.append(value[0])
    return filtered_items


def remove_brackets(title: str) -> str:
    return re.sub(r'\[.*?\]', '', title)