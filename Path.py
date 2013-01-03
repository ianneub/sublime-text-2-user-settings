import os

path = [os.environ['PATH']]
path.append('/usr/local/bin')
path.append('/usr/local/sbin')
path.append('/Users/ianneub/.nvm/v0.8.16/bin')
path.append('/Users/ianneub/.rvm/gems/ruby-1.9.3-p194/bin')
path.append('/Users/ianneub/.rvm/gems/ruby-1.9.3-p194@global/bin')
path.append('/Users/ianneub/.rvm/rubies/ruby-1.9.3-p194/bin')
path.append('/Users/ianneub/.rvm/bin')
path.append('/usr/bin')
path.append('/bin')
path.append('/usr/sbin')
path.append('/sbin')
path.append('/usr/local/git/bin')
os.environ['PATH'] += ':'.join(path)

print 'The End of Path Wars! PATH = ' + os.environ['PATH']