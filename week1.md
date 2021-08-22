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
