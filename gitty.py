from datetime import datetime
import git
import os

def create_commit_on_date(repo, commit_date, commit_message="Enter Message Here"):
    
    
    
    
    repo.index.commit(commit_message, author_date=commit_date, commit_date=commit_date)

def main():
    repo_url = input("Enter the github repo URL: ")
    local_path = input("Enter the local path: ")
    token = input("Enter the Personal Access Token: ")
    commit_date_str = input("Enter the commit date (YYYY-MM-DD HH:MM:SS): ")

    repo_url_with_token = repo_url.replace('https://', f'https://{token}@')

    if not os.path.exists(local_path):
        repo = git.Repo.clone_from(repo_url_with_token, local_path)
    else:
        repo = git.Repo(local_path)

    try:
        commit_date = datetime.strptime(commit_date_str, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
        return

    print(f"Creating commit for: {commit_date}")
    create_commit_on_date(repo, commit_date)

    origin = repo.remote(name='origin')
    origin.push()
    print("Finished creating the backdated commit.")

if __name__ == "__main__":
    main()
