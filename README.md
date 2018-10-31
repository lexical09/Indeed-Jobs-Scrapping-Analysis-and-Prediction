# Indeed-Web-Scrapping-Analysis-and-Salary-Prediction
I scraped Indeed.com for data on job titles, salaries, locations, summaries of job description, analyzed the data I scraped and predicted salary using random forest binary classifier.

Most listings do not come with salary information, but being to able extrapolate and predict the expected salaries from other listings can help guide negotiations or at least get an insight of what to expect if you are new to the job market like me. 

### Overview of data :
* There are 630,988 results found for Data Scientist from my list of 86 cities. 
* 590,466 jobs (93.58%) with no salary
* 615,441 (97.54%) of the entries are duplicated
* The salaries are given as text and usually with ranges

### Results:
The accuracy score and across validation score of each Random Forest models:

|Features Used|Accuracy|Cross Validation|
|------|------|------|
|City|0.655|0.538 ± 0.108|
|Summary|0.704|0.731 ± 0.065|
|Title|0.805|0.804 ± 0.057|
|All 3 above|0.81|0.77 ± 0.073|

Below are the predicticted salary for each feture used:

#### City

![](./images/city.png)

#### Job Summary

![](./images/summary.png)

#### Job Title

![](./images/title.png)

#### Combination of city, job summary and job title:

![](./images/combination.png)


