import os
import pathlib
import sys
import json
import subprocess
import time
import urllib3
import shutil
import hashlib
import datetime
import secrets
import glob

# from logging_agent import *

# Attempt to migrate to class for better module integration and differentiation (may not be useful and hinder performance

#  |||  Exception List  |||  #
#   0   :   Success
#   1   :   Value cannot be compared
#   2   :   IO Error, cannot access files
#   3   :   Update Crash, can't determine CWD or HOME
#  ________________________  #

versions = "https://raw.githubusercontent.com/78Alpha/AZNG_Projects/Beta/Data/Versions.ver"

versions_beta = "https://raw.githubusercontent.com/78Alpha/AZNG_Projects/Beta/Data/Versions.ver"

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


def get_version():  # Extract the versions from the local version file
    """
    :param versions_loc: Local version file
    :arg current_folder || This argument is the apps current directory, does not assume for accuracy (AZNG)
    :arg versions_file || The versions.txt file, or any variable containing one
    :var verify || Variable contains the loaded results from the versions file that was downloaded
    """
    return_value = []
    try:
        with open(f"{data_directory}{versions_loc}", 'r') as software:  # Open the versions file in read mode
            try:
                verify = json.load(software)  # Use json to load the variables, simple formatting
            except:
                return [char_buf_lim(str(get_version).split(' ')[1]), return_value, "LoadListFail"]
            software.close()  # close the file from further operation
    except:
        return [char_buf_lim(str(get_version).split(' ')[1]), return_value, "FileReadError"]
    return verify  # Return the variable instead of an exit code, no safety for failure implemented


def download_file(file_name=None, version=None):  # Download a specified file form the REPO
    """
    :arg file_name | File name to be used for the output file of a download
    :arg version | The release version to be targeted
    :arg github | The github source link for use of retrieval
    :arg app_directory | Move downloaded program to main program folder, finishing the update
    """
    return_value = []
    try:
        with urllib3.PoolManager().request('GET', f"{github_source}{version}/{file_name}", preload_content=False) as down_data, open(f"{file_name}", 'wb') as output_file:  # Download a file in part 1, storing in memory and create file for dumping of that item
            shutil.copyfileobj(down_data, output_file)  # Copy the downloaded file from memory into a file for permanent storage
            down_data.close()
            output_file.close()  # close output file, no further modification should be necessary
        move = subprocess.call(f"move {file_name} {app_directory}", shell=True)  # Operation to move the downloaded file to the correct directory
        if move != 0:
            return_value.append(move)
            return [char_buf_lim(str(checksum_files).split(' ')[1]), return_value, "MoveFailed"]
        return [char_buf_lim(str(download_file).split(' ')[1]), return_value, "FileDownloaded"]  # Process proceeds without fail
    except:
        return [char_buf_lim(str(download_file).split(' ')[1]), return_value, "FileNotDownloaded"]  # Put in log possible errors, split program if necessary


def checksum_files(app=None):
    return_value = []
    master_sum = hashlib.sha512()
    try:
        with open(f"{app_directory}{app}", 'rb') as application:
            binary_data = application.read()
            application.close()
        master_sum.update(binary_data)
        return [char_buf_lim(str(checksum_files).split(' ')[1]), return_value, "HashGenerated"]
    except:
        return [char_buf_lim(str(checksum_files).split(' ')[1]), return_value, "FileNotFound"]


def compare_versions(fileversions=None, versions=None):  # Compare version files and program versions
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
    return_value = []
    software_list = ""
    versions_list = ""
    len_software = 0
    len_versions = 0
    try:
        software_list = fileversions["SoftwareList"]  # Load data
        versions_list = versions["SoftwareList"]  # Load data
        len_software = len(software_list)  # Store length
        len_versions = len(versions_list)  # store Length
        # return [char_buf_lim(str(compare_versions).split(' ')[1]), return_value, "SoftwareLists"]
    except:
        return [char_buf_lim(str(compare_versions).split(' ')[1]), return_value, "ListLoadFail"]
    if len_versions > len_software:  # Check if there is a difference in size to the number of programs in remote versions file
        for software in software_list:  # Get software name
            if software not in versions_list:  # Check if the old software is in the new list
                deletion = subprocess.call(f"del {app_directory}\\{software}", shell=True)
                # os.remove(f"{app_directory}\\{software}")  # Delete aged software
                if deletion != 0:
                    return_value.append(deletion)
                    return [char_buf_lim(str(attempt_self_update).split(' ')[1]), return_value, "ItemDeleteFailed"]
        for software in versions_list:  # Get software name
            if software not in versions_list:  # If it doesn't exist, get it
                logging_agent(download_file(file_name=software,
                              version=versions[f"{software}"]))  # Download the missing file from the stable branch
                logging_agent(create_shortcut_url(application=software,
                                    icon=f"{app_directory}\\Assets\\{software}.ico"))  # Create a basic URL shortcut on the desktop
            else:
                pass
    elif len_software == len_versions:  # Check if the lists contain the same number of items
        if software_list == versions_list:  # check if the lists are actually the same
            for software in software_list:  # Get software name
                if software not in versions_list:  # Check if the old software is in the new list
                    deletion = subprocess.call(f"del {app_directory}\\{software}", shell=True)
                    if deletion != 0:
                        return_value.append(deletion)
                        return [char_buf_lim(str(attempt_self_update).split(' ')[1]), return_value, "ItemDeleteFail"]
                    # os.remove(f"{app_directory}\\{software}")  # Delete aged software
            for software in versions_list:  # get software name
                need_update = False  # set needing update to false
                version_data = versions[f"{software}"].split(".")  # Split version string to digits
                try:
                    comparison_version = fileversions[f"{software}"].split(".")  # Split version string to digits
                except:
                    comparison_version = ["0", "0", "0"]  # Default it
                for i in range(len(version_data)):  # Cycle through the numbers to see if any are different, typically greater
                    if version_data[i] == comparison_version[i]:  # If the version is the same, simply pass
                        pass
                    else:
                        need_update = True  # Tag it to needing an update if version is different
                if need_update:  # If it does need an update, then update it
                    logging_agent(download_file(file_name=software,
                                  version=versions[f"{software}"]))  # Download the file
                    logging_agent(create_shortcut_url(application=software,
                                        icon=f"{app_directory}\\Assets\\{software}.ico"))  # Give it a dirty shortcut
                else:
                    pass
        elif software_list != versions_list:  # Check if the version lists contain the same software
            for software in software_list:  # Get software name
                if software not in versions_list:  # Check if the old software is in the new list
                    deletion = subprocess.call(f"del {app_directory}\\{software}", shell=True)
                    if deletion != 0:
                        return_value.append(deletion)
                        return [char_buf_lim(str(test_function2).split(' ')[1]), return_value, "DeleteItemFail"]
                    # os.remove(f"{app_directory}\\{software}")  # Delete aged software
            for software in versions_list:  # get software name
                need_update = False  # set needing update to false
                version_data = versions[f"{software}"].split(".")  # Split version string to digits
                try:
                    comparison_version = fileversions[f"{software}"].split(".")  # Split version string to digits
                except KeyError:
                    comparison_version = ["0", "0", "0"]  # Default it
                for i in range(len(version_data)):  # Cycle through the numbers to see if any are different, typically greater
                    if version_data[i] == comparison_version[i]:  # If the version is the same, simply pass
                        pass
                    else:
                        need_update = True  # Tag it to needing an update if version is different
                if need_update:  # If it does need an update, then update it
                    logging_agent(download_file(file_name=software,
                                  version=versions[f"{software}"]))  # Download the file
                    logging_agent(create_shortcut_url(application=software,
                                        icon=f"{app_directory}\\Assets\\{software}.ico"))  # Give it a dirty shortcut
                else:
                    pass
    elif len_versions < len_software:
        for software in software_list:  # Get software name
            if software not in versions_list:  # Check if the old software is in the new list
                deletion = subprocess.call(f"del {app_directory}\\{software}", shell=True)
                if deletion != 0:
                    return_value.append(deletion)
                    return [char_buf_lim(str(test_function2).split(' ')[1]), return_value, "DeleteItemFail"]
                # os.remove(f"{app_directory}\\{software}")  # Delete aged software
        for software in versions_list:  # get software name
            need_update = False  # set needing update to false
            version_data = versions[f"{software}"].split(".")  # Split version string to digits
            try:
                comparison_version = fileversions[f"{software}"].split(".")  # Split version string to digits
            except KeyError:
                comparison_version = ["0", "0", "0"]  # Default it
            for i in range(
                    len(version_data)):  # Cycle through the numbers to see if any are different, typically greater
                if version_data[i] == comparison_version[i]:  # If the version is the same, simply pass
                    pass
                else:
                    need_update = True  # Tag it to needing an update if version is different
            if need_update:  # If it does need an update, then update it
                logging_agent(download_file(file_name=software,
                              version=versions[f"{software}"]))  # Download the file
                logging_agent(create_shortcut_url(application=software,
                                    icon=f"{app_directory}\\Assets\\{software}.ico"))  # Give it a dirty shortcut
            else:
                pass
    else:
        return [char_buf_lim(str(compare_versions).split(' ')[1]), return_value, "ItemMoveAttempt"]
    return [char_buf_lim(str(compare_versions).split(' ')[1]), return_value, "ItemMoveAttempt"]


def move_updated_items(application=None):  # Move items after update completion, check hash to confirm correctness
    return_value = []
    # os.system(f"move {application_directory}{application}.exe {temp_directory}{application}.old")  # Move current version to temp directory under old to prevent corruption
    # os.system(f"move {application}.exe {application_directory}{application}.exe")  # Move in place application to application directory
    move_to_old = subprocess.call(f"move '{app_directory}{application}.exe' '{temp_directory}{application}.old'", shell=True)
    if int(move_to_old) != 0:
        return_value.append(move_to_old)
        return [char_buf_lim(str(test_function2).split(' ')[1]), return_value, "FailedToOld"]
    move_updated = subprocess.call(f"move '{application}.exe' '{app_directory}{application}.exe'", shell=True)
    if int(move_updated) != 0:
        return_value.append(move_updated)
        return [char_buf_lim(str(test_function2).split(' ')[1]), return_value, "FailedToUpdate"]
    return [char_buf_lim(str(test_function2).split(' ')[1]), return_value, "ItemMoveSuccess"]


def attempt_self_update():  # Initiate the update process as standalone or add in library
    return_value = []
    beta_key = False
    try:
        open(f"{data_directory}InitiateBeta.yes", 'r')  # If 'Beta' file exists, enter the beta mode, download experimental versions from Dev branch
        # return [char_buf_lim(str(attempt_self_update).split(' ')[1]), return_value, "BetaFound"]
    except:  # If it does not exist, just continue as normal
        temp_var_exist = 0
        if f"{temp_directory}Core_T.exe" in glob.glob(f"{temp_directory}*.*"):  # Launch copied updater from user home in case the updater needs updating
            print(f"{temp_directory}Core_T.exe" in glob.glob(f"{temp_directory}*.*"))
            try:
                open(f"{temp_directory}Core_T.exe", 'r')  # Make sure the updater exists in the home directory
                temp_var_exist = 1
            except:
                pass
            if temp_var_exist != 0:  # if the Updater_T does exist
                deletion = subprocess.call(f"del {temp_directory}Core_T.exe", shell=True)
                if deletion != 0:
                    return_value.append(deletion)
                    return [char_buf_lim(str(attempt_self_update).split(' ')[1]), return_value, "DeleteFail"]
                # os.system(f"del {home}Updater.exe")  # Delete the original updater application
            else:
                pass
            logging_agent(download_ver_file())   # Obtain update data
            # os.system(f"move {versions_loc} {data}{versions_loc}")
            try:
                with open(f"{data_directory}{versions_loc}", 'r') as version_file:  # Extract version data and push to variable for later use
                    version_list = json.load(version_file)
                    version_file.close()
            except:
                return [char_buf_lim(str(attempt_self_update).split(' ')[1]), return_value, "FileReadError"]
            try:
                with open(f"{data_directory}{versions_ver}", 'r') as version_list_remote:  # Extract version data and push to variable for later use
                    version_list_remote = json.load(version_list_remote)
                    version_file.close()
            except:
                return [char_buf_lim(str(attempt_self_update).split(' ')[1]), return_value, "FileReadError"]
            # print(f"Updater launched from: {home}")
            logging_agent(compare_versions(fileversions=version_list, versions=version_list_remote))
        elif f"{temp_directory}Core_T.exe" not in glob.glob(f"{temp_directory}*.*"):  # If not in the home directory
            print(f"{temp_directory}Core_T.exe" in glob.glob(f"{temp_directory}"))
            shell_call = subprocess.call(f"copy {app_directory}Core.exe {temp_directory}Core_T.exe", shell=True)
            if shell_call != 0:
                return_value.append(shell_call)
                return [char_buf_lim(str(attempt_self_update).split(' ')[1]), return_value, "CopyError"]
            else:
                try:
                    open(f"{temp_directory}Core_T.exe").close()
                except:
                    return [char_buf_lim(str(attempt_self_update).split(' ')[1]), return_value, "UpdaterFindErr"]
                update_call = subprocess.call(f"start {temp_directory}Core_T.exe", shell=True)
                print(update_call)
                if update_call != 0:
                    return_value.append(update_call)
                    return [char_buf_lim(str(attempt_self_update).split(' ')[1]), return_value, "UpdaterLaunchErr"]
                else:
                    sys.exit()
            # return [char_buf_lim(str(attempt_self_update).split(' ')[1]), return_value, "MasterError"]
        else:
            print(glob.glob(f"{temp_directory}*.*"))
            return [char_buf_lim(str(attempt_self_update).split(' ')[1]), return_value, "DirectoryError"]


def download_ver_file():  # Retrieve the most recent version file from the Github Repo
    """
    :param data:
    :param versions_ver:
    :param versions_loc:
    :param versions_remote:
    :arg versions | The URL to the versions.txt file
    """
    return_value = []
    try:
        with urllib3.PoolManager().request('GET', f"{versions}", preload_content=False) as down_data, open(f"{data_directory}{versions_ver}", 'wb+') as output_file:  # Download the versions file into memory and dump it into an external file
            shutil.copyfileobj(down_data, output_file)  # Copy downloaded file out of memory and to solid storage
            try:
                size_file = 1
            except:
                return [char_buf_lim(str(download_ver_file).split(' ')[1]), return_value, "GetSizeFail"]
            if size_file > 0:
                pass
            else:
                return_value.append(size_file)
                return [char_buf_lim(str(download_ver_file).split(' ')[1]), return_value, "DownloadEmpty"]
            move_download = subprocess.call(f"move {versions_ver} {data_directory}{versions_loc}")
            if move_download != 0:
                return_value.append(move_download)
                return [char_buf_lim(str(download_ver_file).split(' ')[1]), return_value, "MoveFail"]
            # os.system(f"move {versions_ver} {data}{versions_loc}")  # Replace old versions file
        #     output_file.close()  # Clear file from memory
        # try:
        #     size_file = os.path.getsize()
        # except:
        #     return [char_buf_lim(str(download_ver_file()).split(' ')[1]), return_value, "FileNotFound"]
        return [char_buf_lim(str(download_ver_file).split(' ')[1]), return_value, "DownloadPushed"]
    except:
        return_value.append("URLLIB3")
        return [char_buf_lim(str(download_ver_file).split(' ')[1]), return_value, "ExceedTries"]


def create_shortcut_url(application=None, icon=None):  # Create a desktop  shortcut via the URL file method
    """
    :param icon: The location of the icon file, however, this usually does not work; Reason being a windows bug
    :arg application | Name of the application that the shortcut is being created
    :var home | User home directory, used to extract Desktop and as a point of reference for where the application is stored
    :var desktop | The user Desktop as set in environment
    :var clean_home | Convert the back slashes to regular slashes so it works like a URL
    """
    return_value = []
    desktop = os.path.expanduser("~\\Desktop")  # Grab user desktop path, doesn't quite work if they have Desktop located in OneDrive folder
    icon = f"{root}{icon}.ico"
    try:
        with open(f"{desktop}\\{application}.url", 'w+') as url_short:
            clean_home = home.replace("\\", "/")
            url_short.write(f"[InternetShortcut]\nURL=file:///{clean_home}/{application}\nIconFile={root}\\{icon}.ico")  # Create the shortcut file, use URL instead of .lnk for ease
            url_short.close()
        return [char_buf_lim(str(create_shortcut_url).split(' ')[1]), return_value, "URLCreated"]
    except FileNotFoundError:
        return [char_buf_lim(str(create_shortcut_url).split(' ')[1]), return_value, "URLCreationError"]


def hash_template(file=None):  # Do not exceed 4 GB or memory will overflow, memory safety not added!
    return_value = []
    try:
        file_ = open(file, 'rb').read()
    except:
        return [char_buf_lim(str(hash_template).split(' ')[1]), return_value, "FileReadError"]
    try:
        file_hash = hashlib.sha512().update(file_).hexdigest()
    except:
        return [char_buf_lim(str(hash_template).split(' ')[1]), return_value, "HashingError"]
    return_value.append(file_hash)
    return [char_buf_lim(str(hash_template).split(' ')[1]), return_value, "HashReturned"]


def comp_template(applications=None, hashes=None):
    return_value = []
    try:
        hashes_ = json.load(hashes)
    except:
        return [char_buf_lim(str(comp_template).split(' ')[1]), return_value, "FileLoadError"]
    for app in applications:
        if hashes_(f"{app}") == hash_template(app)[1][0]:
            pass
            # return [char_buf_lim(str(test_function2).split(' ')[1], return_value, status]
        else:
            return_value.append(app)
            return [char_buf_lim(str(test_function2).split(' ')[1]), return_value, "HashMismatch"]
    return [char_buf_lim(str(comp_template).split(' ')[1]), return_value, "HashesMatch"]  # Here we would copy back the old file or download again


def test_function(other, this="that"):  # Debug function used for testing logging
    import secrets
    return_values = []
    value = 0.3 * 2000.0 / 1293012
    status = secrets.choice(["SuccessProcess", "Failure", "ThisIsWayTooFingLong"])
    return_values.append(value)
    return [char_buf_lim(str(test_function).split(' ')[1]), return_values, status]


def test_function2(arg1):
    return_values = [arg1]
    return [char_buf_lim(str(test_function2).split(' ')[1]), return_values, "ReturnStatus"]


def char_buf_lim(returned_value, spacing=20):
    """
    :param spacing: Spacing of characters to adhere to the log method
    :param returned_value: The error value return in string format, may be success but needs filtering
    :var init_len: The length of the string value returned by a process
    :return: Formatted string with length determined by below (Default: 20)
    """
    init_len = len(returned_value)
    if init_len != spacing:  # Check if the string is not 20 Char long
        if init_len > spacing:  # If greater, cut it
            out = returned_value[:spacing]  # No longer than determined value
            return out
        else:  # Add spacing to assure it is 20
            out = returned_value + (" " * (spacing - init_len))
            return out
    else:  # Return okay value
        return returned_value


def logging_agent(function=None, data=data_directory, home=home):
    """
    :param function: The function to be logged
    :param data: The data directory that the log file will be kept in
    :param home: $HOME; simply used to extract a user name to determine who to speak with and contact of error
    :var current_date: The current date the log was called
    :var current_time: The current time the log was called
    :var user: The extracted user name from the $HOME directory
    :var values: The actual error or success string to be pushed to log, formatted.
    :return: Does not return value, writes to file instead
    """
    current_date = str(datetime.date.today())
    current_time = str(datetime.datetime.now().strftime("%H:%M:%S"))
    user = home.split('\\')[-1]
    with open(f"{data}log.txt", 'a+') as logging:  # Open pre-existing log file, included in zip
        try:
            values = char_buf_lim(str(function[-1]))
        except:
            values = "ERROR"
        try:
            funct_name = str(function[0])
        except:
            funct_name = "ERROR"
        logging.write(f"{char_buf_lim(current_date, 10)} {char_buf_lim(current_time, 8)} : {funct_name} {values} | {user}\n")  # Flush to log
    return function


logging_agent(attempt_self_update())

