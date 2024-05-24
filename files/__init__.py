import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


CSV_FILE_PATH_CREATE_POSTS = get_path(filename="create_posts.csv")
CSV_FILE_PATH_UPDATE_POSTS = get_path(filename="update_post.csv")
