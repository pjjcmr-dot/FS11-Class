# 개발 환경 설정 가이드 (Development Environment Setup Guide)

## Python 설치 (Python Installation)

### Windows
1. https://www.python.org/downloads/ 에서 Python 다운로드
2. 설치 시 "Add Python to PATH" 옵션 체크
3. 설치 확인:
```bash
python --version
pip --version
```

### macOS
```bash
# Homebrew를 사용하여 설치
brew install python3

# 확인
python3 --version
pip3 --version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip

# 확인
python3 --version
pip3 --version
```

## 코드 에디터 설치 (Code Editor Installation)

### Visual Studio Code (추천)
1. https://code.visualstudio.com/ 에서 다운로드
2. 설치 후 실행
3. 필수 확장 프로그램 설치:
   - Python
   - Pylance
   - Code Runner (선택사항)

### VSCode 설정
```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "autopep8",
    "editor.formatOnSave": true,
    "editor.tabSize": 4
}
```

## Git 설치 및 설정 (Git Installation and Configuration)

### Git 설치
- Windows: https://git-scm.com/download/win
- macOS: `brew install git`
- Linux: `sudo apt install git`

### Git 초기 설정
```bash
# 사용자 정보 설정
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 기본 브랜치 이름 설정
git config --global init.defaultBranch main

# 설정 확인
git config --list
```

## 가상 환경 설정 (Virtual Environment Setup)

### Python 가상 환경 생성
```bash
# 가상 환경 생성
python -m venv venv

# 가상 환경 활성화
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 가상 환경 비활성화
deactivate
```

### 패키지 관리
```bash
# requirements.txt 생성
pip freeze > requirements.txt

# requirements.txt에서 설치
pip install -r requirements.txt
```

## 프로젝트 구조 생성 (Project Structure Creation)

```bash
# 프로젝트 디렉토리 생성
mkdir my_project
cd my_project

# Git 저장소 초기화
git init

# 가상 환경 생성
python -m venv venv

# .gitignore 파일 생성
cat > .gitignore << EOF
venv/
__pycache__/
*.pyc
.env
.vscode/
EOF

# README.md 파일 생성
echo "# My Project" > README.md
```

## 유용한 패키지 설치 (Useful Packages Installation)

```bash
# 기본 개발 도구
pip install pytest          # 테스트 프레임워크
pip install black           # 코드 포맷터
pip install pylint          # 코드 검사 도구
pip install ipython         # 향상된 Python 쉘

# 데이터 분석 (선택사항)
pip install numpy pandas matplotlib

# 웹 개발 (선택사항)
pip install flask requests
```

## 문제 해결 (Troubleshooting)

### Python 버전 관리
```bash
# 여러 Python 버전이 있는 경우
python3.9 -m venv venv      # 특정 버전 사용
```

### pip 업그레이드
```bash
python -m pip install --upgrade pip
```

### 권한 오류 (Permission Error)
```bash
# --user 플래그 사용
pip install --user package_name
```

## 첫 번째 프로그램 실행 (Running Your First Program)

1. 파일 생성: `hello.py`
```python
print("Hello, FS11!")
```

2. 실행:
```bash
python hello.py
```

3. 출력 확인:
```
Hello, FS11!
```

## 다음 단계 (Next Steps)

1. Week 01 강의 자료 확인
2. 예제 코드 실행해보기
3. 첫 번째 과제 시작하기

## 도움말 (Help)

문제가 발생하면:
1. 에러 메시지를 자세히 읽기
2. Google 또는 Stack Overflow에서 검색
3. 강의 이슈 페이지에 질문 등록
