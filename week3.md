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