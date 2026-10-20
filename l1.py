"""

::::::::::::::::::::::::::: JMETER :::::::::::::::::::::::::::


1.  Apache Jmeter is pure java open source software, which was first developed by stefano mazzocchiof the apache software foundation, designed too load test functional behaviour and measure performance. 

2.  you can use Jmeter to analyze and mmeasure the peformance off web application or a variety of services.

3.  Performance testing means testing a web application against heavy load , multiple and concurrent traffic.

4.  Jmeter originally used for testing web appliation oof fpt applications.Nowadays, it is used for functional test, database server test and API testing etc.   


>>  Open source
>>  Friendly GUI
>>  Platform independent
>>  Full Multi-threading framework
>>  Visualiize test results
>>  easy installation
>>  highly extensible.
>>  Unlimited testing capabilities
>>  support multiple protocols


WorkFlow:

step 1:  Send request to target servers
step 2:  Get statistics information of target server
step 3:  Generate test reports in different format


Variables in Jmeter:

${variable_name}  :  It is used to reference a variable in jmeter.
like:  country = Delhi,   ${country}








::::::::::::::::::::::::::: ASSERTIONS :::::::::::::::::::::::::::

Assertions helps to verifies that your server under test returns the expected results.

Types of Assertions: 

1.  Response Assertion
2.  Duration Assertion
3.  Size Assertion
4.  XML Assertion
5.  HTML Assertion
7.  Xpath Assertion
6.  XML Schema Assertion
8.  Json Assertion






::::::::::::::::::::::::::: LISTENERS :::::::::::::::::::::::::::








::::::::::::::::::::::::::: COMPONENTS :::::::::::::::::::::::::::


1.  Thread Groups

    Collection of threads. each thread reppresents one user using the application under test.  Each thread simulates one real user request to the server.
    
    The control for a thread group allow you to set the number of threads for each group.
    
    Example: if you set the number of threads as 100, Jmeter will create and simulate 100 user requests too the server under test.    


2.  Samplers

    Samplers are different types oof reqquest send by thread groups
    Like: HTTP, FTP, JDBC Request etc
    

3.  Listeners.

    It shows the resullts of the test execution.
    They can show results in a different format such as tree, table, graph or log file.
    
    Like:  
    Graph shows results on graph.
    Tree shows a HTML Format.
    Table shows as in tablee format.
    Log shows summary in text file. 


4.  Configuration Elements

    Set up deffaults and variables for later use by samplers.
    Commonly used configurations elements in jmeter.    


5.  Timers

    Jmeter sends requests without applying any delay between each sampler/request.
    It perform lead /stress testing on your server without any delay, it will be overloaded. Then it won't be able to give you realistic results annd fail to simulate real world user traffic experience.
    Jmeter timers are the solution to all these problems.
    Timer element can be added in test plan to apply wait between each sampler/request.

    Types of Timer
    
    1.  constant :  Fixed

    2.  Uniform randon timer    :   
    
        Random delay max
        constant delay offset
           
        0.X * random delay max + constant delay offset
        
        x = 0-9
        
        example:    0.X * 100 + 0
                    0-99 milli sec

    
    3.  BSF timer
    4.  JSR223 timer
    5.  Beanshell timer
    6.  Gaussian random timer :  time delay according to gaussain formula

    according to all pattern timers formula.


6.  Controllers

    Let you handle the order of processing samplers in a thread group. It can be used to control the flow of the test execution.
    It decide "when and how" to send the requests to the server.
    
    Typees of logic controllers:
    
    >   critical section controller
    >   Foreach controller
    >   if controller               :   execute the request if the condition is true.
    >   loop controller             :   Like for loop in programming, it will execute the request for a number of times.
    >   interleave controller       :   execute one request from the list of requests in a round robin fashion. in next loop, it will execute the next request in the list.
    >   Include controller          :   It allows you to include another test plan in the current test plan.
    >   Module controller           :   It will add a dependency on other controller in the test plan. It will execute the request of other controller in the current test plan. 
    >   Once only controller   
    >   Random controller           :   takes one request randomly from the list of requests.
    >   Random order controller     :   execute the requests in random order.
    >   Recording controller
    >   Runtime controller
    >   Simple controller
    >   Switch controller
    >   Transaction controller
    >   Throughput controller       :   distribute the load to the requests in a thread group according to the percentage of throughput specified for each request. (either     percent or by number of requests)
    >   While controller
    






::::::::::::::::::::::::::: PERFORMANCE TESTING :::::::::::::::::::::::::::


A type of non-functional testing to ensure software application will perform well under their expected workload. It can also be used to determine the scalability and reliability of the application.
The goal is not to find bugs, but to eliminate performance bottlenecks.

Focus:
1.  Speed
2.  Scalability
3.  Stability

Its popularly called as "Performance Testing" or "Load Testing" or "Stress Testing" or "Volume Testing" or "Scalability Testing" or "Soak Testing".


>>  Types

1.  Load Testing        >   check performance under expected load.
2.  Stress Testing      >   check performance under extreme load.
3.  Spike Testing       >   check performance under sudden increase and decrease of load.
4.  Endurance Testing   >   check performance over an extended period.
5.  Volume Testing      >   check performance with a large volume of data.


>>  Performance Testing Problems:

1.  Long Load Time
2.  Poor Response Time
3.  Poor scalability
4.  Bottlenecking
5.  Others like:  CPU, Memory, Network, Disk I/O, OS limitations etc.


>>  Perfrormance Testing process:

1.  Identify the test environment
2.  Plan and design tests
3.  Identify performance acceptance criteria
4.  Configure the test environment
5.  Implement the test design
6.  Execute the test
7.  Analyze and report.


>>  Performance Testing metrics:

1.  Processing usage
2.  Memory usage
3.  Disk time
4.  Bandwidth
5.  Private bytes
6.  committed memory
7.  response time
8.  throughput
9.  Amount of connections pooling
10.  maximum active sessions
11.  hit ratio
12.  hit per second
13.  thread count


>>  Performance Testing Tools:

1.  Apache Jmeter
2.  MicroFocus LoadRunner
3.  NeoLoad
4.  smartMeter LoadNinja








::::::::::::::::::::::::::: PARAMETERIZATION :::::::::::::::::::::::::::

1.  Jmeter internal parameters
2.  Read values from external files like csv, excel, xml, json etc





::::::::::::::::::::::::::: CORRELATION :::::::::::::::::::::::::::

Get the value from the response of one request and use it in another request.
Referencing is done at run time dynamically so it is called dynamic referencing. It is used to handle the dynamic values in the response of a request.
 
 
 




"""



