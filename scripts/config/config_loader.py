from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from tomlkit import dumps, parse

# ============================================================
# プロジェクトルート自動検出
# ============================================================


def find_project_root(
    markers: Iterable[str] = ("pyproject.toml", ".git", "scripts"),
) -> Path:
    """
    指定されたマーカーが見つかるまで親ディレクトリを遡り、
    そのディレクトリをプロジェクトルートとみなす。

    Parameters
    ----------
    markers : Iterable[str]
        プロジェクトルートとみなすためのファイル/ディレクトリ名

    Returns
    -------
    Path
        プロジェクトルートのパス
    """
    current = Path(__file__).resolve()

    # ファイル自身ではなく、その親ディレクトリから探索を開始する
    for parent in current.parents:
        if any((parent / m).exists() for m in markers):
            return parent

    raise RuntimeError("プロジェクトルートを特定できませんでした")


# ============================================================
# プロジェクト構造を dataclass で明示化
# ============================================================


@dataclass(frozen=True)
class ProjectPaths:
    ROOT: Path
    SCRIPTS: Path
    PAGES: Path
    HTML_OUTPUT_FILE: Path
    DOCS: Paths
    HTML_TEMPLATE_FILE: Path
    LIBRARY: Path
    CONFIG: Path
    CONFIG_TOML: Path
    SNIPPETS: Path
    WORK: Path
    TEMPLATES: Path
    TEMPLATE_ALGO_PY: Path


# ============================================================
# インスタンス生成
# ============================================================

ROOT = find_project_root()

PATHS = ProjectPaths(
    ROOT=ROOT,
    SCRIPTS=ROOT / "scripts",
    CONFIG=ROOT / "scripts" / "config",
    CONFIG_TOML=ROOT / "scripts" / "config" / "config.toml",
    DOCS=ROOT / "docs",
    HTML_OUTPUT_FILE=ROOT / "docs" / "index.html",
    PAGES=ROOT / "pages",
    HTML_TEMPLATE_FILE=ROOT / "pages" / "templates" / "template.html",
    LIBRARY=ROOT / "library",
    SNIPPETS=Path("/mnt/c/Users/eieib/AppData/Roaming/Zed/snippets/python.json"),
    WORK=ROOT / ".work",
    TEMPLATES=ROOT / "templates",
    TEMPLATE_ALGO_PY=ROOT / "templates" / "template_algo.py",
)


# ============================================================
# その他設定
# ============================================================

ENCODING: str = "utf8"
URLROOT: str = "https://atcoder.jp"
KEY_CONTESTID: str = "CONTESTID"


def load_config_tomlkit() -> TOMLDocument:
    """tomlkit を用いて config.toml を読み込む（コメント保持）。"""
    with PATHS.CONFIG_TOML.open(mode="r", encoding=ENCODING) as f:
        return parse(f.read())


def save_config_tomlkit(data: TOMLDocument) -> None:
    """tomlkit を用いて config.toml に書き戻す（コメント保持）。"""
    with PATHS.CONFIG_TOML.open(mode="w", encoding=ENCODING) as f:
        f.write(dumps(data))
