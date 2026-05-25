from setuptools import setup, find_packages

setup(
    name="vscode-training-todo",           # 项目名字
    version="1.0.0",                       # 版本号
    description="VS Code Python 训练项目 - Todo 任务管理工具",
    author="ljk9996",
    packages=find_packages(),              # 自动找到所有 Python 包
    install_requires=[                     # 依赖包（从 requirements.txt 来）
        "requests>=2.32.0",
    ],
    entry_points={                         # 命令行入口
        "console_scripts": [
            "todo=todo:main",              # 输入 "todo" 就运行 todo.py 的 main()
        ],
    },
    python_requires=">=3.8",              # 最低 Python 版本
)