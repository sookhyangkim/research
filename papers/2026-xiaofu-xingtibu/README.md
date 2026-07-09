# 馮夢龍 《笑府》 形體部 논문 — 연구 꾸러미

 馮夢龍 ≪笑府≫ 形體部의 신체 감각과 웃음- 핵심도(Keyness) 분석과 ‘몸의 세 경계’ 정독을 중심으로
 
이 폴더는 위 논문에 사용한 데이터·코드·산출물을 논문의 완성 시점에서 동결한
research compendium다. `data-raw/`는 한 번 동결되면 다시 손대지 않는다.

## 메타

| 항목 | 값 |
|------|-----|
| 슬러그 | `2026-xiaofu-xingtibu` |
| 대상 | 馮夢龍 編《笑府》卷十 形體部 |
| 게재지 | (미정) |
| 연도 | 2026 |
| 상태 | 준비 중 (in preparation) |
| 코퍼스 버전 | (태그 발급 후 `manifest.yaml`에 기입) |

## 무엇을 · 어떤 데이터로

形體部 笑話 본문 **58편**(篇名 41 · 又 10 · 무제 同題 추가 7)을 정리·교감한 텍스트가
1차 자료다. 정량(빈도) 분석과 정성(가까이 읽기)을 병행하며, 빈도표 등 파생 자료는
추후 `data-processed/`에 추가한다.

- 底本: 《馮夢龍全集》 所收 《笑府》(上海古籍出版社, 影印本)
- 校勘: 海峽本(1992) 등 通行本 참조, 최종 판단은 연구자
- 상세는 `data-raw/SOURCES.md`

## 폴더 구조 (표준)

```
2026-xiaofu-xingtibu/
├── README.md            이 카드
├── manifest.yaml        메타데이터 + 코퍼스 버전 핀
├── data-raw/            ★ 원본 로우데이터 (읽기 전용·수정 금지)
│   ├── xiaofu_j10_xingtibu_text.txt
│   ├── xiaofu_j10_xingtibu_text.jsonl
│   └── SOURCES.md
├── data-processed/      가공·파생 데이터 (빈도표 등, 추후 추가)
├── code/                raw → processed → output 분석 스크립트 (추후)
├── output/              출판된 그림·표 (추후)
└── env/requirements.txt 실행 환경
```

현재는 `data-raw/`의 본문 텍스트만 동결되어 있고, 빈도표·분석 코드 등은
확정되는 대로 같은 표준에 따라 추가한다.

## 라이선스

- 본문 텍스트(전근대 원문): 퍼블릭 도메인.
- 번호 부여·층위 분리·篇名 정리·교감 등 편집 산물: CC BY-NC 4.0.

---

# Bodily Sensation and Laughter in Feng Menglong's *Xiafu*: A Keyness Analysis and Close Reading of the Three Boundaries of the Body- Research Compendium

*What did people laugh at in the late Ming? — Body and the senses in the "Physique"
section (形體部) of Feng Menglong's* Xiaofu (笑府)

This folder is a research compendium that freezes the data, code, and outputs used in
the paper above at the time of publication. Once frozen, `data-raw/` is never modified again.

## Metadata

| Field | Value |
|-------|-------|
| Slug | `2026-xiaofu-xingtibu` |
| Subject | Feng Menglong (ed.), *Xiaofu*, Vol. 10, "Physique" section (形體部) |
| Venue | (TBD) |
| Year | 2026 |
| Status | In preparation |
| Corpus version | (to be recorded in `manifest.yaml` once a tag is issued) |

## What & from which data

The primary source is the collated text of **58 jokes** from the "Physique" section
(41 titled · 10 *you* 又 same-topic add-ons · 7 untitled same-topic add-ons). The study
combines quantitative (word-frequency) and qualitative (close-reading) analysis;
derived materials such as frequency tables will be added to `data-processed/` later.

- **Base text (底本):** *Xiaofu* in *The Complete Works of Feng Menglong*
  (Shanghai Guji Publishing House, photo-reprint / 影印本)
- **Collation (校勘):** checked against the Haixia edition (1992) and other current
  editions; all final readings are the author's own judgment
- See `data-raw/SOURCES.md` for details

## Standard folder structure
