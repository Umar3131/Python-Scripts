#___________--System Organization--___________________

import os
import psutil  

def remove_temp_files(temp_dir):
    try:
        if os.path.exists(temp_dir):
            for file_name in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, file_name)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  
                        print(f"Deleted file: {file_path}")
                    elif os.path.isdir(file_path):
                        os.rmdir(file_path)  
                        print(f"Deleted directory: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
        else:
            print(f"Directory {temp_dir} does not exist.")
    except Exception as e:
        print(f"Error: {e}")


def log_disk_usage(log_file):
    try:
        usage = psutil.disk_usage('/')  
        with open(log_file, 'a') as f:
            f.write(f"Total: {usage.total / (1024 ** 3):.2f} GB, "
                    f"Used: {usage.used / (1024 ** 3):.2f} GB, "
                    f"Free: {usage.free / (1024 ** 3):.2f} GB, "
                    f"Percent Used: {usage.percent}%\n")
        print(f"Disk usage logged in {log_file}")
    except Exception as e:
        print(f"Error logging disk usage: {e}")

if __name__ == '__main__':
    temp_dir = r'C:\Users\HP\Desktop\TestTemp'  
    log_file = 'disk_usage_log.txt'  

    
    remove_temp_files(temp_dir)

    log_disk_usage(log_file)
