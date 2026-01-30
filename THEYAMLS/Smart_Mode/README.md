# 📂 Smart 模式 / 路由专用 (Smart Mode)

[🔙 返回主页](../../README.md)

> 📊 共收录 **10** 个配置文件

## ⚔️ 参数横向对比

| 配置文件 | 混合端口 | 面板端口 | 模式 | TUN | 策略组 | 规则数 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [`OneSmart_Lite_Config.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Smart_Mode/666OS/OneSmart_Lite_Config.yaml) | 7893 | 127.0.0.1:9090 | rule | 🚫 | **16** | 21 |
| [`OneSmart_Config.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Smart_Mode/666OS/OneSmart_Config.yaml) | 7893 | 127.0.0.1:9090 | rule | 🚫 | **31** | 36 |
| [`clash-fallback-smart-std.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Smart_Mode/liandu2024/clash-fallback-smart-std.yaml) | 7893 | 0.0.0.0:9090 | rule | ✅ | **36** | 42 |
| [`clash-all-smart.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Smart_Mode/liandu2024/clash-all-smart.yaml) | 7893 | 0.0.0.0:9090 | rule | ✅ | **38** | 43 |
| [`clash-all-fallback-smart.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Smart_Mode/liandu2024/clash-all-fallback-smart.yaml) | 7893 | 0.0.0.0:9090 | rule | ✅ | **57** | 48 |
| [`MihomoSmartProMax.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Smart_Mode/HenryChiao/MihomoSmartProMax.yaml) | 7893 | 127.0.0.1:9090 | rule | 🚫 | **41** | 45 |
| [`MihomoSmartProPlus.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Smart_Mode/HenryChiao/MihomoSmartProPlus.yaml) | 7893 | 127.0.0.1:9090 | rule | 🚫 | **41** | 44 |
| [`MihomoSmartAIO.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Smart_Mode/HenryChiao/MihomoSmartAIO.yaml) | 7893 | 127.0.0.1:9090 | rule | 🚫 | **69** | 52 |
| [`mihomo_smart.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Smart_Mode/echs-top/mihomo_smart.yaml) | 0 | 127.0.0.1:9090 | rule | ✅ | **31** | 34 |
| [`smart.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Smart_Mode/qichiyuhub/smart.yaml) | 7890 | - | rule | ✅ | **28** | 23 |

## 📝 详细结构分析
### 👤 666OS
#### 📄 OneSmart_Config.yaml
- **文件路径**: `666OS/OneSmart_Config.yaml` (20.1 KB)
<details>
<summary>🔍 点击查看 31 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| 一键智能 | `select` |
| 网络测试 | `select` |
| 人工智能 | `select` |
| 电报消息 | `select` |
| 社交平台 | `select` |
| 游戏平台 | `select` |
| 货币平台 | `select` |
| Emby服 | `select` |
| 国际媒体 | `select` |
| 新闻媒体 | `select` |
| 苹果服务 | `select` |
| 谷歌服务 | `select` |
| 微软服务 | `select` |
| 脸书服务 | `select` |
| 国外流量 | `select` |
| 国内流量 | `select` |
| 兜底流量 | `select` |
| 手动选择 | `select` |
| 直接连接 | `select` |
| 高质量线路 | `fallback` |
| ... | (剩余 11 个隐藏) |

</details>

---
#### 📄 OneSmart_Lite_Config.yaml
- **文件路径**: `666OS/OneSmart_Lite_Config.yaml` (12.5 KB)
<details>
<summary>🔍 点击查看 16 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| 一键智能 | `select` |
| 人工智能 | `select` |
| 社交平台 | `select` |
| 国际媒体 | `select` |
| 国外流量 | `select` |
| 国内流量 | `select` |
| 兜底流量 | `select` |
| 手动选择 | `select` |
| 直接连接 | `select` |
| 香港智能 | `smart` |
| 台湾智能 | `smart` |
| 日本智能 | `smart` |
| 狮城智能 | `smart` |
| 韩国智能 | `smart` |
| 美国智能 | `smart` |
| 欧洲智能 | `smart` |

</details>

---
### 👤 HenryChiao
#### 📄 MihomoSmartAIO.yaml
- **文件路径**: `HenryChiao/MihomoSmartAIO.yaml` (32.1 KB)
<details>
<summary>🔍 点击查看 69 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| 默认代理 | `select` |
| 故障转移 | `fallback` |
| 国外流量 | `select` |
| 国内流量 | `select` |
| 兜底流量 | `select` |
| 直接连接 | `select` |
| 网络测试 | `select` |
| UKwifi | `select` |
| 抖快书定位 | `select` |
| Emby服 | `select` |
| 油管视频 | `select` |
| 奈飞视频 | `select` |
| 迪士尼+ | `select` |
| Max | `select` |
| Prime Video | `select` |
| Apple TV+ | `select` |
| TikTok | `select` |
| 哔哩哔哩 | `select` |
| Spotify | `select` |
| 国外媒体 | `select` |
| ... | (剩余 49 个隐藏) |

</details>

---
#### 📄 MihomoSmartProMax.yaml
- **文件路径**: `HenryChiao/MihomoSmartProMax.yaml` (25.1 KB)
<details>
<summary>🔍 点击查看 41 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| 默认代理 | `select` |
| 故障转移 | `fallback` |
| 国外流量 | `select` |
| 国内流量 | `select` |
| 兜底流量 | `select` |
| 直接连接 | `select` |
| 网络测试 | `select` |
| UKwifi | `select` |
| 抖快书定位 | `select` |
| Emby服 | `select` |
| 油管视频 | `select` |
| 奈飞视频 | `select` |
| 国际媒体 | `select` |
| 新闻媒体 | `select` |
| 电报消息 | `select` |
| 推特社交 | `select` |
| 社交平台 | `select` |
| 人工智能 | `select` |
| 货币平台 | `select` |
| 游戏平台 | `select` |
| ... | (剩余 21 个隐藏) |

</details>

---
#### 📄 MihomoSmartProPlus.yaml
- **文件路径**: `HenryChiao/MihomoSmartProPlus.yaml` (25.7 KB)
<details>
<summary>🔍 点击查看 41 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| 默认代理 | `select` |
| 故障转移 | `fallback` |
| 国外流量 | `select` |
| 国内流量 | `select` |
| 兜底流量 | `select` |
| 直接连接 | `select` |
| 网络测试 | `select` |
| UKwifi | `select` |
| 抖快书定位 | `select` |
| Emby服 | `select` |
| 油管视频 | `select` |
| 奈飞视频 | `select` |
| 国际媒体 | `select` |
| 新闻媒体 | `select` |
| 电报消息 | `select` |
| 推特社交 | `select` |
| 社交平台 | `select` |
| 人工智能 | `select` |
| 货币平台 | `select` |
| 游戏平台 | `select` |
| ... | (剩余 21 个隐藏) |

</details>

---
### 👤 echs-top
#### 📄 mihomo_smart.yaml
- **文件路径**: `echs-top/mihomo_smart.yaml` (18.2 KB)
<details>
<summary>🔍 点击查看 31 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| PROXY | `select` |
| PROXYDNS | `select` |
| AD | `select` |
| SPEEDTEST | `select` |
| FCM | `select` |
| BOTTEST | `select` |
| TELEGRAM | `select` |
| META | `select` |
| TWITTER | `select` |
| TIKTOK | `select` |
| NETFLIX | `select` |
| SPOTIFY | `select` |
| BILIBILI | `select` |
| YOUTUBE | `select` |
| AI | `select` |
| PIXIV | `select` |
| GITHUB | `select` |
| ONEDRIVE-DL | `select` |
| STEAM-CN | `select` |
| GOOGLE | `select` |
| ... | (剩余 11 个隐藏) |

</details>

---
### 👤 liandu2024
#### 📄 clash-all-fallback-smart.yaml
- **文件路径**: `liandu2024/clash-all-fallback-smart.yaml` (18.2 KB)
<details>
<summary>🔍 点击查看 57 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| ChatGPT | `select` |
| Gemini | `select` |
| Copilot | `select` |
| Perplexity | `select` |
| Claude | `select` |
| Meta AI | `select` |
| GitHub | `select` |
| Reddit | `select` |
| Telegram | `select` |
| WhatsApp | `select` |
| Facebook | `select` |
| YouTube | `select` |
| TikTok | `select` |
| Netflix | `select` |
| HBO | `select` |
| Disney | `select` |
| Amazon | `select` |
| Crunchyroll | `select` |
| Spotify | `select` |
| Nvidia | `select` |
| ... | (剩余 37 个隐藏) |

</details>

---
#### 📄 clash-all-smart.yaml
- **文件路径**: `liandu2024/clash-all-smart.yaml` (15.1 KB)
<details>
<summary>🔍 点击查看 38 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| ChatGPT | `select` |
| Claude | `select` |
| Meta AI | `select` |
| Perplexity | `select` |
| GitHub | `select` |
| Telegram | `select` |
| Twitter(X) | `select` |
| WhatsApp | `select` |
| Facebook | `select` |
| YouTube | `select` |
| TikTok | `select` |
| Disney | `select` |
| Netflix | `select` |
| HBO | `select` |
| Spotify | `select` |
| Amazon | `select` |
| Apple | `select` |
| Microsoft | `select` |
| Google | `select` |
| Nvidia | `select` |
| ... | (剩余 18 个隐藏) |

</details>

---
#### 📄 clash-fallback-smart-std.yaml
- **文件路径**: `liandu2024/clash-fallback-smart-std.yaml` (17.7 KB)
<details>
<summary>🔍 点击查看 36 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| AI | `select` |
| Meta AI | `select` |
| Perplexity | `select` |
| Stream Media | `select` |
| GitHub | `select` |
| Reddit | `select` |
| Nvidia | `select` |
| Apple | `select` |
| Microsoft | `select` |
| Games | `select` |
| Crypto | `select` |
| Test | `select` |
| Block | `select` |
| 国外 | `select` |
| 国内 | `select` |
| 其他 | `select` |
| 所有-手选 | `select` |
| 所有-智选 | `smart` |
| 香港-故转 | `fallback` |
| 香港-手选 | `select` |
| ... | (剩余 16 个隐藏) |

</details>

---
### 👤 qichiyuhub
#### 📄 smart.yaml
- **文件路径**: `qichiyuhub/smart.yaml` (13.0 KB)
<details>
<summary>🔍 点击查看 28 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| 🚀 默认代理 | `select` |
| 📹 YouTube | `select` |
| 🍀 Google | `select` |
| 🤖 ChatGPT | `select` |
| 👨🏿‍💻 GitHub | `select` |
| 🐬 OneDrive | `select` |
| 🪟 Microsoft | `select` |
| 🎵 TikTok | `select` |
| 📲 Telegram | `select` |
| 🎥 NETFLIX | `select` |
| ✈️ Speedtest | `select` |
| 💶 PayPal | `select` |
| 🍎 Apple | `select` |
| 🐟 漏网之鱼 | `select` |
| 🇭🇰 香港节点 | `select` |
| 🇯🇵 日本节点 | `select` |
| 🇸🇬 狮城节点 | `select` |
| 🇺🇲 美国节点 | `select` |
| 🔯 香港故转 | `fallback` |
| 🔯 日本故转 | `fallback` |
| ... | (剩余 8 个隐藏) |

</details>

---