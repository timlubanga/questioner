from .dbconn import destroy, execute_create_tables,create_admin
from .utils.helper import check_if_user_exists

def maindb(url):
	destroy(url)
	execute_create_tables(url)
	create_admin(url)

def test_main_db(url):
	destroy(url)
	execute_create_tables(url)
	create_admin(url)
	


