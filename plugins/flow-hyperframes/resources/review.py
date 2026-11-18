"""Run the project's storyboard reviewer on hosts without named subagent calls."""

import json
import subprocess
import sys
if sys.version_info < (3, 11):
    sys.exit("Python 3.11 이상으로 실행하세요.")

import tomllib
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    role = tomllib.loads((root / ".codex/agents/storyboard_reviewer.toml").read_text())
    request = sys.stdin.read().strip()
    if role["sandbox_mode"] != "read-only" or not request:
        raise SystemExit("A read-only role and a nonempty review request are required.")
    command = [
        "codex", "-a", "never", "exec", "--ephemeral", "--ignore-user-config",
        "--skip-git-repo-check", "--sandbox", role["sandbox_mode"], "--cd", str(root),
        "-c", "developer_instructions=" + json.dumps(role["developer_instructions"], ensure_ascii=False),
        "-",
    ]
    try:
        result = subprocess.run(command, input=request, text=True, encoding="utf-8", stdout=subprocess.PIPE)
    except FileNotFoundError:
        print("검수 호출 실패: codex CLI를 찾을 수 없습니다. 설치·PATH와 인증 상태를 확인하세요.", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"검수 호출 실패: {exc}. 실행 권한과 환경을 확인하세요.", file=sys.stderr)
        return 1
    if result.returncode:
        print("검수 호출이 실패했습니다. 위 오류를 기록하고 인증·네트워크·실행 권한을 확인하세요. 판정은 미확인입니다.", file=sys.stderr)
    elif not result.stdout.strip():
        print("검수 응답이 비어 있습니다. 판정은 미확인입니다.", file=sys.stderr)
        return 1
    if result.stdout:
        sys.stdout.buffer.write(result.stdout.encode("utf-8"))
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
