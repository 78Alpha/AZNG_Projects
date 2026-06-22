import webbrowser

import encrypt_manager
import fileprocessor


def link_constructor(start_date=315, end_date=221, start_time=2211, end_time=444, site="PDX9", password="wrong", time_zone="America/Los_Angeles",
                     enc3=None):
 if enc3 is None:
     enc3 = {}
 config_list = ["Start_Time", "End_Time", "Site", "Start_Date", "End_Date", "Time_Zone"]
 config_dict = {"Start_Time": start_time, "End_Time": end_time, "Site": site, "Start_Date": start_date, "End_Date": end_date, "Time_Zone": time_zone}



 constructed_links = {}
 for key, value in enc3.items():
  temp_link = ""
  for segment in value:
   if segment not in config_list:
    enc = encrypt_manager.AESCipher(password).decrypt(segment)
    temp_link += str(enc)
   elif segment in config_list and segment == "Site":
    temp_link += f"({config_dict[segment]})"
   else:
    temp_link += str(config_dict[segment])
  constructed_links[key] = temp_link
 return constructed_links

def link_open(links):
 link_data = {}
 for key, value in links.items():
  webbrowser.open_new_tab(value)
  fileprocessor.prepare_udq(key)
  link_data[key] = ""
 return link_data

