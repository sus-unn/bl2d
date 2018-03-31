#sus_bl2d
#3d 프로그램인 blender에서 2d 애니메이션을 만드는 유틸리티입니다.
#일본식 애니메이션 제작 시스템에 맞추려고 합니다.

#현재는 bl2d.py등의 스크립트 파일에 ASCII코드가 아닌 문자(한국어, 일본어, 한자 등)을 넣는 것은 금지입니다.
#template.blend의 오브젝트들의 이름들을 바꾸면 안됩니다. 심각한 오류를 발생시킬 수 있습니다.

#이 유틸리티의 기능들과 애드온의 기능은 아직 미완성입니다.
#================================================================================================

정보:
	
	Blender에서 2d 애니메이션 그리기
	
	버젼: 0.01 알파
	
	제작자: 수선
	
	연락처: typ3ys.xz@gmail.com, https://twitter.com/SusunnK  (DM 가능)
	
	저장소: https://github.com/sus-unn/bl2d
	
	
#미러: 없음

	
	
템플릿 파일 출력:

#프리뷰(기본)

	프레임 크기 = 1280 * 720
	
#종이 (인쇄용) (기본)

	DPI = 128
	
	사이즈 = A4
	

요구사항:

    User Preferences에서 애드온을 zip파일 형식으로 추가해야 합니다.(Install Add-On from file)
    
    'International fonts'를 활성화하세요.
	2.79버젼 이상의 블렌더가 설치되어야 합니다.
    
권장사항: 

    BLAM (https://github.com/stuffmatic/blam)
    
    Layer Management (is in blender by default, yet disabled)
	
	개발자라면:
		Git
		Python

	
#사용법:

	(0. 아직 알파 버젼으로 개발중이고 애드온 파일은 미완성입니다.. User preference에서 애드온을 추가하는것은 아직은 무의미합니다.)
	
	1. 블렌더 2.79나 그 이상의 버젼을 설치해주십시요. 이전의 버젼에서는 작동하지 않을수도 있습니다.
	
	2. https://github.com/sus-unn/bl2d에서 zip형태로 다운받거나 , 터미널에서 git을 이용할수도 있습니다. ( "git clone https://github.com/sus-unn/bl2d.git")
	
	3. '.zip'파일을 지우지 마십시요.. 만약에 git 클라이언트를 통해 다운을 받았다면, zip파일로 전체의 사본을 만들어주세요. (.gti폴더는 제외하는게 좋습니다.)
	
	4. User preference 메뉴에서 'Install Add-On from File'을 눌러 zip파일을 추가해주세요.
	
	5. 만약 직접 다운을 받았다면, zip압축을 해제하고 template.blend를 열어주세요.
	
	6. 템플릿 파일을 원하는 경로와 이름으로 'Save As'(다른 이름으로 저장하기)해주거나 복사해주세요. 템플릿파일을 수정하는것은 권장되지 않습니다.
	
	
#미완성
	
	1. 용지 출력 스크립트를 사용할 때에는 3d View 패널이 'Camera View'로 되있어야 합니다.
	
	2. 타임 시트 자동완성 기능은 미완성입니다.
	
	3. 레이아웃 용지의 자동화기능은 미완성입니다.
	
	4. 타임시트를 자동화할때 동화표시를 어떻게 할지는 미정입니다. 
	
	5. 애드온파일은 현재 실질적으로 기능이 없습니다.
	
	6. Preset_Lib은 준비되지 않았습니다.
	
	



Tips:

	숫자 패드에서 0키를 누르면 현재 활성화된 카메라 시점으로 이동합니다.
	숫자 패드에서 0을 다시 누르면 이전의 시점으로 돌아갑니다.
	Ctrl +  숫자패드 0을 누르면 현재 선택한 카메라가 활성화됩니다. (렌더링할때 이 카메라로 보게 됩니다.)
	가운데 마우스 휠로 줌 인/아웃할수 있습니다.
	가운데 마우스 휠을 누르고 마우스를 움직이면 3차원 회전을 할 수 있습니다.
	쉬프트키 + 가운데 마우스 휠을 누르면 카메라를 PAN할수 있습니다.
	쉬프트키 + 숫자패드 4키를 누르면 왼쪽으로 2차원 회전을 합니다.
	쉬프트키 + 숫자패트 6키를 누르면 오른쪽으로 2차원 회전을 합니다.
	컨트롤키 + 쉬프트키 + 가운데 마우스 휠을 누르면 시점이 카메라방향으로 움직입니다. (트랙백/업이라 생각하면 됩니다.)
	T를 누를 때마다 왼쪽의 툴바가 열리고/닫힙니다.
	N을 누를 때마다 오른쪽의 속성 패널이 열리고/닫힙니다.
	
	D를 누르면 Grease Pencil을 그릴 수 있습니다.
	D를 누르고 오른쪽 마우스버튼을 누르면 Grease Pencil 지우개를 쓸 수 있습니다.
	
	Alt+A를 누르면 애니메이션을 재생할 수 있습니다.
	
	왼쪽/오른쪽 화살표 키로 1프레임씩 이동할 수 있습니다.
	위/아래 화살표 키로 키프레임 단위로 이동할 수 있습니다.
	
	촬영프레임으로 프리뷰 하려면, OpenGL Render Animation을 하면 됩니다.
	템플릿파일에 내장된 'key_export.py'를 누르면 용지를 이미지로 출력할수 있습니다.
	
	
	'Camera_2dPanTBTU' 를 X축과 Z축으로 이동하면 카메라를 PAN시킬수 있습니다.
	'Camera_2dPanTBTU' 를 Y축으로 움직이면 카메라를 트랙백/업 시킬수 있습니다.
	주 카메라는 항상 'Camera_3DAimTarget'를 바라봅니다.
	
	
	"Main"씬은 주 작업 공간입니다.
	"TimeSheet"씬은 타임시트 작업 공간입니다.
	"Preset_Lib"은 미리 정의된 오브젝트들을 포함하고 있습니다. (follow, 中割り 지시자 같은)
	
	일부 오브젝트들은 프리뷰나 용지인쇄를 할때 불편하므로 기본적으로 선택이 불가하거나 숨겨져 있습니다.
	
For Developers:

#Please contribute

	1. install git
	2. in terminal(Windows: Powershell or cmd), type: "git clone https://github.com/sus-unn/bl2d"
	3. if you don't know anything about git, please google 'git' and learn about it.