# Week 1: Troubleshooting Concepts

# Summary
## 1. Introduction to debugging
### 1.1 Definition
- Troubleshooting: 
  - The process of identifying, analyzing and solving problems.
  - Fixing problems in the system running the application.
- Debugging:
  - The process of identifying, analyzing and removing bugs in a system.
  - Fixing the bugs in the actual code of the application.
- Debuggers: Let us follow the code line by line, inspect changes in variable assignments, interrupt the program when a specific condition is met, and more. 
- Reproduction case: A clear description of how and when the problem appears.
- System calls: Cals that the programs running on our computer make to the running kernel.

### 1.2 Problem Solving Steps
__Getting information__:
- Gathering as much information as we need about the current state of things
- What the issue is, when it happens, and what the consequences are, for example
- Fingding reproduction case (which is a clear description of how and when the problem appears.)

__Finding the root cause__:
- Get to the bottom of what's going on, what triggered the problem, and how we can change that. 

__Performing the necessary remediation__:
- Trying to find short-term solutions in order to progressively resume normal activities. Then working on methods to solve long-term issues and make necessary adjustments to avoid future problems.

### 1.3 Command and tools
- tcpdump, wireshark: Show us ongoing network connections and help us analyze the traffic going over cabbles.
- ps, top, free: Show us the number and types of resources used in the system.
- strace: Look at the system calls made by a program.
- strace -0: store the output into a file and then browse the content of that file. The -0 flag, lets us refer back to the file later if we need to so, let's go with that one.
- intrace: Look at the library calls made by a software.
- astrois: 

## 2. Understanding the problem
- A reproduction case:
  -  A way to verify if the problem is present or not.
  -  Make the reproduction case as simple as possible.

- Figuring out what's causing the problem:
  -  Reading the logs available to track and find an error message.
  -  Trying to isolate the conditions that trigger the issue to gain reproduction case.
  -  Finding the root cause.

- Fingding the root cause:
  - Usually, when you have a reproduction case, you still don't know the root cause of the problem.
  - Following a cycle of looking at the information we have, coming up with a hypothesis that could explain the problem, and then testing our hypothesis.
    - If we confirm our theory, we found the root cause. 
    - If we don't, then we go back to the beginning and try different possibility.
  - Need to come up with an idea of a possible cause, check if it's correct and if not, come up with a different idea until we find one that explains the problem.
    - Look at information we currently have and gather more if we need.
    - Searching online for the error messages that we get.
    - Looking at the documentation of the applications involved can also help us.

- Heisenbug:
  - Observer effect: observing a phenomenon alters the phenomenon.
  - When we meddle with them, the bug goes away.
  - These bugs usually point to bad resource management: the memory was wrongly allocated, the network connections weren't correctly initialized, or the open files weren't properly handled.

## 3. Binary search a problem
### 3.1 Definition
- Linear Search:
  - Theory:
    - Start from the first entry and then check if the name is the one that we're looking for.
    - If it doesn't match, move to the second element and check again, and keep going until we find the employee with the name we're looking for, or we get to the end of the list.
  - The time it takes to find the result is proportional to the length of the list.

- Binary Search:
  - Condition: The lists has to be sorted out.
  - Theory:
    - Comparing the name that we're looking for with the element in the middle of the list and check if it's equal, smaller, or bigger.
    - If it's smaller, we look at the element in the middle of the first half. 
    - If it's bigger, we look at the element in the middle of the second half. 

### 3.2 Command
- wc: counts characters, words, and lines in a file.
- wc -l: print the amount of lines in a file.
- head -: print the first lines in the file.
- tail -: print the last lines.


# Week 2: Slowness

# Summary
## 1. Understand Slowness
## 1.1 Why is my computer slow?
A slow computer is likely because you have too many programs running. This takes up a lot of processing power and impacts performance and speed.

- Identifying __the bottleneck__ and Addressing slowness:
  - CPU time
    - Can close other running programs that you don't need right then.
  - Don't have enough space on disk
    - Can uninstall applications that you don't use, or delete or move data that doesn't need to be on that disk.
  - Network bandwidth
    - Stopping any other processes that are also using the network.
We need to make sure that we're actually improving the bottleneck and not just wasting our money on new hardware that will go unused.

- Monitoring the usage of our resources:
  - Linux systems
    - top: see how many processes are running and how the CPU time or memory is being used.
    - iotop, iftop: see which processes are currently using the most disk IO usage or the most network bandwidth
  - MacOS
    - Activity Monitor: lets us see what's using the most CPU, memory, energy, disk, or network
  - Windows
    - Resource Monitor and Performance Monitor: analyze what's going on with the different resources on the computer including CPU, memory, disk and network

## 1.2 How computers use resources
When an application is accessing some data, the time spent retrieving that data will depend on where it's located.
- If the data will be in the __CPU's internal memory__, and our program will retrieve it really fast.
- If the data will be in __RAM__, our program will still get to a pretty fast.
  - RAM is limited.
  - When you run out of RAM:
    - The OS will just remove from RAM anything that's cached, but not strictly necessary.
    - If there's still not enough RAM after that, the operating system will put the parts of the memory that aren't currently in use onto the hard drive in a space.
- If the data will be in __a file__, our program will need to read it from disk, which is much slower than reading it from RAM.
- Reading data from over the __network__, we have a lower transmission speed.

Three possible reason for a machine being slow due to swapping:
- There are too many open applications and some can be closed, some of them aren't needed. '
- The available memory is just too small for the amount that computer is using, consider upgrading RAM.
- One of the running programs may have a memory leak.

## 1.3 Possible Causes of Slowness
Slow when starting up:
- Cause: it's probably a sign that there are too many applications configured to start on boot.
- Solving: going through the list of programs that start automatically and disabling any that aren't really needed.

Slow after days of running just fine, and the problem goes away with a reboot:
- Cause: there's a program that's keeping some state while running that's causing the computer to slow down.
- Solving:
  - Change code.
  - If you don't have access to the code, another option is to schedule a regular restart to mitigate both the slow program and your computer running out of RAM.

## 2. Slow Code
We should always start by writing direct code that functions as it should. Only try to expedite if it does make a difference. Try to evalute the time difference it takes to run a code versus the length of time needed for it to be written.

- How we can make our code more efficient?
  - If we want our code to finish faster, we need to make our computer do less work, and to do this, we'll have to avoid doing work that isn't really needed.
    - Storing data that was already calculated to avoid calculating it again using the right data structures for the problem and reorganizing the code so that the computer can stay busy while waiting for information from slow sources like disk or over the network
  - Figuring out where our code is spending most of its time
    - __Profiler__: a tool that measures the resources that our code is using, giving us a better understanding of what's going on, help us see how the memory is allocated and how the time spent.

Using the right Data Structures:
- If you need to access elements by position or will always iterate through all the elements, use a list to store them.
- If we need to look up the elements using a key, we'll use a dictionary.

Expensive Loops:
- Need to think about what actions we're going to do inside the loop, and when possible, avoid doing expensive actions.
- If you do an expensive operation inside a loop, you multiply the time it takes to do the expensive operation by the amount of times you repeat the loop.

- How you access the data inside the loop?
  - If you store the data in a file, your script will need to parse the file to fetch it. It will be unnecessary and time-consuming if the script reads the whole file everytime. 
  - Instead, you could parse the file outside of the loop, put the information into a dictionary, and then use the dictionary to retrieve the data inside the loop.


# Week 3: Crashing programs

# Summary
## 1. Introduction  
### 1.1 What is crashing?  
A program terminates unexpectedly, a device reboots for no apparent reason, the operating system hangs and we lose all our unsaved work.  
Generally, the cause of these crashes is that the software ran into an unexpected situation, a state that the developers didn't anticipate. Because these are unexpected situations, they can be triggered by very broad range of things:
- It could be a hardware problem, like a broken ramjet that causes a program to get invalid data when trying to access the memory.  
- There could be a bug in some part of the code, which does an unsupported operation, like trying to read an element from an empty list. 
- It could be an issue in the overall system, like if a program expects a certain library to be present or a certain directory to exist, but they don't or there could be a problem with the input provided by the user.

__Steps__:
- Techniques to understand the root causes and fix the problems, or at least lessen the damage.  
- Dealing with complex systems.  
- Document a problem and its solutions. Writing postmortems.  

### 1.2 Systems that crash.
A program that terminates unexpectedly, we go through our usual cycle of:
- Gathering information about the crash:
  - Reduce the scope of the problem, start with the actions that are easier and faster to check. 
  - Looking at the logs to see if there's any error that may point to what's happening.
  - Check if the user can reproduce the problem by doing this same action on a different computer.
  - If this happens reliably. Do all invoice generations fail? Is it confined to one specific product or customer?
  - To further reduce the scope, you'll want to know if it's just that application or the whole system. To check this out, you can try moving away the local configuration for the program and using the default configuration instead, or maybe even reinstalling the application.
  - The hardware or the OS causes the problem

- Find the root cause:
  - Look at the log: system log files and `/var` log or the user log files on Linux; Mac OS Console app; Event Viewer on Windows.
  - Extra log: strace on Linux, dtruss on MacOC, Process Monitor on Windows.
  - Figure out what changed might cause the error: New version of the program -> Change log on Version Control System.
  - Create the smallest possible reproduction case. Remember we want to make the reproduction case as small as possible this lets us better understand the problem and also quickly check if its present or not when we attempt to fix it. Even if we end up unable to fix the issue having a small and simple reproduction case is extremely helpful in reporting a bug to the program's developers.
  - After doing all of this, we should have some idea of what the root cause of the issue is and maybe even how to fix it.
- Applying the right fix:
  - Our code: Debug the program and fix the bug. Other's code: If we can't change/rewrite the program, find the way to work around.
  - Possible ways of fixing:
    - The input doesn't match the format: Provide a Wrapper, a Proxy that acts as compatibility layer.
    - Overall system environment: Dynamic libraries from different OS. Workaround: Running the application inside a Virtual Machine or a container.
    - Can't find a way to stop an application from crashing but we can make sure that if it crashes it starts back again: Deploy a watchdog - Checks whether a program is running and when it's not, starts the program again. Doing this won't avoid the crash itself. But it will at least ensure that the service is available.
    - Remember to _always_ report the bug to the application developers, include as much information as possible, share good reproduction case.
# -
## 2. Code that crashed
### 2.1 Accessing Invalid Memory
- Memory assigned for a process. C/C++ Pointers.
- We're usually dealing with undefined behavior.
- Possible Errors:
  - Forgetting to initialize a variable 
  - Trying to access a list element outside of the valid range
  - Trying to use a portion of memory after having given it back 
  - Trying to write more data than the requested portion of memory can hold
  - ...  
- Best way to understand: Attach a debugger to the faulty program.
- __Valgrind__ (on MacOS and Linux) is a very powerful tool that can tell us if the code is doing any invalid operations no matter if it crashes are not. Valgrind lets us know if the code is accessing variables before initializing them. __Dr. Memory__ is a similar tool that can be used on both Windows and Linux. 

### 2.2 Unhandled Errors and Exceptions
- If your program is crashing with an unhandled error, you want to first do some debugging to figure out what's causing the issue. 
- Add statements that print data related to the codes execution. Statements like these could show the contents of variables, the return values of functions or metadata like the length of a list or size of a file. This technique is called __printf debugging__
--- 
- Once you figured it out, you want to make sure that you fix any programming errors and that you catch any conditions that may trigger an error. This way, you can make sure the program doesn't crash and leave your users frustrated
-  Instead of crashing unexpectedly, you want the program to inform the user of the problem and tell them what they need to do. 
- Modify the code to catch that error and tell the user what the permission problem is so they can fix it
### 2.3 Fixing Someone Else's Code
- Spend some time getting acquainted with the code so that we can understand what's going on.
- Writing comments
- Writing tests

- Focus on the functions or modules that are part of the problem that you're trying to fix:
  - Start with the function where the error happened
  - Then the function or functions that call it, and so on ... until you can grasp the contexts that led to the problem.
### 2.4 Debugging a C Segmentation Fault / Python Crash
- C:
  - GDB debugger: backtrace, up, list, print <symbol>
  - Off-by-one error
- Python:
  - pdb3: next, continue

### 2.5 Resources for Debugging Crashes
# -
## 3. Handling Bigger Incidents
### 3.1 Crashes in Complex Systems
- Example of an e-commerce site: 
  - Checking the log. 
  - Finding the log related to the service. 
  - Separating the changes, rollbacking the suspicious changes.
  - Removing faulty servers from the pool, or deploying new servers on demand
- On-cloud services

### 3.2 Communication and Documentation
- Document what you're doing in a bug or ticket
### 3.3 Efective Postmortems
- Postmortems: Documents that describe details of incidents to help us learn from our mistakes. It helps us avoid dealing with them again or at least learn how to deal with the next incident better.
- Document what happened, why it happened, how it was diagnosed, how it was fixed, and finally figure out what we can do to avoid the same event happening in the future.
- What should you write in a postmortem?
  - What the impact of the issue was.
  - How it got diagnosed.
  - The short-term remediation you applied.
  - The long-term remediation you recommend.
  - A summary that highlights: 
    - The root cause
    - The impact
    - What needs to be done to prevent the issue from happening again
- Certain tools or systems available:
  - Solve the problem quickly by doing a roll back to the previous version.
  - Before users even noticed it because we had good monitoring and alerting.
  - ...
- Writing a postmortem can sometimes help you understand the services that you're working with much better.
# -
# Week 4: Managing resources

## 4.1 Managing Computer Resources
### 4.1.1 Memory leak
- Memory leak: A chunk of memory that's no longer needed is not released
- Possible problems:
  - A program uses a lot of RAM, other programs will need to be swapped out and everything will run slowly.
  - If the program uses all of the available memory, then no processes will be able to request more memory, and things will start failing in weird ways.
- Memory leaks are less of an issue for programs that are short lived, but can become especially problematic for processes that keep running in the background.
- Memory leaks caused by a device driver, or the OS itself: Only a full restart of the system releases the memory
- What can we do if we suspect a program has a memory leak? We can use a memory profiler to figure out how the memory is being used:
  - C/C++: Valgrind
  - Python ... : 
  - Help us identify which information we're keeping in memory that we don't actually need.
### 4.1.2 Managing Disk Space
- Disk space:
  - Installed binaries and libraries
  - Applications' data
  - Cached information
  - Logs
  - Temporary files or backups
- System performance decreases as the available disk space get smaller - Data fragmented, Programs crashed while storing data
- Solutions:
  - Uninstalling applications
  - Cleaning up old data
  - Adding more drive
- Checking if some apps filling disk with useless data
  - Disk usage by applications
  - Users' mailboxes
  - Log/temporary files: Some programs keep logging error messages, temp files that wouldn't be cleaned up ...

### 4.1.3 Network Saturation
- Latency: The delay between sending a byte of data from one point and receiving it on the other. This value is directly affected by the physical distance between the two points and how many intermediate devices there are between them.
- Bandwitdh of the connection: How much data can be sent or received in a second. This is effectively the data capacity of the connection.
- Available bandwidth: 

















