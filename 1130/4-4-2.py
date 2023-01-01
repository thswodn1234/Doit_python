# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:43:23 2022

@author: user
"""
import usecsv, re

E = """England head coach Gareth Southgate was keen to focus on his side’s “resilience” and retaining control of their World Cup destiny after a drab 0-0 draw with the United States.
The highs of an opening 6-2 thrashing of Iran were quickly forgotten as Southgate’s side laboured to a performance labelled “terrible” by former Manchester United midfielder Roy Keane.

“I knew it would be difficult for us after such a high (against Iran) to replicate that type of performance, so I’m really pleased with how the players have applied themselves,” Southgate told ITV.

“Some of our quality in the final third could have been a little bit better, but we’ve shown great resilience to defend against an opponent that kept asking questions and we’ve just not been able to open them up with that really clear-cut chance.
"""

K = """잉글랜드의 가레스 사우스게이트 감독은 미국과의 단조로운 0-0 무승부 이후 그의 팀의 "회복력"과 월드컵 운명의 통제권을 유지하는 데 집중하고 싶어했습니다.
이란을 6-2로 대파한 첫 경기의 최고점은 사우스게이트 측이 전 맨체스터 유나이티드 미드필더 로이 킨이 "끔찍하다"고 표현한 경기에 힘을 쏟으면서 빠르게 잊혀졌다.

사우스게이트는 ITV와의 인터뷰에서 "(이란을 상대로) 그런 높은 경기를 치른 후 우리가 그런 유형의 경기를 재현하기 어려울 것이라는 것을 알고 있었기 때문에 선수들이 어떻게 적응했는지 정말 기쁩니다."라고 말했습니다.

“파이널 써드에서 우리의 품질 중 일부는 조금 더 나을 수 있었지만 계속 질문을 던지는 상대를 방어하는 데 큰 탄력성을 보여줬고 정말 명확하게 열지 못했습니다. 컷 기회.

"""

E = re.sub(r"[\n]","",E)
K = re.sub(r"[\n]","",K)

Elist = re.split(r'\.', E)

Klist = re.split(r'\.', K)

total = []

for i in range(len(Elist)):
    total.append([Elist[i], Klist[i]])
    
usecsv.writecsv("EK.csv", total)