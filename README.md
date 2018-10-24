# Indeed-Web-Scrapping-Analysis-and-Salary-Prediction
In this project, I scraped Indeed.com for data on job titles, salaries, locations, summaries of job description, analyzed the data I scraped and predicted salary using random forest binary classifier.

In this notebook, I will analyze the job data I scraped from Indeed.com for data scientist position from my list of cities. While most listings DO NOT come with salary information (as you will see in this exercise), being to able extrapolate and predict the expected salaries from other listings can help guide negotiations or at least an insight of what to expect if you are new to the job market like me. 

Normally, regression could be used for a task like this; however, since there is a fair amount of natural variance in job salaries, I approached this as a classification problem using random forest classifier.

### Overview of data :
* There are 630,988 results found for Data Scientist from my list of 86 cities. 
* 590,466 jobs (93.58%) with no salary
* 615,441 (97.54%) of the entries are duplicated
* The salaries are given as text and usually with ranges

### Results:
The accuracy score and across validation score of each Random Forest models shown below:

|Features|Accuracy|Cross Validation|
|------|------|------|
|City|0.655|0.538 ± 0.108|
|Summary|0.704|0.731 ± 0.065|
|Title|0.805|0.804 ± 0.057|
|All 3 above|0.81|0.77 ± 0.073|
