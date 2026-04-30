### WHEN A PROJECT IS NEW
- On github.com - create a repository
a. Provide the repository name
b. Set the privacy
c. Get your repo url on creation


- Start git process from project terminal
1. initializing the git folder
2. connect local project to repo url: git remote add origin <url>
3. Initial adding of files
4. make commit : git commit -m "write a commit msg"
5. Ensure you have a password token to allow push
6. push using token via this command
git push origin master
where master is referencing the default branch where work will be saved

### Incase the push doesnt work based off permissions
- select project saving location - open terminal here 
- gh auth logout
- gh auth login

after login proceed to do push

### to get project on a new device
- select project saving location - open terminal here
- git clone linktorepo

### To update project repo
- git add .
- git commit -m "commit msg here"
- git push -u origin master/main
