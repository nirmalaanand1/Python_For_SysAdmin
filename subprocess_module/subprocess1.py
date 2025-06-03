import subprocess
import shlex
import sys

def run_command(command):
    """Execute a shell command and stream output live"""
    print(f"`\n Running: {command}")
    process = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    for line in process.stdout:
        print(line.strip())
    process.wait()
    if process.returncode != 0:
        print(f"command failed with exit code {process.returncode}")
    return process.returncode

def check_git_status():
    print(f"`\n Git Status")
    run_command("git status")

def check_disk_usage():
    print(f"\n Disk Usage")
    run_command("df -h")

def ping_host(host="google.com"):
    print(f"\n Pinging {host}...")
    result = subprocess.run(["ping","-c","1","host"],capture_output=True, text=True)
    if result.returncode == 0:
        print("Host Rechable")
    else:
        print("Host Unreachable")

def restart_service(service="ngnix"):
    print(f"Restarting {service}")
    run_command(f"sudo systemctl restart {service}")

def terraform_plan():
    print("\n Running Terraform Plan:.. ")
    run_command("terraform init")
    run_command("terraform plan")

def azure_resource_list():
    print("\n Listing Azure resource list")
    run_command("az group list --output table")

def main():
    print("====DevOps Utimlity Tools=====")
    print("Choose and option:")
    print("1. Check Git Status")
    print("2. Check Disk Usage")
    print("3. Ping a Host")
    print("4. Restart a System Service")
    print("5. Run Terraform Plan")
    print("6. List Azure Resource Groups")
    print("0. Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":
        check_git_status()
    elif choice =="2":
        check_git_status()
    elif choice =="3":
        ping_host()
    elif choice =="4":
        restart_service()
    elif choice == "5":
        terraform_plan()
    elif choice == "6":
        azure_resource_list()
    elif choice == "0":
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice")

if __name__=="__main__":
    main()