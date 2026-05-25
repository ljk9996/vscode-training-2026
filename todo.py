from utils import load_tasks, save_tasks, add_task, list_tasks, mark_done, delete_task


def main():
    tasks = load_tasks()
    add_task(tasks, "买牛奶")
    add_task(tasks, "交电费")
    add_task(tasks, "写周报")
    list_tasks(tasks)

    # 测试删除功能
    delete_task(tasks, 2)
    list_tasks(tasks)

    mark_done(tasks, 1)
    list_tasks(tasks)


if __name__ == "__main__":
    main()