# 2022-2 인공지능금융투자 팀 프로젝트
- 6팀
</br></br>

## 🙆‍♀️ 팀원
- 팀장: 정보시스템공학과 윤수윤  
- 팀원: 정보시스템공학과 김예지, 통계학과 신효민
</br>

## 💻 협업 툴
- 개발: 깃허브 (https://github.com/2022AIFT/2022AIFT)
- 기록, 일정 공유 등: 노션 (https://www.notion.so/d1066cf0171648bab4b3a0a8ac2deadd)
</br>

## 🔍 브랜치 전략: Github-Flow 
<img src = "https://user-images.githubusercontent.com/105106912/193440259-71f2af1e-e0ef-4d07-ae82-ea6ff5f8f2ce.png" width = "70%" height = "70%"></br>
- 수시로 릴리즈 되어야 할 필요가 있는 서비스를 지속적으로 테스트하고 배포하는 팀이라면 github-flow 와 같은 간단한 work-flow가 적합  
- **main 브랜치에는 개발이 끝난 내용들을 merge**만, 개발은 다른 브랜치를 따로 만들어서 그 브랜치에서 수행.
- main 브랜치에 merge 하기 전에는 충분한 테스트가 필요 (merge 전에 pull request)
- 항상 원격지에 자신이 하고 있는 일들을 올려 다른 사람들도 확인할 수 있도록 해줘야 함
- 맡은 파트 끝나면 노션에 기록
</br>

## 📕 기타 사항
1. 자동 로그인 설정 (최초 1회 설정)
- KOAStudio 실행 후 좌측 상단의 Open API 접속 클릭 > 계좌 정보 입력해 로그인
<img src = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4aebabae-a6e0-408e-87a3-f37c9b5f4148/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T104143Z&X-Amz-Expires=86400&X-Amz-Signature=18bd4f971e571e89b4e9bc1e9fe321b396b88e7a693c4eba253374ee0f351743&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject" width = "30%" height = "30%"></br>
- ‘숨겨진 아이콘 표시’ 클릭해서 아래 그림에 있는 아이콘 우클릭 > 계좌비밀번호저장 클릭
- 1️⃣ AUTO 체크 2️⃣ 계좌 비밀번호(모의투자는 초기 비밀번호 모두 0000으로 동일) 입력 3️⃣ 전체계좌에 등록 클릭
<img src = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/01f8ddbf-fa8c-4e83-8ba6-98e1c0cc03b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T104332Z&X-Amz-Expires=86400&X-Amz-Signature=5d9db2923224e2006e62a60242633d4cc5b352b5b7bca4d934975d84ac0883cb&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject" width = "30%" height = "30%"><img src = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/63028253-41ed-43a6-be65-79c160482677/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221208T104454Z&X-Amz-Expires=86400&X-Amz-Signature=1b972a40e588252acb52d5fdd0b0c67a2d54745e6c7def78653f10f4d379d08d&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject" width = "70%" height = "70%"></br>
- 설정 후 효과: 로그인 창이 뜨면 자동으로 로그인됨  
2. 버전처리 (versioning.py)
- 하루에 한번씩 실행하기 (이유: 자동 로그인 설정해놓으면 버전처리가 안 됨. versioning.py 실행하면 자동로그인을 잠시 해제해 버전처리를 받고, 버전처리가 끝나면 다시 자동로그인 설정함)
- 주의사항: 코드 제일 마지막 줄은 개인정보 보호를 위해 가린 채로 깃허브에 업로드함. 실제로 pull을 받아서 실행하고자 할 때는 마지막 줄을 사용자의 아이디, 비밀번호로 수정 후 실행
```python
if __name__ == "__main__":
    # 실행 전 아이디, 비밀번호, 공동인증서 비밀번호 차례대로 입력
    version("아이디 입력", "비밀번호", "공동인증서 비밀번호")
```
