import subprocess

if __name__ == '__main__':

    cmd = 'python shell.py'

    proc = subprocess.Popen(
        cmd,
        shell=True
    )
    proc.wait()
    print('finish')
