class Die:
    def __init__(self):
        self.val = 7
        self.rolls = 0

    def roll_die(self):
        self.rolls += 3
        self.val -= 1
        if self.val < 0: self.val = 9
        return self.val

class UniversePlay:
    WIN_POINTS = 21

    def __init__(self, players):
        self.p1 = players[0]-1
        self.p2 = players[1]-1
        self.win1 = 0
        self.win2 = 0

    # TODO: This can be speed up by introducing a state cache
    def play_game(self):
        def do_turn(player1_pos, player1_points, player2_pos, player2_points, player_turn, num_of_games_in_this_state=1):
            if player1_points >= self.WIN_POINTS:
                self.win1 += num_of_games_in_this_state
                return
            if player2_points >= self.WIN_POINTS:
                self.win2 += num_of_games_in_this_state
                return

            if player_turn == 0:
                do_turn(player1_pos + 3, player1_points + (player1_pos + 3) % 10 + 1, player2_pos, player2_points,
                        1 - player_turn, num_of_games_in_this_state * 1)
                do_turn(player1_pos + 4, player1_points + (player1_pos + 4) % 10 + 1, player2_pos, player2_points,
                        1 - player_turn, num_of_games_in_this_state * 3)
                do_turn(player1_pos + 5, player1_points + (player1_pos + 5) % 10 + 1, player2_pos, player2_points,
                        1 - player_turn, num_of_games_in_this_state * 6)
                do_turn(player1_pos + 6, player1_points + (player1_pos + 6) % 10 + 1, player2_pos, player2_points,
                        1 - player_turn, num_of_games_in_this_state * 7)
                do_turn(player1_pos + 7, player1_points + (player1_pos + 7) % 10 + 1, player2_pos, player2_points,
                        1 - player_turn, num_of_games_in_this_state * 6)
                do_turn(player1_pos + 8, player1_points + (player1_pos + 8) % 10 + 1, player2_pos, player2_points,
                        1 - player_turn, num_of_games_in_this_state * 3)
                do_turn(player1_pos + 9, player1_points + (player1_pos + 9) % 10 + 1, player2_pos, player2_points,
                        1 - player_turn, num_of_games_in_this_state * 1)
            else:
                do_turn(player1_pos, player1_points, player2_pos + 3,
                        player2_points + (player2_pos + 3) % 10 + 1, 1 - player_turn, num_of_games_in_this_state * 1)
                do_turn(player1_pos, player1_points, player2_pos + 4,
                        player2_points + (player2_pos + 4) % 10 + 1, 1 - player_turn, num_of_games_in_this_state * 3)
                do_turn(player1_pos, player1_points, player2_pos + 5,
                        player2_points + (player2_pos + 5) % 10 + 1, 1 - player_turn, num_of_games_in_this_state * 6)
                do_turn(player1_pos, player1_points, player2_pos + 6,
                        player2_points + (player2_pos + 6) % 10 + 1, 1 - player_turn, num_of_games_in_this_state * 7)
                do_turn(player1_pos, player1_points, player2_pos + 7,
                        player2_points + (player2_pos + 7) % 10 + 1, 1 - player_turn, num_of_games_in_this_state * 6)
                do_turn(player1_pos, player1_points, player2_pos + 8,
                        player2_points + (player2_pos + 8) % 10 + 1, 1 - player_turn, num_of_games_in_this_state * 3)
                do_turn(player1_pos, player1_points, player2_pos + 9,
                        player2_points + (player2_pos + 9) % 10 + 1, 1 - player_turn, num_of_games_in_this_state * 1)


        do_turn(self.p1, 0, self.p2, 0, 0, 1)
        return max(self.win1, self.win2)

def part1(inp):
    points = [0, 0]
    die = Die()
    pos = [inp[0]-1, inp[1]-1]
    while points[0] < 1000 and points[1] < 1000:
        pos[0] += die.roll_die()
        pos[0] %= 10
        points[0] += pos[0]+1
        if points[0] >= 1000: return points[1] * die.rolls
        pos[1] += die.roll_die()
        pos[1] %= 10
        points[1] += pos[1]+1
        if points[1] >= 1000: return points[0] * die.rolls

def part2(inp):
    return UniversePlay(inp).play_game()

def prep_data(inp):
    return [int(i.strip()[28:]) for i in inp]

with open("input_test.txt") as f:
    data_test = prep_data(f.readlines())

with open("input.txt") as f:
    data = prep_data(f.readlines())

assert part1(data_test) == 739785
print(part1(data))
assert part2(data_test) == 444356092776315
print(part2(data))
