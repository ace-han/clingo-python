import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# with `env_file is not None` `os.environ._data.PWD` is BASE_DIR
# refer to https://django-environ.readthedocs.io/en/latest/#multiple-env-files
# ENV_PATH=other-env ./manage.py runserver
env.read_env(env.str("ENV_PATH", default=".env"))

