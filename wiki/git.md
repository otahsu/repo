# GIT Basic
* Note that in local operations, GIT have 3 main sections: working dictionary, staging area, git repository.
* The action from work dictionary to staging area is called 'stage files'.
* The action from staging area to git repository is called 'commit'.
* The action from git repository to working dictionary is called 'checkout'.
* Note that 'stage' is only a state of a file, the state would not be changed by 'checkout' to another 'branch'
* 'git commit' save snapshots (not changesets) of local working dictionary to git local repository(repo/.git/), but only save a pointer to the unmodified files. 
* Note that 'branch', like 'HEAD', is a pointer to a commit, and 'master' is the default name.
* Git is a content-addressable filesystem. In .git/, there are four important databases:
	1. 'objects' directory stores all the content for your database, 
	2. 'refs' directory stores pointers into commit objects in that data (branches, HEAD, tags, remotes), 
	3. 'HEAD' points to the branch you currently have checked out,
	4. file 'index' is where Git stores your staging area information. 

## initial a local repos
```
$git init
$git add .gitignore
```

## git clone
* clone by SSH protocal, clone 'ginkgo' repository that codebeamer specifies in SCM repositories
```
$git clone ssh://opc_cb@c0105/git/ginkgo
//after doing so, you can find ./ginkgo in your PWD.
```  
* clone by local protocal
```
//Note that it may clone 'master' branch only for thif 'local protocol'
$git clone file:///ban/chhsuzt/py_recipe
```
* bare clone, i.e., clone only .git without working dict. and remove the remote-tracking branch mapping.
```
//git clone --bare <repository> [target dict], if the target is not assigned, the defualt name is 'repo.git'
$git clone --bare file:///ban/chhsuzt/repos ./repo/.git
```  
* project admin in CB can create 'git repository', but it's bare without having a branch or commit.
```
//you need to commit and push it to origin/master for 1st commit. 
$git push origin master
```
```
//push up an empty repos. for the first time.
//'u'=set upstream(add tracking/tracked ref automatically?), 'all' = all refs(branches?HEAD?)
$git remote add origin https://otahsu@bitbucket.org/otahsu/src.git
$git push -u origin --all   
```

## git add
```
//it has 2 usages, one is to track an untracked file,
$git add filename_untracked
$git status
//the other is to stage an unstaged file.
$git add filename_unstaged
//note that we can commit the staged files while the tracked files don't record the changes
$git commit
```

## git diff
* diff HEAD and 2 commit before HEAD in the local branch
    ```
    $git diff HEAD HEAD~2
    ```
* diff 2 <commit-1> <commit-2>, the commit numbers can be known by GUI
```
// the syntax is diff <commit-1> to <commit-2>
//note that the commit number is an unique SHA-hash 
$git diff HEAD 2cc551571b1ad38e43eded052cd25f4a5238e990
$git diff <commit> [--] [<path>...]
//This  form is to view the changes you have in your working tree dict. relative to the named <commit>. 
$git diff <commit> <commit> [--] [<path>...]
```

## git log
```
//log the whole commit history in all branches
$git log
//log the last 3 commits
$git log -3
```

## git mv
```
//It can move or rename a file
$git mv filename_old filename_new
```

## git rm
```
//It can delete the file
$git rm filename
```

## git commit
* git commit -a' can commit all including unstaged files
```  
$git commit -a
```
* git commit filename' can commit one file discarding if it's staged or not.
```
$git commit filename
```
* replace the last commit with new commit msg.
```
//Don't use it if it has been in remote branch!!
$git commit --amend -m 'try amend'
$git log
commit f163d64f6fdc3f54dc5904f1f4e36dfeefa9391f
Author: chhsuzt <chhsuzt@tsmc.com>
Date:   Wed May 15 16:12:41 2013 +0800

    try amend
```

## git remote

* git remote -v' shows the remote server name and URL.
the default ref is 'origin'.(?why 2 loctions of fetch/push)
```
$git remote -v
$git remote show
origin  ssh://opc_cb@c0105/git/scm_sandbox_git (fetch)
origin  ssh://opc_cb@c0105/git/scm_sandbox_git (push)
```  

* show the detail msg of the remote URL - 'origin'
```  
  $git remote show origin
    * remote origin
    Fetch URL: ssh://opc_cb@c0105/git/scm_sandbox_git
    Push  URL: ssh://opc_cb@c0105/git/scm_sandbox_git
    HEAD branch: master
    Remote branches:
      Pt1        tracked
      branchTest tracked
      master     tracked
    Local branch configured for 'git pull':
      master merges with remote master
    Local ref configured for 'git push':
      master pushes to master (up to date)

* rm a remote
```  
$git remote rm origin
```  

* add a new remote 
```
$git remote add <name> <url>
$git remote add x86_64_rh4.0917 file:////vol0/quota_ctrl/chhsuzt/backup/x86_64_rh4.0917
```

* add a new track branch to a remote branch
```  
//it will add a local repository in the same name to the remote branch.
$git checkout --track origin/branch
// create a new branch on a remote from the local existing branch. 
$ git push <remote> <branch>
```

* see git configure file
```
$cat .git/config
//or list the config, 'l' = list all
$git config -l
```

* add alias to the git conf file globally
```
$git config --global alias.co checkout
$git config -l
```

* to open the GUI 'qgit' 'gitk'
```
$ qgit
```

* update gitk
press 'F5'

* add a new dic recursively to local repository
```
//that is, commit the files in ./dic
$git add ./dic
```

* to remove the file in the local repository and working dir simutaneously. That is, it equals to 1. rm the file 2.commit this changeset 
```
$git rm file
```

* find 'less' document for some cmd in GIT
```
$git help cmd
```

*'git pull' would 'fetch' from and 'merge' with another repository or a local branch.
Not like hg, 'git pull' would not overwrite the uncommited files in the local working folder.
```
//git would auto merge with local commit and pull-in updates
//after merge, you can push the Change-Set
git commit -a
git pull   
git push
```
```
// conflict and auto-merge
// person1 and person2 modify fileA in the same time
// person1 has pushed his code
// when person2 push his code,
// case 1(they modified different files): git would auto-merge
// case 2(they modified the same fileA, no matter which lines have be modified): git would show the err msg as below
>>error: failed to push some refs to 'ssh://opc_cb@c0105/git/scm_sandbox_git'
>>To prevent you from losing history, non-fast-forward updates were rejected
>>Merge the remote changes (e.g. 'git pull') before pushing again.  See the
>>'Note about fast-forwards' section of 'git push --help' for details.
// person2 need to pull the remote to the local and merge the format below by hands.
>>++<<<<<<< HEAD
>> +chchchch
>>++=======
>>+ fjfjfjffj
>>++>>>>>>> 1b398c38f4c7c55ad68f5d3784115a3711afdd47
// after merge, person2 can push the code
```

## git fetch

> 'git checkout file' would checkout the file from local repository to working directory.
> git checkout file
> case that want to modify golden code only temporarily.	
> 1. push/pull a golden code 'file_old.py'.
> 2. modify golden code 'file_old.py' only in working dir.
> 3. edit new code 'file_new.py' that import 'file_old.py' without add or commit it.
> 4. checkout to recover the golden code from local repository to working dir.
```
    git checkout -f //force checkout all files
	git checkout -- file //checkout one file
```
> 5. commit/push 'file_new.py'.

* remove chages in working dict to the last commit.
```
$git checkout -f //force checkout all files
$git checkout -- .. //co all.
$git checkout -- file //checkout one file
```

## git branch
    //default branch is 'master' branch.
    //With no arguments, existing branches are listed and the current branch will be highlighted with an asterisk(*).
    //git use a pointer to the current branch, called 'HEAD'
    $git branch 
    *master
    //make a local branch of the current working dictionary as 'branch_name'
    $git branch branch_name
    $git branch
    * master
    branch_name
  
    //checkout form some branch to working dictionary, now 'HEAD' point to branch_name
    $git checkout branch_name
    Switched to branch 'branch_name'
    //merge a local branch into 'master'
  	    //edit file and make a new commit on the new local branch.
        //this file was edited on both branchs.
  	    $git add file
  	    $git commit
  	    //back to 'master' branch
        $git checkout master 
        //merge 'branch_name' into 'master'
	    $git merge branch_name
   	    Auto-merging file
	   CONFLICT (add/add): Merge conflict in file
	   Automatic merge failed; fix conflicts and then commit the result.
	   //open 'file' to merge it mannually.
       //note that the <<<<< ==== >>>> format.  	
	   $gvim file
	   <<<<<<< HEAD
	   ### on branch master
	   11111
	   =======
	   #### on branch_name
	   >>>>>>> branch_name
	   $git status
       #	Unmerged paths:
	   #   (use "git add/rm <file>..." as appropriate to mark resolution)
	   #       both added:         file
	   //stage and commit the unmerged file
	   $git add file
	   $git commit 
	   // insert commit msg
	   Merge branch 'branch_name'

	   Conflicts:
            file
	   //show the msg
	   [master 32fad60] Merge branch 'branch_name'
    //delete the 'branch_name'(may delete tag only, not the history path?)
    $git branch -d branch_name
    Deleted branch branch_name (was d3a4e3d).
    //git status(? it means that whole paths would push to 'origin' without tags)
	$git status
	# On branch master
	# Your branch is ahead of 'origin/master' by 11 commits.
	#
	nothing to commit (working directory clean)
  
    //git branch show only local branch, to see remote-tracking and local branches
    $git branch --all
    * master
    remotes/origin/HEAD -> origin/master
    remotes/origin/Pt1
    remotes/origin/branchTest
    remotes/origin/master
    //to see remote-tracking branches. Note that itself is a local branch that maps to the remote.
    $git branch -r

//git hash-object
    //Compute object ID, that is 40-character checksum hash by SHA-1 hash algorithm.

//git pull
    $git pull <remote> <branch>
    $git pull origin day3-130819

//git push
    //for specifaclly, you can push code only sto remote for one brach
    $git push <remote> <branch> //the remote branch is created automaticaalu if it doesn't exist.
    $git push origin day3-130819
    Counting objects: 36, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (29/29), done.
    Writing objects: 100% (30/30), 6.07 KiB, done.
    Total 30 (delta 19), reused 0 (delta 0)
    To ssh://opc_cb@c0105/git/daytona-blessed
    * [new branch]      day3-130819 -> day3-130819

    //1st push for new empty CB repos.
    $git commit //commit a null README
    $git push origin master //create master branch in origin

//git tag
//There are 2 types of tags - lightweight and annotated.
//The precedor is save only a pointer to a commit.The latter saves the full objs, is more recommended.
	//list all name of tags
	$git tag
    //list tags for grep.
    $git tag -l "*pds" 
	//add a new 'lightweight' tag on a commit object
	$git tag tagname c409da3b63098e7cc266e5b737479fd8affbe0b1
    //or co to any commit and tag it
    $git co xxxxxxxxx
    $git tag -a tagname
	//add a new 'annotated' tag on a commit obj
    $git tag -a tagename 
    //delete a tag 9fceb02d0ae598e95dc970b74767f19372d61af8
	$git tag -d tagname
    //show the msg of a tag
    $git show tagname
    //sharing(push) a tag, note that 'git push' would not push tags by default.
    $git push origin tagname
    //push all tags
    $git push --tags origin
    //delete remot tag
    $git push --delete origin AIO_Label_v1.1
       
//git checkout
	//checkout a commit object, that cause 'deattch' state from 'HEAD of a branch'.
	$git checkout c409da3b63098e7cc266e5b737479fd8affbe0b1
    //checkout a tag
    //note that after you checkout to a tag, the HEAD is in 'detached HEAD' state without and branch.
    $git checkout tag_name
    //checkout to previous commit state by force
    $git checkout -f
    //checkout to a branch, in fact, 'HEAD of a branch' 
	$git checkout branch_name
	//on a commit of 'deattch' state, make a new branch  
	$git checkout -b branchname
    //resolve binary confilct( chosse one line below)
    $git checkout --their -- lib/libtmglib.a
    $git checkout --ours -- path/to/conflicted-file.txt

//"detached HEAD state" - It means simply that HEAD refers to a specific commit, as opposed to referring to a named branch/tag.
// show GIT object
$ git show HEAD

//use 'kdiff3' as git external tool
//.gitconfig
[difftool "kdiff3"]
	path = /vol0/ap/iht/x86_64_rh4/ihtruntime/bin/kdiff3
	trustExitCode = false
[difftool]
	prompt = false
[diff]
	tool = kdiff3
[mergetool "kdiff3"]
	path = /vol0/ap/iht/x86_64_rh4/ihtruntime/bin/kdiff3
	trustExitCode = false
[mergetool]
	keepBackup = false
[merge]
	tool = kdiff3
$ git difftool sha1 sha2

// git diff for a file of different commits
$ git diff commit1-sha commit2-sha PathToFile
$ git difftool commit1-sha commit2-sha PathToFile //open with external tools.

// three-way merge by kdiff3 - base, local, remote(base is the common
// ancenstor, is to merge from remote to local)
// what's the role of 'base'? and why build-in git diff doesn't show 'base'? 
$ git mergetool 

// use kdiff3 to merge(or rollback) by mannaul
//click "Merge Current File" then "right-click" to do merge work.
$ git difftool 4d358c9c940fea08b1196dd2aa59fa2f15fd5f4c 9283409e0e4d616985b11bd440951d553e88749d third.txt

//Note that the conflict lines would be started from <<<<<<< to >>>>>>>, and
//seperated by ========= in the middile.

//git log --diff-filter
```
--diff-filter=[ACDMRTUXB*]

Select only files that are

A Added
C Copied
D Deleted
M Modified
R Renamed
T have their type (mode) changed
U Unmerged
X Unknown
B have had their pairing Broken
* All-or-none
```