后台启动.py ：cd ~/BMC-qwen_model_PH
sudo nohup python3 app.py > flask.log 2>&1 &

如果你只想在系统启动时执行一个 Python 脚本，可以使用 cron 的 @reboot 选项。这样，脚本会在系统每次启动时自动执行一次。
1.编辑 cron 表
打开终端，输入以下命令来编辑 cron 表：
crontab -e
2.添加启动时执行的任务
在编辑器中，添加以下一行：
@reboot /usr/bin/python3 /path/to/your/script.py
这行命令表示每次系统启动时，cron 会自动执行指定的 Python 脚本。
3.确保路径正确
确保 python3 的路径正确，通常可以通过以下命令查找：
which python3
并且确保替换 /path/to/your/script.py 为你的 Python 脚本的实际路径。
4.保存并退出
在编辑完 cron 表后，保存并退出编辑器。对于 nano 编辑器，按 Ctrl + O 保存，Ctrl + X 退出。
5.检查是否成功设置
你可以通过以下命令查看当前的 cron 任务：
crontab -l
确保输出中包含 @reboot 任务。
6.重启系统
重启系统来测试是否成功在启动时执行你的 Python 脚本：
sudo reboot
当系统重新启动后，指定的 Python 脚本将会执行一次。
7.查看日志（可选）
如果你希望脚本执行时输出日志，或者想调试错误，可以将标准输出和标准错误输出重定向到一个文件：
@reboot /usr/bin/python3 /path/to/your/script.py >> /path/to/logfile.log 2>&1
这样，任何输出（包括错误）都会被记录到 logfile.log 文件中，便于后续查看。
