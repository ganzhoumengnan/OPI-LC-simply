import subprocess
import sys

package_list = ["requests", "python-dotenv", "buidl"]


def install_package(package_name):
    try:
        # 使用pip安装包
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        print(f"包 '{package_name}' 安装成功.")
    except subprocess.CalledProcessError as e:
        print(f"包 '{package_name}' 安装失败. 错误信息: {e}")


def install_all_packages():
    print("车哥为你安装各种节点所需依赖包中····")
    for package_name in package_list:
        install_package(package_name)
    print("所有包安装完毕")
    next_step = input("按回车继续下一步\n")


install_all_packages()
import requests
import tarfile


def run_another_script(script_path):
    try:

        subprocess.check_call(['python', script_path])
        print(f"脚本 '{script_path}' 运行成功.")
    except subprocess.CalledProcessError as e:
        print(f"脚本 '{script_path}' 运行失败. 错误信息: {e}")


def download_file(url, destination):
    try:

        response = requests.get(url)
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"文件下载成功到: {destination}")
    except Exception as e:
        print(f"文件下载失败. 错误信息: {e}")


def to_sqlite3():
    file_path = "./light_client_brc20_sqlite_last.sqlite3.tar.bz2"
    print("开始解压,耐心等吧。解压完成后在目录内会生成一个40多G的bd.sqlite3文件，没有进度条。等就是了")
    with tarfile.open(file_path, 'r:bz2') as tar:
        tar.extractall()

    print(f"{file_path} 解压完成")


if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~车哥一键轻节点安装正式开启~~~~~~~~~~~~~~~~~~~~\n"
          "在开启前请确保你安装了PostgreSQL，并且安装了python并加入到系统全局，不会就去推特@mengnanm看教程")
    print("下载数据库文件，时间会比较久\n"
          "你也可以去用自己的下载工具去：\n"
          "https://opi-light-client-files.fra1.digitaloceanspaces.com/light_client_brc20_sqlite_last.sqlite3.tar.bz2\n"
          "下载完成后放到OPI-LC-main/brc20/sqlite目录下，也就是现在运行脚本的目录下\n"
          )
    user_choose = input("选择自己下载请输入0，脚本自动下载请输入1\n")
    if user_choose == "1":
        print("文件自行下载中。时间比较久慢慢等吧8G的文件，或者关闭脚本重新开启自行下载\n")
        download_file(
            "https://opi-light-client-files.fra1.digitaloceanspaces.com/light_client_brc20_sqlite_last.sqlite3.tar.bz2",
            "./light_client_brc20_sqlite_last.sqlite3.tar.bz2")

    else:
        input("选择自己下载，并在下载完成后放到对应目录后按回车继续\n")
    user_choose_2 = input(
        "确保light_client_brc20_sqlite_last.sqlite3.tar.bz2在脚本sqlite目录下，开始解压请按1(如果已经解压完成别输入1，要不然会覆盖掉重新解压)，如果已经解压了输入0\n")
    if user_choose_2 == "1":
        to_sqlite3()
    else:
        print("选择不解压")

    next_step = input(
        "解压完成开始配置，一直按回车用默认选项，除非到了Report name： 输入你的节点名称就行，最好不要带中文和字符，带了报错去打开.evn修改，按下回车后开始配置\n")
    user_choose_3 = input("按回车开始配置，如果上次配置好了直接输入0跳过\n")
    if user_choose_3 == "0":
        pass
    else:
        run_another_script("./initialise_sqlite.py")
    user_choose_4 = input("配置信息已完成，开始同步节点,然后别管了，不报错就成功了，按回车正式运行轻节点\n")
    run_another_script("./brc20_light_client_sqlite.py")
