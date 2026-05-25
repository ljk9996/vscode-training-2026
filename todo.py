import argparse
from utils import load_tasks, save_tasks, add_task, list_tasks, mark_done, delete_task


def main():
    # 创建解析器（程序的"入口招牌"）
    parser, subparsers = create_parser()

    # add 子命令：添加任务
    add_parser = subparsers.add_parser("add", help="添加新任务")
    add_parser.add_argument("title", help="任务标题")

    # list 子命令：列出任务
    list_parser = subparsers.add_parser("list", help="列出所有任务")

    # done 子命令：标记完成
    done_parser = subparsers.add_parser("done", help="标记任务完成")
    done_parser.add_argument("task_id", type=int, help="任务ID")

    # delete 子命令：删除任务
    delete_parser = subparsers.add_parser("delete", help="删除任务")
    delete_parser.add_argument("task_id", type=int, help="任务ID")

    # 解析用户输入（把命令行文字变成程序能懂的对象）
    args = parser.parse_args()

    # 根据命令执行不同操作
    tasks = load_tasks()

    if args.command == "add":
        add_task(tasks, args.title)

    elif args.command == "list":
        list_tasks(tasks)

    elif args.command == "done":
        mark_done(tasks, args.task_id)

    elif args.command == "delete":
        delete_task(tasks, args.task_id)

    else:
        # 如果没有输入命令，显示帮助信息
        parser.print_help()

def create_parser():
    parser = argparse.ArgumentParser(description="Todo 任务管理工具")

    # 添加子命令（像 git add / git commit 一样）
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    return parser,subparsers


if __name__ == "__main__":
    main()
