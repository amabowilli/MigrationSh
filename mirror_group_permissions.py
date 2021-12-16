from resources.instance_init import ServerInstance, CloudInstance
from resources.mirror_operations import ServerDetails as SD, ActionOnItems as AOI
from resources.logger import logger

def main() -> None:
    server = ServerInstance()
    cloud = CloudInstance()

    '''
    get list of groups_to_migrate that only contain groups that are actively used in Server. 
        Ignores Jira/Connie groups that may have been synced from upstream user directory like Jira or LDAP
    get all global groups and their perms to then be able to apply to resources/instance_actions.CloudActions.set_group_permissions
    get full layout of projects/repos so that we can flatten the permissions and apply the effective permission to a given group on a given repo
    '''

    logger.info('Scanning Bitbucket Server instance for structure and group data')
    groups_to_migrate, global_groups, server_structure = SD.scan_server_structure(server)
    logger.info('Starting group sync to cloud')
    group_workspace_privileges = AOI.mirror_groups(server, cloud, groups_to_migrate, global_groups)
    logger.info('Starting to mirror groups and permissions')
    AOI.mirror_repo_groups(server, cloud, groups_to_migrate, server_structure)
    AOI.print_group_privilege_details(group_workspace_privileges, cloud.workspace)


if __name__ == '__main__':
    main()
    exit()
