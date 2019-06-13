# pyspark-example-app
Example PySpark Application for PySpark Workshop Series

This is the pyspark app we will build upon during our workshop series. 
For each workshop, we will create a new branch to push our changes to by first syncing our forked repo's master branch with this repo's master branch. 
Then after making changes, you can create a pull request to merge your changes back to this repo. 

### How to get started setting up your environment
* Join the [Teams chat](https://teams.microsoft.com/l/channel/19%3a8de987dbd06d4caeaeee085647601973%40thread.skype/PySpark%2520Workshop%2520Series?groupId=7f3ee77b-7617-41ed-bb5f-4fd98d181093&tenantId=9ca75128-a244-4596-877b-f24828e476e2) to join the conversation. If you hit any road blocks, message us there.
* If you have any additions, corrections, or vicious criticisms of these instructions, please put them in the Teams chat for us to correct. We want to make this work for everyone, and also express that it's someone else's fault. 

#### For Windows users
* *IMPORTANT* Open this link in Microsoft Edge! Click [this link](http://boxstarter.org/package/url?https://gist.githubusercontent.com/nguyenuy/6b16704a43f8568c020c4b6bed152a83/raw/7ebd3f59a85303a6180272bf0c31bd68a2710ed1/simple_windows_dev_environment)
* It should download an application and prompt you to run. Accept all prompts. 
* This will run a script on your machine to install all the required dependencies to run the workshop application
* When prompted for your password, it's asking for your windows password, because several restarts will be required by the application install. Just let it do its thing, restarting several times, until finally the CMD window tells you to ```Type ENTER to exit```. Hit ENTER and you're done! 
* Thank Uy for the automation script next time you see him, or in the Teams chat.
#### For Mac users:
* Open Terminal and execute the above command: ```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)“```
   * Note: If you just get a ">" after hitting enter and nothing happens, try closing your terminal window, opening a new window, and entering 
```xcode-select –install```
Then try the above command again to install homebrew once your command line developer tools have been installed.
* Confirm installation by executing:```brew update```
* Install some packages (git, pycharm, caskroom, java8)
    * ```brew install git```
    * ```brew cask install pycharm-ce``` – this will install as an application
    * ```brew tap caskroom/versions```
    * ```brew cask install java8```
    * ```brew install python3```
* Export Java Home environment variable
    ```export JAVA_HOME=`/usr/libexec/java_home -v 1.8` ```
* Navigate (in Terminal) to a new directory you want your Spark install to live in. Download Spark to that local directory. 
    * Change the statement below to match whatever the most recent version of Spark is
    ```curl -O https://www-us.apache.org/dist/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz```
* Untar Spark 2.4 tarball```tar zxvf spark-2.4.3-bin-hadoop2.7.tgz```
* In your bash profile (if you’re using the default shell), add the following line to .bash_profile```export SPARK_HOME=/path/to/spark/spark-2.4.3-bin-hadoop2.7```and 
* Update your PATH variable to the following: ```export PATH=$PATH:$SPARK_HOME/bin```
* Open a new terminal and test your installation by running:```pyspark```
* Install a few more packages
    * ```pip install jupyter```
    * ```pip install findspark```
    * ```pip install jupytext```



#### Create a GitHub Account
If you don't already have one. A personal account is fine.
Never used GitHub before? Here are some helpful links:
* [Introduction](https://www.youtube.com/watch?v=BCQHnlnPusY)
* [Branches](https://www.youtube.com/watch?v=oPpnCh7InLY)
* [Forks and Pull Requests](https://www.youtube.com/watch?v=_NrSWLQsDL4&t=145s)

Set global Git username on your machine if you don't have one set already
* In terminal or cmd prompt enter the following (but with your name and GitHub email):
    * ```git config --global user.name “FirstName LastName”```
    * ```git config --global user.email “email@gmail.com”```
        * NOTE: If your email is set to private in github, they'll provide you with a no-reply email address like
         22250475+githubuser@users.noreply.github.com. Use this email for your local git config.




#### Create a Fork of Our Repository on GitHub
* Navigate to https://github.com/mehtaparas/pyspark-example-app
* Click “Fork” at the top right. This creates a copy of our simple PySpark application under your Git user. 
* Now you should have this repository saved. Click “Clone or download” to get the URL. 
* Open PyCharm app on your computer
* Select "Checkout From Version Control" in the New Project window
* Enter the URL from your forked repository

#### Familiarize Yourself With the Project and Commit Your First Changes
* Inside the pyspark-example-app is the main.py python script, which contains the code that will be run initially when the application is executed. 
* Inside the data folder are json files, each containing a name and some skills.
* In the top main menu, select File -> Settings -> Project:\[project name\] -> Project Interpreter
    and make sure the interpreter is your new Python install. Currently 3.7. 
    * If not, create a new one.
    * Click the settings wheel then Add
    * For location, create a new empty folder somewhere, mine was C:\Users\kendra.billings\PycharmProjects\pyspark-example-app\Python_Interpreter
    * For base interpreter find where your python.exe is. The most recently installed one. Mine was at C:\Python37\python.exe
    * Select OK
    * You'll have to wait for a bit for the project to process these changes. Check the status at the bottom of your screen. 
* Find the requirements.txt in the root directory and open it. Above you should see
    a yellow bar with an option to install project dependencies. Click on it and wait for the
    progress indicator at the bottom of the screen to indicate it's finished indexing. 
* Right click on one of the data files and select “Copy”
* Right click on the data folder and select “Paste”
* Name the file [your last name].json and select “OK”
* When the prompt comes up to add the following file to Git, chose “Add”
* Edit the file to reflect your particular skills (feel free to be creative), and save.
* Commit your change
    * You can either do this using Git Bash or select the green check park at top right in PyCharm
    * Make sure only your json file is checked for commit. All the vcs and unversioned files don’t need to be committed. They’re unique to your set up. 
    * Enter a useful commit message. What change did you make?
    * If you set a global git user earlier in the Git set up, you can leave the “Author” field blank.
    * Select commit
* Select VCS -> Git -> Push in the top bar to push your locally committed changes to your origin repo on GitHub.
    * Make sure destination is origin/\[current branch\]



### How to sync your forked local master branch with the original repo master branch
* Open the Git Bash application and navigate to your project's directory
* Add remote with the name "upstream" that points to the original repo 
    * git remote add upstream https://github.com/mehtaparas/pyspark-example-app.git
* Fetch branches and commits from upstream repo
    * git fetch upstream
* Switch to your local master branch if you haven't already
    * git checkout master
* Merge changes from the upstream master branch into your local master branch
    * git merge upstream/master
* For more details refer to: 
    * https://help.github.com/en/articles/syncing-a-fork
    
### How to submit a pull request
* Navigate to the original repo:
    * https://github.com/mehtaparas/pyspark-example-app
* Click "New pull request"
* Click hyperlink "compare across forks"
* Make sure base repository is set to: mehtaparas/pyspark-example-app
* Set base branch to "workshop1" or whatever the current workshop is
    * Don't submit a pull request to the master branch!
* Make sure head repository is set to your forked repo and compare is set to the branch your changes are in
* Add a title and a meaningful description of the changes you've made then click "Create Pull Request"
* For more details, refer to:
    * https://help.github.com/en/articles/creating-a-pull-request-from-a-fork
