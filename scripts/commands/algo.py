import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from ..config.config_loader import ENCODING, KEY_CONTESTID, PATHS, load_config_tomlkit

# from tomlkit import parse


CONTESTID = load_config_tomlkit()[KEY_CONTESTID]
template_path = PATHS.TEMPLATE_ALGO_PY


class Task:
    def __init__(self, task: str) -> None:
        self.taskid = ""
        self.contest = ""
        self.url = ""
        _isalp = re.fullmatch(r"[a-zA-Z]", task)
        _isurl = re.fullmatch(
            r"https://atcoder\.jp/contests/([^/]+)/tasks/([^/]+)", task
        )
        assert _isalp or _isurl, f"❌task is invalid ***{task}***"
        if _isurl:
            self.url = task
            self.contest, self.taskid = _isurl.groups()
        else:
            self.contest = CONTESTID
            self.taskid = f"{self.contest}_{task}"
            self.url = f"https://atcoder.jp/contests/{self.contest}/tasks/{self.taskid}"

    def __str__(self) -> str:
        _wk: list[str] = [self.taskid, self.contest, self.url]
        return "\n".join(_wk)


def prepare_task_dir(task: Task) -> Path:
    task_dir = PATHS.WORK / task.taskid
    task_dir.mkdir(parents=True, exist_ok=True)
    return task_dir


def download_testcases(task: Task, task_dir: Path) -> None:
    test_dir = task_dir / "test"
    if test_dir.exists():
        return

    original_dir = Path.cwd()
    try:
        os.chdir(task_dir)
        print(f"📥 ダウンロード中: {task.url}")
        subprocess.run(["oj", "d", task.url], check=True)
    finally:
        os.chdir(original_dir)


def prepare_script(task: Task) -> bool:
    target_script = PATHS.WORK / f"{task.taskid}.py"
    no_script = not target_script.exists()
    if no_script:
        shutil.copy(template_path, target_script)

    with open(target_script, "r", encoding=ENCODING) as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith('"""http'):
        lines.insert(0, f'"""{task.url}"""\n')
        with open(target_script, "w", encoding=ENCODING) as f:
            f.writelines(lines)

    subprocess.run(["zed", str(target_script)], check=True)
    return no_script


def run_tests(task: Task, task_dir: Path) -> None:
    print(f"🧪 テスト実行: {task.taskid}")
    main_script = task_dir / "main.py"
    target_script = PATHS.WORK / f"{task.taskid}.py"
    shutil.copy(target_script, main_script)

    original_dir = Path.cwd()
    try:
        os.chdir(task_dir)
        subprocess.run(
            ["oj", "t", "-c", "python3 main.py"],
            check=False,
        )
    finally:
        os.chdir(original_dir)


def run_submit(task: Task, task_dir: Path) -> None:
    print(f"🧪 提出: {task.taskid}")
    main_script = task_dir / "main.py"
    target_script = PATHS.WORK / f"{task.taskid}.py"
    shutil.copy(target_script, main_script)

    original_dir = Path.cwd()
    try:
        os.chdir(task_dir)
        subprocess.run(
            ["oj", "submit", task.url, "main.py", "-l", "6082"],
            # ["acc", "submit","-t", task.url, "main.py"],
            check=False,
        )
    finally:
        os.chdir(original_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="ジョブとタスクを指定するスクリプト")
    parser.add_argument("task", help="タスク名/url")
    parser.add_argument("-s", "--submit", action="store_true", help="submit オプション")

    args = parser.parse_args()

    task = Task(args.task)
    task_dir = prepare_task_dir(task)

    if args.submit:
        run_submit(task, task_dir)

        return

    no_answer = prepare_script(task)
    download_testcases(task, task_dir)

    if no_answer:
        return

    run_tests(task, task_dir)


if __name__ == "__main__":
    main()
