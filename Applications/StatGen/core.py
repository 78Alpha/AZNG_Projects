import encrypt_manager
import fileprocessor
import hash_manager
import network_manager
import timekeeper
from hash_manager import compare_password

enc3 = {'drive_by_floor': [
            b'9z2OhyC13pHxs/6y+/Zh0yMW2u6WaJ7ea6uJP4F8R/kwzUEUvmRag9PA+ryGTOAvF3OXgDJPuiLP4qOpYwLo5XQ2ZTp/balNz7wk7UQctvk=',
            'Site', b'1c+6iDJo12kl3umqtbivjTUf2O4yjfUoeMX13yj803w=', 'Start_Date',
            b'F+0GaRwtFbdI2uTMO9JS3jH4u7Wrj9DmwCR0v1klHwQ=', 'Start_Time',
            b'e7Rfvri6WclsCXs3PV9Pj6dl1/FQoEPN5kTP9E60K3w=', 'End_Date',
            b'dttvbmbnYeWGbP7Zd0WODidzFZgJajvSswRJSqLNqXI=', 'End_Time',
            b'XYIBJVPa8TkmiDs3HUga/LkvW//YrYT32DgbNxslimGsbhNSPWSxG3MOyrGDrAn+kzJzybZ4s7b7DqX7xOPOJcAtNsbmqUgkPXFPUfu1MdeT5LOKUfLFYsKCHjPFFMoj2IUYy42tzXEOLSiK6WUgqsbyBeCb1NcoHyEfN7sFDrI=',
            'Time_Zone', b'qDdWgkCmseKKgcWVcgUUTH2i3GUdu2mYzQHiNspO9VOzNb/lB0EOx2ENmF+gBZjo'],
    'floor_by_floor': [
        b'xbZagnSu3xp0y963sqgEk3DyhF2lUvIvX4VjPC0ZVN0cSUCqG5oSKJnjFWO/tG3V6S6YXEKslT45lQZlgLVbybd6MTSJBbds9Cp+OerdGXk=',
        'End_Date', b'iq4fX8rUnNand7ptYl3p1+BAt8AN+5epwlCZCD657uQ=', 'End_Time',
        b'0R/lOKxLpiGpb3kAXWCwDIRb831rp0VVdUnZ8hvh0Bg=', 'Start_Date', b'gK6Oi5rzetqGBBvc2yfA6CaZGJfo/FgQG6Ro94LgCtE=',
        'Start_Time',
        b'DNLX+LLoofpRbqk8AscvIp147E95sdB28KwcVjXGhIeeTCuLxaWNubK0Igg+/5sLoIloH5cIK1md4pFn2tSaVRZspBpWlMnWrr8SdDRSBMT0r4+/e/nidywKzDnsECfa',
        'Site', b'ic3HhsQPzzh27OwKmgQVwTCyYOTrSMPG5i2jHmzr+YWjS7+qYrpGMxxgQPLz9zwUs5J5y/GziezQPdg+Q+u/qg==',
        'Time_Zone', b'LfU52MCkqcVjPxk5SRt9IM6tNZdKRcI3NQPq5KLNzlKSnsfoOUYCC+8vB80bXpgc'],
    'drive_by_user': [
        b'eGAFFNWV+9rwmlBSWbU0xni8ahTbl90mRhbheJzsv2vhy+HDSDdyUM93604rfaXoy0D7s+14O5ZFUPEHZrqUhiJDIWnPZeFYJZAR2+DL+bk=',
        'Site', b'j/oI2nB3+5n3xS00V5zlF6aQlWdcO1L+Lg4PXHpmX20=', 'Start_Date',
        b'ffj+ncc3FaUWLB1gLNjk9DN8kyP6972lyzhcFdbcqWE=', 'Start_Time', b'lZkOXoukUXI+Ils5l0y+WuMeUX8mXPSLYTdImqBgvQg=',
        'End_Date', b'jvKuPX6OsmjRcUK0NFrNIP9nNLszDouNSGczIHy+WyA=', 'End_Time',
        b'4fSTDqDA9i+TcaJ8Rol6OKutZpBMaWbDIguHNJL7hcoWiky5vhWCLIdCFxYV9fmrMfljel9HhicvbZ6aaPP/e2frYXRLDVcTMzF57IvSRxxtAz4oJNVAtL/ghg372lBHKz79yEnhkC7sb6lbOoMVpmi4bwZI/8Bi5ILaFDtvtf8=',
        'Time_Zone', b'WMPoWjaT0DpBjHyJnQR2CZUbMzkOPUptkL5JykNjGKz1ppgGFFcjV/x4PPzQycIM'],
    'floor_by_user': [
        b'GtfWpKZH9uNU6bVi6/Rudb59oersPnMSfJx4MwYlww5fNv/Eru6G162xO3ztJbMR0cBRwM34AFrEGmtv6u73cbkW9317//k53GsHQ4Ymac4=',
        'Site', b'xqf0M87MAZ+VxSWDWQ42couR7O4WijT6D8oqqDqIZrg=', 'Start_Date',
        b'wX3Y6NaIedhR7SjlJTfCyq5Zr+gzxdDk2e6SEpXkB5Y=', 'Start_Time', b'sjDJKWgVXooZnVXy1rWTbJ+M0rxuUM1lFlHJAQAUORo=',
        'End_Date', b'iN/IF2BFYCvQuKbSlrE7owjrVJmbROJvAu46EPGr1z8=', 'End_Time',
        b'HlxfiSi/hRxaOOfxx0Yk8K7Kutl7kowvDy3coypG9KGzca2ybhGDHah12xQjpJpax+SIN3H1vq9mU554w4ofBAVikoJ1hE4LUbZsKTWMAx4Po4OXVvJvBy43dLNk5XXgUWzfOfeWpviq8cgf1NLxdaaIiT0o0CPGUD/5+N6crZ0=',
        'Time_Zone', b'0qIyoSVsZGm8GNLQ2+O0NsqkexWnI9kvxZHTGqpEFQ7KcjhvjjaJ0YYjDDgm7z8d'],
    'gaps_by_floor': [
        b'/APX6ts/ZE5+VvPVOcTlS+5MHLT0jmsiTy+XJUyrWvPr3jGzq0qwZxmQgfZ9t11Qvr1WkaoNnNa1PKsuvE6Iuoi6g59PibjaXBtFhptj84Y=',
        'Site', b'ogEQZpxQGKc7irmIM4XRsorc0GYk5CCaxYuja12KJ3W8bPZLV0E/+xIixaag/4CK9EVKAPCVE2WUghalx1i09g==',
        'Start_Date', b'V562dqI1IpRM2uZbDL820Gzz+e7LasxPamkGKPFk72g=', 'Start_Time',
        b'289lo9QPR9OaV3d6SEIZyHFbBO66SuEW16kTyZZb2s0=', 'End_Date', b'gLo0Mjv2WC7Z9tjU/8/abQ0q3qdeefOlHB8E8o41/rI=',
        'End_Time',
        b'C35FDMLoDACZlzDcK0DJ1TY3TcObNJoI+L7dNGdJDUZCOW6bzGIwEiRLKz/V+VsIhV536ebWrlMgZz7aCYBr02Q8KmJPA1yUn8SwgSwmWFD3IfqjfXS+oT8dUlJ0/iIdotIQmEGtV673VuhYAghOCafetRh/Hn5D0Hzae8gzoZk=',
        'Time_Zone', b'Hca3fVpVcRiea6waKaDTgYAYlFqBgltunqHo9vxjomIhp/EtIwWYiShZlZJ/wxIu'],
    'station_by_user': [
        b'SGftpHiivwwu1SVf0EHYeOAysQA3LFae8mbbMtfFoJLiogDRAOTyLeNPIEQXuHKkgzGN0CH0yjZGNte+NE68lBYprcBwKbp5F0MsVdJsH2M=',
        'Site', b'khwR1tIsuJBG8vf7dORM8ES7LLtKLy5xChMrCnY3xhQ=', 'Start_Date',
        b'1x8rAV7ipK2k8lM3JxyfNhXDtsNvTAtmMtGw/tN6vp8=', 'Start_Time', b'V5miILVpzFd5Je5vaahBCgAm7F+uZ0J0dIiTaDGf9Nw=',
        'End_Date', b'b23ez1hQ9ukj3wKnlNlvVFwZGe6KP5G6omkv5rRWHtM=', 'End_Time',
        b'Z1Je775sV7Hz1XVzsvsqoNVeekfYlVl8/PPfDQyZTooryx7MhGGX8key7/8vgri/OnowIlZPPlZ+KaKQkbUXxpMoc4U3loRBccCJhuG665z2wxaRGUCmdYNqIk4UsrIyfof4+qRAhHkWsrF2RNhXW3sxJ2okOzsZOksvjM19a7c=',
        'Time_Zone', b'xQygoSbeiFu/GWU5Akwy7o6nIRn1NRfZrd4wVmvCU+gDWdGVxCbtGbmfpgX64Vej']}

def run_stats(config_):
    try:
        fileprocessor.delete_old_files()
    except:
        return "File Delete Failed! Close Open CSV Files!"
    try:
        start_date, end_date, start_time, end_time = timekeeper.convert_time(start_time=config_["SOS"], end_time=config_["EOS"], time_zone=config_["Timezone"])
    except:
        return "Time Fields Unfulfilled Or Non-Existant!"
    try:
        links = network_manager.link_constructor(start_date=start_date, end_date=end_date, start_time=start_time, end_time=end_time, site=config_["Site"], password=config_["Password"], time_zone=config_["Timezone"], enc3=enc3)
        # print(links)
    except:
        return "Link Construction Failed!"
    try:
        link_data = network_manager.link_open(links)
        # print(link_data)
    except:
        return "Browser Open Failed"
    try:
        fileprocessor.stat_file_gen(link_data)
    except:
        return "Stat File Generation Failed!"
    try:
        fileprocessor.open_stats()
    except:
        return "Failed to Open Stats File!"
    return "Success"

def save_config(config_):
    try:
        fileprocessor.save_config(config_, time_bit=timekeeper.time_name())
        return "Success"
    except:
        return "Failed to Save Config File!"

def load_config(file_):
    try:
        config_ = fileprocessor.load_config(file_)
        # print(type(config_))
        if config_ is False or type(config_) is not dict:
            return "Config File Is Not Valid!"
        return config_
    except:
        return "Failed to Load Config File!"

def check_default():
    try:
        result, default = fileprocessor.check_default()
        if result:
            config_ = fileprocessor.load_config(default)
            return config_
        else:
            return None
    except:
        return "Failed to Check Default!"

def read_configs():
    try:
        result = fileprocessor.read_configs()
        # print(result)
        return result
    except:
        return "Failed to Read Configs!"

def pass_check(config_):
    try:
        result = hash_manager.compare_password(config_["Password"])
        return result
    except:
        return "Password Incorrect!"
