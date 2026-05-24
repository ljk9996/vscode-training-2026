import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"

def load_tasks():
    """从文件加载任务列表（增加容错：文件不存在或为空时返回空列表）"""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:  # 文件存在但内容为空
                return []
            return json.loads(content)
    except (json.JSONDecodeError, ValueError):
        return []  # JSON 损坏也返回空列表

def save_tasks(tasks):
    """保存任务列表到文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(title):
    """添加新任务"""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ 已添加任务: {title}")

def list_tasks():
    """列出所有任务"""
    tasks = load_tasks()
    if not tasks:
        print("📭 暂无任务")
        return
    print("\n📋 任务清单:")
    for t in tasks:
        status = "✅" if t["done"] else "⬜"
        print(f"  {status} [{t['id']}] {t['title']} ({t['created_at']})")

def mark_done(task_id):
    """标记任务完成"""
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"🎉 任务完成: {t['title']}")
            return
    print("❌ 找不到该任务")

def main():
    """自动化测试：直接添加任务，不用手动输入"""
    print("🧪 开始测试...")
    
    add_task("买牛奶")
    add_task("交电费")  
    add_task("写周报")
    
    print("\n📋 查看所有任务:")
    list_tasks()
    
    print("\n✅ 标记第2个任务完成:")
    mark_done(2)
    
    print("\n📋 再次查看:")
    list_tasks()

if __name__ == "__main__":
    main()