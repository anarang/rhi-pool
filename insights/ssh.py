import paramiko
import logging
from insights.configs import settings
import time

logger = logging.getLogger(__name__)


class SSHConnection:

    @staticmethod
    def get_ssh_connection(ip):
        ssh_client = paramiko.SSHClient()
        logger.info("initiated paramiko client")
        ssh_client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        key_filename = settings.ssh.ssh_key_path

        while True:
            try:
                ssh_client.connect(hostname=ip, username="cloud-user",
                                        key_filename=key_filename)
                logger.debug("SSH connection established")
                break
            except paramiko.ssh_exception.NoValidConnectionsError:
                time.sleep(5)

        return ssh_client
