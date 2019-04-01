import os
from flask import Flask, jsonify, request
from urllib import request as req

#Imports the Discovery Functionality
from watson_developer_cloud import DiscoveryV1

#We are setting the rootpath for our website
app = Flask(__name__)

discovery = DiscoveryV1(
    version='2019-03-27',
    iam_apikey='4Abib3S5BvlEpbz82Jrqab4eecxe-QrT5OuihaxOrh7E',
    url='https://gateway.watsonplatform.net/discovery/api'
)

@app.route('/') #Links to root directory
def Welcome():
    return app.send_static_file('index.html')


@app.route('/process', methods=['POST'])
def process():

    course_list = ['ANAT 100', 'ARTH 250', 'BCHM 218', 'BIOL 102', 'BIOL 103', 'BIOL 350', 'CISC 101', 'COGS 100', 'DEVS 100', 'ENIN 140', 'FILM 240', 'FILM 260', 'GNDS 120', 'GNDS 215', 'HIST 125', 'HIST 263', 'HIST 270', 'HLTH 200', 'HLTH 230', 'MATH 121', 'PHGY 170', 'PSYC 205']
    

    # Queries for courses with group work
    if request.form['name'] == 'yes': # Corresponses with line 52 in index.html
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'group')) 

        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)
        
        return jsonify({'name' : filtered_course_list})
    else:
        return jsonify({'error' : 'Error: No preferences selected. Try again!'})    
         
   #     print('The following courses have been identified as group-oriented courses:', ", ".join(filtered_course_list), end=".")
                

@app.route('/search', methods=['POST']) #WIP
def search():
    
    course_list = ['ANAT 100', 'ARTH 250', 'BCHM 218', 'BIOL 102', 'BIOL 103', 'BIOL 350', 'CISC 101', 'COGS 100', 'DEVS 100', 'ENIN 140', 'FILM 240', 'FILM 260', 'GNDS 120', 'GNDS 215', 'HIST 125', 'HIST 263', 'HIST 270', 'HLTH 200', 'HLTH 230', 'MATH 121', 'PHGY 170', 'PSYC 205']
    
    # Queries for courses with exams
    if request.form['output1'] == '1': # Corresponses with line 44 in index.html
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'final, exam, proctored'))

        filtered_course_list = []
        
        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        print('The following courses have been identified as courses with exams:', ", ".join(filtered_course_list), end=".")

    # Queries for courses with no exams
    elif request.form['output1'] == '2': # Corresponses with line 45 in index.html
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'text:!proctored'))

        filtered_course_list = []
        
        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        print('The following courses have been identified as courses with no exams:', ", ".join(filtered_course_list), end=".")
    
    # Queries for courses with or without exams
    elif request.form['output1'] == '0': # Corresponses with line 43 in index.html
        # my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'final, exam, proctored)) # Not quite clear what the functionality of this option is.

        filtered_course_list = []
        
        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        print('The following courses have been identified as courses with or without exams:', ", ".join(filtered_course_list), end=".")
        
    # Queries for courses with group work
    elif request.form['course_selection'] == '4': # Corresponses with line 52 in index.html
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'group')) 

        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)
        
        print('The following courses have been identified as group-oriented courses:', ", ".join(filtered_course_list), end=".")

    # Queries for courses with individual work
    elif request.form['output1'] == '5': # Corresponses with line 53 in index.html
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'text:!group'))

        filtered_course_list = []
        
        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        print('The following courses have been identified as courses without group work:', ", ".join(filtered_course_list), end=".")
        
    # Queries for courses with group work or individual work
    elif request.form['output1'] == '3': # Corresponses with line 51 in index.html
        # my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'final, exam, proctored')) # Not quite clear what the functionality of this option is.

        filtered_course_list = []
        
        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        print('The following courses have been identified as courses with group work or individual work:', ", ".join(filtered_course_list), end=".")

    # Returns filtered course list to page
    return jsonify(filtered_course_list)

port = os.getenv('PORT', '5019')

if __name__ == "__main__":
    app.run(port= int(5019), debug=True)