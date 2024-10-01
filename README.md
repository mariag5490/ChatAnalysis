Ferocia Code Exercise Data Engineer


Data governance
Please write some commentary about what you would consider or how you would
approach data quality and sensitivity as part of ingesting and managing data in a
data warehouse. We’re looking to get a picture of how you would discover and
solve problems which would prevent the safe and effective use of data by the
teams at Ferocia.

Data governance is very critical in a Data warehouse to ensure data quality and to protect sensitive information. A systematic approach can reduce risks and enhance decision-making.

-> Define a proper Data Governance framework that involves clearly defined policies regarding data handling, quality standards and sensitivity requirements. It should include data classification and usage guidelines 
-> Continuously access the quality of data for its completeness and validity. This can be automated using scripts to run periodic checks on incoming data during ingestion (check for duplicates, conformance to the data types and formats, missing data, null handling). Data profiling can help us understand outliers or inconsistent data.
-> Set up monitoring tools to alert data stewards when quality issues are detected and a root cause analysis can be done to prevent future issues.
-> When possible correct invalid data based on business rules. If data can not be corrected there should be proper mechanisms to delete or archive them.
-> Categorize sensitive information based on its sensitivity and then implement Role based Access controls to control access to data. Encrypt sensitive data to prevent unauthorized acceses 


Quality

Data is seldom ever neat and tidy. Providing clean, consumable, trusted data to
the teams in the business is an an important part of managing a data warehouse.
There are a number of issues which could be present in the chats and categories
files which would affect their quality, correctness, completeness, etc.
1. How would you measure the overall data quality of these files?
2. What measures would you put in place to identify issues which would effect
data quality?
3. What would you do with invalid data that is identified?


It is important to ensure quality of data since it not only improves performance but enhance the reliability of data in data warehouse.

1. How would you measure the overall data quality of these files?
-> measure the proportion of missing and null values in key field
-> the number of duplicate records in the dataset
-> check if the data type of fields conforms to formats and rules
-> check for valid date formats in the date time fields

2. What measures would you put in place to identify issues which would effect
data quality?
-> implement automated scripts to regularly check for duplicates and null key fields 
-> use data profiling tools that generates insights about data quality
-> create dashboards to visualize key metrics related to data quality

3. What would you do with invalid data that is identified?
-> Correct invalid data if possible with business rules and logic
-> fill the null or missing values with appropriate data
-> Flag the incorrect data for further investigation


Sensitivity

It’s also important to ensure the safe-keeping of data which can contain sensitive
information. Given that chat sessions will contain open text from customers (not
included in the provided schema), there is a risk that sensitive data may be
included in chat messages. Examples of sensitive data could be: credit card
numbers, passport identifiers, phone numbers, names, email addresses, drivers
licences, etc.
1. What measures will need to be taken in controlling access to this open text
data?
2. What measures would you put in place regarding its secure storage?
3. If redaction of sensitive text was necessary, how would you tackle it?


Safe-keeping of Data is very important to maintain privacy and to be compliant with regulations.
1. What measures will need to be taken in controlling access to this open text
data?

-> Role based access to control the access to sensitive data. Access should be granted to data based on their roles.
-> Multi Factor Authentication to verify the user
-> Audit logs should be maintained to record the history of data accessed
-> Masking of sensitive information in a way unauthorized users will not be able to get this information 

2. What measures would you put in place regarding its secure storage?

-> Encrypt sensitive data stored in file systems and data bases
-> Categorize the data based on sensitivity and store sensitive data in a more secure environment
-> Use access controls and row-level security in databases 

3. If redaction of sensitive text was necessary, how would you tackle it?

-> Identify sensitive information in chats using regular expressions by creating a list of patterns that represent sensitive data. Replace the sensitive data with **** and names of customers can be made generic



Data Pipeline

Title : Real-Time Customer Chat Analysis using PySpark

Overview:
This project implements a chat analysis system with a focus on processing the chat streams, transforming them to understand important metrics and then store the results for reporting. The goal is to enable business to understand peaks in customer interactions via chats in different subject categories. With the help of this analysis, the customer service agent rosters are updated so that more agents can be available during peak hours. This in turn helps to respond to customer queries more efficiently and in a planned manner.

Problem Statement
Business Struggle to derive insights from large volumes of raw unformatted data. This project tackles the issue by creating a real-time processing pipeline that understanding customer requirement and provide assistance and availability in a scalable manner.



Technology Stack

Programing Language : Python
Framework : Apache PySpark
IDE : PyCharm
Database : HDFS/S3/PostgresSQL (configurable for source)
Other Libraries : Spark Streaming (not implemented)

Data Sources 

The project processes chat and category data in the format of csv. The source from where the data is fetched is made configurable to read from local, s3, hdfs or a database. 

Architecture 

Ingestion : Data is ingested from local csv files using PySpark. The pipeline is designed to handle different data sources using 'chat.conf'. The source contains the specific paths and configurations for different sources. The source is passed as an argument during run

Data Cleansing : Preprocess and clean the incoming data to remove duplicates, invalid categories and data with inconsistent date formats. The timestamp formats are also changed to AUS/MEL timezone

Data Transformation : 7 different transformations are done to develop the metrics for analysis.

Output Writer : The result of Analysis (7 metrics) is written to specific files( 7 metrics files) in the path output/chat_analysis

Unit Testing : Unit test cases are stored in the path test/test_chat_analysis. Individual test files are created for each module. Tests are done based on sample data created for chat and categories in test_data folder.

Performance Monitoring : Implemented logging and monitoring key parts of the pipeline to track stages and errors. We can use Spark UI for monitoring performance

Code Reusability and Maintainability : Modular code is developed to separate logic. Configurations are stored in external files for flexibility. 

Error Handling : Wrapped each major function with a try-except block to catch and log errors.

Schema Enforcement is ensured by defining schemas for chat and category data to ensure data consistency

Run : 2 input arguments are given; one for spark env (local) and the other for source env (local)



Result
The output of the pipeline provides 7 different metrics which helps in identifying the customer peak hours and categories. It also throws insights to the time taken for resolving multiple categories and hence helps the agents to create more know how in the difficult categories.

Future Enhancements:
1) To make the source more flexible by adding kafka and other remote sources
2) To make the data writer more flexible so that the output can be written into a configurable source like s3, hdfs or databases
3) To implement the same in medallion architecture in Databricks to seamlessly stream incremental data and update aggregates.
4) Perform integration testing for end-to-end debugging and confirm the streaming aggregates.



