# 1. connect to aws
# 2. get all servers, filter only up servers
# 3. shutdown the server
# 4. verify server is actually stopped
from time import sleep
USERNAME = 'danny'
PASSWORD = '123'


def get_connection(user, password):
    """
    This connects to aws

    :param user: The username
    :param password: The password
    :return: Connection string
    """

    print(f"connecting to aws, with {user} and {password}")
    return True # in real life we return the connection object


def get_all_servers(connection):
    """
    Get list of all servers
    :param connection:
    :return: Servers that are up
    :rtype: List
    """

    print("Getting all servers") # in real life: all_server = connection.ec2.get_servers
    return True


def check_is_up(server, connection=None):

    if server.is_up == "up": # in real life: server.is_up is doing aws call to get the actual status
        return True

def shutdown(server):

    if check_is_up(server):
        server.shutdown # in real life it sends shutdown to aws server

    while check_is_up(server):
        print("server is still shutting down")
        sleep(10)
        ## think how to make this loop safer with additional condition
        # this to avoid cases that something happened with the api
        # hint: cooldown and fallback

    return True

if __name__ == '__main__':
    conn = get_connection(USERNAME, PASSWORD)
    all_servers_list = get_all_servers(conn)

    # This is not optiomal. it shutdowns down and waits for each machine
    # think of way to make it more effective (hint - shutdown all, then check the status of all)
    # this is example synchronious vs async operations

    for server in all_servers_list:
        shutdown(server)  # dsdsds