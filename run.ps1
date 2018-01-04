$env_exist = (Get-ChildItem venv | Measure-Object).count

if ($env_exist -le 1){
    virtualenv venv
}

.\venv\Scripts\activate

if ($env_exist -le 1){
    pip install -r requirements.txt
}

[Environment]::SetEnvironmentVariable("PYTHONDONTWRITEBYTECODE",1)
python app.py