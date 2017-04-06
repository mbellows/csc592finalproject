# csc592finalproject

// setup for the first time, do this in the directory where you want to store the files
git clone https://github.com/mbellows/csc592finalproject.git

-------------
// When doing all these commands in the terminal, you must be in the path you specified for the project

// see what is changed, gives you an idea what you are about to do
git fetch
git status 

// add all changed files to your 'stage' (stuff that will be committed)
git add --all 

// commit your changes (local only)
git commit -m "some helpful description of what you did"

// share your changes with everyone else
git push origin

// get other people's changes
git fetch
git pull

------------

// dealing with conflicts (two people change the same piece of the same file independently)
// step 1: open the file with conflicts and look for sections that look like this:

<<<<< head
stuff you change
======
stuff they changed
>>>>>> their commit name

// step 2: combine / resolve the changes so both people are happy
// step 3: tell git the changes are resolved
git add <file name>

// commit and push as per usual