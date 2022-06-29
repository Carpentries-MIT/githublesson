#!/usr/bin/env python
# coding: utf-8

# # Version Control with Git and GitHub
# 
# This notebook is to keep the notes for introducing Git and GitHub during the Software Carpentry Workshop (SWC) @ MIT. The content of this introduction is based on the SWC lesson on "[Version Control with Git](http://swcarpentry.github.io/git-novice/)" but we are using the application GitHub Desktop instead of the Git Bash command line. 

# ## Automated Version Control

# ### Purpose
# * Keep track of **what each person did and when** in a project.
# * Go back to and question specific changes as well as "undo" when needed
# * Notify conflict between copies from collaborators and merge changes selectively
# 
# Useful for any digital projects, including software coding, data analysis, visualization, and presenting etc. 

# ![Naming Convention Saga with "Final"](http://swcarpentry.github.io/git-novice/fig/phd101212s.png)

# ### Version control with word processors 
# E.g. Microsoft Word - track changes & Office365/WordOnline; GoogleDoc / Version history, LibreOffice / Recording and Displaying Changes
# 
# * Record progress that can be rewinded to start
# ![Record Changes](http://swcarpentry.github.io/git-novice/fig/play-changes.svg)
# 
# * Two users can make independent sets of changes on the same document
# ![Resulting two sets](http://swcarpentry.github.io/git-novice/fig/versions.svg)
# 
# * Owner can incoporate multiple users' changes to the same base document
# ![Merge changes](http://swcarpentry.github.io/git-novice/fig/merge.svg)

# ## Git, GitHub, GitHub Desktop, and GitHub Enterprise @ MIT
# * **Git** - the open source version control tool on your local computer 
# 
# * **GitHub** - A cloud server hosting Git repositories; can be connected to your local Git repos; Currently owned by Microsoft. https://github.com
# 
# * **GitHub Desktop** -  A desktop application that can simplify your workflow connecting your local repos to GitHub cloud. 
# 
# * **GitHub Enterprise @ MIT** - An instance of GitHub hosted by MIT for MIT students, faculty and staff use. 
# https://github.mit.edu/
# 
# [Read more on GitHub Enterprise @ MIT](https://ist.mit.edu/github-enterprise) 
# 

# ## Setting Up Git and GitHub Desktop

# ### Installing Git and GitHub Desktop
# Make sure you followed the instruction on [our workshop page](https://carpentriesmit.github.io/2021-08-05-mit/) to:
# * Install Git
# * Install GitHub Desktop ([GitHub Help page](https://help.github.com/en/desktop/getting-started-with-github-desktop/installing-github-desktop))
# * Create an account on https://github.com 
# * Share your GitHub account on our course Etherpad top section

# ### Configuring Git
# Configure Git with:
# * your name and email address
# * what our preferred text editor is
# * and that we want to use these settings globally (i.e. for every project). 
# 
# #### Checking Git version
# ```
# $ git --version
# 
# ```
# 
# #### Configuring your identity
# In Git Bash (Windows) or Terminal (Mac), run the following using your own name and email address. These will be associated with any changes you push to GitHub later. 
# 
# ```
#  $ git config --global user.name "Vlad Dracula"
# 
#  $ git config --global user.email "vlad@tran.sylvan.ia"
# ```
# 
# #### Configuring your default text editor
# ```
# # to nano
# $ git config --global core.editor "nano -w"
# 
# # or to Atom if you have it installed
# $ git config --global core.editor "atom --wait"
# 
# ```
# #### Check your settings and get help
# ```
# $ git config --list
# 
# $ git config -h
# 
# $ git config --help
# 
# ```
# 
# It is necessary to configure Git locally before we start using GitHub Desktop to connect to GitHub.

# ### Setting up GitHub Desktop
# 
# Read more on [GitHub Desktop Help](https://help.github.com/en/desktop/getting-started-with-github-desktop/setting-up-github-desktop) 

# ### Authenticating to GitHub in GitHub Desktop
# Use **GitHub Desktop** menu
# * on Mac, Preference --> Accounts --> Sign in GitHub.com with your account
# * on Windows, File --> Options --> Accounts --> Sign in GitHub.com with your account 
# 
# See [here](https://help.github.com/en/desktop/getting-started-with-github-desktop/authenticating-to-github-using-the-browser) for more help if you have configured two-factor authentication for GitHub.

# ### Configuring Git for GitHub Desktop
# Use **GitHub Desktop** menu
# * on Mac, Preference --> Git --> add your name and email
# * on Windows, File --> Options --> Git --> add your name and email
# 
# If you have signed in with your Github.com account when you first open your GitHub Desktop, your Git would have been configured with information from your Github.com account. 

# ## Creating a local repository
# Use **GitHub Desktop**
# * *Create a New Repository on your Hard Drive...*
# Or *File --> New Repository...*
# 
# Fill out the fields in the form and *Create Repository* with:
# * Repo (i.e. folder) name: **planets**
# 
# ![NewRepoFields](./images/CreateRepoGitHubDesktop.png)
# 
# 

# Once you click on *Create Repository*, GitHub Desktop will create a folder at the Local Path you specified and initialize it as a repository (repo). 
# 
# Use the Finder on Mac or File Explorer on Windows to navigate to the folder.
# 
# The repo **planets** now has a README.md file and two hidden files, .gitattributes and .gitignore, as well as one hidden directory .git, where Git stores all its repository data.  
# 
# **Tip**: To toggle display hidden files, 
# * On Mac, Command + Shift + Dot
# * On Windows 10 / 8, from the File Explorer window (shortcut: windows key + E)  choose --> View --> Show/hide --> check Hidden Items.

# ## Tracking Changes using GitHub Desktop
# 
# ### Add a text file
# Create a **mars.txt** file using a plain text editor (e.g. Nano, Notepad++, Atom, Sublime Text etc.. )
# 
# Example: using Bash and Nano to do so. Make sure that you are under the directory **planets**. 
# 
# ```
# $nano mars.txt
# 
# ```

# Type the text below into the **mars.txt** file and save the file
# > Cold and dry, but everything is my favorite color

# After saving the file, look at the GitHub Desktop window. You will see the change highlighted. 
# ![addedmars](./images/AddedMars.png)

# Git now knows that i's supposed to keep track of **mars.txt**, but it hasn’t recorded these changes as a commit yet.
# To do so, type in the following message to the Note and Description areas on the lower bottom of the GitHub Desktop page. 
# > Summary: Create mars.txt
# 
# > Description: Start notes on Mars as a base
# 
# And then, click on the *Commit to main* button

# Good commit messages start with a brief (<50 characters) summary statement about the changes made in the commit. Generally, the message should complete the sentence “If applied, this commit will” . If you want to go into more detail, use the Description field to explain. Use this additional space to explain why you made changes and/or what their impact will be.

# Now, look at the GitHub Desktop, it tells us that there is no local changes and everything is up-to-date. 
# 
# ![aftercommit](./images/AfterCommit.png) 

# ### Tracking edits
# 
# Add more information to **mars.txt**
# 
# > The two moons may be a problem for Wolfman
# 
# ```
# $ nano mars.txt
# $ cat mars.txt
# ```

# When you see the change highlighted on GitHub Desktop window, repeat the *Commit to Main* process above. This time, with the commit message as 
# 
# > Summary: Update mars.txt
# 
# > Description: Add concerns about effects of Mars' moons on Wolfman 

# When you click on the *Commit to Main* button, you move the changes Git tracked at the staging area to the repository as shown in the figure below. 
# 
# ![stagingarea](https://swcarpentry.github.io/git-novice/fig/git-staging-area.svg)

# When you have multiple changes to one file or changes to multiple files, you can select the changes you'd like to group for any given commit. 
# 
# For example, add one more line below to **mars.txt**
# > But the Mummy will appreciate the lack of humidity
# 
# And then, add the following line to **README.md**
# > This is the story of Wolfman and Dracula who are investigating if it is possible to send a planetary lander to Mars.
# 
# Note how you can check and uncheck multiple changes to include or not include for a given commit. 
# 
# ![multiplechanges](./images/MultipleChanges.png)

# First, select mars.txt changes and Commit with the following message:
# 
# > Summary: Update mars.txt
# 
# > Description: Added mummy's concern. 
# 
# Second, select README.md changes and Commit with the following message:
# 
# > Summary: Update README.md
# 
# > Description: Added what the project story is. 
# 
# This process can be illustrated by the following figure:
# ![addmultiple](https://swcarpentry.github.io/git-novice/fig/git-committing.svg)

# ### Tips:
# 
# 1. The **History** tab will show you details of all the commits. You may choose to revert a specific commit with the tool too. But be careful to not creating any conflicts. 
# 
# ![History](./images/History.png)
# 
# 2. Git does not track directories on their own, only files within them. Try make a subfolder **spaceships** and leave it empty. It does not show up on the GitHub Desktop **Changes**. 
# 
# 

# ### Practice
# 1. Under the **spaceships** folder, create a new file **venus.txt** and add your iniital thoughts about Venus as a base for you and your friends
# 1. Now check GitHub Desktop. What change(s) are listed? venus.txt? folder spaceships? Or both? 
# 1. Commit the change with a message. Looking into the history, do you see a separate commit for the folder **spaceships** itself?   

# ## Ignoring Things
# What if we have files that we do not want Git to track for us, like backup files created by our editor or intermediate files created during data analysis?
# 
# You can add those file path and names to the hidden .gitignore file. 
# 
# Open the current .gitignore file under your **planets** repo to examine it. Because we chose the **Git Ignore** for python when we initialized the repo in GitHub Desktop, the list of file names here are those system files Python project often has that you don't need to track. This file tells Git to ignore changes happen to those files. 
# 
# ![gitignorefilepython](./images/gitignorefile.png)
# 

# Different types of programming may have different system files to ignore. Using the tool in GitHub to initialize repos help to create the default for each type of programming. But please check the file to make sure that the files you do want to keep track are not accidently listed here, especially when you observe anything strange. 

# ## Remote into GitHub
# 
# So far, we are doing Version Control on our local computer. In order to collaborate with others and take full advantage of the sophisticated version control features, we need to use hosting services like GitHub, Bitbucket or GitLab to hold the master copies where collaborators could share changes with each other. 
# 
# The relationship between the local Git repo and the remote one can be illustrated as below. 
# ![githubremote](https://swcarpentry.github.io/git-novice/fig/github-repo-after-first-push.svg)

# On GitHub Desktop, you can use the *Publish repository* button post your local repo to GitHub.com or GitHub Enterprise @ MIT, since we have configured our GitHub account into the GitHub Desktop. 
# 
# Note: When publishing to GitHub, you cannot keep a repo private with a free GitHub account. But you can do so if you are using your GitHub Enterprise @ MIT account. 
# 
# ![publishrepo](./images/publishrepo.png)
# 
# 

# Once you successfully published your repo, go to a browser and log onto your account on GitHub.com and take a look at the repository added there. All the files and commit history are synchronized to the remote GitHub repo.
# 
# ![repogithub](./images/RepoOnGitHub.png)

# ### Push changes from local repo to remote repo
# 
# Still use Bash and Nano to add one more line below to **mars.txt**
# 
# > Let's figure out how to get to Mars first 
# 
# Once you saved the change, commit the change to your local repo with the following message. 
# 
# > Summary: Update mars.txt
# 
# > Description: Added the next steps about Mars. 
# 
# Once it's committed, you will see a new option to *Push origin*. Use that to push the changes from your local repo to the remote repo on GitHub.com. Then, check the remote repo to see if the changes appear. You may need to refresh your browser. 
# 
# ![pushchanges](./images/PushChanges.png)
# 

# ### Fetch and pull changes from remote repo to local repo
# 
# On your GitHub.com repo page in the browser, open the README.md file and use the pencil icon (**Edit this file**) tool to add the following sentence to the file. 
# 
# > I made this edit on the remote GitHub repo through web broswer. 
# 
# Use the bottom box to Commit changes with the following message:
# 
# > Summary: Update README.md
# 
# > Description: Added a line to test fetching.
# 
# ![commitweb](./images/CommitChangeWeb.png)

# Once that change is commited, come back to your GitHub Desktop, click on the *Fetch Origin* button. GitHub Desktop will compare the remote and local repos and show you the option to "Pull 1 commit from the origin remote". Click on *Pull origin* to pull the changes from the remote repo to your local repo. 
# 
# ![pullremote](./images/PullRemote.png)

# Now, the local and remote repos are synchronize with all the content and change history. 
# 
# **Tip**: It's a good practice to always *Fetch Origin* and *Pull origin* before you start working on your local repo to avoid any potential conflicts. 
# 

# **Tip**: You may also create a repo under the GitHub.com account in the browser and then configure your local repo to it. See this [link here for the steps](https://swcarpentry.github.io/git-novice/07-github/index.html). 

# ## Collaborating

# <!-- * for in-person class* Now, you all have a repo named **planets** under your GitHub.com account. Let's invite a collaborator to work together on the project.  -->
# 
# The first approach to work collaboratively on a project using GitHub is to invite a collaborator to the project. 

# ### Invite collaborator
# 
# <!-- * for in-person class* Form a two people team with your neighbour in the class to complete the rest of the tasks. One of you will be the **Owner** and another one will be the **Collaborator**. -->
# Your instructors will invite you as collaborators for a practice project. 
# 
# As a project owner, you can give your collaborator access to your repo by clicking on the **Settings** button on the right of your GitHub.com Repo page. You may need to ask your collaborator's GitHub username to find them. 
# 
# ![collaborator](./images/Collaborator.png)

# Collaborator, you need to first accept the invitation from the Owner. There should be an email sent to you with an acceptance button to click on. Or you can look for the invitation at [https://github.com/notifications](https://github.com/notifications) once you are logged in.  

# Now, the Collaborators can access the repo. Note that the repo will still be under the Owner's account. On that repo page, click on the greenbutton *Codes* on the right side. And choose "Open in Desktop". You will be prompted to choose a local path to save this repo. 
# 
# **Caution**: please do not choose the path where you put your own **planets** repo. Instead, create a folder Collaboration first then put the new repo from the Owner under that. 
# 
# ![download](./images/CloneOpen.png)
# 
# 

# The Collaborator may also take the URL or SSH link from the popup window and then use the GitHub Desktop, File --> Clone Repository... to accomplish the same task. 

# The Collaborator can now make a change in her clone of the Owner’s repository, exactly the same way as we’ve been doing before with their own repository. 

# ### Branch
# 
# If you are the owner or have collaborator permissions on a repository, you can create a branch off of the repository's default branch so you can safely experiment with changes. The default branch of a repository is usually the Master branch or Main branch. 
# 
# #### Create a branch
# On the top of the GitHub Desktop, switch to the branch that you want to base the new branch on by clicking the Current Branch and choosing it from the list. For now, it would be just the Main branch. Then, click on New Branch. 
# 
# ![Branchcreate](./images/BranchCreate.png)
# 
# Type the name of the new branch you want to create (e.g. test-YourInitials) and then *Create Branch*. Caution: make sure you use a different name for the new branch from your collaborators to avoid future conflict. 
# 
# ![BranchName](./images/BranchName.png)

# Once the branch is created on the Collaborator's local repo, the Collaborator will see an option to publish it to the remote repo. Please do so and the Owner will see the new branch and new edits committed once the Owner refresh the repo in the browser. 
# 
# The two branches now have the exact same content. But you may add future edits to them separately. They are also connected. Individual commits can be pulled from one branch to another independently. 
# 
# Here is a network graph that may help you understand the concept of branches. The live version can be accessed here. https://github.com/datacarpentry/OpenRefine-ecology-lesson/network
# 
# ![Branchnetwork](./images/BrachNetwork.png)

# ### Practice:
# The Collaborator makes a change to the mars.txt file in the newly created branch and push the change to the Owner's remote repo. The Owner can fetch and pull that change to the Owner's local repo. 
# 
# **TIP**: When you are using GitHub Desktop to switch between branches, the local folder for the repo in your File Explorer or Finder will automatically be switched to that branch. 
# 
# <!-- *for in-person session.* If time allows, exchange your roles as Owner and Collaborator and run the process again. Be careful not to put the repos with same names into the same folder.  -->

# ### Conflicts
# 
# During collaboration, if the Owner and the Collaborator attempted to change the same part of a file at the same time, there can be conflict. The party who pushes the change to the remote repo later will be asked to resolve the conflict. 
# 
# Owner and Collaborator both browse to the same branch of their local copy of the Owner's repo **planets**.
# 
# Owner and Collaborator make changes to the same line of *mars.txt* file on their own computer. And then the Owner push the changes to the remote repo first.
# 
# If the Collaborator changes the same line before fetch/pull the Owner's changes of that line, the Collaborator will see a message about **Conflicts** when the Collaborator tries to push the change to the remote repo. 
# 
# The process can be demonstrated by the figure below. 
# ![conflicts](https://swcarpentry.github.io/git-novice/fig/conflict.svg)
# 
# GitHub Desktop will prompt the Collaborator to resolve the conflicts by merging the changes before the commit can be pushed to the remote repo. 
# 
# An example of conflicts: 
# ```
# Cold and dry, but everything is my favorite color
# The two moons may be a problem for Wolfman
# But the Mummy will appreciate the lack of humidity
# <<<<<<< HEAD
# We added a different line in the other copy
# =======
# This line added to Wolfman's copy
# >>>>>>> dabb4c8c450e8475aee9b14b4383acc99f42af1d
# ```
# 
# Our change is preceded by <<<<<<< HEAD. Git has then inserted ======= as a separator between the conflicting changes and marked the end of the content downloaded from GitHub with >>>>>>>. (The string of letters and digits after that marker identifies the commit we’ve just downloaded.)
# 
# It is now up to us to edit this file to remove these markers and reconcile the changes. We can do anything we want: keep the change made in the local repository, keep the change made in the remote repository, write something new to replace both, or get rid of the change entirely. 
# 
# Remember to delete all the added symbols and separators. 
# 
# Once the changes are merged and saved, you can push the new commit to the remote repo. 
# 

# 
# ### Pull changes between branches
# 
# Once you are ready with the changes made in one branch, you can pull them into another branch. 
# 
# On GitHub Desktop, click on Branch --> Create Pull Request will take you to a web browser page as below. 
# 
# ![pullrequest](./images/PullRequest.png)
# 
# If there is no conflict between the two branches, the Owner will be prompted to Merge pull request to the master branch as below. 
# 
# ![mergepull](./images/mergepull.png)
# 
# Then, the Owner can confirm the merge with a message to explain. 
# ![confirmmerge](./images/ConfirmMerge.png)

# ## Fork
# 
# A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project, and without being added as a collaborator of a public repository.
# 
# 
# ### Fork a public repository
# Here is an example repository for you to Fork. 
# Go to https://github.com/CarpentriesMIT/CO2EmissionPractice  
# 
# Use the top right button to *Fork* the repository. Notice that the content stays the same but the account will be changed from the original owner to yours once the fork is successful. 
# 
# ![forkoption](./images/ForkOptions.png)
# 
# 
# Once it's forked, you can Clone it to your GitHub Desktop as a local copy to edit. 
# 
# Forked repositories are linked to the original repository, often referred to as the upstream repository. 
# 
# When you click on *Fetch Origin* in GitHub Desktop, it will fetch from both the 'origin' and 'upstream' remotes. 
# 
# Under History, when "Select Branch to Compare", you will see the option of comparing with both the "origin" and "upstream" remotes. 
# 
# ![Forkbranchupstream](./images/ForkBranchUpstream.png)
# 
# 
# [Read more on Fork](https://github.community/t5/Support-Protips/Contributing-to-Repositories-with-GitHub-Desktop/ba-p/17712) 
# 
# 
# 
# 

# ### Send pull request to a public repository
# 
# You can use GitHub Desktop, Branch --> Create Pull Request to submit your pull request to the upstream remotes. 
# 
# ### Practice
# 
# Make a change to the "CO2EmissionAnalysis.ipynb" file or the README.md file in the repository you forked earlier. And try to make a pull request to the upstream repo. 
# 
# Read more about [Creating a pull request from a fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork)

# In[ ]:




