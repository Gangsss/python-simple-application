## 이미지 뷰어
- 진행 이유 
	- 컴퓨터 비전을 공부하기 전, OpenCV 라이브러리에 익숙해지기
	- OS 모듈 익숙해지기

### 사용 라이브러리
- os
- OpenCV
	- [한글 Document](http://opencv-python.readthedocs.io/en/latest/index.html)
	- [옥수별님 블로그](https://blog.naver.com/samsjang/220498694383)
	- Opencv 설치가 아마 제일 어려울 듯..

	 
### 로직
- 현재 폴더의 이미지를 선택해 불러오기
- 불러온 이미지에서 키보드 좌, 우 방향키를 통해 이전 다음 이미지 불러오기
- 제일 좌측 혹은 제일 우측 이미지일 경우 계속 돌아가도록 설정
- ESC 버튼을 누를 경우 종료
- Crop 기능
	- 마우스 드래그를 통해 rectangle을 만든 후 c를 누르면 Crop되도록
	- rectangle이 존재하지 않을 경우 터미널에 "There is a no rectangle" 출력
- Reset 기능
	- r 버튼을 누를 경우 현재 이미지의 원본 상태로 reset
- Gray화
	- g 버튼을 누를 경우 현재 보이는 이미지가 gray로 출력
	- gray된 사진에서 g를 누를 경우엔 color로 변환