import urllib.request
import urllib.parse
import re
import json
import time

cafes = [
    "동탄 영천동 꾸덕 카페 리뷰", "역삼 베통 리뷰", "행궁동 츄플러스 리뷰",
    "수원 평지담 리뷰", "홍라드 수원역점 리뷰", "수원역 퀸트 리뷰",
    "망원 브릭베이글 리뷰", "압구정 마이페이보릿쿠키테리아 리뷰", "압구정 이웃집통통이 리뷰",
    "망원 해브어 리뷰"
]

results = {}

for c in cafes:
    print(f"Searching Naver for {c}...")
    try:
        q = urllib.parse.quote(c)
        req = urllib.request.Request(f"https://search.naver.com/search.naver?query={q}", headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        links = list(set(re.findall(r'href="(https://blog\.naver\.com/[^"]+)"', html)))
        clean_links = [l for l in links if "PostView.naver" in l or "PostList.naver" not in l]
        
        results[c] = clean_links[:3]
    except Exception as e:
        print(f"Error for {c}: {e}")
        results[c] = []
    time.sleep(1)

with open("naver_links_cafes_141_150.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved to naver_links_cafes_141_150.json")
