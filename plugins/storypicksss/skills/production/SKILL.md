---
name: production
description: "Flow와 HyperFrames로 숏폼 제작을 시작하거나 기존 제작의 다음 단계로 이어갈 때 사용한다."
---

현재 작업 폴더가 사용자가 선택한 작품 폴더인지 확인한다. 새 제작이면 이 SKILL.md가 있는 폴더 기준 `../../scripts/init_project.py`를 Python 3으로 실행하고 작품 폴더 경로를 인자로 준다. 사용자가 새 폴더 생성을 요청하면 해당 경로를 사용한다. 이미 초기화한 작품은 그 폴더에서 이어간다.

작품 폴더에서 `work/status.md`를 읽고 `python3 .production/read_stage.py rules`와 현재 단계 번호로 작업지시서를 확인한다. Windows는 `py -3`을 쓴다. 입력은 사용자 제공 자료, 출력은 `.production/layout.md`의 종류별 폴더를 사용한다.

1~4단계는 환경 확인·브리프·시나리오 승인·진행 방식 결정이다. 5~7단계는 flow-storyboard, 8~11단계는 flow-scene-video, 12~15단계는 hyperframes-preview-edit로 이어간다. 콘티 검수에는 프로젝트의 storyboard_reviewer 역할을 사용한다. 새 프로젝트에서 역할을 아직 검색할 수 없으면 콘티 스킬에 있는 읽기 전용 대체 실행 절차를 쓴다.

완료할 때 진행 기록에 작품·장면 버전, 입력 및 산출물 경로, 사용자의 선택, 남은 작업을 적는다. 사용자가 “다음”이라고 하면 그 기록에서 이어간다.
