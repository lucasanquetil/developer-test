# 0. Prerequisite
Before using this project, you will need to have the following installed and set up on your system:

- Python 3.7 or higher
- Flask web framework (version 2.2.3 or higher)

# 1. Installation

1. Clone the repository: `git clone https://github.com/lucasanquetil/developer-test.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the application: either through the command-line or the web usage

# 2. Command-line interface usage
In order to run the command_line interface usage, you should not have to install de dependencies of `requirements.txt`

1. Open a terminal at the project root `developer-test`
2. Run the executable `give-me-the-odds` file with the Millennium Falcon file and the Empire file as arguments
```
./give-me-the-odds examples/example1/millennium-falcon.json examples/example1/empire.json
```

# 3. Web usage
In order to run the command_line interface usage, you do have to install the dependencies of `requirements.txt`

1. Open a terminal at the project root `developer-test`
2. Run the `main.py` file with the Millennium Falcon file as argument to launch the Flask web application
```
python3 main.py examples/example4/millennium-falcon.json
```
3. You should see this page at the adress: http://127.0.0.1:8000
![Index page screenshot of the web application](../resources/1%20index_page.png)
4. You just have to upload your empire.json file
![Index page screenshot of the web application when uploading a file](../resources/2%20upload%20file.png)

5. Finaly the web page refreshes with the result
![Index page screenshot of the result of the web application](../resources/3%20results.png)


# 4. Testing files
In order to test the separate modules, just run the python unittest files

1. Open a terminal at the project root `developer-test`

2. Run each test file:

`python3 tests/model/test_empire.py`

`python3 tests/model/test_millennium_falcon.py`

`python3 tests/model/test_journey.py`

`python3 tests/model/test_solver.py`

`python3 tests/utils/test_data.py`


# 5. Implementation choices
I chose to write the application mostly in Python3 because this is the language I am the most comfortable with. 
I wrote the front-end usage with a mix of Flask, HTML and Javascript because it was the simplest and the most straight forward path since I am not an expert in front-end development.

I chose a _Model-View-Controller_ architecture which has many benifits. 
First an MVC application separates the responsibility of the different tasks making it easier to manage the complexity of the application as each layer can be modified independently without affecting the others.
Second an MVC application is modularized which allowed me to create reusable code that can be used in different parts of the application. This helped to reduce the development time and make the code more maintainable.
Finaly an MVC application promotes code organization and standardization, which made it easier for me to reread the code and improve upon what was done at each work session. 


# 6. Encountered challenges
It has been quite a time since I got involved into a development project so I had to get out of my comfort zone and go back revisit my old courses to make sure I produced the best code possible. 
I actually very much enjoyed the exercice which took me back to my primary education. It really was a pleasure and a fulfillement to "get back on track", therefore I sincerely thank Giskard to give me such opportunity of testing my skills and keeping me pushing the pace without forgetting my primary skills.
