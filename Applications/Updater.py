import os
import pathlib
import sys
import json
import subprocess
import time
import urllib3
import shutil
import time
import hashlib

#  |||  Exception List  |||  #
#   0   :   Success
#   1   :   Value cannot be compared
#   2   :   IO Error, cannot access files
#   3   :   Update Crash, can't determine CWD or HOME
#  ________________________  #

versions = "https://github.com/78Alpha/AZNG_Projects/blob/Beta/Data/Versions.ver"  # lINK TO VERSIONS FILE; DON'T DELETE!

versions_beta = ""

github_source = "https://github.com/78Alpha/AZNG_Projects/releases/"  # Source of distributed software, used for downloading

github_beta = ""

home = str(pathlib.Path.home())  # Get the user home directory, this is also home for the application, RW permissions are required!
my_cwd = os.getcwd()  # Get the current directory of where the updater application is running, meant to move it if necessary
temp_directory = f"{home}\\AZNG\\Temp\\"  # A temporary directory for use by junk data; mainly to offload old executables.
assets_directory = f"{home}\\AZNG\\Assets\\"  # Assets/art directory
app_directory = f"{home}\\AZNG\\Applications\\"  # The directory to be the apps home/working folder
data_directory = f"{home}\\AZNG\\Data\\"
root = f"{home}\\AZNG\\"
versions_ver = "Versions.ver"
versions_loc = "Versions.loc"
# error_log = open(f"{home}\\AZNG\\error_log.log", 'a+')


def get_version(current_folder, versions_loc):  # Extract the versions from the local version file
    """
    :arg current_folder || This argument is the apps current directory, does not assume for accuracy (AZNG)
    :arg versions_file || The versions.txt file, or any variable containing one
    :var verify || Variable contains the loaded results from the versions file that was downloaded
    """
    with open(f"{current_folder}\\{versions_loc}", 'r') as software:  # Open the versions file in read mode
        verify = json.load(software)  # Use json to load the variables, simple formatting
        software.close()  # close the file from further operation
    return verify  # Return the variable instead of an exit code, no safety for failure implemented


def download_file(file_name, version, github, app_directory):  # Dwonload a specified file form the REPO
    """
    :arg file_name | File name to be used for the output file of a download
    :arg version | The release version to be targeted
    :arg github | The github source link for use of retrieval
    :arg app_directory | Move downloaded program to main program folder, finishing the update
    """
    with urllib3.PoolManager().request('GET', f"{github}{version}/{file_name}", preload_content=False) as down_data,\
            open(f"{file_name}", 'wb') as output_file:  # Download a file in part 1, storing in memory and create file for dumping of that item
        shutil.copyfileobj(down_data, output_file)  # Copy the downloaded file from memory into a file for permanent storage
        down_data.close()
        output_file.close()  # close output file, no further modification should be necessary
    os.system(f"move {file_name} {app_directory}")  # Operation to move the downloaded file to the correct directory
    return 0


def compare_versions(fileversions="LOCAL", versions="REMOTE", github_source=None, app_directory=None):  # Compare version files and program versions
    """
    :arg fileversions | The local versions file kept for update reference
    :arg versions | The remote versions file downloaded from a separate source
    :arg github_source | The source github link for checking and downloading versions files and other needed software pieces
    :arg app_directory | The main app directory, should be an AZNG folder
    :var software_list | Contains the local loaded versions list
    :var versions_list | Contains the remote versions list
    :var len_software | The length of the list of items loaded from local versions file
    :var len_versions | The length of the list of items loaded from remote versions file, used as a basic/sanity check
    :var need_update | Check True or False if a piece of software is in need of updating
    :var version_data | Split the versions.txt string into digits to be checked later on as a list
    :var comparrison_version | same as version_data but for local versions file
    """
    software_list = fileversions["SoftwareList"]  # Load data
    versions_list = versions["SoftwareList"]  # Load data
    len_software = len(software_list)  # Store length
    len_versions = len(versions_list)  # store Length
    if len_versions > len_software:  # Check if there is a difference in size to the number of programs in remote versions file
        for software in software_list:  # Get software name
            if software not in versions_list:  # Check if the old software is in the new list
                os.remove(f"{app_directory}\\{software}")  # Delete aged software
        for software in versions_list:  # Get software name
            if software not in versions_list:  # If it doesn't exist, get it
                download_file(file_name=software,
                              version=versions["Stable"],
                              github=github_source,
                              app_directory=app_directory)  # Download the missing file from the stable branch
                create_shortcut_url(application=software,
                                    home=home,
                                    icon=f"{app_directory}\\Assets\\{software}.ico")  # Create a basic URL shortcut on the desktop
            else:
                pass
    elif len_software == len_versions:  # Check if the lists contain the same number of items
        if software_list == versions_list:  # check if the lists are actually the same
            for software in software_list:  # Get software name
                if software not in versions_list:  # Check if the old software is in the new list
                    os.remove(f"{app_directory}\\{software}")  # Delete aged software
            for software in versions_list:  # get software name
                need_update = False  # set needing update to false
                version_data = versions[f"{software}"].split(".")  # Split version string to digits
                try:
                    comparison_version = fileversions[f"{software}"].split(".")  # Split version string to digits
                except KeyError:
                    comparison_version = ["0", "0", "0"]  # Default it
                for i in range(len(version_data)):  # Cycle through the numbers to see if any are different, typically greater
                    if int(version_data[i]) == int(comparison_version[i]):  # If the version is the same, simply pass
                        pass
                    else:
                        need_update = True  # Tag it to needing an update if version is different
                if need_update:  # If it does need an update, then update it
                    download_file(file_name=software,
                                  version=versions[f"{software}"],
                                  github=github_source,
                                  app_directory=app_directory)  # Download the file
                    create_shortcut_url(application=software,
                                        home=home,
                                        icon=f"{app_directory}\\Assets\\{software}.ico")  # Give it a dirty shortcut
                else:
                    pass
        elif software_list != versions_list:  # Check if the version lists contain the same software
            for software in software_list:  # Get software name
                if software not in versions_list:  # Check if the old software is in the new list
                    os.remove(f"{app_directory}\\{software}")  # Delete aged software
            for software in versions_list:  # get software name
                need_update = False  # set needing update to false
                version_data = versions[f"{software}"].split(".")  # Split version string to digits
                try:
                    comparison_version = fileversions[f"{software}"].split(".")  # Split version string to digits
                except KeyError:
                    comparison_version = ["0", "0", "0"]  # Default it
                for i in range(len(version_data)):  # Cycle through the numbers to see if any are different, typically greater
                    if int(version_data[i]) == int(comparison_version[i]):  # If the version is the same, simply pass
                        pass
                    else:
                        need_update = True  # Tag it to needing an update if version is different
                if need_update:  # If it does need an update, then update it
                    download_file(file_name=software,
                                  version=versions[f"{software}"],
                                  github=github_source,
                                  app_directory=app_directory)  # Download the file
                    create_shortcut_url(application=software,
                                        home=home,
                                        icon=f"{app_directory}\\Assets\\{software}.ico")  # Give it a dirty shortcut
                else:
                    pass
    elif len_versions < len_software:
        for software in software_list:  # Get software name
            if software not in versions_list:  # Check if the old software is in the new list
                os.remove(f"{app_directory}\\{software}")  # Delete aged software
        for software in versions_list:  # get software name
            need_update = False  # set needing update to false
            version_data = versions[f"{software}"].split(".")  # Split version string to digits
            try:
                comparison_version = fileversions[f"{software}"].split(".")  # Split version string to digits
            except KeyError:
                comparison_version = ["0", "0", "0"]  # Default it
            for i in range(
                    len(version_data)):  # Cycle through the numbers to see if any are different, typically greater
                if int(version_data[i]) == int(comparison_version[i]):  # If the version is the same, simply pass
                    pass
                else:
                    need_update = True  # Tag it to needing an update if version is different
            if need_update:  # If it does need an update, then update it
                download_file(file_name=software,
                              version=versions[f"{software}"],
                              github=github_source,
                              app_directory=app_directory)  # Download the file
                create_shortcut_url(application=software,
                                    home=home,
                                    icon=f"{app_directory}\\Assets\\{software}.ico")  # Give it a dirty shortcut
            else:
                pass
    else:
        return 1
    return 0

def move_updated_items(application, application_directory, temp_directory):
    os.system(f"mv {application_directory}{application}.exe {temp_directory}{application}.old")
    os.system(f"mv {application}.exe {application_directory}{application}.exe")


def attempt_self_update(temp=None, assets=None, data=None, apps=None, versions_loc=None, versions_ver=None, github_source=None, github_beta=None, root=None, versions=None, home=None):  # Initiate the update process as standalone or add in library
    try:
        open(f"{data}InitiateBeta.yes", 'r')
    except FileNotFoundError:
        temp_var_exist = 0
        if os.getcwd() == home:
            try:
                open(f"{home}Updater_T.exe", 'r')
                temp_var_exist = 1
            except FileNotFoundError:
                pass
            if temp_var_exist != 0:
                os.system(f"del {home}Updater.exe")
            else:
                pass
            download_versions_file(versions_remote=versions, versions_loc=versions_loc, versions_ver=versions_ver, data=data)
            # os.system(f"mv {versions_loc} {data}{versions_loc}")
            with open(f"{data}{versions_loc}", 'r') as version_file:
                version_list = version_file.readlines()
                version_file.close()

            # print(f"Updater launched from: {home}")
        elif os.getcwd() != home:
            os.system(f"copy Updater.exe {home}")
            # return_value = subprocess.check_output([f"start {home}\\Updater_Micro.exe; exit 0"], stdout=subprocess.PIPE, stderr = subprocess.STDOUT, shell = True)
            open(".\\temp.txt", 'w+').write(str(subprocess.check_output([f"start {home}\\Updater_Micro.exe; exit 0"], stdout=subprocess.PIPE, stderr = subprocess.STDOUT, shell = True)))
            breakpoint()
            time.sleep(10)
            input()
            # sys.exit()
        else:
            return 3


def download_versions_file(versions_remote=None, versions_loc=None, versions_ver=None, data=None):  # Retrieve the most recent version file from the Github Repo
    """
    :arg versions | The URL to the versions.txt file
    """
    with urllib3.PoolManager().request('GET', f"{versions_remote}", preload_content=False) as down_data, open("Versions.loc", 'wb') as output_file:  # Download the versions file into memory and dump it into an external file
        shutil.copyfileobj(down_data, output_file)
        os.system(f"mv {versions_ver} {data}{versions_loc}")
        output_file.close()


def create_shortcut_url(application, root, icon):  # Create a desktop  shortcut via the URL file method
    """
    :arg application | Name of the application that the shortcut is being created
    :arg home | User home directory, used to extract Desktop and as a point of reference for where the application is stored
    :var desktop | The user Desktop as set in environment
    :var icon | The location of the icon file, however, this usually does not work; Reason being a windows bug
    :var clean_home | Convert the back slashes to regular slashes so it works like a URL
    """
    desktop = os.path.expanduser("~\\Desktop")
    icon = f"{root}{icon}.ico"
    with open(f"{desktop}\\{application}.url", 'w+') as url_short:
        clean_home = home.replace("\\", "/")
        url_short.write(f"[InternetShortcut]\nURL=file:///{clean_home}/{application}\nIconFile={root}\\{icon}.ico")
        url_short.close()
    return 0

def error_logging(user_inputs=None, error_log=error_log):
    pass

# attempt_self_update(home=home, my_cwd=my_cwd)
# input()
# sys.exit()
