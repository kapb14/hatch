from hatch.structures import File
from hatch.utils import normalize_package_name

TEMPLATE = """\
# Byte-compiled / optimized / DLL files
__pycache__/
*.pyc
*.py[cod]
*$py.class

# Environments
.env
.venv
env/
venv/
ENV/

# pyenv
.python-version

# misc
*.bak/
*.log
.idea/
.vscode/
wheelhouse/

# Distribution / packaging
.Python
develop-eggs/
build/
docs/build/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# PyBuilder
target/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# Jupyter Notebook
.ipynb_checkpoints

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# C extensions
*.so

# mypy
.mypy_cache/

"""


class GitIgnore(File):

    def __init__(self, package_name):
        super(GitIgnore, self).__init__(
            '.gitignore', TEMPLATE.format(package_name_normalized=normalize_package_name(package_name))
        )
