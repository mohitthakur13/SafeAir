# SafeAir

### Table of contents
 - [Description](#description)
 - [Requirements](#requirements)
 - [How to use](#how-to-use)
 - [What could and must be added before production](#needs-to-be-added)
 - [Further suggestions](#further-suggestions)
 - [Documentation](#documentation)
 ---
 
 ## Description
 Data Analytics platform is a processing pipeline that works in the following way: 
 <ol>
 <li> Data is inputted to the processing stack (data_stack.py) - At this time of submission, as the API was not active, the data is being read from the file device_data. </li>
<ol> <li>The stack is LIFO, implying that the latest data is processed first. It assumes that the data is being fed to it in a time chronological manner. </li></ol>
 <li> The stack then sends the reading (one by one) to the pollutant analytics engine (pollutanta_data/analytics.py) and the index engines (index_analytics/[ENGINE_NAME].py).
<ol>
<li>The pollutant analytics engine computes the pollutant analytics and sends it to the consolidator (analytics_consolidator.py). </li>
<li> Index engines compute the value of the indices and sends it to the alert engine (index_analytics/analytics.py - which is a classifier of the index values). </li> 
 <li> The alert engine uses user_settings.py to read the index operational ranges set by the user. </li>
</li> 
  </ol>
<li> The alert engine appends the index value and the alert analytics for the index and sends it to the consolidator. </li>
<li> The consolidator then collects the pollutant analytics and the index analytics and appends to the reading and sends it to the output writer. </li>
<li> The output writer outputs the analytics into the JSON format in the file output/output.data </li>
 </ol>
 
 
 ## Requirements
The only requirement is Python 3+ and a few packages within.

 ## How to use
 
 ### Input
 Expected input:
 
<img src='https://github.com/mohitthakur13/SafeAir/blob/master/readme_images/input_reading.png?raw=true' width=600, height=400>

### Output
The output 'data_analytics' is divided into two categories:
<ol>
<li> pollutant_analytics 

<img src='https://github.com/mohitthakur13/SafeAir/blob/master/readme_images/pollutant_analytics.png' width='600'>

The pollutant 'quality' parameter belongs to one of 4 categories: 
<ol>
 <li> out_of_lower_bound - which is ignored</li>
 <li> good</li>
 <li> moderate</li>
 <li> unhealthy</li>
 <li> hazardous</li>
 <li> out_of_upper_bound - which takes the max value from the pollutant ranges (See tech docs.)</li>
 </ol>

'Validity' parameter categorizes the pollutant value into the following
<ol>
 <li> (good, moderate, unhealthy, hazardous) --> VALID</li>
  <li> out_of_lower_bound --> INVALID but is ignored</li>
 <li> out_of_upper_bound --> INVALID but max value is taken</li>
 </ol>
</li>


<li> index_analytics 
<img src='https://github.com/mohitthakur13/SafeAir/blob/master/readme_images/index_analytics.png' width=600>

The 'alert_type', representing the type of alert, is categorized into the following:
<ol>
 <li> out_of_lower_bound - below the operational range of the index set by the user </li>
  <li> in_operational_range - Within the operational range of the index set by the user </li>
  <li> out_of_upper_bound - above the operational range of the index set by the user </li>
 </ol>
 </ol>
 
Note that the pollutant_analytics gives a list of "out of bound" pollutants. This implies that if an index is out of bound, looking at the "out of bound" pollutants will tell which pollutant(s) is causing the index to go out of bound.

#### How to use:
<ol>
<li>Choose how to get the readings from the SafeAir decvice:
<ol>
<li>If directly from API - then configure that by uncommenting the code in main.py </li>
<li>Default - read past data from device_data </li> </ol>
 </li>
 <li> Run main.py </li>
 <li> Once the program is runs successfully, check for the output in a file output.output.data </li>
 </ol>
 
 
 
 ## What could and must be added before production
 <ol>
 <li>Offsets (OPTIONAL): Threshold limit in time after which an alert is issued, meant to cater to accidental jumps in the readings dues to device issues etc. </li>
 <li>
  Alert messages for the user (MUST): The alert analytics parameter 'alert_type' must be mapped to a user understandable and actionable message.
  </li>
 <li>
  User index setting reconfiguration (MUST).
  <ol> 
   <li>
    A threshold based approach is proposed in the google documents that advices to define threshold in amount (number of alerts) and in time (duration) to suggest the user for a re-configuration of operational index ranges. This is not necessarily part of the core data analytics and could also be done separately within the app.
   </li>
  </ol>
  </li>
 <li>Testing (MUST): The data analytics platform must be tested well with the rest of the app before deploying in production.</li>
 </ol>
 
 
 
 ## Further suggestions
 <ol>
 <li>
  Concurrency: No parallel programming have been used. Although since the code is modular the first approach should be to simply run (either using multithreading or asyncio) to run index engines concurrently. Then more advanced approaches could be used for paralleizing over multiple processors if need be.
  </li>
 <li>
  Predictive Engine: As the groundwork for the basic data analytics has been laid, other predictive and recommendation services could be built on top.
 </li>
 </ol>
 
 
 ## Documentation
 Please find the project related documentation in the SafeAir_Docs folder. The files should be imported first to the google drive for reading and editing.
 
 
 
 
 
 
