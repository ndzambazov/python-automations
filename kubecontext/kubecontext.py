import yaml
import sys
import os


kubeconfig_file = os.path.join(os.path.expanduser("~"), ".kube/config")

def color(style,content):
    orange_color = "\033[38;5;208m"
    red_color = "\033[1;31m"
    green_color = "\033[1;32m"
    reset_color = "\033[0m"

    if style == "ERROR":
        print(f"{red_color}ERROR: {content} {reset_color}")
    elif style == "WARNING":
        print(f"{orange_color}WARNING: {content} {reset_color}")
    elif style == "INFO":
        print(f"{green_color}INFO: {content} {reset_color}")


def get_context():
    get_context = "kubectl config get-contexts"
    output = os.popen(get_context).read()
    highlight_output = ""
    for line in output.splitlines():
        if line.startswith("*"):
            highlight_output += f"\033[30;1m\033[47m{line}\033[0m\n"
        elif "CURRENT" in line:
            highlight_output += f"\033[1;1m{line}\033[0m\n"
        else:
            highlight_output += f"\033[2;1m{line}\033[0m\n"
    print(highlight_output)


def load_yaml(filepath):
    try:
        with open(filepath, "r") as f:
            data = yaml.safe_load(f)
            return data
    except FileNotFoundError:
        color("WARNING", "File doesnt exist ..")
        exit(1)
    except Exception as e:
        print(e)


def set_kube_context(context_name):
    set_context = f"kubectl config use-context {context_name}"
    os.system(set_context)
    get_context()


parsed_yaml = load_yaml(kubeconfig_file)
names = [context['name'] for context in parsed_yaml['contexts']]

if len(sys.argv) > 1:
    arg_context_name = sys.argv[1]
    print(names)
    if arg_context_name in names:
        color("INFO", f"Setting Kubernetes context to {arg_context_name}...")
        set_kube_context(arg_context_name)
    else:
        color("ERROR", f"Context {arg_context_name} not found in the YAML file.")
        get_context()

else:
    color("ERROR", "No context name provided. Please choose from the following")
    get_context()
