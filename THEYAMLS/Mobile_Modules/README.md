# 📂 Android 手机模块 (Mobile Modules)

[🔙 返回主页](../../README.md)

> 📊 共收录 **4** 个配置文件

## ⚔️ 参数横向对比

| 配置文件 | 混合端口 | 面板端口 | 模式 | TUN | 策略组 | 规则数 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [`config.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Mobile_Modules/Surfing/config.yaml) | 7890 | 0.0.0.0:9090 | Rule | 🚫 | **34** | 38 |
| [`config.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Mobile_Modules/ClashMix/config.yaml) | 7890 | 0.0.0.0:9090 | rule | ✅ | **5** | 9 |
| [`config.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Mobile_Modules/BoxProxy/config.yaml) | 7890 | 0.0.0.0:9090 | Rule | ✅ | **3** | 4 |
| [`config.yaml`](https://github.com/HenryChiao/mihomo_yamls/blob/main/THEYAMLS/Mobile_Modules/AkashaProxy/config.yaml) | 7890 | 127.0.0.1:9090 | rule | ✅ | **20** | 14 |

## 📝 详细结构分析
### 👤 AkashaProxy
#### 📄 config.yaml
- **文件路径**: `AkashaProxy/config.yaml` (8.2 KB)
<details>
<summary>🔍 点击查看 20 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| 代理设置 | `select` |
| 国内分流 | `select` |
| 屏蔽 | `select` |
| AI分流 | `select` |
| 中国 | `select` |
| 香港 | `select` |
| 台湾 | `select` |
| 日本 | `select` |
| 美国 | `select` |
| 英国 | `select` |
| 新加坡 | `select` |
| 全部节点 | `select` |
| 中国自动选择 | `url-test` |
| 香港自动选择 | `url-test` |
| 台湾自动选择 | `url-test` |
| 日本自动选择 | `url-test` |
| 美国自动选择 | `url-test` |
| 英国自动选择 | `url-test` |
| 新加坡自动选择 | `url-test` |
| 自动选择 | `url-test` |

</details>

---
### 👤 BoxProxy
#### 📄 config.yaml
- **文件路径**: `BoxProxy/config.yaml` (4.2 KB)
<details>
<summary>🔍 点击查看 3 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| 国外代理 | `select` |
| 国内直连 | `select` |
| 漏网之鱼 | `select` |

</details>

---
### 👤 ClashMix
#### 📄 config.yaml
- **文件路径**: `ClashMix/config.yaml` (6.5 KB)
<details>
<summary>🔍 点击查看 5 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| 代理 | `select` |
| 自动切换 | `fallback` |
| 智能选择 | `smart` |
| 广告 | `select` |
| 中国网站 | `select` |

</details>

---
### 👤 Surfing
#### 📄 config.yaml
- **文件路径**: `Surfing/config.yaml` (19.0 KB)
<details>
<summary>🔍 点击查看 34 个策略组详情</summary>

| 策略组名称 | 类型 |
| :--- | :--- |
| 总模式 | `select` |
| 订阅更新 | `select` |
| 小红书 | `select` |
| 抖音 | `select` |
| BiliBili | `select` |
| Steam | `select` |
| Apple | `select` |
| Microsoft | `select` |
| Telegram | `select` |
| Discord | `select` |
| Spotify | `select` |
| TikTok | `select` |
| YouTube | `select` |
| Netflix | `select` |
| Google | `select` |
| GoogleFCM | `select` |
| Facebook | `select` |
| OpenAI | `select` |
| GitHub | `select` |
| Twitter(X) | `select` |
| ... | (剩余 14 个隐藏) |

</details>

---