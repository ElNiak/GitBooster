# script/git_auto_committer.py
import os
import random
import datetime
import argparse
from git import Repo
from crontab import CronTab

def modify_file(repo_path, file_to_modify):
    """Modify the specified file with a random line."""
    file_path = os.path.join(repo_path, file_to_modify)
    
    # Ensure the file is inside the repository folder
    if not os.path.commonpath([repo_path]) == os.path.commonpath([repo_path, file_path]):
        raise ValueError("The file to modify must be inside the repository folder.")
    
    # Create subdirectories if they do not exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Create the file if it does not exist and append the modification
    with open(file_path, 'a') as file:
        file.write(f"\nAutomated update at {datetime.datetime.now()}")

def commit_and_push(repo_path, commit_messages):
    """Commit and push changes to the repository."""
    repo = Repo(repo_path)
    if repo.is_dirty(untracked_files=True):
        # Add changes to the staging area
        repo.git.add(A=True)
        # Commit changes
        commit_message = random.choice(commit_messages)
        repo.index.commit(commit_message)
        # Push changes
        origin = repo.remote(name='origin')
        origin.push()
        print(f"Changes pushed: {commit_message}")
    else:
        print("No changes to commit.")

def schedule_cron_job(script_path, frequency, user=''):
    """Schedule the script in the crontab."""
    if not user:
        user = os.getlogin()
        
    cron = CronTab(user=user)  # Use the current user's crontab

    # Check if the job already exists
    for job in cron:
        if script_path in job.command:
            print("Cron job already exists.")
            return

    # Create a new cron job
    job = cron.new(command=f'python3 {script_path}')
    if frequency == "hourly":
        job.minute.every(60)
    elif frequency == "daily":
        job.hour.every(24)
    elif frequency == "every3hours":
        job.hour.every(3)
    else:
        raise ValueError("Unsupported frequency value")
    
    cron.write()  # Save the crontab
    print(f"Cron job scheduled with frequency: {frequency}")

def remove_cron_job(script_path, user=''):
    """Remove the script's cron job."""
    if not user:
        user = os.getlogin()
    print(f"Attempting to remove cron job for script: {script_path}")
    cron = CronTab(user=True)
    jobs_removed = [job for job in cron if script_path in job.command]
    print(f"Found {len(jobs_removed)} job(s) to remove.")
    for job in jobs_removed:
        print(f"Removing job: {job}")
        cron.remove(job)
    cron.write()
    if jobs_removed:
        print("Cron job(s) removed successfully.")
    else:
        print("No cron job found to remove.")
        
def main():
    """Main function to handle file modification, commit, push, and scheduling."""
    parser = argparse.ArgumentParser(description="Automate GitHub stats by pushing commits to a repository.")
    parser.add_argument(
        '--repo-path', 
        type=str, 
        required=True, 
        help="Path to the local GitHub repository."
    )
    parser.add_argument(
        '--file-to-modify', 
        type=str, 
        required=True, 
        help="File to modify in the repository."
    )
    parser.add_argument(
        '--commit-messages', 
        type=str, 
        nargs='+', 
        default=["Automated update 🚀", "Keeping things active 📈", "Bot-generated commit 🤖", "Random commit for stats 🎯"],
        help="List of commit messages to choose from."
    )
    parser.add_argument(
        '--schedule', 
        type=str, 
        choices=["hourly", "daily", "every3hours"], 
        default="every3hours",
        help="Frequency of running the script automatically (hourly, daily, every3hours)."
    )
    parser.add_argument(
        '--setup-cron', 
        action='store_true', 
        help="If set, the script will schedule itself in the crontab."
    )
    
    parser.add_argument('--remove-cron', action='store_true', help="If set, the script will remove its cron job.")
    
    parser.add_argument(
        '--user', 
        type=str, 
        help="If set, use this user (no check) for the cronjob, else it uses the logged user."
    )
    
    args = parser.parse_args()
    
    assert os.path.exists(args.repo_path), "Repository path does not exist."
    assert args.remove_cron != args.setup_cron, "Choose either --setup-cron or --remove-cron."

    # Modify and push changes
    modify_file(args.repo_path, args.file_to_modify)
    commit_and_push(args.repo_path, args.commit_messages)

    # Optionally schedule the cron job
    if args.remove_cron:
        remove_cron_job(script_path)
    elif args.setup_cron:
        script_path = os.path.abspath(__file__)
        schedule_cron_job(script_path, args.schedule)

if __name__ == "__main__":
    main()
