"""
예시 분석 스크립트: data-raw(동결) → data-processed → output.

철칙: data-raw는 읽기만 한다. 모든 가공물은 여기서 재생성된다.
사용: python code/analyze.py
"""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path

PAPER = Path(__file__).resolve().parent.parent
RAW = PAPER / "data-raw" / "corpus-extract-v0.3.jsonl"
PROCESSED = PAPER / "data-processed"
OUTPUT = PAPER / "output"


def load_raw() -> list[dict]:
    with RAW.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def main() -> None:
    PROCESSED.mkdir(exist_ok=True)
    OUTPUT.mkdir(exist_ok=True)

    rows = load_raw()

    # 가공: 편집 조작 빈도 집계 → data-processed
    op_counts = Counter(op for r in rows for op in r.get("operations", []))
    (PROCESSED / "operation_counts.json").write_text(
        json.dumps(dict(op_counts), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # 산출: 논문용 표 → output
    lines = ["| 편집 조작 | 빈도 |", "|---|---|"]
    lines += [f"| {op} | {n} |" for op, n in op_counts.most_common()]
    (OUTPUT / "table_operations.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"이본 {len(rows)}건 분석 → data-processed/, output/ 갱신")


if __name__ == "__main__":
    main()
