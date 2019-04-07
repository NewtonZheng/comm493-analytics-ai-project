# comm493-analytics-ai-project
Final COMM493 Analytics and AI for Business Project

[Video Demo Link](https://youtu.be/aSixoxLwBRk)

There are two ways to run the code below:
1. Run using JupyterLab
2. Run using localhost

# To run in JupyterLab
cd the folder that contains all the coding files in this Github repository
Change the port in FinalCodev6.py to the appropriate port for your JupyterLab

Then run the following code:

'''
python3 FinalCodev6.py

'''

# To run locally

In FinalCodev6.py, change 'from watson_developer_cloud import DiscoveryV1' to 'from ibm_watson import DiscoveryV1'

Run the following code in command terminal to set up the Python virtual environment, flask, and IBM Watson:

'''
python -m venv env
env\Scripts\activate
pip install flask
pip install --upgrade "ibm-watson>=3.0.3"
'''

If you already have a virtual Python environment set up with Flask and IBM Watson installed, you can run the following code:

'''
set FLASK_APP=FinalCodev6.py
flask run

'''

Open localhost:5000 (http://127.0.0.1:5000/) on your browser to launch program

Control C to exit program in command terminal