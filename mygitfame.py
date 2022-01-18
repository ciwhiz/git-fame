import gitfame
import os

cwd = os.getcwd()
print(cwd)
print("--------------------- start git fame ---------------------")
# TODO: please input your git repo path
git_dir = 'you shoud input'

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
out_format = '--format=json'
# ===test data set====
t_git_dir = 'c:/sho_ws/jira_creator'
t_branch = ['--branch=origin/event/test', '--branch=origin/event/test2']
t_since = ['--since=2022-01-17', '--since=2022-01-17']
# for i in range(len(t_branch)):
#     gitfame.main(['--sort=commits', '-wt', t_branch[i], t_since[i], '-e', out_format, t_git_dir])

for i in range(len(check_branch)):
    gitfame.main(['--sort=commits', '-wt', check_branch[i], since_date[i], '-e', out_format, git_dir])
