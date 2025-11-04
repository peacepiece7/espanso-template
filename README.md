# Espanso Template

```zsh
espanso start
espanso restart
espanso log
espanso path
```

## espanso 설치 및 실행

[Install Espanso](https://espanso.org/install/)

```zsh
# for mac
brew install espanso
brew install python

# for windows
choco install espanso
choco install python
```

[delays-characters package 설치](https://hub.espanso.org/delays-characters)

```zsh
espanso install delays-characters
python -m pip install pynput
```

## windows permission

```powershell
takeown /f C:\tools\espanso /r /d y
icacls C:\tools\espanso /setowner <USER_NAME> /T
```

## global vars

```yaml
global_vars:
  - name: PAKCAGE_REPOSITORY_PATH
    type: echo
    params:
      echo: 'C:/Users/<USER_NAME>/repo/espanso-template'
```
