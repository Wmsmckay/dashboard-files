import subprocess

def find_device():
    output = subprocess.check_output(['lsusb']).decode('utf-8')
    if '0079:0006' in output:
        print('Arcade buttons found!')
    else:
        raise ValueError('Device not found')

if __name__ == '__main__':
    find_device()
