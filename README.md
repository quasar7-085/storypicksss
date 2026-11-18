# Flow HyperFrames

Google Flow에서 장면을 만들고 HyperFrames Desktop에서 편집할 수 있는 한국어 Codex 플러그인입니다. 승인한 시나리오를 기준으로 컷별 콘티와 한·영 프롬프트를 만들고, 선택한 영상과 내레이션을 편집 가능한 프로젝트로 전달합니다.

## 설치

Codex CLI에서 다음 두 명령을 실행합니다. 첫 번째 명령은 이 GitHub 저장소를 마켓플레이스로 등록하고, 두 번째 명령은 플러그인을 설치합니다.

```sh
codex plugin marketplace add quasar7-085/repo
codex plugin add flow-hyperframes@flow-studio
```

설치 결과는 `codex plugin list --marketplace flow-studio`로 확인합니다. Codex에서 작품을 저장할 폴더를 열고 새 채팅을 시작합니다. 로컬에 복제한 저장소로 설치하려면 첫 명령 대신 저장소 루트에서 `codex plugin marketplace add .`을 실행합니다.

## 첫 영상 만들기

1. 제작할 컴퓨터에 Python 3, gflow, HyperFrames Desktop을 준비하고 사용할 Google Flow 계정으로 로그인합니다. 독립 콘티 검수의 CLI 대체 경로를 쓰려면 Python 3.11 이상과 로그인된 Codex CLI가 필요합니다. [gflow 설치](https://github.com/ffroliva/gflow-cli) · [HyperFrames Desktop 설치](https://github.com/heygen-com/hyperframes/blob/main/docs/studio-app/index.mdx)
2. 작품 폴더에서 원고나 이미지를 첨부하고 아래처럼 요청합니다. 플러그인이 제작 폴더를 준비하고 환경 확인부터 시작합니다.
3. 시나리오를 승인하고 순차 또는 일괄 진행을 고릅니다. 생성된 컷을 선택하면 HyperFrames 타임라인으로 이어집니다. MP4가 필요하면 편집본 버전을 지정해 내보내기를 요청합니다.

> Flow HyperFrames로 이 자료를 바탕으로 30초 세로 영상을 만들어줘. 시나리오부터 보여줘.

> 02는 통과. 03A는 화면 밖 내레이션만 들리고 인물은 입을 다문 채 표정으로만 연기하도록 프롬프트를 수정해줘.

## 생성 파일은 어디에 있나요?

아래는 **작품 폴더**입니다. 새 버전을 만들어도 이전 작업을 보관합니다.

```text
my-film/
├── sources/                     제공 원본
├── work/status.md               현재 단계와 선택한 컷
├── outputs/
│   ├── planning/                시나리오
│   ├── images/references/       캐릭터·소품
│   ├── images/storyboards/      장면 콘티
│   ├── prompts/                 ko·en 프롬프트
│   ├── video/scenes/            장면별 원본 영상
│   ├── edit/cut-v01/            HyperFrames 프로젝트와 assets
│   └── exports/                 내보낸 영상
├── .production/                 작품에 적용한 작업지시서와 도구
└── .codex/agents/               읽기 전용 콘티 검수 역할
```

예를 들어 `s03a-board-v02.png`, `s03a-prompt-en-v02.md`, `s03a-flow-v02.mp4`는 03A 컷의 콘티·프롬프트·생성 영상입니다. 각 파일의 버전은 독립적으로 관리하고 채택 조합은 진행 기록에 남깁니다. [전체 파일명 규칙](plugins/flow-hyperframes/resources/layout.md)

## 플러그인 저장소 구조

| 경로 | 용도 |
|---|---|
| `.agents/plugins/marketplace.json` | GitHub에서 설치할 때 읽는 마켓플레이스 목록 |
| `plugins/flow-hyperframes/` | 플러그인 매니페스트와 Codex 호환 매니페스트 |
| `plugins/flow-hyperframes/skills/` | 제작 시작, 콘티, 장면 생성, 편집 스킬 |
| `plugins/flow-hyperframes/resources/` | 15단계 지시서, 파일명 규칙, 콘티 검수 역할과 실행 도구 |
| `plugins/flow-hyperframes/scripts/` | 작품 폴더 초기화 |

플러그인 소스를 복제한 개발자는 `python3 plugins/flow-hyperframes/scripts/init_project.py ../my-film`으로 작업 폴더를 직접 만들 수 있습니다. 기존 작품에서 다시 실행하면 편집한 지시서와 생성 파일을 보존합니다. [15단계 작업지시서](plugins/flow-hyperframes/resources/workflow.md)
