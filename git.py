#Import dependencies
from subprocess import call

#Commit Message
commit_message = "Adding sample files"

#call('cd ~/domains/projects', shell=True)

#Stage the file
call('git add ~/domains/projects/*', shell = True)

# Add your commit
call('git commit -m "daily update"', shell = True)

#Push the new or update files
call('git push origin master', shell = True)


