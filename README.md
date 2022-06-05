# mini2

AI SCHOOL 6기 미니 프로젝트2

- [주제](#주제)
- [분석 과정](#분석-과정)
- [느낀점](#느낀점)

## 주제

티어별로 챔피언에 대한 인식들을 픽률과 밴률로 분석하기

## 분석 과정

- [데이터 수집](#데이터-수집)
- [데이터 전처리](#데이터-전처리)
- [데이터 분석 및 시각화](#데이터-분석-및-시각화)

### 데이터 수집

```python
# 라이브러리
import json # json 파일로 저장하기 위해서 사용
import time # request할 때 너무 빠른 호출을 방지하기 위해 사용
from tqdm import tqdm # 진행 과정을 확인하기 위해서 사용
```

#### 데이터 가져오기

opgg 사이트에서 network 탭에서 찾았다.  
`https://www.op.gg/_next/data/{코드}/champions.json?region=kr`

또한, 필요할 때마다 요청하는 것보다 실시간 정보가 아니기 때문에 저장하는 게 낫겠다고 판단해서 json 파일로 필요한 것만 저장했다.

~~지금 생각해보니 tier_list에서 all 분석 안했는데 굳이 불러 올 필요가 있었나 싶네... 일단 다 불러 오고 나서 생각했던지라 나의 미스테이크...~~

### 데이터 전처리

```python
# 라이브러리
import pandas as pd
```

먼저 원하는 데이터프레임 형식을 생각하고 난 뒤 그 데이터프레임을 만들려면 어떤 딕셔너리 형태여야지 이쁘게 만들 수 있는지 생각했다.

- 데이터 프레임
  | tier | champion | position | win_rate | pick_rate | ban_rate |
  | ---- | -------- | -------- | -------- | --------- | -------- |
  | all | Akali | mid | 0.456 | 0.055 | 0.054 |

- 딕셔너리  
  `{ (Akali, mid) : [ win, pick, ban ], (Akali, top) : [ win, pick, ban ] } }`

또한, 데이터 특성을 보기 위해서 long-form 형식으로 바꾸기 위해 melt를 했다.

### 데이터 분석 및 시각화

```python
# 라이브러리
import matplotlib.pyplot as plt # 그래프 보여주기 전용
import seaborn as sns # 데이터 특성 확인용 시각화

import plotly.express as px # 메인 시각화
```

데이터 정보를 확인하기 위해 shape, head, isnull, info, describe를 이용했다. 그리고 데이터 특성을 파악하기 위해서 boxplot, violinplot으로 시각화해 어렴풋이 파악할 수 있었다.

대망의 마지막에는 그래프를 어떤 걸 쓸지 잘 떠오르지 않았다. 그래서 내가 알고 있는 지식에서는 다른 건 나타내기 어려울 것 같아 두 변수를 나타내는 scatter를 이용했다. 그리고 전체 포지션을 훑어보면서 전반적으로 파악했고 또한 세부적으로 분석해봤다.

밑의 내용은 전부 분석한 내용을 복붙했다.

- 전체  
  애니메이션 계속 돌려보다보면 어디 티어 부분에서 연속적으로 몇 개의 점은 느리게 움직이는 것이 보였다. 이를 통해 그 티어에서는 동일한 챔피언에 대한 생각이 비슷함을 알 수 있다.

  또한, 위치가 빠르게 바뀌는 점들을 통해 티어별로 챔피언에 대한 다른 생각들을 가지고 있다는 것을 알 수 있으며 대부분 0쪽에 가까이 분포해있지만 특정 몇 십개들의 점들은 그 밖에 튀어 있는 걸 보니 모든 챔피언을 고루 사용하지는 않는 것 같음을 알 수 있다.

- TOP  
  갱플랭크의 밴률이 압도적으로 높다. 일단 밴하자 느낌일 수도 있고 ㄹㅇ 사기일 수도 있다. 물론, 실버 이하로는 다리우스가 밴률과 픽률이 전반적으로 높은 편이다. 이를 보니 이 티어한테는 갱플랭크보다 다리우스가 전반적으로 무서운가 보다.

  그웬은 마스터부터 픽률이 꽤 높다. 그 이전 티어들은 상대적으로 선호하지 않는 걸 보니 뭔가… 고수들만 할 수 있는건가…? 물론, 아이언에서는 세트의 픽률이 꽤 높다. 조작 난이도가 쉬운 편인 것 같다. ~~아님말고~~

  실버에서는 픽률이 전반적으로 골고루 나왔다는 점이 신기했다.

- MID  
  제드는 플레티넘까지 밴률이 압도적으로 높다. 그러나 다이아부터는 르블랑, 탈리야가 치고 올라왔고 마스터부터는 제드 대신 카타리나가 치고 올라오기 시작해 르블랑, 탈리야, 카타리나가 밴률의 상위를 전반적으로 차지한다. 이를 통해 플레까지는 제드가 상대하기 까다롭다고 생각하고 그 이상부터는 제드 보다는 르블랑, 탈리야, 카타리나가 상대하기 까다롭다고 생각하는 것 같음을 알 수 있다. 물론, 그렇다고 플레까지 아예 르블랑, 탈리야가 밴률이 낮지 않은 걸 보니 미드는 까다롭다고 생각하는 챔피언이 다른 곳에 비해 상대적으로 많은 것 같았다.

  아리는 실버부터 픽률이 압도적으로 높다. (밴률도 거의 3~4위를 할 정도로 높다) 그러나 그 이하 티어들은 야스오가 픽률이 높았다. ~~야스오.. 원챔충…?~~ 그리고 그랜드 마스터부터는 조랑 탈리야가 뒤따라 높았다. 마스터 이하 에서는 빅토르가 치고 올라 왔고 다이아 이하에서는 아리 빼고 픽률이 비슷비슷 하다가 골드 이하부터 야스오와 요네가 같이 치고 올라왔다. 이를 통해서 아리는 전반적으로 다들 강하다고 생각하는 것 같음을 알 수 있었고 저티어에서는 아리보다 야스오와 요네를 좀 더 선호하는 걸 보니 간지 때문인지 조작 난이도 때문인지 알 수 없지만… 둘을 더 선호하는 것 같음을 알 수 있다. 또한, 아리는 인기가 엄청 많음을 알 수 있다. 밴률도 높은 것을 보니 강하다는 인식이 많은 것 같은데 ~~왜 패치 안해?~~

  고티어에서 밴률이 골고루 있는 걸 보니 미드는 강하다고 생각하는 챔피언이 많은 것 같아서 신기했다.

- SUPPORT  
  블리츠랭크와 노틸러스의 밴률이 다이아까지 전반적으로 높다. 그러나 블리츠랭크가 플레까지는 압도적이었으나 다이아 부터는 점점 밴률이 떨어졌다. 대신 노틸러스가 높았다. 또한 세나가 골드부터 천천히 밴률이 높아져 그랜드 마스터에는 노틸러스를 치고 올라가며 압도적으로 높았다. 그리고 실버 이하로는 럭스의 밴률이 상승하다가 아이언에 밴률 2위가 될 만큼 저티어에서는 럭스를 많이 밴했다.

  럭스는 브론즈까지 픽률이 압도적으로 높다. 그 이상 티어들은 몇 개의 챔피언들이 골고루 픽률이 높다가 다이아에서 노틸러스의 픽률이 점점 높아졌다. 그리고 전반적으로는 세나가 픽률이 높았다.

  유미가 플레부터는 픽률과 밴률이 비슷했다. 그 이하 티어에서는 오히려 픽률이 높았다. 전반적으로 픽률이 높은 편이었다.

- JUNGLE  
  탈리야는 다이아부터 밴률이 압도적으로 높다. 미드에서도 높게 나타난 걸 보니 어딜 가나 상대하기 까다로운가 보다. 그리고 그 이하로 실버까지는 그레이브즈가 압도적으로 높게 나타났지만 그 이하 티어에서는 마스터 이가 급속도로 치고 올라왔다.

  그 밑으로는 다이아부터는 탈론과 니달리가 자주 보였지만 골드부터는 니달리 대신 리신이 자주 보였다. 그리고 그 이하 티어에서는 탈론 대신 샤코가 급속도로 높아졌다. 또한, 골드부터 다이아까지는 오공도 꽤 높게 보였다.

  → 이를 통해 다이아 이상에서는 탈리야, 탈론, 니달리, 그레이브즈가 상대하기 까다롭다고 생각하는 걸 알 수 있었고 실버까지는 탈리야, 니달리보다는 리신과 샤코를 상대하기 까다롭다고 생각하는 것 같음을 알 수 있었다.

  마스터부터는 비에고가 픽률이 제일 높다. 그러나 실버부터 다이아까지는 그레이브즈가 제일 높다. 그리고 아이언부터 브론즈까지는 마스터 이가 제일 높다.

  마스터부터는 그레이브즈, 오공이 함께 픽률이 높았지만 다이아에서 전반적으로 픽률이 줄어들면서 격차가 좁아졌다. 그래서 골드에서 플레까지는 비에고 대신 리신이 높지만 오히려 실버에서 오공 대신 비에고의 픽률이 높아지는 현상이 있다. 그리고 아이언에서는 리신보다 케인의 픽률이 높았다.

  → 이를 통해 마스터 이상에서는 비에고를 제일 선호한다는 것을 알 수 있었고 브론즈 이하에서는 마스터 이를 제일 선호한다는 것도 알 수 있었다. 또한 플레 이하에서는 리신이 잘 먹히는 듯 전반적으로 리신에 대한 선호가 높다는 것을 알 수 있었다.

- ADC  
  루시안과 칼리스타가 압도적으로 그랜드 마스터부터 밴률 이 높다. 마스터에서 칼리스타 대신 사미라가 치고 올라왔다. 브론즈에서 사미라가 루시안을 치고 올라와서 압도적으로 높았다.

  모든 티어에서 이즈리얼이 픽률이 압도적으로 높았다. 그랜드 마스터 이전에는 카이사가 픽률이 높았다가 아이언에서는 카이사 대신 미스포츈이 높아졌다. 물론 전반적으로 루시안은 픽률도 높았다.

  → 원딜이 챔피언 수가 적어서 그런지 사람들이 생각하는 게 전반적으로 비슷했다.

### 느낀점

- 어려웠던 점:
  어떤 그래프를 쓸지 정하는 게 어려웠다. 그 전에 주제를 선정하는데도 어려워서 일단 구현했지만 그래서 내가 뭘 분석하고 싶은지를 모르니 복잡해졌었다. 그래서 다시 처음으로 돌아가자고 생각해서 다 놓고 구상부터 다시했다. 분석하고 싶은 목적만 분명히 하고 그 다음은 나중에 생각하자고 생각해서 틈틈히 고민했다. 산책하면서 고민하다가 아이디어가 생각나면 노션에 적었다. 그러다가 분석 목표가 겨우 정해졌지만 문제는 어떤 그래프로 할지가 고민이었다. 픽률과 밴률로 인식을 분석한다. 이 얼마나 추상적인가... 그런것도 있지만 분석을 어떻게 하는지 몰라서 그런것도 있고... 아무튼 그래서 plotly의 갤러리를 계속해서 뒤지면서 어떻게 결과가 나올지 고민하면서 어떤 걸 쓸지 고민했다. 그러다가 제일 분석하기 편해보이는 걸로 골랐다.
- 배운 내용과 의견:
  좀 결과물이 맘에 안들긴한다... 시각화 했지만 결과적으로 한 눈에 보기 어려운 시각화인데 이게 맞나? 싶기도 하고...ㅠㅠ 그래서 분석하는데도 이것 저것 고려하다보니 대가리 깨질 뻔했다... 이게 맞나? 만 계속 생각이 드는 이번 결과물이었다.. 잘 모르는 통계만 주구장창 팠더니 정작 아는 건 있는데 적용하는 법을 몰라서 이번엔 분석에 초점을 맞춰서 다시 공부해봐야겠다. 이거보다 더 좋은 방안도 있을 것 같은데... 그래도 강사님들한테 배운거 최대한 써먹으려고 고민을 많이 했다. melt 배운거 하나 써서 뿌듯하다^\_^ 전 프로젝트에서는 구현에 초점을 맞췄다면 이번에는 분석에 초점을 맞추려고 많이 노력했다. 아직 부족한 게 많다고 생각해서... 잘하는 사람들껄 좀 많이 봐야겠다. 힝... 사실 내가 잘 하고 있는건지 모르겠다...
