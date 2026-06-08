import urllib.request
import urllib.parse
import re
import json
import time

cafes = [
    "성남 카페정순 리뷰", "동탄 프랭크커핀바 리뷰", "연남 조앤도슨 리뷰",
    "행궁동 버터맨션 리뷰", "동탄 리프 카페 리뷰", "동탄 뵈르 베이커리 리뷰",
    "송파 레밍스 카페 리뷰", "오산 그레이스그래니 리뷰", "동탄 유일무이 카페 리뷰",
    "수원 권선 리프커피 리뷰"
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

with open("naver_links_cafes_121_130.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved to naver_links_cafes_121_130.json")
