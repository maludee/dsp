# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > - ls = list files  
- pwd = print working directory  
- cd = change directory  
- cd ../ = go up one directory  
- mk dir = make new directory  
- * = wildcard  
- mv = move file  
- rm = remove file  
- cp = copy directory or file  
- sort = sorts alphabetically  
- clear = clears the terminal window


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > - list files in current directory  
- list all files in directory including those that start with "." 
- list long format files in table  
- list files in long format with file sizes using unit suffixes  
- list files in long format w/ unit suffixes and including files that start with "."  
- list files sorted by time modified  
- list files with colorized output, in long format, and with slashes after directory names.  


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > - -m displays names as a comma-separated list  
- -r displays files in reverse order  
- -R displays subdirectories in addition to file list  
- -u displays files by access name  
- -1 displays each entry as a line  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is used to execute a command based on output from another command. One example of its use is to create files based on a list of file names. For example: cat list_of_files | xargs touch would do this.  

> > The syntax is command1 | xargs command2.



 

