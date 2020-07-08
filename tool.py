import sys
from jinja2 import Environment, FileSystemLoader


def main():
    with open("workplan.txt", "w+") as workplan:
        workplan.writelines(build_template())

def get_real():
    real_ip_list = []
    if "win32" in sys.platform:
        real_location = ".\\nat_files\\real.txt"
    elif "darwin" in sys.platform:
        real_location = ".//nat_files/real.txt"
    with open(real_location, "r") as real_file:
        for real in real_file:
            real_ip_list.append(real.strip('\n'))
        return list(filter(None, real_ip_list))
        

def get_nat():
    nat_ip_list = []
    if "win32" in sys.platform:
        nat_location = ".\\nat_files\\nat.txt"
    elif "darwin" in sys.platform:
        nat_location = ".//nat_files/nat.txt"
    with open(nat_location, "r") as nat_file:
        for nat in nat_file:
            nat_ip_list.append(nat.strip('\n'))
        return list(filter(None, nat_ip_list))

def build_template():
    real_list = get_real()
    nat_list = get_nat()
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template("asa_nat_template.jinja2")
    output = template.render(checks_list=zip(real_list, nat_list),
                             nat_ip=nat_list[0], verify_list=zip(real_list, nat_list),
                             backout_list=zip(real_list, nat_list))
    return output

if __name__ == "__main__":
    main()
