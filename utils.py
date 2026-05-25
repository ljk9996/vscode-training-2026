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
        return []


def save_tasks(tasks):
    """保存任务列表到文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(tasks, title):
    """添加新任务"""
    max_id = max([task["id"] for task in tasks], default=0)
    task = {
        "id": max_id + 1,
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"已添加任务：{title}")


def list_tasks(tasks):
    """列出所有任务"""
    if not tasks:
        print("暂无任务")
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
            print(f"任务 [{task_id}] 已完成")
            return
    print(f"找不到任务 [{task_id}]")


def delete_task(tasks, task_id, force=False):
    """删除指定任务
    
    Args:
        tasks: 任务列表
        task_id: 要删除的任务ID
        force: 是否强制删除（跳过确认提示，用于测试）
    """
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            if not force:
                confirm = input(f"确认删除 [{task_id}] {task['title']}? (y/n): ")
                if confirm.lower() != 'y':
                    print("已取消删除")
                    return
            tasks.pop(i)
            save_tasks(tasks)
            print(f"已删除任务 [{task_id}]")
            return
    print(f"找不到任务 [{task_id}]")