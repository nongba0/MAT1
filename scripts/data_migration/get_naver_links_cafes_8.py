import urllib.request
import urllib.parse
import re
import json
import time

cafes = [
    "화성 씨포케익 리뷰", "성남 태평동커피집 리뷰", "오산 초이베이크샵 리뷰",
    "안국 러프러프 아뜰리에 리뷰", "안국 도토리가든 리뷰", "안국 어니언 리뷰",
    "대전 정동문화사 리뷰", "대전 땡큐베리머치 리뷰", "동탄 더힐846 카페 리뷰",
    "성남 어서오슈 카페 리뷰", "강남 마르케 카페 리뷰"
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

with open("naver_links_cafes_101_111.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved to naver_links_cafes_101_111.json")
