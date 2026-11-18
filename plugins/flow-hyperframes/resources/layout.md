# 제작 폴더와 파일명

작품마다 별도 폴더를 사용한다. 제작 중 생긴 파일은 아래 용도별로 저장하고, 사용자에게 전달할 때 실제 경로를 링크한다.

| 폴더 | 내용 | 이름 예시 |
|---|---|---|
| `sources/` | 사용자가 제공하거나 선택한 원본 사본 | 받은 파일명 유지 |
| `work/` | 진행 기록, 임시 파일, 검수 요청과 응답 | `status.md` |
| `outputs/planning/` | 브리프와 승인 시나리오 | `scenario-v01.md` |
| `outputs/images/references/` | 인물·소품 참조 | `character-mother-v01.jpg` |
| `outputs/images/storyboards/` | 장면별 콘티 | `s03a-board-v02.png` |
| `outputs/prompts/` | 같은 버전의 한국어 검토본과 영어 제출본 | `s03a-prompt-ko-v02.md`, `s03a-prompt-en-v02.md` |
| `outputs/video/scenes/` | Flow에서 받은 원본 영상 | `s03a-flow-v02.mp4` |
| `outputs/edit/` | 버전별 HyperFrames 프로젝트 | `cut-v02/index.html`, `cut-v02/hyperframes.json`, `cut-v02/assets/` |
| `outputs/exports/` | 사용자가 요청한 내보내기 | `film-v02.mp4` |

- 컷 번호는 두 자리로 쓰고 분할 컷은 소문자를 붙인다. 버전은 자산별로 증가시키고 이전 판을 보존한다. 확장자는 실제 포맷을 따른다.
- Flow 결과는 내려받은 뒤 해당 장면 폴더에 복사한다. 진행 기록에 원래 이름·생성 ID·새 경로·채택 버전을 남긴다. Finder 선택을 받았을 때도 같은 방식으로 대응시킨다.
- 편집본에 쓰는 미디어는 해당 편집본의 `assets/`에 복사해 상대 경로로 연결한다. 승인한 화면과 음성의 출처가 다르면 둘 다 기록한다. 폴더 전체를 옮겨도 다시 열 수 있어야 한다.
- 배치 생성이나 재개 시 이미 쓰인 이름은 덮어쓰지 않는다. 같은 장면·요청 ID의 완료 파일이 있으면 그 경로를 재사용한다.
