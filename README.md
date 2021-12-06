# WebBalloon
**WebBalloon is a CLI unminify application. It has the following features:**
  - unminifies JavaScript file contents passed in through standard input and sends the result to standard output
  - unminifies CSS file contents passed in through standard input and sends the result to standard output
  - configurable output indentation (default is 2 spaces)

**License:** [BSL-1.0](/LICENSE)

## Installation
Prerequisites: [Python3](https://www.python.org/downloads/)
```
# Cd into the project directory ("webballoon")
# Make the install script executable.
chmod u+x ./install.sh
# Run the install script. (installs the dependency Python packages and copies the Python script to /usr/local/bin)
./install.sh
```

## Usage
```
usage: webballoon.py [-h] [--indent INDENT]

optional arguments:
  -h, --help       show this help message and exit
  --indent INDENT  the indent size in spaces.(default 2)
```

## Examples
#### De-minify JavaScript file.
```
cat script.min.js | webballoon.py
```

#### De-minify JavaScript file with 4 spaces indent.
```
cat script.min.js | webballoon.py --indent 4
```

#### De-minify CSS file.
```
cat style.min.css | webballoon.py
```

#### De-minify CSS file with 4 spaces indent.
```
cat style.min.css | webballoon.py --indent 4
```

