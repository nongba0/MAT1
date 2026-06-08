import urllib.request
import urllib.parse
import re
import json
import time

cafes = [
    "야탑 카페 웨더베인 리뷰", "성남 세가지 카페 리뷰", "송파 슈퍼플 아사이볼 리뷰",
    "양재천 행운간 카페 리뷰", "동탄 화이트스노우 리뷰", "동탄 포이파이 리뷰",
    "성남 과일블럭 리뷰", "이태원 아벡쉐리 리뷰", "송파 밀빛 카페 리뷰",
    "모란 소질 커피 리뷰"
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

with open("naver_links_cafes_91_100.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved to naver_links_cafes_91_100.json")
