# DH 논문 연구 아카이브 (xiaohua-research)

디지털인문학 논문마다 사용한 **로우데이터·분석코드·산출물**을 자기완결적
꾸러미(research compendium)로 영구 보관하는 저장소.

코퍼스(`xiaohua-corpus`)가 *계속 자라는* 자료라면, 이곳의 논문 꾸러미는
출판 시점에 *얼어붙는* 자료다. 한 번 동결된 `data-raw/`는 다시 손대지 않는다.

## 두 저장소의 관계

```
xiaohua-corpus  ──(버전 태그 v0.3 + Zenodo DOI)──▶  papers/<논문>/manifest.yaml
   (살아있음)        + 그때 쓴 데이터의 동결 추출본          (얼어붙음)
```

논문은 코퍼스를 **경로가 아니라 버전으로** 가리킨다. 코퍼스가 나중에
구조를 바꿔도 논문 꾸러미는 `data-raw/`의 동결본 덕분에 그대로 재현된다.

## 새 논문 시작

```bash
python new_paper.py 2025 fengmenglong-network
# → papers/2025-fengmenglong-network/ 골격 생성
```

## 논문 색인

| 폴더 | 제목 | 게재지 | 연도 | 상태 | 코퍼스 버전 |
|------|------|--------|------|------|-------------|
| `2024-xiaohua-podcast` | 인성교육을 위한 명청 소화 팟캐스트 (예시) | 중국어문논총 | 2024 | published | v0.3 |

> 논문을 추가할 때마다 이 표 한 줄과 `papers/README.md`를 갱신한다.

## 꾸러미 표준 구조

```
papers/<연도-슬러그>/
├── README.md          출처 카드 (무엇을·어떤 데이터로)
├── manifest.yaml      메타데이터 + 코퍼스 버전 핀
├── data-raw/          ★ 원본 로우데이터 (읽기 전용·수정 금지) + SOURCES.md
├── data-processed/    가공·파생 데이터 (code로 재생성 가능)
├── code/              raw → processed → output 분석 스크립트
├── output/            출판된 그림·표
└── env/requirements.txt
```

## 운영 원칙

- **`data-raw/`는 신성불가침.** 정제·집계는 `code/`가 raw를 읽어 재생성한다.
- **대용량·바이너리**: 50MB 초과 파일은 Git LFS 또는 Zenodo에 두고 링크만 남긴다.
- **저작권·개인정보**: 雲四庫 본문, 설문 응답 등 민감 데이터는 비공개로 두고
  공개본에는 `SOURCES.md`에 출처·수집법만 기록한다. (`.gitignore` 참조)
- **소급 정리**: 기존 논문은 (로우데이터 + 핵심 스크립트 1개 + README) 최소 단위로
  가볍게 아카이브하고, 신규 논문부터 표준을 온전히 적용한다.
