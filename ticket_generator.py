from sortedcontainers import SortedSet
import random


def get_3_rand_numbers(start_num, end_num):
    bingo_column = SortedSet([])
    random_col_size = random.randint(1, 3)
    while len(bingo_column) < random_col_size:
        rand_number = random.randint(start_num, end_num)
        bingo_column.add(rand_number)
    return bingo_column


def get_bingo_ticket():
    bingo_column_1 = get_3_rand_numbers(1, 9)
    bingo_column_2 = get_3_rand_numbers(10, 19)
    bingo_column_3 = get_3_rand_numbers(20, 29)
    bingo_column_4 = get_3_rand_numbers(30, 39)
    bingo_column_5 = get_3_rand_numbers(40, 49)
    bingo_column_6 = get_3_rand_numbers(50, 59)
    bingo_column_7 = get_3_rand_numbers(60, 69)
    bingo_column_8 = get_3_rand_numbers(70, 79)
    bingo_column_9 = get_3_rand_numbers(80, 89)

    bingo_ticket = [bingo_column_1,bingo_column_2,bingo_column_3,bingo_column_4,bingo_column_5,bingo_column_6,bingo_column_7,bingo_column_8,bingo_column_9]

    return bingo_ticket



def bingo_ticket_generator():
    bingo_ticket_columns = []
    bingo_elements_len = 0

    while bingo_elements_len < 15:
        bingo_ticket_columns = get_bingo_ticket()
        print(bingo_ticket_columns)
        bingo_elements_len = sum([len(x) for x in bingo_ticket_columns])
        print(bingo_elements_len)

    while bingo_elements_len > 15:
        index_to_del_from = random.randint(0, 8)

        print(index_to_del_from)
        print(bingo_ticket_columns[index_to_del_from])
        print(len(bingo_ticket_columns[index_to_del_from]))

        if len(bingo_ticket_columns[index_to_del_from]) > 1:
            len_of_ticket = len(bingo_ticket_columns[index_to_del_from])
            bingo_ticket_columns[index_to_del_from].pop(random.randint(0,len_of_ticket-1))
            bingo_elements_len = sum([len(x) for x in bingo_ticket_columns])
        # bingo_elements_len = sum([len(x) for x in bingo_ticket])  #
    print(bingo_ticket_columns)

def row_maker():
    bingo_ticket_generator()
    bingo_ticket_in_rows = []
    for x in range(1, 3):
        postion_list = []
        row = sorted(list)
        for i in bingo_ticket_generator().bingo_ticket_columns:

            if len(i) == 3:
                index = bingo_ticket_generator().bingo_ticket_columns[i]
                postion_list.append(index)
                print(postion_list)
                pos_to_add = i[0]
                row.add(pos_to_add)
                i.pop(0)

            if len(row) < 5 and len(i) == 2:
                index = bingo_ticket_generator().bingo_ticket_columns[i]
                postion_list.append(index)
                print(postion_list)
                pos_to_add = i[0]
                row.add(pos_to_add)
                i.pop(0)

            if len(row) < 5 and len(i) == 1:
                index = bingo_ticket_generator().bingo_ticket_columns[i]
                postion_list.append(index)
                print(postion_list)
                pos_to_add = i[0]
                row.add(pos_to_add)
                i.pop(0)
row_maker()
def ticket_maker():
    row1 = []


if __name__ == "__main__":
    bingo_ticket_generator()