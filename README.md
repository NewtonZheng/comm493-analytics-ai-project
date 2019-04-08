# comm493-analytics-ai-project
Final COMM493 Analytics and AI for Business Project
Product: Inquiry
[Video Demo Link](https://youtu.be/aSixoxLwBRk)

# What does InQuiry do? 

InQuiry is a web app that provides Queen's University students with a way to search for online Arts & Science courses based on their group and exam preferences. Once the user inputs a “yes” or “no” into the preference fields, the application generates a query to IBM Watson's discovery tool. IBM Watson will use the discovery tool to scan through the PDFs of a sample of 22 online Queen's courses, where a list of courses relevant to the filtered search will be returned to the web interface.

InQuiry is built with Python, IBM Watson, Javascript, HTML, and CSS.

# How to run the code in this Github Repository

There are two ways to run the code in this Github repository:
1. Run using JupyterLab
2. Run using localhost

# To run in JupyterLab
cd the folder that contains all the coding files in this Github repository. 
Change the port in `FinalCodev6.py` to the appropriate port for your JupyterLab (current port is 5020).

Then run the following code:

```
python3 FinalCodev6.py

```

# To run locally

In `FinalCodev6.py`, change `from watson_developer_cloud import DiscoveryV1` to `from ibm_watson import DiscoveryV1`

Run the following code in command terminal to set up the Python virtual environment, flask, and IBM Watson:

```
python -m venv env
env\Scripts\activate
pip install flask
pip install --upgrade "ibm-watson>=3.0.3"
```

If you already have a virtual Python environment set up with Flask and IBM Watson installed, you can run the following code:

```
set FLASK_APP=FinalCodev6.py
flask run

```

Open localhost:5000 (http://127.0.0.1:5000/) on your browser to launch program.

Control C to exit program in command terminal.
