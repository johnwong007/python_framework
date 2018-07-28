#coding=utf-8


class Player:
    ''' '''

    def __init__(self, user_id, user_name, table_id, seat_pos, user_chips):

        self.user_id = str(user_id)
        self.user_name = user_name
        self.table_id = table_id
        self.seat_pos = seat_pos
        self.user_last_chips = 0
        self.user_chips = user_chips


