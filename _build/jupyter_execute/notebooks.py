#!/usr/bin/env python
# coding: utf-8

# # Version Control with Git and GitHub
# 
# This notebook is the lesson plan for introducing Git and GitHub during the Carpentries @ MIT workshop. The content of this introduction is based on the Software Carpentry lesson on "[Version Control with Git](http://swcarpentry.github.io/git-novice/)" but we are using the application GitHub Desktop instead of the Git Bash command line.

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
# * Record progress that can be rewound to start
# ![Record Changes](http://swcarpentry.github.io/git-novice/fig/play-changes.svg)
# 
# * Two users can make independent sets of changes in the same document
# ![Resulting two sets](http://swcarpentry.github.io/git-novice/fig/versions.svg)
# 
# * Owner can incoporate multiple users' changes to the same base document
# ![Merge changes](http://swcarpentry.github.io/git-novice/fig/merge.svg)

# ## Git, GitHub, GitHub Desktop, and GitHub Enterprise @ MIT
# * **Git** - The open source version control tool on your local computer 
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
# Make sure you followed the instructions on [our workshop page](https://carpentriesmit.github.io/2022-08-02-mit-online/) to:
# * Install Git
# * Install GitHub Desktop ([GitHub Desktop Help page](https://help.github.com/en/desktop/getting-started-with-github-desktop/installing-github-desktop))
# * Create an account on https://github.com 
# * Share your GitHub account on our course Etherpad (in the participants name/contact list)

# ### Configuring Git
# Configure Git with:
# * your name and email address
# * our preferred text editor
# * the preference to use these settings globally (i.e for every project)
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
#  $ git config --global user.name "Happy Hiker"
# 
#  $ git config --global user.email "happy.hiker@moun.tai.ns"
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
# * Repo (i.e. folder) name: **hiking**
# 
# ![NewRepoFields](./images/CreateRepoGitHubDesktop.png)
# 
# 

# Once you click on *Create Repository*, GitHub Desktop will create a folder at the Local Path you specified and initialize it as a repository (repo). 
# 
# Use the Finder on Mac or File Explorer on Windows to navigate to the folder.
# 
# The repo **hiking** now has a README.md file and two hidden files, .gitattributes and .gitignore, as well as one hidden directory .git, where Git stores all its repository data.  
# 
# **Tip**: To toggle display hidden files, 
# * On Mac, Command + Shift + Dot
# * On Windows 10 / 8, from the File Explorer window (shortcut: windows key + E)  choose --> View --> Show/hide --> check Hidden Items.

# ## Tracking Changes using GitHub Desktop
# 
# ### Add a text file
# Create a **plans.txt** file using a plain text editor (e.g. Nano, Notepad++, Atom, Sublime Text etc.. )
# 
# Example: using Bash and Nano to do so. Make sure that you are under the directory **hiking**. 
# 
# ```
# $nano plans.txt
# 
# ```

# Type the text below into the **plans.txt** file and save the file
# > This is our summer hiking plan.

# After saving the file, look at the GitHub Desktop window. You will see the change highlighted. 
# ![addedplans](./images/AddedPlans.png)

# Git now knows that it's supposed to keep track of **plans.txt**, but it hasn’t recorded these changes as a commit yet.
# To do so, type in the following message to the Note and Description areas on the lower bottom of the GitHub Desktop page. 
# > Summary: Create plans.txt
# 
# > Description: Start notes on hiking plans
# 
# And then, click on the *Commit to main* button

# Good commit messages start with a brief (<50 characters) summary statement about the changes made in the commit. Generally, the message should complete the sentence “If applied, this commit will.” If you want to go into more detail, use the Description field to explain. Use this additional space to explain why you made changes and/or what their impact will be.

# Now, look at the GitHub Desktop, it tells us that there is no local changes and everything is up-to-date. 
# 
# ![aftercommit](./images/AfterCommit.png) 

# ### Tracking edits
# 
# Add more information to **plans.txt**
# 
# > Vermont is nice this time of year.
# 
# ```
# $ nano plans.txt
# $ cat plans.txt
# ```

# When you see the change highlighted on GitHub Desktop window, repeat the *Commit to Main* process above. This time, with the commit message as 
# 
# > Summary: Update plans.txt
# 
# > Description: Add thoughts on locations 

# When you click on the *Commit to Main* button, you move the changes Git tracked at the staging area to the repository as shown in the figure below. 
# 
# ![stagingarea](https://swcarpentry.github.io/git-novice/fig/git-staging-area.svg)

# When you have multiple changes to one file or changes to multiple files, you can select the changes you'd like to group for any given commit. 
# 
# For example, add one more line below to **plans.txt**
# > Christine thinks Maine is way better!
# 
# And then, add the following line to **README.md**
# > This is the place where our group is debating where to go hiking and what to do when we get there. 
# 
# Note how you can check and uncheck multiple changes to include or not include for a given commit. 
# 
# ![multiplechanges](./images/MultipleChanges.png)

# First, select plans.txt changes and Commit with the following message:
# 
# > Summary: Update plans.txt
# 
# > Description: Added Christine's thoughts. 
# 
# Second, select README.md changes and Commit with the following message:
# 
# > Summary: Update README.md
# 
# > Description: Added what the group is trying to do. 
# 
# This process can be illustrated by the following figure:
# ![addmultiple](https://swcarpentry.github.io/git-novice/fig/git-committing.svg)

# ### Tips:
# 
# 1. The **History** tab will show you details of all the commits. You may choose to revert a specific commit with the tool too. But be careful to not create any conflicts. 
# 
# ![History](./images/History.png)
# 
# 2. Git does not track directories on their own, only files within them. Try to make a subfolder **packing** and leave it empty. It does not show up on the GitHub Desktop **Changes**. 
# 
# 

# ### Practice
# 1. Under the **packing** folder, create a new file **supplies.txt** and add your iniital thoughts about what we should bring on a hiking trip
# 
# <!-- Instructor Notes: In the supplies.txt, you may add line 1 and line 2 below. 
# maps and boots
# water and food
# --> 
# 
# 2. Now check GitHub Desktop. What change(s) are listed? supplies.txt? the packing folder? Or both? 
# 3. Commit the change with a message. Looking at the history, do you see a separate commit for the folder **packing** itself? 
# 
# <!-- Instructor Notes: You should only see a commit for the file not the folder --> 

# ## Ignoring Things
# What if we have files that we do not want Git to track for us, like backup files created by our editor or intermediate files created during data analysis?
# 
# You can add those file paths and names to the hidden .gitignore file. 
# 
# Open the current .gitignore file under your **hiking** repo to examine it. Because we chose the **Git Ignore** for python when we initialized the repo in GitHub Desktop, the list of file names here are those system files that a Python project often has that you don't need to track. This file tells Git to ignore changes happening to those files. 
# 
# ![gitignorefilepython](./images/gitignorefile.png)
# 

# Different types of programming may have different system files to ignore. Using the tool in GitHub to initialize repos helps to create the default for each type of programming. But please check the file to make sure that the files you do want to keep track of are not accidently listed here, especially when you observe anything strange. 

# ## Remote into GitHub
# 
# So far, we are doing Version Control on our local computer. In order to collaborate with others and take full advantage of the sophisticated version control features, we need to use hosting services like GitHub, Bitbucket or GitLab to hold the master copies where collaborators could share changes with each other. 
# 
# The relationship between the local Git repo and the remote one can be illustrated as below. 
# ![githubremote](https://swcarpentry.github.io/git-novice/fig/github-repo-after-first-push.svg)

# On GitHub Desktop, you can use the *Publish repository* button to post your local repo to GitHub.com or GitHub Enterprise @ MIT, since we have configured our GitHub account into the GitHub Desktop. 
# 
# Note: When publishing to GitHub (either with a free account or an MIT Enterprise GitHub account), you can publish either a private or public repository. 
# 
# ![publishrepo](./images/publishrepo.png)
# 
# 

# Once you successfully published your repo, go to a browser and log onto your account on GitHub.com and take a look at the repository added there. All the files and commit history are synchronized to the remote GitHub repo.
# 
# ![repogithub](./images/RepoOnGitHub.png)

# ### Push changes from local repo to remote repo
# 
# Still use Bash and Nano to add one more line below to **plans.txt**
# 
# > Phoebe suspects Maine is full of bears. 
# 
# Once you saved the change, commit the change to your local repo with the following message. 
# 
# > Summary: Update plans.txt
# 
# > Description: Added new opinion on destination. 
# 
# Once it's committed, you will see a new option to *Push origin*. Use that to push the changes from your local repo to the remote repo on GitHub.com. Then, check the remote repo to see if the changes appear. You may need to refresh your browser. 
# 
# ![pushchanges](./images/PushChanges.png)
# 

# ### Fetch and pull changes from remote repo to local repo
# 
# On your GitHub.com repo page in the browser, open the README.md file and use the pencil icon (**Edit this file**) tool to add the following sentence to the file. 
# 
# > I made this edit on the remote GitHub repo through web browser. 
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
# In a virtual class, our instructors will invite you as collaborators for a practice project owned by the instructor. The instructor will play the Owner role and all students will play the Collaborator role for the rest of the session. 
# 
# <!-- Instructor Note: for virtual sessions, instructors should have collected students' GitHub user accounts. Add them to an example repo you own as collaborators before the session.  -->
# 
# As a project owner, you can give your collaborator access to your repo by clicking on the **Settings** button on the right of your GitHub.com Repo page. You may need to ask your collaborator's GitHub username to find them. 
# 
# ![collaborator](./images/Collaborator.png)

# ### Accept invitation
# Collaborator, you need to first accept the invitation from the Owner. Look for an email sent to you with an *View Invitation* button to click on. Make sure you have logged in your GitHub account in the browser before clicking on the *View Invitation*  button.  
# 
# 
# <!-- Instructor Note:  It may be helpful to show the sample email and/or the notification page on the screen. Switching to the screen of another instructor or use screenshots here. -->
# 
# ![collabInviteEmail](./images/CollabInvitationEmail.png)
# 
# Or you can look for the invitation under the *Your Organizations* section [https://github.com/settings/organizations](https://github.com/settings/organizations) once you are logged in.
# 
# ![collabInviteOrgPage](./images/CollabInviteOrgPage.png)

# Once the Collaborators *Join* and *Accept Invitation* for the project, they can access the repo. Note that the repo will still be under the Owner's account. On that repo page, click on the greenbutton *Codes* on the right side. And choose "Open in Desktop". You will be prompted to choose a local path to save this repo. 
# 
# **Caution**: please do not choose the path where you saved your own **hiking** repo, if the repo names are both **hiking**. Instead, create a subfolder *Collaboration* first then save the new repo from the Owner under that. 
# 
# ![download](./images/CloneOpen.png)
# 
# 

# The Collaborator may also take the URL or SSH link from the popup window and then use the GitHub Desktop, File --> Clone Repository... to accomplish the same task. 

# The Collaborator can now make a change in her clone of the Owner’s repository, exactly the same way as we’ve been doing before with their own repository. 
# 
# <!-- Instructor Note: Bring up the Settings/Collaborator page to check and show collaborators who have accepted the invitation. -->

# ### Branch
# 
# If you are the owner or have collaborator permissions on a repository, you can create a branch off of the repository's default branch so you can safely experiment with changes. The default branch of a repository is usually the Main branch. 
# 
# #### Create a branch
# 
# <!-- Instructor Note:  Ask each student to create a new branch named test-YourInitials and publish it to the collaborative repo. Show the branches as people push them to the collaborative repo. Ask Instructor 2 to create a branch with their initials too for demo of pull request between branches and creating conflict below. -->
# Use the *Current Repository* tab on your GitHub Desktop to navigate to the repo you'd like to create a branch in. 
# 
# On the top of the GitHub Desktop, switch to the branch that you want to base the new branch on by clicking the Current Branch and choosing it from the list. For now, it would be just the Main branch. Then, click on New Branch. 
# 
# ![Branchcreate](./images/BranchCreate.png)
# 
# Type the name of the new branch you want to create (e.g. test-YourInitials) and then *Create Branch*. Caution: make sure you use a different name for the new branch from your collaborators to avoid future conflict. 
# 
# ![BranchName](./images/BranchName.png)

# Once the branch is created on the Collaborator's local repo, the Collaborator will see an option to publish it to the remote repo. Please *Publish branch* and the Owner will see the new branch and new edits committed once the Owner refresh the repo in the browser. 
# 
# ![PublishBranch](./images/PublishBranch.png)
# 
# The two branches now have the exact same content. But you may add future edits to them separately. They are also connected. Individual commits can be pulled from one branch to another independently. 
# 
# <!-- Instructor Note: After students pushed their branches to the collaborative repo, go to the Insights / Network section to show the relationship among branches.  -->
# 
# Here is a network graph for the Yelp source code repo that may help you understand the concept of branches. The live version can be accessed here. https://github.com/Yelp/yelp.github.io/network 
# 
# ![Branchnetwork](./images/BranchNetwork.png)

# 
# ### Pull request to merge changes between branches
# 
# Once you are ready with the changes made in one branch, you can send a *Pull request* to request merging them into another branch. A Collaborator can *Confirm Merging* in the target branch, that may or may not be created by them, unless the Owner has setup rules for the pull requests to be reviewed by specific members before merging. 
# 
# <!-- Instructor Steps: (no switch of screenshare. Only Instructor 1 shares screen.) 
# 1. Instructor 2 add a file members.txt on the test-Instuctor2Initials branch and push to the repo with a committ note of "only added for test-Instructor2Initials". 
# 2. Instructor 1 clicks on the "x branches" link on the right of "main" on the top left to see all branches. 
# 3. Under "Active branches", Instructor 1 click on "New pull request butoon" next to the branch test-Instructor2Initials. 
# 4. New pull request is displayed as "base: main <- compare:test-Instructor2Initials" 
# 5. Type in the committ notes to add "sending pull request to main branch". Then click on Create pull request . 
# 6. Instructor 1 go to Pull requests tab and click on the pending pull request to "Merge pull request". Type in notes and Confirm Merge. 
# 7. Note: Owner - Instructor 1 would see options to "review by certain people" etc. before merging. Collaborators don't see the options but still can confirm Merge, unless owner setup the Protection of the main branch. 
# 
# --> 
# 
# A *Pull request* can be initiated on the browser page of the Github repo.
# 
# On GitHub Desktop: click on Branch --> Create Pull Request will take you to a web browser page.  
# 
# ![CreatePullRequest_Desktop](./images/CreatePullRequest_Desktop.png) 
# 
# On your Browser: you can browse to Braches page by clicking on the number of Branches link on the top left of your GitHub.com repo page. For each *Active Branch*, you will see a *New Pull Request* button on the right side. 
# 
# ![CreatePullRequest_Browser](./images/CreatePullRequest_Browser.png)
# 
# *Create Pull Request* or *New Pull Request* link takes you to a page where you can review the changes, write a message for the pull request, and create the pull request. 
# 
# ![pullrequest](./images/PullRequest.png)
# 
# If there is no conflict between the two branches, they are ready to be Merged. All requests can be accessed from the Pull Requests tab. 
# 
# ![mergepull](./images/mergepull.png)
# 
# Both the Collaborator and the Owner can confirm the Merge, unless the Owner has setup Rules for pull requests to be reviewed by specific members. 
# 
# ![mergepull](./images/mergepull_owner.png)
# 
# Read more about [different types of merge on this GitHub.com support page](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges#rebase-and-merge-your-pull-request-commits) 
# 
# Choose the type of merge you'd like, write a summary, and Confirm the merge. 
# ![confirmmerge](./images/ConfirmMerge.png)
# 
# <!-- Instructor Note: Instructor can show the Network visual after demonstrating the merge -->

# ### Practice:
# The Collaborator makes a change to the **plans.txt** file in the newly created branch and push the change to the Owner's remote repo. The Owner can fetch and pull that change to the Owner's local repo. 
# 
# <!-- Instructor Note: In a virtual class, instructor asks all students to make a change in their branch and push it to the collaborative repo. Instructor choose one branch to demonstrate fetching and pulling the change of that branch to the owner's local repo. It may be the easiest to choose Instructor 2's branch. -->
# 
# 
# 
# **TIP**: When you are using GitHub Desktop to switch between branches, the local folder for the repo in your File Explorer or Finder will automatically be switched to that branch. 
# 
# <!-- Instructor Note: Instructor can switch between the branches, delete a file in one branch and commit, and show how the File Finder can display differently when switching between the branches.  -->
# 
# <!-- *for in-person session.* If time allows, exchange your roles as Owner and Collaborator and run the process again. Be careful not to put the repos with same names into the same folder.  -->

# ### Conflicts
# 
# During collaboration, if the Owner and the Collaborator attempted to change the same part of a file at the same time, there can be conflict. The party who pushes the change to the remote repo later will be asked to resolve the conflict. 
# 
# <!-- Instructor Note: Two instructors need to work together on this part. No need to switch screen sharing though. Instructor#1 and Instructor#2 both go to the branch Intructor#2 created and edit the same line of the same file. Instructor#2 commit and push the change first. Instrctor#1 wait for the signal from Instructor#2 and then try to commit and push to see the conflict message. -->
# 
# Owner and Collaborator both browse to the same branch of their local copy of the Owner's repo **hiking**.
# 
# Owner and Collaborator make changes to the same line of *plans.txt* file on their own computer. And then the Collaborator push the changes to the remote repo first.
# 
# <!-- Instructor Note: 
# 1. Under the test-Instructor2Initials branch, Instructor 2 add to Line 4 of plans.txt with "But we should be fine if we are careful" with commit notes "Justify this destination." Commit and push this edit. 
# 2. Under the test-Instructor2Inisitals branch, Instructor 1 add to Line 4 of plans.txt with "Ye says Maine has great ocean views" with commit notes "Added new opinion on destination". Commit but do not push this edit yet.  
# 
# -->
# 
# If the Owner changes the same line before fetch/pull the Collaborator's changes of that line, the Owner will see a message about **Conflicts** when the Owner tries to push the change to the remote repo. 
# 
# First, the Owner will see GitHub Desktop note for "Pull Origin". 
# ![PullOrigin](./images/PullOrigin.png)
# 
# After clicking on "Pull origin", the Conflict notification window will show up. 
# 
# ![ConflictNotice](./images/ConflictNotice.png) 
# 
# The process can be demonstrated by the figure below. 
# ![conflicts](https://swcarpentry.github.io/git-novice/fig/conflict.svg)
# 
# GitHub Desktop will prompt the Owner to resolve the conflicts by merging the changes before the commit can be pushed to the remote repo. 
# 
# An example of conflicts: 
# ```
# This is our summer hiking plan.
# Vermont is nice this time of year.
# Christine thinks Maine is way better!
# <<<<<<< HEAD
# Phoebe suspects Maine is full of bears. Ye says Maine has great ocean views.
# =======
# Phoebe suspects Maine is full of bears. But we should be fine if we are careful.
# >>>>>>> 93c4124ba58d7db63f7fb852d6afba9cd0cc7ad8
# 
# ```
# 
# Our change is preceded by <<<<<<< HEAD. Git has then inserted ======= as a separator between the conflicting changes and marked the end of the content downloaded from GitHub with >>>>>>>. (The string of letters and digits after that marker identifies the commit we’ve just downloaded.)
# 
# It is now up to us to edit this file to remove these markers and reconcile the changes. We can do anything we want: keep the change made in the local repository, keep the change made in the remote repository, write something new to replace both, or get rid of the change entirely. 
# 
# Remember to delete all the added symbols and separators. 
# 
# If you are using a visual editor, you may see the highlight of Conflicts as in the screenshot below from Atom. 
# ![ConflictVisual](./images/ConflictVisualAtom.png) 
# 
# Once the changes are merged and saved, you can push the new commit to the remote repo. 
# 
# ![ConflictResolve](./images/ConflictResolve.png) 
# 
# <!-- Instructor note: You can decide to use either the Instructor 1's edit or Instructor 2's edit. -->
# 
# Do not forget to Push origin after resolving the conflict. 
# 
# ![PushOriginAfter](./images/PushOriginAfter.png)
# 
# <!-- Instructor Note:  If students would like to practice resolving conflict. You can make a change in the main branch, commit/push, and then ask students to make the changes on the same line and try to push. The danger is that there will be many conflicts for the same file to resolve. -->
# 

# ## Fork
# 
# A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project, and without being added as a collaborator of a public repository.
# 
# 
# ### Fork a public repository
# Here is an example repository for you to Fork. 
# Go to https://github.com/CarpentriesMIT/CO2EmissionPracticeDemo   
# 
# Use the top right button to *Fork* the repository. Notice that the content stays the same but the location of the repo will be changed from the original owner's account to yours once the fork is successful. 
# 
# ![forkoption](./images/ForkOptions.png)
# 
# When you Fork a repo, you can choose if you would like to include the Default branch only or all branches in the repo. 
# 
# ![forkbranchoption](./images/ForkBranchOption.png)
# 
# 
# Once it's forked, you can use Code / Open it on GitHub Desktop as a local copy to edit. Your GitHub Desktop will ask the Fork Behavior you prefer - directly interact with the forked repo under your account or the original repo you forked from. 
# 
# ![ForkBehaviorOptions](./images/ForkBehaviorOptions.png)
# 
# The Fork Behavior can be switched between the two modes under the menu Repository / Repository Settings. 
# 
# ![ForkBehaviorSetting](./images/ForkBehaviorSetting.png)
# 
# Forked repositories are linked to the original repository, often referred to as the upstream repository. 
# 
# When you click on *Fetch Origin* or *Fetch Upstream* in GitHub Desktop depending on which Branch you switched to on GitHub Desktop. 'Origin' means the Repo you forked to your account, while 'upstream' means the original Repo you forked from. 
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
# Make a change to the "CO2EmissionAnalysis.ipynb" file or the README.md file in the repository you forked earlier. And try to make a pull request to the upstream repo under the CarpentriesMIT account. 
# 
# Read more about [Fork a Repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

# In[ ]:




