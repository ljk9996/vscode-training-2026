from utils import load_tasks, save_tasks, add_task, list_tasks, mark_done

def main():
    tasks = load_tasks()
    add_task("买牛奶")
    add_task("交电费")
    add_task("写周报")
    list_tasks(tasks)
    mark_done(tasks, 2)
    list_tasks(tasks)

if __name__ == "__main__":
    main()