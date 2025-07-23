import streamlit as st
import numpy as np
import random

# 설정값
ROWS = 10
COLS = 15
NUM_MINES = 20

# 게임 초기화 함수
def initialize_game():
    board = np.zeros((ROWS, COLS), dtype=int)
    mine_positions = random.sample(range(ROWS * COLS), NUM_MINES)
    for pos in mine_positions:
        x, y = divmod(pos, COLS)
        board[x][y] = -1  # 지뢰

    st.session_state.mines =_
