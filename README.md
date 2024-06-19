# PyOpencv_Gui
This repo is used to develop a GUI to demonstrate some image processing

## Dependency
The environment with python and modules are used as below:
- Python 3.10.9
- Opencv python
- PyQt5

## How to use
The folder structure is: <br/>

- /
    - / \<module_folder\>
        -   Qt_\<module\>.ui $~~~~~~~~~~~$ # Gui design file that can be changed/updated with qt design tool
        -   ui_Qt_\<module\>.py $~~~~~~~~~~~$ # The generated design in python of Gui
        -   \<module\>_Gui.py $~~~~~~~~~~$ # The gui control action, it inherited ui_Qt_\*\*\* and MainWindow_Gui.py
        -   \<module\>_Alg.py $~~~~~~~~~~$ # The implementation of algorithm with opencv and other libs.
        -   \_\_init\_\_.py  $~~~~~~~$ # stub file that python can treat folder as module


* To modify Gui design Qt_\<module\>.ui, we can use Qt designer tool, to open tool we use the command:
> qt5-tools designer

* To generate design file in python from, we use pyuic5 tool of PyQt5 with command
> pyuic5 Qt_\<module\>.ui -o ui_Qt_\<module\>.py
