import pandas as pd
import requests
from tqdm import tqdm

# 🔑 INSERT your YouTube Data API v3 key here
API_KEY = "AIzaSyCf4Cweyt6jpfIaXa07A_gj5tApvvNu10k"

# 📁 Input CSV file name (from previous script)
INPUT_CSV = "yt_finance_data.csv"

# 📁 Output CSV file name
OUTPUT_CSV = "final_yt_data.csv"

# 🚀 Step 1: Load CSV
df = pd.read_csv(INPUT_CSV)

# 🛠 Optional Renaming (if your columns use alternate names)
df.rename(columns={
    "title": "video_title",
    "comments_count": "comments"
}, inplace=True)

# 🔍 Step 2: Get all unique channel IDs
unique_channel_ids = df["channel_id"].unique()

# 🧠 Step 3: Fetch channel names using YouTube Data API
channel_name_map = {}
for channel_id in tqdm(unique_channel_ids, desc="Fetching channel names"):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        items = data.get("items", [])
        if items:
            channel_name = items[0]["snippet"]["title"]
            channel_name_map[channel_id] = channel_name
        else:
            channel_name_map[channel_id] = "Unknown"
    except Exception as e:
        print(f"Error fetching channel name for {channel_id}: {e}")
        channel_name_map[channel_id] = "Error"

# 🧩 Step 4: Map channel names into the DataFrame
df["channel_name"] = df["channel_id"].map(channel_name_map)

# 📊 Step 5: Select and reorder final columns
final_columns = ["channel_name", "channel_id", "video_url", "video_title", "views", "likes", "comments"]
df = df[final_columns]

# 💾 Step 6: Save to CSV
df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
print(f"\n✅ Data saved successfully to: {OUTPUT_CSV}")
