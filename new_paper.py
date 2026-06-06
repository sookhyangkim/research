"""
새 논문 꾸러미를 표준 구조로 찍어내는 스크립트.

사용:
    python new_paper.py 2025 fengmenglong-network
    → papers/2025-fengmenglong-network/ 생성
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

MANIFEST = """\
paper:
  title: ""
  venue: ""
  year: {year}
  status: draft        # draft / under-review / published
  doi: ""
corpus:
  repo: https://github.com/<user>/xiaohua-corpus
  version: ""          # 사용한 코퍼스 git 태그 (예: v0.3)
  zenodo_doi: ""
  extract: data-raw/corpus-extract.jsonl
data_sources:
  - name: ""
    tool: ""
    accessed: ""
    note: ""
environment: env/requirements.txt
"""

README = """\
# {year} — (제목)

## 한 줄 요약
(이 논문이 무엇을 했는가)

## 재현 방법
```bash
cd env && pip install -r requirements.txt && cd ..
python code/analyze.py
```

## 데이터 출처
`data-raw/SOURCES.md`, `manifest.yaml` 참조.
"""

SOURCES = """\
# 데이터 출처 기록 (data-raw)

`data-raw/`는 읽기 전용이다. 파일별 출처·수집일·도구·공개여부를 남긴다.

| 파일 | 출처 | 수집일 | 도구 | 공개 | 비고 |
|------|------|--------|------|------|------|
|      |      |        |      |      |      |
"""


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("사용법: python new_paper.py <연도> <슬러그>")
    year, slug = sys.argv[1], sys.argv[2]
    base = ROOT / "papers" / f"{year}-{slug}"
    if base.exists():
        raise SystemExit(f"이미 존재: {base}")

    for sub in ("data-raw", "data-processed", "code", "output", "env"):
        (base / sub).mkdir(parents=True)
    (base / "manifest.yaml").write_text(MANIFEST.format(year=year), encoding="utf-8")
    (base / "README.md").write_text(README.format(year=year), encoding="utf-8")
    (base / "data-raw" / "SOURCES.md").write_text(SOURCES, encoding="utf-8")
    (base / "env" / "requirements.txt").write_text("", encoding="utf-8")
    for keep in ("data-processed", "output"):
        (base / keep / ".gitkeep").touch()

    print(f"생성됨: {base}")
    print("→ README의 논문 색인 표에 한 줄 추가하는 것을 잊지 마세요.")


if __name__ == "__main__":
    main()
