## Usage
### Set up chromedriver
copy chromedriver.exe to C:\Windows if on windows

symlink chromium-chromedriver to chromedriver if on linux

If you need an arm version of chromedriver on a debian based distro check out https://launchpad.net/ubuntu/trusty/armhf/chromium-chromedriver
For other distros download from electron releases if it's not in your package manager

### Create config.json
Follow the format in config.json.example
Copy your login cookies (In chrome go to developer tools/application and click on cookies)

### Install dependencies
run
```
virtualenv python3 env
source env/bin/activate (or on windows env/Scripts/activate.bat)
pip install -r requirements.txt
```

### Run
    python3 main.py
