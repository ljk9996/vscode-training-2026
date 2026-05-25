import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"

def load_tasks():
    """从文件加载任务列表"""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
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
    print(f"✅ 已添加任务：{title}")

def list_tasks(tasks):
    """列出所有任务"""
    if not tasks:
        print("📭 暂无任务")
        return
    for task in tasks:
        status = "✅" if task["done"] else "⬜"
        print(f"{status} [{task['id']}] {task['title']} ({task['created_at']})")

def mark_done(tasks, task_id):
    """标记任务完成"""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"✅ 任务 [{task_id}] 已完成")
            return
    print(f"❌ 找不到任务 [{task_id}]")