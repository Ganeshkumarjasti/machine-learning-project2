# machine-learning-project2
This is my first machine learning project


creating conda environment

'''
conda create -p venv python==3.7 -y
'''

'''
conda avtivate venv/
'''

pip install -r requirements.txt


To add files to git

'''
git add <file_name>
'''

> Note : To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
'''
git status
'''

To check all version maintained by git

'''
git log

'''

to create version/commit all changes by git

'''
git commit -m "message
'''

To send version/changes to github

'''
git push origin main
'''

To check remote url
'''
git remote -v
'''

To setup CI/CD Pipeline in heroku we need 3 information

1. HEROKU_EMAIL = ganeshkumarjasti97@gmail.com
2. HEROKU_API_KEY = 0c144dd0-9d3d-44b5-80d9-78c76313cd6a
3. HEROKU_APP_NAME = machine-learning-project2


BUILD DOCKER IMAGE

'''
docker build -t <image_name>:<tagname> .
'''

> Note: Image name for docker must be lowercase


To list docker image 
'''
docker image
'''

Run docker image
'''
docker run -p 5000:5000 -e PORT=5000 ad63d6d076c9
'''

To check running container in docker

'''
docker ps

'''

to stop any container
'''
docker stop container id
'''


'''
python setup.py install
'''

install ipykernel
'''
pip install ipykernel
'''