# 2024 — 인성교육을 위한 명청 소화 팟캐스트 (예시 꾸러미)

> 이 폴더는 꾸러미 구조를 보여주는 **예시**다. 실제 논문으로 채울 때
> 자리표시자를 교체한다.

## 한 줄 요약
명청 소화를 팟캐스트 형식으로 재구성해 인성교육 자료로서의 가능성을 분석한 논문의
재현 패키지.

## 무엇이 들어 있나
- `data-raw/` — 분석에 쓴 원본 데이터(동결). 수정 금지.
- `code/` — `data-raw`를 읽어 표·그림을 재생성하는 스크립트.
- `output/` — 논문에 실린 산출물.
- `manifest.yaml` — 사용한 코퍼스 버전·DOI, 데이터 출처, 실행 환경.

## 재현 방법
```bash
cd env && pip install -r requirements.txt && cd ..
python code/analyze.py        # data-raw → data-processed → output
```

## 데이터 출처
`data-raw/SOURCES.md` 및 `manifest.yaml`의 `data_sources` 참조.
