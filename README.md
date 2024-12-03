# 🚀 GitBooster

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
2. Install the required Python libraries:

```bash
python3 -m venv .venv
source .venv/bin/activate
python setup.py install
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
python setup.py sdist bdist_wheel
```

### Usage

- 1️⃣ *Run the Script Manually*: Modify a file, commit, and push the changes:

```bash
python3 gitbooster.py --repo-path /path/to/repo --file-to-modify activity_file.txt
```

- 2️⃣ *Schedule the Script*: Add a cron job to automate the script execution:

```bash
python3 gitbooster.py --repo-path /path/to/repo --file-to-modify activity_file.txt --setup-cron --schedule daily
```

- 3️⃣ *Customize Commit Messages*: Use your own list of commit messages:

```bash
python3 gitbooster.py --repo-path /path/to/repo --file-to-modify activity_file.txt --commit-messages "Boosted activity" "Automation is awesome" "Another automated commit"
```

#### 🔧 Arguments

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
python3 gitbooster/gitbooster.py --repo-path $PWD/. --file-to-modify activity_file.txt --commit-messages "Boosted activity" "Automation is awesome" "Another automated commit" --setup-cron --schedule daily
```

 
### 🎯 Why Use GitBooster?

1. 🕒 Save Time: No need to manually make changes or push updates.
2. 📈 Boost GitHub Stats: Keep your contribution graph consistently green.
3. 🔄 Fully Automated: Set it and forget it with cron scheduling.

### 💡 Future Enhancements

- Add support for multiple file modifications.
- Support for custom time schedules.
- Integration with GitHub API for real-time repository insights.

### 📜 License
