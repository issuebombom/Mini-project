# Desktop App Hider (for Mac)
<br/>
- 데스크탑이 지저분해서 짜증이 날 때 해당 코드를 실행하면 데스크탑(바탕화면)의 아이콘을 깨끗하게 숨겨줍니다.
- tkinter를 활용해서 GUI 형태를 가집니다.
### 작동 방식은 아래와 같이 단순합니다.
1. 터미널을 실행합니다.
2. defaults write com.apple.finder CreateDesktop false를 입력 후 엔터
3. killall Finder 입력 후 엔터를 누르면 파인더를 재시작합니다.
4. 바탕화면에 있던 아이콘들이 사라졌습니다.
5. 위 작업에서 false를 true로 바꿔서 입력 후 동일한 순서로 실행하면 아이콘이 다시 보여집니다.
