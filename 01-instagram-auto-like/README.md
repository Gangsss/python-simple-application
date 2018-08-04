## 인스타그램 자동 좋아요
- 진행 이유 
	- Python 익숙해지기
	- css selector를 찾는 과정은 데이터 크롤링 과정과 유사하기 때문에 크롤링할 때 도움이 됨
	

### 사용 라이브러리
- [Selenium](http://selenium-python.readthedocs.io/)
	- Chrome Driver 권장

### 로직
- 인스타그램 로그인
- 인스타그램 타임라인 좋아요
- 인스타그램 특정 해시태그 좋아요 
- 인스타그램 특정 지역 좋아요
- 특정 댓글에 자동으로 답글 달기
	- 예시 : 와 사진이 정말 이뻐요 -> 감사합니다 


### 심화
- 서버(AWS EC2, GCP Compute Engine)에 Cronjob 설정
- AWS Lambda를 사용해 Cronjob 설정 
- 특정 댓글일 경우 답글 달기 개선 : 단순 로직이 아닌 딥러닝 모델 사용
	