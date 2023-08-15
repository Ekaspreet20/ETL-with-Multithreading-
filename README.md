# ETL-with-Multithreading

Welcome to the world of data manipulation and optimization! In this project, we explored a fascinating technique called ETL. ETL stands for Extract, Transform, and Load – a way to handle data. 

It is like a puzzle where we take pieces of information, rearrange them, and combine them in a new way.
In our journey, we compared three ways of doing a task:

1. **Using SQL queries:** It's like asking a smart database to give us the pieces we need.
2. **Using the File System:** Here, we're like a craftsperson, organizing small parts into a bigger picture.
3. **Using Multi-threading:** Think of it as having multiple workers simultaneously doing parts of the puzzle.

To make things even more interesting, we figured out the best number of workers (threads) to do the job efficiently. It's like having the right number of people working together so they don't get in each other's way.

A **thread** is the smallest sequence of instructions that a scheduler can manage independently. It is a component of a process. Multiple threads can exist within the same process, executing concurrently and sharing resources such as memory.

### WHY MULTI-THREADING?
-Parallelism and Improved Performance
######
-Responsiveness
######
-Resource Sharing
######
-Efficient Resource Utilization
######
-Real-time Systems
######
-Faster execution
######
-Easy Communication
######

## RESULT:
On comparing the time taken by three methods for different sets of data(1 lakh, 5lakh, 7lakh, 10lakh, 50lakh, 1Cr, 2Cr, 3Cr, 4Cr, and 5Cr), it is found that Multithreading takes the least time. 
##### 
Case 1 - Using SQL queries
##### 
Case 2 - Using File System
##### 
Case 3 - Using Multi-threading
##### 

<img src="https://github.com/Ekaspreet20/ETL-with-Multithreading-/assets/65918628/7c766615-f166-4285-94ac-328efed7b119" width="600" />

### Snippet of data:-
#### BEFORE:
<img src="https://github.com/Ekaspreet20/ETL-with-Multithreading-/assets/65918628/e9b92274-740d-432a-be83-dc5508084dd0" width="600" />

#### AFTER:
<img src="https://github.com/Ekaspreet20/ETL-with-Multithreading-/assets/65918628/86dc2628-cec5-4924-8ae8-9032a68a64ff" width="600" /> 

