참고한 리포지토리: https://github.com/theAIGuysCode/OIDv4_ToolKit

참고한 영상: https://www.youtube.com/watch?v=zJDUhGL26iU&t=200s

## SkypDGU에 있는 [RequiredColab](https://github.com/SkypDGU/RequiredColab)과  를 같은 폴더에 놓고 진행

**txt_90.py, txt_90_lr.py, txt_90_ud.py, txt_90_udlr.py:** 원본 Label폴더를 참고해 원본 이미지에 맞는 txt파일 생성(각 파이썬 파일마다 90도 회전 시킨 이미지의 txt파일, 90도 회전 좌우반전시킨 이미지의 txt파일, 90도 회전 상하반전 시킨 이미지의 txt파일,  90도 회전 상하좌우반전시킨 이미지의 txt파일을 생성하여 원본 Label폴더 안에 위치한 Label_90에 저장시킨다 )

**turn_image.py:** 원본 이미지 폴더에 있는 이미지들을 90도 회전, 90도 회전 좌우반전, 90도 회전 상하반전, 90도 회전 상하좌우반전 시켜  Person_90이라는 폴더에 저장.
