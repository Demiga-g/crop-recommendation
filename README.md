# Crop Recommendation


Environment Setup

Docker
Anaconda
Ubuntu

Create a virtual environment with only the libraries need by the application

For this [pyenv](https://github.com/pyenv/pyenv) is used to get the specific Python version

```bash
pipenv install scikit-learn==1.2.2 flask --python=3.10.13
pipenv shell
```

**Optional Step:** For some reasons, running `pipenv` in my local machine was slow so I used a remote AWS EC2 instance and committed the changes to another branch which will be later merged with the main branch. Here are the commands used in the remote machine:

```bash
git checkout -b remote
git push origin remote
```

To obtain the files in my local instance, I used `git pull`.


## Creating a Pre-Commit

Creating a config file and a hook for pre-commit

```
pre-commit sample-config > .pre-commit-config.yaml
pre-commit install
```

Check the content of the pre-commit file to confirm the Python location and where the pre-commit needs to execute every time we make a commit 

```bash
less .git/hooks/pre-commit
```



