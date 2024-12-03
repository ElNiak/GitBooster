# 🚀 GitBooster

[![Upload Python Package](https://github.com/ElNiak/GitBooster/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ElNiak/GitBooster/actions/workflows/python-publish.yml)
[![Pylint](https://github.com/ElNiak/GitBooster/actions/workflows/pylint.yml/badge.svg)](https://github.com/ElNiak/GitBooster/actions/workflows/pylint.yml)
[![Python application](https://github.com/ElNiak/GitBooster/actions/workflows/python-app.yml/badge.svg)](https://github.com/ElNiak/GitBooster/actions/workflows/python-app.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/67da47ea926743e1b5dce0af09b9ed57)](https://app.codacy.com/gh/ElNiak/GitBooster/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

**GitBooster** is a Python-powered automation tool designed to keep your GitHub activity graph green by automatically modifying files, committing changes, and pushing them to your repositories. With seamless scheduling via cron jobs, GitBooster ensures your contributions remain consistent, all while being easy to configure and use.

---

## 🌟 Features

- **Automated File Updates**: Randomly appends updates to a file in your repository.
- **Dynamic Commit Messages**: Choose from a list of customizable commit messages.
- **Automatic Scheduling**: Set up cron jobs directly from the script for periodic execution.
- **Fully Configurable**: Easily manage repository path, file, commit messages, and schedule with command-line arguments.

---

## 🚀 Getting Started

### Prerequisites

1. **Install Python** (3.6 or higher)
2. (a) Install the required Python libraries:

```bash
python3 -m venv .venv
source .venv/bin/activate
python setup.py install
```

2. (b) Install from pip:

```bash
python3 -m  pip install gitbooster
```

3. Create a Repository:
   It is strongly recommended to use a dummy repository for testing and automation to avoid cluttering important repositories.
   Example:

```bash
git init dummy-repo
cd dummy-repo
echo "Initial commit" > README.md
git add README.md
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/dummy-repo.git
git push -u origin main
```

- Build the package:
    
```bash
rm -rf build dist *.egg-info;
python setup.py sdist bdist_wheel;
pip install dist/GitBooster-0.0.1-py3-none-any.whl;
```

### Usage

1. *Run the Script Manually*: Modify a file, commit, and push the changes:

```bash
python3 gitbooster.py --repo-path /path/to/repo --file-to-modify activity_file.txt
```

2. *Schedule the Script*: Add a cron job to automate the script execution:

```bash
python3 gitbooster.py --repo-path /path/to/repo --file-to-modify activity_file.txt --setup-cron --schedule daily
```

 3. *Customize Commit Messages*: Use your own list of commit messages:

```bash
python3 gitbooster.py --repo-path /path/to/repo --file-to-modify activity_file.txt --commit-messages "Boosted activity" "Automation is awesome" "Another automated commit"
```

### 🔧 Arguments

| Argument            | Type      | Default            | Description                                                                                     |
|---------------------|-----------|--------------------|-------------------------------------------------------------------------------------------------|
| `--repo-path`       | String    | **Required**       | Path to your local GitHub repository.                                                          |
| `--file-to-modify`  | String    | **Required**       | Name of the file to modify within the repository.                                              |
| `--commit-messages` | List      | Random messages    | List of commit messages to randomly choose from.                                               |
| `--setup-cron`      | Flag      | `False`            | If set, the script will schedule itself in the crontab.                                        |
| `--remove-cron`     | Flag      | `False`            | If set, the script will remove itself in the crontab.                                          |
| `--schedule`        | String    | `every3hours`      | Frequency for scheduling (`hourly`, `daily`, or `every3hours`).                                |
| `--user`            | String        | `username`         | If set, use this user (no check) for the cronjob, else it uses the logged user              |


### Example

```bash
cd GitBooster/;
python3 -m -pip install gitbooster;
gitbooster --repo-path $PWD/. --file-to-modify activity_file.txt --commit-messages "Boosted activity" "Automation is awesome" "Another automated commit" --setup-cron --schedule daily
```

```bash
Modifying file: /home/ElNiak/Documents/Projects/GitBooster/./activity_file.txt
Ensured directories exist for: /home/ElNiak/Documents/Projects/GitBooster/./activity_file.txt
Appended modification: 
Automated update at 2024-12-03 09:57:17.438760
Committing and pushing changes in repo: /home/ElNiak/Documents/Projects/GitBooster/.
Repository has changes.
Changes added to staging area.
Committed changes with message: Automation is awesome
Changes pushed to remote repository: Automation is awesome
Scheduling cron job for user: ElNiak
Created new cron job: * * * * * python3 /home/ElNiak/Documents/Projects/GitBooster/gitbooster/gitbooster.py
Set job frequency to daily.
Cron job scheduled with frequency: daily
```

 
### 🎯 Why Use GitBooster?

1. 🕒 Save Time: No need to manually make changes or push updates.
2. 📈 Boost GitHub Stats: Keep your contribution graph consistently green.
3. 🔄 Fully Automated: Set it and forget it with cron scheduling.

### 💡 Future Enhancements

- Add support for multiple file modifications.
- Support for custom time schedules.
- Integration with GitHub API for real-time repository insights.
- Automated github repository creation.
