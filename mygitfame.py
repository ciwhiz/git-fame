import gitfame
import os

# https://github.com/casperdcl/git-fame

cwd = os.getcwd()
print(cwd)
print("--------------------- start git fame ---------------------")
# TODO: please input your git repo path
git_dir = 'c:/sho_ws/jira_creator'

single_branch = '--branch=origin/master'
single_since_date = '--since=2021-01-01'

check_branch = ['--branch=origin/event/4.0.12xx', '--branch=origin/event/4.0.11xx', '--branch=origin/event/4.0.10xx',
                '--branch=origin/event/3.6.13xx', '--branch=origin/event/3.6.12xx',
                '--branch=origin/event/3.6.11xx', '--branch=origin/event/3.6.10xx', '--branch=origin/event/3.5.18xx',
                '--branch=origin/event/3.5.17xx', '--branch=origin/event/3.5.19xx',
                '--branch=origin/event/3.5.15xx']
since_date = ['--since=2021-12-13', '--since=2021-11-16', '--since=2021-11-05', '--since=2021-09-29',
              '--since=2021-08-04',
              '--since=2021-06-30', '--since=2021-06-09', '--since=2021-04-08', '--since=2021-03-12',
              '--since=2021-04-07',
              '--since=2021-02-02']

tv_repo_dir = 'c:/sho_ws/TV_ux3.5'

tv_branch = ['--branch=origin/master', '--branch=origin/ux3.5', '--branch=origin/ux3.5_lms_things_4_28_2_beta',
             '--branch=origin/6.0MR2', '--branch=origin/rcmd01', '--branch=origin/nmrm_accessibility',
             '--branch=origin/nmrm', '--branch=origin/6.0Init', '--branch=origin/6.0MR1']
tv_since_date = ['--since=2021-01-01', '--since=2021-07-06', '--since=2021-10-01', '--since=2021-03-26',
                 '--since=2021-07-13', '--since=2021-04-22', '--since=2021-03-10', '--since=2021-02-04',
                 '--since=2021-03-10']

out_format = '--format=json'
# ===test data set====
t_git_dir = 'c:/sho_ws/jira_creator'
t_branch = ['--branch=origin/event/test', '--branch=origin/event/test2']
t_branch_single = '--branch=origin/master'
t_since = ['--since=2022-01-17', '--since=2022-01-17']
t_since_single = '--since=2021-12-01'
# for i in range(len(t_branch)):
#     gitfame.main(['--sort=commits', '-wt', t_branch[i], t_since[i], '-e', out_format, t_git_dir])

# for i in range(len(check_branch)):
#     gitfame.main(['--sort=commits', '--loc=surv|ins|del', '-wt', check_branch[i], since_date[i], '-e', out_format, git_dir])

# for i in range(len(tv_branch)):
#     gitfame.main(['--sort=commits', '-wt', tv_branch[i], tv_since_date[i], '-e', out_format, tv_repo_dir])

# single branch
# gitfame.main(['--sort=loc', '-wt', single_branch, single_since_date, '--loc=ins,del,surv', '-e', out_format, git_dir])

gitfame.main(['--sort=loc', '-MCt', t_branch_single, t_since_single, '--loc=ins,del', '-e', t_git_dir])


