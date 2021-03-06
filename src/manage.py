from storage.flask_app import create_app
from models.model import Subscriptions, ChannelPlaylistItem, \
    ChannelContentDetail, ChannelList, \
    ChannelStatistics, ChannelSnippet, \
    TopLevelComment, RepliesComments, \
    VideoStatistics
from flask_migrate import MigrateCommand
from flask_script import Manager, Shell

app = create_app('development')
manager = Manager(app)


def make_shell_context():
    return dict(Subscriptions=Subscriptions, ChannelPlaylistItem=ChannelPlaylistItem,
                ChannelContentDetail=ChannelContentDetail, ChannelList=ChannelList,
                ChannelStatistics=ChannelStatistics, ChannelSnippet=ChannelSnippet,
                TopLevelComment=TopLevelComment, RepliesComments=RepliesComments,
                VideoStatistics=VideoStatistics)


manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    print(app.url_map)
    manager.run()
