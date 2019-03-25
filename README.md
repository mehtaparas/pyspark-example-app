# pyspark-example-app
Example PySpark Application for PySpark Workshop Series

This is the pyspark app we will build upon during our workshop series. 
For each workshop, we will create a new branch to push our changes to by first syncing our forked repo's master branch with this repo's master branch. 
Then after making changes, you can create a pull request to merge your changes back to this repo. 

### How to sync your forked local master branch with the original repo master branch
* Add remote with the name "upstream" that points to the original repo 
    * git add remote upstream https://github.com/mehtaparas/pyspark-example-app.git
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
* Set base branch to "workshop1"
    * Don't submit a pull request to the master branch!
* Make sure head repository is set to your forked repo and compare is set to the branch your changes are in
* Add a title and a meaningful description of the changes you've made then click "Create Pull Request"
* For more details, refer to:
    * https://help.github.com/en/articles/creating-a-pull-request-from-a-fork