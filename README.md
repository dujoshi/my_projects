# my_projects


Git commands to be used mainly 

git clone <From> <local_name> -b <branch>

git status ===> will provide the status of change file in git repo
git stash  ===> remove all changes
git clean -fd ===> clean full git

git pull --rebase ===> will keep the existing work 
git pull ====> will pull the fresh repo. 


Before Committing we need to see the following : 

       1- Check if there is any compile error in your python code : 
                python -m py_compile <file_name.py>
       2- Check if there is any yaml error in  your yaml file

                   >>> import yaml
                   >>>with open('test/system/someyame.yml', 'r') as st:
                             print (yaml.load(st))

  