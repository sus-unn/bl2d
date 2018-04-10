BL2D 메뉴얼
=========

설치(일반)
-------

1. [공식 깃허브 저장소](https://github.com/sus-unn/bl2d)에서 'Clone or Download'를 누르고 Download As Zip으로 zip 파일로 다운받습니다.

2. Blender에서 다운받은 '.zip'파일을 애드온에 추가합니다.

3. zip파일에서 template.blend파일의 압축을 해제합니다. (이하 템플릿)

4. 템플릿을 원하는 작업경로에 원하는 이름으로 복사합니다.

5. 템플릿 내에서 레이아웃, 원화를 그릴 수 있습니다.

설치(개발자)
---------

1. 무엇보다도, git 클라이언트 프로그램이 설치되어 있어야 합니다.

(Git에 대헤서 들어보신적이 없다면, 숙지하고 오십시요.)

2. 작업경로의 터미널에서 다음과 같이 입력합니다:
```bash
git clone --mirror https://github.com/sus-unn/bl2d.git bl2d/.git
cd bl2d
git config --unset core.bare
git config receive.denyCurrentBranch updateInstead
git checkout master
```
(이렇게 함으로서, bl2d의 모든 branch를 복사하게 됩니다.)

3. ".git"폴더까지 포함하여, 저장소 폴더를 통째로 zip파일로 압축합니다.

4. Blender에서 압축한 .zip파일을 애드온에 추가합니다.

5. Blender의 사용자 추가 애드온이 설치되는 경로에서 bl2d 폴더를 찾아갑니다. Git 로컬 저장소 자체가 통째로 복사되어 있습니다!!

(윈도우의 경우 사용자 추가 애드온은 %APPDATA%\Blender Foundation\Blender\(Belnder 버젼)\scripts\addons\ 에 주로 있습니다.)

6. 애드온 설치 경로에서 원하는 데로 git을 이용한 개발작업을 할 수 있습니다.

(7. 수정후 템플릿 파일에서 F8을 누르면 수정된 애드온을 Blender가 다시 로드해옵니다)

주의사항
------

Template내에 기본적으로 있는 오브젝트들은 절대 삭제, 이름변경을 해서는 안됩니다.
애드온이 정상적으로 작동하지 않을 수도 있습니다.

Scene 구성
--------

BL2D의 템플릿은 Scene으로 작화, 타임시트, '미리 정의된 오브젝트'의 작업공간을 나누고 있습니다.

'Main': 주 작업공간입니다. 이 공간에서 작화를 합니다.

'TimeSheet': 타임시트가 이곳에 생성됩니다.

'Preset_Lib' : 미리 정의된 오브젝트들  - 지시자 등이 이곳에 보관됩니다.

오브젝트 구성
---------

템플릿 내의 각각의 씬에는 기본적으로 여러 오브젝트들이 있습니다.

모든 오브젝트들은 각자 역할이 있고, 애드온은 이 오브젝트들에 의존적이기에 이름을 바꾸거나 삭제해서는 안됩니다. 

어떤 오브젝트들은 사용자에게 방해되거나, 잘못 선택되는 상황을 피하기 위해 선택이 불가하거나 숨겨져 있습니다.

카메라
-----

'Main' 씬에는 세 개의 카메라가 있습니다. 'Camera_Main', 'Camera_Scan_Frame', 'Camera_WholeSheet' 가 그것입니다.

'Camera_Mai'n은 기본적인 촬영 카메라입니다. 이 카메라의 경계선은 촤종 화면의 경계선이고, 촬영프레임과 같습니다.

'Camera_Scan_Frame'은 스캔프레임에 대응하는 카메라입니다. 

현재는 딱히 필요없어 보이지만, 블렌더내에서 동화를 만들고 그것을 출력해 타 프로그램에서 채색을 하는 상황이 생길수도 있어 대응하기 위해 만들었습니다.

'Camera_WholeSheet'는 전체 용지를 촬영하는 카메라입니다. 원화출력을 할 때에 사용됩니다.

세 카메라는 모두 숨겨져 있고, 기본적으로 선택이 불가능합니다. 

대신, 'Camera_Main'과 'Camera_Scan_Frame'은 'Camera_2dPanTBTU'를 Parent로 하고 있어, 'Camera_2dPanTBTU'를 움직이면 같이 움직입니다.

'Camera_2dPanTBTU'를 이용해 X, Y 방향으로 PAN을 해거나 Z방향으로 TU, TB이 가능합니다.

'Camera_WholeShee'는 용지 오브젝트 'Sheet'를 Parent 오브젝트로 삼고 있고, 용지 크기가 바뀌거나 위치가 바뀔 때마다 자동으로 대응합니다.

또한, 세 카메라는 기본적으로 Orthographic 카메라인데, 이는 세 카메라 모두 투시/원근을 무시한다는 뜻입니다. 이는 정확성을 위해서 그런 것이고, 목적에 따라 Perspective 뷰로 바꿀 수 있습니다.

그러나, 'Camera_WholeSheet'는 용지만을 촬영하기 위함이기에 Perspective뷰로 바꾸는 것이 권장되지 않습니다.

UI
--

애드온을 설치하면 'BL2D'라는 탭이 좌측 툴바에 생깁니다.

이 탭에는 'Info' ,'Output', 'Cel', 'Indicators', 'Book'라는 패널이 있습니다.

현재는 'Info', 'Output' 패널만이 기능이 있습니다.

'Info' 패널에는 BL2D에 대한 정보가 있습니다.

'Output' 패널에는 'Export Keyframes', 'Export full sheet preview'라는 두 버튼이 있습니다.

'Export Keyframes'를 누르면 현재 컷의 원화를 모두 출력합니다.

'Export full sheet preview'를 클릭하면 현재 컷의 전체 용지 프리뷰를 출력합니다.