from gbf_backmeup.crawler import parse_text


class TestParseText:
    def test_en_text(self):
        # no http
        message = ''
        boss_name = 'Yggdrasil Omega'
        level = '60'
        room = 'DB4D4E3A'
        text = ('{} :Battle ID\n'.format(room)
               + 'I need backup!\n'
               + 'Lvl {} {}'.format(level, boss_name))
        boss, battle = parse_text(text, 'en')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        # no message
        message = ''
        level = '60'
        room = 'DB4D4E3A'
        text = ('{}{} :Battle ID\n'.format(message, room)
               + 'I need backup!\n'
               + 'Lvl {} {}\n'.format(level, boss_name)
               + 'https://asfasdfsa')
        boss, battle = parse_text(text, 'en')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        # word message
        message = 'msg1 '
        text = ('{}{} :Battle ID\n'.format(message, room)
               + 'I need backup!\n'
               + 'Lvl {} {}\n'.format(level, boss_name)
               + 'https://asfasdfsa')
        boss, battle = parse_text(text, 'en')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        # sentence message
        message = 'msg1 msg2 '
        text = ('{}{} :Battle ID\n'.format(message, room)
               + 'I need backup!\n'
               + 'Lvl {} {}\n'.format(level, boss_name)
               + 'https://asfasdfsa')
        boss, battle = parse_text(text, 'en')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        # multiple line message
        message = 'msg1 msg2 \n msg3 '
        text = ('{}{} :Battle ID\n'.format(message, room)
               + 'I need backup!\n'
               + 'Lvl {} {}\n'.format(level, boss_name)
               + 'https://asfasdfsa')
        boss, battle = parse_text(text, 'en')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        message = 'Lv75 セレスト・マグナ\n '
        text = ('{}{} :Battle ID\n'.format(message, room)
               + 'I need backup!\n'
               + 'Lvl {} {}\n'.format(level, boss_name)
               + 'https://asfasdfsa')
        boss, battle = parse_text(text, 'en')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        message = 'msg1 msg2 \n msg3 \n 123 '
        text = ('{}{} :Battle ID\n'.format(message, room)
               + 'I need backup!\n'
               + 'Lvl {} {}\n'.format(level, boss_name)
               + 'https://asfasdfsa')
        boss, battle = parse_text(text, 'en')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)

    def test_ja_text(self):
        # no http
        message = ''
        boss_name = 'マキュラ・マリウス'
        level = '100'
        room = 'DB4D4E3A'
        text = ('{} :参戦ID\n'.format(room)
               + '参加者募集！\n'
               + 'Lv{} {}'.format(level, boss_name))
        boss, battle = parse_text(text, 'ja')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        # no message
        message = ''
        level = '60'
        room = 'DB4D4E3A'
        text = ('{}{} :参戦ID\n'.format(message, room)
               + '参加者募集！\n'
               + 'Lv{} {}'.format(level, boss_name))
        boss, battle = parse_text(text, 'ja')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        # word message
        message = 'トレハン '
        text = ('{}{} :参戦ID\n'.format(message, room)
               + '参加者募集！\n'
               + 'Lv{} {}\n'.format(level, boss_name)
               + 'https://asfasdfsa')
        boss, battle = parse_text(text, 'ja')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        # sentence message
        message = 'msg1 msg2 '
        text = ('{}{} :参戦ID\n'.format(message, room)
               + '参加者募集！\n'
               + 'Lv{} {}\n'.format(level, boss_name)
               + 'https://asfasdfsa')
        boss, battle = parse_text(text, 'ja')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        # multiple line message
        message = 'msg1 msg2 \n msg3 '
        text = ('{}{} :参戦ID\n'.format(message, room)
               + '参加者募集！\n'
               + 'Lv{} {}\n'.format(level, boss_name)
               + 'https://asfasdfsa')
        boss, battle = parse_text(text, 'ja')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        message = 'Lv75 セレスト・マグナ\n '
        text = ('{}{} :参戦ID\n'.format(message, room)
               + '参加者募集！\n'
               + 'Lv{} {}\n'.format(level, boss_name)
               + 'https://asfasdfsa')
        boss, battle = parse_text(text, 'ja')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
        message = 'msg1 msg2 \n msg3 \n 123 '
        text = ('{}{} :参戦ID\n'.format(message, room)
               + '参加者募集！\n'
               + 'Lv{} {}\n'.format(level, boss_name)
               + 'https://asfasdfsa')
        boss, battle = parse_text(text, 'ja')
        assert (boss.level == level and boss.name == boss_name
            and battle.room == room and battle.message == message)
