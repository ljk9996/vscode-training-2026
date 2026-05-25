import os
from utils import load_tasks, add_task, mark_done, delete_task


def setup_function():
    """测试前清理旧数据"""
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")


def test_add_task():
    """测试添加任务"""
    tasks = load_tasks()
    add_task(tasks, "测试任务")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "测试任务"
    assert tasks[0]["done"] == False


def test_mark_done():
    """测试标记完成"""
    tasks = load_tasks()
    add_task(tasks, "测试任务")
    mark_done(tasks, 1)
    assert tasks[0]["done"] == True


def test_delete_task():
    """测试删除任务（force=True 跳过确认）"""
    tasks = load_tasks()
    add_task(tasks, "测试任务")
    delete_task(tasks, 1, force=True)
    assert len(tasks) == 0