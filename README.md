# key store

FastAPI로 작성된 [slow_postbox](https://github.com/chick0/slow_postbox) 프로젝트를 위한 암호화 키 저장소 입니다.

## 설치 및 실행

1. 의존성 설치
2. 환경변수 설정
    1. `.env.example` 파일을 복사해 `.env` 파일을 만든다.
    2. `.env` 파일을 상황에 맞게 수정한다.
3. 서비스 실행
    1. `start.py` 스크립트를 실행해 API 서비스를 실행한다.
       * 토큰을 변경하고 싶다면 `.KEY_STORE` 파일을 삭제후 서비스를 다시 실행하면 된다.

