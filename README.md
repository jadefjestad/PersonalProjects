# PersonalProjects
 Contains a variety of Personal Projects I have worked on

# Virtual Environments Guide
This guide is to how to setup and use a virtual environment in VS Code.

The purpose of setting up a virtual environment is to make it easier to run the code in the future.
We do this because the packages our program relies on often gets updated.
This sometimes changes the functionality of the functions causing the program to no longer work.
What a virtual environment does is freezes the version of the packages so the next time you run the program it runs the exact same way.

This video is helpful.

https://www.youtube.com/watch?v=JWcrseHrh2w

This should be done in the powershell terminal in VScode. These commands can also be done in cmd, but I do not recommend it

### Creating a new virtual environment:

**Change current directory:**

    cd <PATH-OF-DIRECTORY>

**Creating virtual environment in current directory:**

Note: The naming convention is to name a virtual environment: venv

    python -m venv <NAME-OF-VIRTUAL-ENVIRONMENT>

**Activating the virtual environment:**
Note: once activated your prompt should change so that it starts with the name of the virtual environment

    <NAME-OF-VIRTUAL-ENVIRONMENT>\Scripts\activate

Once you activate the environment your command prompt should look something like:

    (<NAME-OF-VIRTUAL-ENVIRONMENT>) PS C:\PATH-OF-CURRENT-DIRECTORY> 

**You will likely encounter an error the first time you run it, in that case run the below command:**

    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted


## Using a virtual environment
Any kind of script can be placed in the same folder as the virtual environment.
Just leave the virtual environment folder alone.
It should be something like this:

    /main folder
        -> venv (a folder)
        -> NAME-OF-SCRIPT-TO-RUN-IN-VIRTUAL-ENVIRONMENT.py
        -> requirements.txt

**Activating the virtual environment:**

    <NAME-OF-VIRTUAL-ENVIRONMENT>\Scripts\activate

**Deactivate the virtual environment with this command:**

    deactivate

**Downloading (python) packages into virtual environment:**

    pip install <PACKAGE-NAME>

**List the packages installed**

    pip list

**Using the requirements text file:**

Run this if there is a requirements file, this will download all the required packages quickly.

    cat requirements.txt
    
**Changing Jupyter Kernal:**

You'll likely have to change the kernal to the version of python you have created in your virtual environment.  in VS code press Ctrl+Shift+P to open up the VS code navigation prompt. Then type in the words:

    Jupyter: Select Interpreter to start Jupyter server

Press enter then navigate to and select python.exe. This should be in venv\Scripts. VS code will likely prompt you to download some Jupyter software, allow the download. This will likely have to be done with the Python interpreter as well if you are running a pure .py script. Same steps just use Python: Select Python Interpreter. If it doesn't pop up try reload the vs code window by doing Ctrl+Shift+P and selecting "Reload Window".

## Preparing an environment for production
You would do this when you are done writing the script and going to put it into usage.

**Creating a requirements text doc:**

This will make it easy for someone else to download the correct package versions.

    pip freeze > requirements.txt
    
## Anaconda

Anaconda must be downloaded from the Anaconda website. These steps can be done within the Anaconda.navigator app or from the cmd. The cmd steps are listed below.

**Check for updates**

    conda update conda
    
**Create new conda environment**

    conda create -n <NAME-OF-ENVIRONMENT> <OPTIONAL-PARAMETERS-NAME-PACKAGES-DOWNLOADED-WITH-ENVIRONMENT> <OPTIONAL-python=3.10>
    
**Activate Environment**

    conda activate <NAME-OF-ENVIRONMENT>
    
**Install packages**

    conda install tensorflow
    
**Deactivate Environment**

    conda deactivate
    
## Jupyter 

I typically use Jupyter Notebooks in VS code version

**Create Python file from Jupyter cell**

    %%writefile $experiment_folder/prep_diabetes.py
    # creates a python file called "prep_diabetes.py" in the "experiment_folder" (folder must be already created)
    
**Creating a folder**

    import os
    os.makedirs(<name-of-new-folder>, exist_ok=True) # does not overwrite
    
## Docker
    
Docker is simular to virtual enviornmnets, but not quite.

**Docker Usage Summary**

    https://gist.github.com/adamveld12/4815792fadf119ef41bd
