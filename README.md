# HOW TO INSTALL AND USE ESPANSO

그대로 Clone 해서 쓰더라도 espanso, python 설치 필요

## ESPANSO 설치

[Install Espanso](https://espanso.org/install/)

or

```zsh
# for mac
brew install espanso

# for windows
choco install espanso
```

## Python 설치

[Install Python](https://www.python.org/downloads/)

or

```zsh
# for mac
brew install python

# for windows
choco install python
```

## 에러 발생시

espanso 시작 및 디버깅

```zsh
espanso start
```

히스토리(로그) 출력

```zsh
espanso log
```

### 1. 패키지 설치

만약에 keypress 이벤트가 안먹으면 다시 설치 해보자

[delays-characters package 설치](https://hub.espanso.org/delays-characters)

```zsh
espanso install delays-characters
```

## pynput 설치

```zsh
python -m pip install pynput
```

## 윈도우 권한 문제

파워쉘 관라자 권한으로 espanso 받으면 사용자 권한 부여 해줘야함

```powershell
takeown /f C:\tools\espanso /r /d y
icacls C:\tools\espanso /setowner <USER_NAME> /T
```

## global_vars

global_vars는 OS에 맞게 설정

```yaml
global_vars:
  - name: PAKCAGE_REPOSITORY_PATH
    type: echo
    params:
      echo: 'C:/Users/<USER_NAME>/repo/espanso-template'
```
