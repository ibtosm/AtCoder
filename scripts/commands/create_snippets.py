from __future__ import annotations

import json
import shutil
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, Iterable, List

from ..config.config_loader import ENCODING, PATHS

# =========================
# Tag
# =========================


LIB_FILE_PATTERN = "Lib_*.py"


@dataclass(frozen=True)
class TagInfo:
    key: str
    marker: str


class Tag(Enum):
    NAME = TagInfo("name", "##############name##############")
    PREFIX = TagInfo("prefix", "######prefix######")
    BODY = TagInfo("body", "######body######")
    DESCRIPTION = TagInfo("description", "######description######")
    END = TagInfo("end", "##############end##############")

    @property
    def key(self) -> str:
        return self.value.key

    @property
    def marker(self) -> str:
        return self.value.marker

    @classmethod
    def from_marker(cls, line: str) -> Tag | None:
        for tag in cls:
            if tag.marker == line:
                return tag
        return None


# =========================
# コメント除去
# =========================


def strip_comment_prefix(line: str) -> str:
    """
    行頭が '#' の場合のみ、以下を行う:
    - '#' を除去
    - 直後のスペースをすべて除去
    """
    if not line.startswith("#"):
        return line

    content = line[1:]
    return content.lstrip(" ")


# =========================
# Snippet
# =========================


@dataclass
class Snippet:
    prefix: List[str] = field(default_factory=list)
    body: List[str] = field(default_factory=list)
    description: List[str] = field(default_factory=list)
    scope: str = "python"

    def to_dict(self) -> dict:
        return {
            "prefix": self.prefix,
            "body": self.body,
            "description": self.description,
            "scope": self.scope,
        }


# =========================
# SnippetCollection
# =========================


@dataclass
class SnippetCollection:
    items: Dict[str, Snippet] = field(default_factory=dict)

    def add(self, name: str, snippet: Snippet) -> None:
        self.items[name] = snippet

    def get(self, name: str) -> Snippet | None:
        return self.items.get(name)

    def names(self) -> Iterable[str]:
        return self.items.keys()

    def update(self, other: SnippetCollection) -> None:
        self.items.update(other.items)

    def to_dict(self) -> dict:
        return {name: snippet.to_dict() for name, snippet in self.items.items()}


# =========================
# パーサ
# =========================


def parse_lib_file(file_path: Path) -> SnippetCollection:
    with file_path.open("r", encoding=ENCODING) as f:
        lines = [line.rstrip("\n") for line in f]

    collection = SnippetCollection()
    current_tag: Tag | None = None
    snippet_name: str | None = None
    snippet: Snippet | None = None

    for line in lines:
        tag = Tag.from_marker(line)
        if tag:
            current_tag = tag
            continue

        if current_tag is Tag.NAME:
            snippet_name = strip_comment_prefix(line)
            snippet = Snippet()
            collection.add(snippet_name, snippet)
            continue

        if current_tag is Tag.END:
            snippet_name = None
            snippet = None
            continue

        if snippet and current_tag:
            content = line if current_tag is Tag.BODY else strip_comment_prefix(line)
            getattr(snippet, current_tag.key).append(content)

    return collection


# =========================
# スニペット収集
# =========================


def collect_snippets(lib_dir: Path) -> SnippetCollection:
    collection = SnippetCollection()

    for file in lib_dir.glob(LIB_FILE_PATTERN):
        parsed = parse_lib_file(file)
        collection.update(parsed)

    return collection


# =========================
# JSON 書き出し
# =========================


def write_snippets(collection: SnippetCollection, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding=ENCODING) as f:
        json.dump(collection.to_dict(), f, indent=4, ensure_ascii=False)


# =========================
# メイン
# =========================


def main() -> str:
    collection = collect_snippets(PATHS.LIBRARY)
    write_snippets(collection, PATHS.SNIPPETS)
    shutil.copy(PATHS.SNIPPETS, PATHS.SNIPPETSLOC)
    return f"✅ Snippets generated: {PATHS.SNIPPETS} {PATHS.SNIPPETSLOC}"


if __name__ == "__main__":
    print(main())
