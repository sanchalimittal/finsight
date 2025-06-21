import scrapetube

channel_ids = [
    "UCe3qdG0A_gr-sEdat5y2twQ",
    "UCwAdQUuPT6laN-AQR17fe1g",
    "UCRzYN32xtBf3Yxsx5BvJWJw",
    "UCwVEhEzsjLym_u1he4XWFkg",
    "UCsNxHPbaCWL1tKw2hxGQD6g",
    "UCEAAzv2OBqxsSczKJ2QZyGQ",
    "UCUgUjyt6jcyxfM4FCmxZcgw",
    "UCVOTBwF0vnSxMRIbfSE_K_g",
    "UCWHCXSKASuSzao_pplQ7SPw",
    "UCPohbSYq4IXhv0yxiy-sT4g",
    "UCMSI1Ck1mJOaxxwJ0bzrYhQ",
    "UCt22CG7b9crZ0HDk1eTiJjA",
    "UCKxWWqBQZYKTA01GkyQdMHA",
    "UC2sIhf108S02F0Qlb2a88eQ",
    "UC6ZkHcW5QQubZ-Q6XYINE3Q",
    "UC_s0g4QdprLkyyN2MDpef7Q",
    "UCthN3CTgZY0WIE9A5u1Qcew",
    "UCqvVj1LkOpA8tjb7RadTvOg",
    "UCw4496t84F_8HvhQPwtmWpQ",
    "UCJLuHmLtOWbB5zurCbmuPDg",
    "UCqW8jxh4tH1Z1sWPbkGWL4g",
    "UCzwCEE_PchiBULMnAJqhGVg",
    "UCzw35O6toJtjqEAAt4LTjKQ",
    "UCw5TLrz3qADabwezTEcOmgQ",
    "UCnSHHfS-nwoZXQkU6xi4L9Q",
    "UCRE9Fp_3g_ekRTLtJM4yBFA",
    "UCCLu5B_Ctsw4N20DJvDykOA",
    "UCfV3cQ6RSM63Yeq5ihOaVlw",
    "UCyHltK3BM77CwZNIpQGv8Tg",
    "UCkJpKzqc2w28Pz7P4_9N6sQ",
    "UCIN47KTcW1V34D4IXA0nSow",
    "UCbK2iqXN8T_UCnN-NQJgm7w",
    "UC94R1OaAaCXM9Gy_LiMS3Tw",
    "UCbUQGFp3PUf3FYZr9UylmGA",
    "UC8d3CoQ_wweVtxoGxCPJchQ",
    "UCbm3JK-6QHGLr7Mdz6dAakQ",
    "UCfV3cQ6RSM63Yeq5ihOaVlw",
    "UCyHltK3BM77CwZNIpQGv8Tg",
    "UCkJpKzqc2w28Pz7P4_9N6sQ",
    "UCIN47KTcW1V34D4IXA0nSow",
    "UCbK2iqXN8T_UCnN-NQJgm7w",
    "UC94R1OaAaCXM9Gy_LiMS3Tw",
    "UCbUQGFp3PUf3FYZr9UylmGA",
    "UC8d3CoQ_wweVtxoGxCPJchQ",
    "UCbm3JK-6QHGLr7Mdz6dAakQ"
]

video_urls = [
  {"channel_id": ch, "video_url": f"https://www.youtube.com/watch?v={v['videoId']}"}
  for ch in channel_ids
  for v in scrapetube.get_channel(ch)[:20]  # latest 20 videos per channel
]

print(f"✅ Collected {len(video_urls)} URLs")
for sample in video_urls[:5]:
  print(sample)