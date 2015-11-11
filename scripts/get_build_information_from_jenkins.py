import jenkins
import argparse
JOB = 'geo2tag-test'
# for search branch number
ACTIONS = u'actions'
LAST_BUILD_REVISION = u'lastBuiltRevision'
NAME = u'name'
BRANCH = u'branch'
NUM_2 = 2
NUM_3 = 3
RESULT = u'result'
SUCCESS = u'SUCCESS'
FIXED = u'FIXED'
ARG_BRANCH = '--branch'
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        ARG_BRANCH,
        required=True)
    args = parser.parse_args()
    server = jenkins.Jenkins(
        'http://jenkins.osll.ru',
        username='tatyana.berlenko',
        password='qwerty')
    last_build_number = server.get_job_info(JOB)['lastCompletedBuild']['number']
    print last_build_number
    for i in range(last_build_number, 0, -1):
        inf = server.get_build_info(JOB, i)
        if len(inf[ACTIONS]) == 7 or len(inf[ACTIONS]) == 8:
            if LAST_BUILD_REVISION in inf[ACTIONS][2]:
                number = 2
            elif LAST_BUILD_REVISION in inf[ACTIONS][3]:
                number = 3
            else:
                print 'branch number for', i, 'build not found'
                continue
        else:
            print i, 'build is not completed'
            continue
        index_branch = inf[ACTIONS][number][LAST_BUILD_REVISION][
            BRANCH][0][NAME].find('/') + 1
        branch = inf[ACTIONS][number][LAST_BUILD_REVISION][
            BRANCH][0][NAME][index_branch:]
        if args.branch == branch:
                if inf[RESULT] == SUCCESS or inf[RESULT] == FIXED:
                    print 'This task', args.branch, 'is successfully completed'
                else:
                    print 'This task', args.branch, \
                        'is unsuccessfully completed'
                break


if __name__ == '__main__':
    main()
