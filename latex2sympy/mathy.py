# https://mathy.ai
# how to execute command line in terminal by python
# https://stackoverflow.com/questions/89228/calling-an-external-command-in-python
import subprocess


# after running the command,
def run_cmd(cmd):
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    return result.stdout.decode("utf-8").strip()



if __name__ == "__main__":
    exp = "2x^2+3x+4+5x^2+6x+7"
    cmd = 'mathy simplify "' + exp + '"'
    result = run_cmd(cmd)
    print(result)
