import os
import psutil


class DiskInfoMenu:
    @staticmethod
    def get_disk_info():
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue

            usage = psutil.disk_usage(part.mountpoint)

            print("device:", part.device)
            print("total:", usage.total)
            print("used:", usage.used)
            print("free:", usage.free)
            print("percent:", usage.percent)
            print("fstype:", part.fstype)
            print("mountpoint:", part.mountpoint)
            print()

        input()
