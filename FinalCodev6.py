#Added in multiple features

import os
from flask import Flask, jsonify, request
from urllib import request as req

#Imports the Discovery Functionality
from watson_developer_cloud import DiscoveryV1

#This sets up the app as a flask app
app = Flask(__name__)

#Here are the API keys to call Watson
discovery = DiscoveryV1(
    version='2019-03-27',
    iam_apikey='4Abib3S5BvlEpbz82Jrqab4eecxe-QrT5OuihaxOrh7E',
    url='https://gateway.watsonplatform.net/discovery/api'
)

@app.route('/') #Links to html home page
def Welcome():
    return app.send_static_file('index.html')


@app.route('/process', methods=['POST'])
def process():

    #The full list of 22 sample courses used in IBM Watson Discovery. If the query runs and the following course IDs are found in the PDFs of the query, then it returns just the ID of the course rather than the content of the entire PDF
    course_list = ['ANAT 100', 'ARTH 250', 'BCHM 218', 'BIOL 102', 'BIOL 103', 'BIOL 350', 'CISC 101', 'COGS 100', 'DEVS 100', 'ENIN 140', 'FILM 240', 'FILM 260', 'GNDS 120', 'GNDS 215', 'HIST 125', 'HIST 263', 'HIST 270', 'HLTH 200', 'HLTH 230', 'MATH 121', 'PHGY 170', 'PSYC 205']

    #Queries for courses with NO EXAMS AND GROUPS
    if (request.form['exam'] == 'no' and request.form['name'] == 'no'):
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'text:!proctored, group'))

        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

         #Return the course results and the appropriate message to the HTML front end

        return jsonify({
            'course_output' : filtered_course_list,
            'text_output' : 'SUCCESS! The following courses have NO EXAMS and NO GROUP WORK: ',

        })

    #Queries for courses with EXAMS AND GROUPS
    elif (request.form['exam'] == 'yes' and request.form['name'] == 'yes'):
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'text:final, exam, proctored, group'))

        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        return jsonify({
            'course_output' : filtered_course_list,
            'text_output' : 'SUCCESS! The following courses have BOTH EXAMS and GROUP WORK: ',

        })

    #QUERY for courses with GROUP WORK BUT NO EXAMS

    elif (request.form['exam'] == 'no' and request.form['name'] == 'yes'):
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'text:!"proctored",text:"group"'))

        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        return jsonify({
            'course_output' : filtered_course_list,
            'text_output' : 'SUCCESS! The following courses have GROUP WORK BUT NO EXAMS: ',

        })

    #QUERY for courses with EXAMS BUT NO GROUP WORK
    elif (request.form['exam'] == 'yes' and request.form['name'] == 'no'):
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'text:"proctored",text:!"group"'))

        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        return jsonify({
            'course_output' : filtered_course_list,
            'text_output' : 'SUCCESS! The following courses have EXAMS BUT NO GROUP WORK: ',

        })




    #Queries for courses with NO EXAMS

    elif request.form['exam'] == 'no':
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'text:!proctored'))

        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        return jsonify({
            'course_output' : filtered_course_list,
            'text_output' : 'SUCCESS! The following courses have NO EXAMS: ',

        })

    #Queries for courses with EXAMS

    elif request.form['exam'] == 'yes':
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'text:final, exam, proctored'))

        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        return jsonify({
            'course_output' : filtered_course_list,
            'text_output' : 'SUCCESS! The following courses have EXAMS: ',

        })


    # Queries for courses with GROUP WORK
    elif request.form['name'] == 'yes': 
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'text:group'))

        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        return jsonify({
            'course_output' : filtered_course_list,
            'text_output' : 'SUCCESS! The following courses have GROUP WORK: ',

        })


    # Queries for courses with NO GROUP WORK
    elif request.form['name'] == 'no':
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'text:!group'))

        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        return jsonify({
            'course_output' : filtered_course_list,
            'text_output' : 'SUCCESS! The following courses have NO GROUP WORK: ',

        })
    else:
        return jsonify({'error' : 'Error: No preferences selected. Try again!'})

#END OF SEARCH QUERIES

port = os.getenv('PORT', '5020')

if __name__ == "__main__":
    app.run(port= int(5020), debug=True)
