# iOS-icon-generator

iOS icon generator is a python script for you to generate a series app icons when developing ios project. If you already got an icon logo in large resolution, eg 1024*1024, and you may need to use other photo editor to generate a series icons for different device, eg, iphone 2x, iphone 4x, ipad 1x, etc. Now you just need one script, and all the needed icons will be generated for you.

## Installation

To use the `ios_app_gen_icon.py`, you just need to install pillow with pip:

    pip install pillow

That's all

## Usage

    python ios_app_gen_icon.py <Your high resolution icon file> <icons output dir> [-p <icon name prefix>]
  
eg, generate a icon set with image ~/Documents/ios-app_1024.png, and output to the current directory, with default file prefix 'app-icon':

    python ios_app_gen_icon.py ~/Documents/ios-app_1024.png .

eg, generate a icon set with image ~/Documents/ios-app_1024.png, and output to the Documents dir in home dir, with default file prefix 'app-icon':

    python ios_app_gen_icon.py ~/Documents/ios-app_1024.png ~/Documents/

eg, generate a icon set with image ~/Documents/ios-app_1024.png, and output to the Documents dir in home dir, with prefix 'hello-app-icon':

    python ios_app_gen_icon.py ~/Documents/ios-app_1024.png ~/Documents/ -p hello-app-icon

That's it. Simple? Right? Have fun. 
