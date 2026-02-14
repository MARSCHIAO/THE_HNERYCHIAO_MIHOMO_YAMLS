import os
import json
import subprocess
import datetime

WORKSPACE_DIR = "workspace"
OLD_STATS_FILE = "old_data/stats.json"
STATS_FILE = os.path.join(WORKSPACE_DIR, "stats.json")
README_FILE = os.path.join(WORKSPACE_DIR, "README.md")

def run_command(cmd):
    """运行系统命令"""
    try:
        subprocess.check_call(cmd, shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print(f"⚠️ Warning: Command failed: {cmd}")

def count_lines(filepath):
    """计算文件行数"""
    try:
        with open(filepath, 'rb') as f:
            return sum(1 for _ in f)
    except:
        return 0

def process_dat_files():
    """遍历目录，解包 dat 文件，并返回统计数据"""
    current_stats = {}
    
    # 遍历 workspace 下的所有作者目录
    for author in os.listdir(WORKSPACE_DIR):
        author_path = os.path.join(WORKSPACE_DIR, author)
        if not os.path.isdir(author_path):
            continue
            
        print(f"🔍 Analyzing {author}...")
        current_stats[author] = {}

        # 遍历作者目录下的子文件夹 (geoip, geosite)
        for category in ["geoip", "geosite"]:
            cat_dir = os.path.join(author_path, category)
            if not os.path.exists(cat_dir):
                continue
                
            # 找到目录下的 .dat 文件
            for file in os.listdir(cat_dir):
                if not file.endswith(".dat"):
                    continue
                
                dat_path = os.path.join(cat_dir, file)
                # 创建导出目录： workspace/Author/geoip/dat_name_export/
                export_dir = os.path.join(cat_dir, f"{file}_text")
                os.makedirs(export_dir, exist_ok=True)
                
                print(f"  -> Extracting {file}...")
                
                # --- GeoIP 处理 ---
                if "geoip" in file.lower():
                    # 1. 获取列表
                    list_file = os.path.join(export_dir, "list.txt")
                    run_command(f"geoip list {dat_path} > {list_file}")
                    
                    # 2. 读取列表并导出每个 tag
                    if os.path.exists(list_file):
                        with open(list_file, 'r') as f:
                            tags = [line.strip().split()[0] for line in f if line.strip()]
                        
                        # 仅导出常用 Tag 防止文件过多 (可选：如果想导出所有，去掉 [:20])
                        # 为了演示，这里导出所有，但实际使用建议做个过滤，否则可能有几百个文件
                        for tag in tags: 
                            out_txt = os.path.join(export_dir, f"{tag}.txt")
                            run_command(f"geoip export -o {out_txt} {dat_path} {tag}")
                            
                            # 统计
                            count = count_lines(out_txt)
                            current_stats[author][f"{file}::{tag}"] = count

                # --- GeoSite 处理 ---
                elif "geosite" in file.lower() or "dlc" in file.lower():
                    # Geosite 工具通常直接支持导出
                    # 先尝试列出 (domain-list-community 没有简单的 list 命令，通常直接解包)
                    # 这里假设我们只关心常见分类，或者尝试导出特定列表
                    # 也可以用 tool 遍历，这里简化逻辑，尝试导出 Google, CN, Apple 等常见
                    
                    # 实际上 domain-list-community 可以通过 export 导出所有包含的 category
                    # 但需要知道名字。通常做法是解包 data 目录。
                    # 由于命令行工具限制，这里我们模拟导出几个关键 tag
                    
                    target_tags = ["google", "cn", "apple", "telegram", "netflix", "openai", "category-ads-all"]
                    
                    for tag in target_tags:
                        out_txt = os.path.join(export_dir, f"{tag}.txt")
                        # geosite (domain-list-community) 语法: -dat path -export tag
                        # 注意：不同版本工具参数可能不同，这里使用 domain-list-community 标准
                        run_command(f"geosite -dat {dat_path} -export {tag} > {out_txt}")
                        
                        if os.path.exists(out_txt) and os.path.getsize(out_txt) > 0:
                            count = count_lines(out_txt)
                            current_stats[author][f"{file}::{tag}"] = count
                        else:
                            # 清理空文件
                            if os.path.exists(out_txt): os.remove(out_txt)

    return current_stats

def generate_markdown(current_stats, old_stats):
    """生成 README.md"""
    lines = ["# 🌍 GeoData Assets & Analytics", ""]
    lines.append(f"> Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (UTC+8)")
    lines.append("")
    
    lines.append("## 📊 规则统计与变化")
    
    for author, rules in current_stats.items():
        if not rules: continue
        
        lines.append(f"### 👤 {author}")
        lines.append("| 文件::标签 | 条目数量 | 较昨日变化 |")
        lines.append("|---|---|---|")
        
        for key, count in sorted(rules.items()):
            # 计算 Diff
            old_count = old_stats.get(author, {}).get(key, 0)
            diff = count - old_count
            
            diff_str = "0"
            if diff > 0: diff_str = f"🔺 +{diff}"
            elif diff < 0: diff_str = f"🔻 {diff}"
            
            lines.append(f"| {key} | {count} | {diff_str} |")
        lines.append("")

    lines.append("## 📂 目录结构说明")
    lines.append("- **geoip/**: 二进制 geoip.dat")
    lines.append("- **geosite/**: 二进制 geosite.dat")
    lines.append("- **xxx_text/**: 解包后的文本规则 (方便 Grep 或 转换)")
    
    with open(README_FILE, "w", encoding='utf-8') as f:
        f.write("\n".join(lines))
    
    # 保存当前的 stats 以备下次对比
    with open(STATS_FILE, "w", encoding='utf-8') as f:
        json.dump(current_stats, f, indent=2)

def main():
    print("⏳ Loading old stats...")
    old_stats = {}
    if os.path.exists(OLD_STATS_FILE):
        try:
            with open(OLD_STATS_FILE, 'r') as f:
                old_stats = json.load(f)
        except:
            print("Old stats file corrupted, skipping diff.")

    print("⏳ Processing assets...")
    current_stats = process_dat_files()
    
    print("⏳ Generating report...")
    generate_markdown(current_stats, old_stats)
    print("✅ Done.")

if __name__ == "__main__":
    main()
