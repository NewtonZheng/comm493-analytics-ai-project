# ONLY POST

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

@app.route('/search', methods=['POST']) #WIP
def search():

    # Queries for courses with group work
    if request.form['output1'] == 'Group Work':
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'group'))

        course_list = ['CISC 101', 'BIOL 103', 'HLTH 230', ] #COMPLETE COURSE LIST LATER.
        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        print('The following courses have been identified as group-oriented courses:', ", ".join(filtered_course_list), end=".")

    # Queries for courses with exams
    elif request.form['output1'] == 'Exam':
        my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'final, exam, proctored'))

        filtered_course_list = []

        for course_name in course_list:
            if course_name in my_course_query:
                filtered_course_list.append(course_name)

        print('The following courses have been identified as courses with exams:', ", ".join(filtered_course_list), end=".")

    # Queries for courses with no exams
    elif request.form['output1'] == 'No Exam':
                my_course_query = str(discovery.query('812fbe50-c0d5-41dc-80c9-77fc6563cb40', 'b213e90d-6df5-4f68-9456-5ba78da80be1', 'proctored'))

                filtered_course_list = []

                for course_name in course_list:
                    if course_name in my_course_query:
                        filtered_course_list.append(course_name)

                print('The following courses have been identified as courses with exams:', ", ".join(filtered_course_list), end=".")

    return jsonify(filtered_course_list)

port = os.getenv('PORT', '5016')

if __name__ == "__main__":
    app.run(port= int(5016), debug=True)
