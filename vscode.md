Shortcuts :

Command Palette (Ctrl+Shift+P)

Reload Window ( Ctrl + R )

Toggle sidebar ( Ctrl + B )

Single line comment ( Ctrl + / )

Multiline comment ( Shift + Alt + A )

Zen Mode :
    To switch back to original mode again to to Command Palette and click Zen Mode.

Multi Cursor: 


Use Interactive Playground to check the new features.

https://code.visualstudio.com/docs/getstarted/tips-and-tricks

https://github.com/Microsoft/vscode-tips-and-tricks

https://www.youtube.com/watch?v=x5GzCohd4eo

Ctrl + W ( close the editor)
Ctrl + P +P (recently used file, keep on pressing "p" to scroll over the list of files )
For looking for functions,classes in a file use :
Ctrl + P + @ --list all methods classes etc
Ctrl + P + @: -- arrange in sections of methods, classes etc
Ctrl + :   -- goes to sepecific line number

------------------------------------------------------------------------
https://hackernoon.com/setting-up-python-dev-in-vs-code-e84f01c1f64b
1.How to create and init “.vscode” in VSCode?

 As soon you do something that needs to go into this folder, for example using "Preferences-Workspace Settings" or by using one of the debugger presets, it gets populated with the files.
 
2.Python plugin
    : Python
    : Intellicode ( AI support for suggestion)
	: Live share code
	: Python Language Server
 

2.Command Pallet : Format document ( For python choose black)
    If you get error that pip is unable to install for --user in venv then manually install 


3.Command Pallet : Python Linter    (Choose pylint)


4.Auto Save : Tick the option "Auto Save" in file menu

5.Hot Exit : You can configure hot exit by setting "files.hotExit"

6.Search across files :  Press Ctrl+Shift+F and enter your search term. Search results are grouped into files containing the search term, with an indication of the hits in each file and its location. 

7.  Run Matplot lib Graphs etc 

https://devblogs.microsoft.com/python/data-science-with-python-in-visual-studio-code/


8. Runing pip in VS code ( Venv )

python -m pip install --upgrade pip

python -m pip list

python -m pip matplotlib

9. Activation of the selected Python environment is not supported in PowerShell. Consider changing your shell to Command Prompt.


	pip install -U pylint

     "[python]": {},

    "python.linting.pylintEnabled": true,
     "terminal.integrated.env.windows": {
        "PYTHONPATH": "$Env:PYTHONPATH;$Env:SPARK_HOME\\python;C:\\Users\\sk250102\\Downloads\\bigdataSetup\\spark-2.2.1-bin-hadoop2.7\\python\\lib\\py4j-0.10.4-src.zip;C:\\Users\\sk250102\\Downloads\\bigdataSetup\\spark-2.2.1-bin-hadoop2.7\\python\\lib\\pyspark.zip"
    },
	
	
	
	//"python.envFile": "${workspaceFolder}/dev.env",
              // "python.autoComplete.extraPaths": [
              //               "~/google-cloud-sdk/platform/google_appengine/lib/webapp2-2.5.2",
              //               "~/google-cloud-sdk/platform/google_appengine",
              //               "~/google-cloud-sdk/lib",
              //               "~/google-cloud-sdk/platform/google_appengine/lib/endpoints-1.0",
              //               "~/google-cloud-sdk/platform/google_appengine/lib/protorpc-1.0"
              //           ],
              //  "terminal.integrated.env.windows": {
              //               "PYTHONPATH" : "C:\\Users\\sk250102\\Downloads\\bigdataSetup\\spark-2.2.1-bin-hadoop2.7\\python\\lib\\py4j-0.10.4-src.zip;C:\\Users\\sk250102\\Downloads\\bigdataSetup\\spark-2.2.1-bin-hadoop2.7\\python\\lib\\pyspark.zip;${env:PYTHONPATH}"
              //  }

10. For file associations normally using Poetry			  

"files.associations": {
        "*.toml": "ini",
    },			  













------------------------------------ Custom Settings.json file -------------------------------------------------------------------


{
    //Basic Setup Configurations
    "terminal.integrated.shellArgs.windows": [
        "-ExecutionPolicy",
        "Bypass"
    ],
    "files.associations": {
        "*.toml": "ini",
    },
    //Editor Configurations
    "editor.minimap.enabled": false,
    "editor.fontSize": 18,
    "editor.formatOnSave": true,
    //Python configurations
    "python.pythonPath": "C:\\Users\\sk\\AppData\\Local\\pypoetry\\Cache\\virtualenvs\\how-long-46llcXc5-py3.6\\Scripts\\python.exe",
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length",
        "88"
    ],
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.pylintArgs": [
        "--max-line-length=88"
    ]
}			  