import streamlit as st
import numpy as np
import random

# 설정
ROWS = 10
COLS = 15
NUM_MINES = 20

def initialize_game():
    board = np.zeros((ROWS, COLS), dtype=int)
    mine_positions = random.sample(range(ROWS * COLS), NUM_MINES)
    for pos in mine_positions:
        x, y = divmod(pos, COLS)
        board[x][y] = -1  # 지뢰

    st.session_state.mines = board
    st.session_state.revealed = np.full((ROWS, COLS), False)
    st.session_state.game_over = False

# 상태 초기화
if "mines" not in st.session_state:
    initialize_game()

st.title("💣 지뢰찾기 (클릭형 UI)")

def count_adjacent_mines(x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if st.session_state.mines[nx][ny] == -1:
                    count += 1
