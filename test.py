import sys, os
sys.path.append(os.path.abspath('../../'))
sys.path.remove(os.path.abspath('.'))

from shgysk8zer0.pyutils.sqlite import Sqlite

db = Sqlite()
db.execute('''CREATE TABLE IF NOT EXISTS "users" (
    `id` INTEGER PRIMARY KEY NOT NULL,
    `username` TEXT NOT NULL UNIQUE,
    `email` TEXT NOT NULL,
    `pass` TEXT NOT NULL UNIQUE,
    `tel` TEXT
);''')

stm = db.prepare('''INSERT INTO `users` (
    `username`,
    `pass`,
    `email`,
    `tel`
) VALUES (
    :user,
    :pw,
    :email,
    :tel
);''')

stm['pw'] = 'fooBar42'
stm['user'] = 'shgysk8zer0'
stm['email'] = 'shgysk8zer0@gmail.com'
stm['tel'] = '+16616196712'

stm.executemany({}, {
    'user': 'czuber',
    'pw': 'myPass',
    'email': 'user@example.com'
})

stm = db.prepare('''SELECT
        `username` AS `uname`,
        `pass` as `pwd`,
        `email`,
        `tel`
    FROM `users`
    WHERE `username` = :user;''')

print(stm(user='shgysk8zer0').fetchone())
print(stm(user='czuber').fetchone())
