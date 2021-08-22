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





