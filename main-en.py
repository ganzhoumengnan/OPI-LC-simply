import subprocess
import sys

package_list = ["requests", "python-dotenv", "buidl"]


def install_package(package_name):
    try:
        # 使用pip安装包
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        print(f" '{package_name}' the Installation Was Successful.")
    except subprocess.CalledProcessError as e:
        print(f" '{package_name}' installation Failed ErrorMessage: {e}")


def install_all_packages():
    print("dependencies_you_need_to_install_various_nodes····")
    for package_name in package_list:
        install_package(package_name)
    print("all_packages_are_installed")
    next_step = input("press_enter_to_proceed_to_the_next_step\n")


install_all_packages()
import requests
import tarfile


def run_another_script(script_path):
    try:

        subprocess.check_call(['python', script_path])
        print(f" '{script_path}' the_run_was_successful.")
    except subprocess.CalledProcessError as e:
        print(f" '{script_path}' failed_error_message: {e}")


def download_file(url, destination):
    try:

        response = requests.get(url)
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"the_file_was_downloaded_successfully: {destination}")
    except Exception as e:
        print(f"file_download_failed_error_message: {e}")


def to_sqlite3():
    file_path = "./light_client_brc20_sqlite_last.sqlite3.tar.bz2"
    print("Start decompressing and be patient. After the decompression is completed, a bd.sqlite 3 file with more than 40 GB will be generated in the directory, and there is no progress bar. Just wait\n")
    with tarfile.open(file_path, 'r:bz2') as tar:
        tar.extractall()

    print(f"{file_path} the_decompression_is_complete")


if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~ light node installation is officially enabled~~~~~~~~~~~~~~~~~~~~\n"
          "Before enabling it, please make sure you have Postgre SQL installed, and python installed and added to the system globally, and you will not just go to Twitter @mengnanm watch the tutorial\n")
    print("It will take a long time to download the database file\n"
          "you_can_also_go_with_your_own_downloading_tool：\n"
          "https://opi-light-client-files.fra1.digitaloceanspaces.com/light_client_brc20_sqlite_last.sqlite3.tar.bz2\n"
          "After the download is complete, put it in the OPI-LC-main/brc 20/sqlite directory, which is the directory where the script is now running\n"
          )
    user_choose = input("If you choose to download it yourself, enter 0, and if you want to download the script automatically, enter 1\n")
    if user_choose == "1":
        print("The file is being downloaded by itself. After a long time, wait for the 8 GB file slowly, or close the script and reopen it to download it yourself\n")
        download_file(
            "https://opi-light-client-files.fra1.digitaloceanspaces.com/light_client_brc20_sqlite_last.sqlite3.tar.bz2",
            "./light_client_brc20_sqlite_last.sqlite3.tar.bz2")

    else:
        input("Select Download by yourself, and press Enter to continue after the download is completed, put it in the corresponding directory\n")
    user_choose_2 = input(
        "Make sure that the light client brc 20_sqlite last.sqlite 3.tar.bz 2 is in the sqlite directory of the script, press 1 to start the decompression \n"
        "(if the decompression has been completed, do not enter 1, otherwise it will be overwritten and re-decompressed), if it has been decompressed, enter 0\n")
    if user_choose_2 == "1":
        to_sqlite3()
    else:
        print("you_select_not_to_unzip")

    next_step = input(
        "Unzip to complete the start configuration, keep pressing enter with the default option, unless you go to Report name: Enter your node name,\n"
        " it is best not to bring Chinese and characters, with an error to open the .evn modification, press enter to start configuration\n")
    user_choose_3 = input("Press enter to start the configuration, if the last configuration was good, directly enter 0 to skip\n")
    if user_choose_3 == "0":
        pass
    else:
        run_another_script("./initialise_sqlite.py")
    user_choose_4 = input("The configuration information has been completed,\n"
                          " start to synchronize the node, and then leave it alone,\n"
                          " it will be successful without reporting an error, and press enter to officially run the light node\n")
    run_another_script("./brc20_light_client_sqlite.py")
