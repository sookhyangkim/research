# SOURCES — 출처·수집·교감 기록

`data-raw/`는 **읽기 전용·동결** 데이터다. 아래 출처와 교감 방침은 출판 시점 기준으로 고정한다.

## 수록 자료

| 파일 | 내용 |
|------|------|
| `xiaofu_j10_xingtibu_text.txt`   | 笑府 卷十 形體部 笑話 본문 58편 (사람이 읽는 정리본) |
| `xiaofu_j10_xingtibu_text.jsonl` | 위와 동일 내용의 기계가독 정본 (줄당 1편) |

- 범위: 形體部 笑話 **본문** 58편 — 篇名 있음 41 · 又(同題 추가편) 10 · 篇名 없는 同題 추가 소화 7.
- 제외: 評語 · 小序 · 夾註(방언·교감 주기)는 본 층위에 포함하지 않는다.
- 표기: 正字. (빈도 분석을 위한 추가 정규화는 별도 `data-processed/`에서 수행하며 본 raw는 손대지 않는다.)

## 底本 (base text)

《馮夢龍全集》 所收 《笑府》, 上海古籍出版社, **影印本**.

## 校勘 (collation)

- 海峽本(福州: 海峽文藝出版社, 1992) 등 **通行本**을 참조해 교감하였다.
- 影印本은 영인 특성상 字形이 불분명한 곳이 있어, 그러한 부분과 異文은 通行本 교감으로 보완하였다.
- 海峽本은 외설 조목을 存目刪文(목차에 제목만 남기고 본문 삭제)하였으므로, 해당 조목 본문은 通行本 교감으로 메웠다.
- **최종 본문 확정(校訂)은 모두 연구자의 직접 판단에 따른다.**

## 동결 정보

- 코퍼스 버전 핀: `manifest.yaml`의 `corpus` 항목 참조.
- 작성일: 2026-06-18.

---

# SOURCES — Provenance, Collection & Collation Record

`data-raw/` is read-only, frozen data. The sources and collation policy below are
fixed as of the time of publication.

## Contents

| File | Description |
|------|-------------|
| `xiaofu_j10_xingtibu_text.txt`   | *Xiaofu*, Vol. 10, "Physique" section (形體部): body text of 58 jokes (human-readable edition) |
| `xiaofu_j10_xingtibu_text.jsonl` | Same content in machine-readable form (one joke per line) |

- **Scope:** 58 jokes from the "Physique" section — 41 titled · 10 *you* (又, same-topic add-ons) · 7 untitled same-topic add-ons.
- **Excluded:** commentary (評語), prefaces (小序), and interlinear notes (夾註, dialect/collation glosses) are not part of this layer.
- **Orthography:** traditional characters (正字). Any further normalization for frequency analysis is done separately in `data-processed/`; this raw layer is never altered.

## Base text (底本)

*Xiaofu* in *The Complete Works of Feng Menglong* (上海古籍出版社 / Shanghai Guji
Publishing House), photo-reprint (影印本).

## Collation (校勘)

- Collated against current editions including the Haixia edition (福州: 海峽文藝出版社 /
  Haixia Literature & Art Publishing House, 1992).
- Because the photo-reprint has some illegible glyphs, those passages and textual
  variants were supplemented through collation with current editions.
- The Haixia edition kept only the titles of bawdy entries while cutting their body
  text (存目刪文); the text of those entries was therefore filled in by collation with
  current editions.
- All final readings (校訂) rest on the author's own judgment.

## Freeze information

- Corpus version pin: see the `corpus` field in `manifest.yaml`.
- Date: 2026-06-18.
