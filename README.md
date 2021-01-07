# SafeAir

### Table of contents
 - [Description](#description)
 - [Requirements](#requirements)
 - [How to use](#how-to-use)
 - [What needs to be added before production](#needs-to-be-added)
 - [Further suggestions](#further-suggestions)
 
 ---
 
 ## Description
 Data Analytics platform is a processing pipeline that works in the following way: 
 1. Data is inputted to the processing stack (data_stack.py) - At this time of submission, as the API was not active, the data is being read from the file device_data.
  1. The stack is LIFO, implying that the latest data is processed first. It assumes that the data is being fed to it in a time chronological manner.
 2. The stack then sends the reading (one by one) to the pollutant analytics engine (pollutanta_data/analytics.py) and the index engines (index_analytics/[ENGINE_NAME].py). 
  2.1 The pollutant analytics engine computes the pollutant analytics and sends it to the consolidator (analytics_consolidator.py).
  2.2 Index engines compute the value of the indices and sends it to the alert engine (index_analytics/analytics.py - which is a classifier of the index values). The alert engine uses user_settings.py to read the index operational ranges set by the user.
 3. The alert engine appends the index value and the alert analytics for the index and sends it to the consolidator. 
 4. The consolidator then collects the pollutant analytics and the index analytics and appends to the reading and sends it to the output writer.
 5. The output writer outputs the analytics into the JSON format in the file output/output.data
 
 ## Requirements
 
 ## How to use
 
 ## What needs to be added before production
 
 ## Further suggestions
 
 
 
 
 
 
 
