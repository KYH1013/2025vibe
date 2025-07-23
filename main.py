import streamlit as st
import numpy as np
import random

# 설정
ROWS = 10
COLS = 15
NUM_MINES = 20

def init_game():
    board = np.zeros((ROWS, COLS), dtype=int)
    mine_positions = random.sample(range(ROWS * COLS), NUM_MINES)
    for pos in mine_positions:
        x, y = divmod(pos, COLS)
        board[x][y] = -1  # 지뢰
    st.session_state.mines = board
    st.session_state.revealed = np.full((ROWS, COLS), False)
    st.session_state.game_over = False
    st.session_state.clicked = None

# 초기화
if "mines" not in st.session_state:
    init_game()

st.title("💣 지뢰찾기 (클릭형 UI - 안정화버전)")

def count_adjacent_mines(x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if dx == 0 and dy == 0:
                continue
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if st.session_state.mines[nx][ny] == -1:
                    count += 1
    return count

def click_cell(i, j):
    if st.session_state.revealed[i][j] or st.session_state.game_over:
        return
    st.session_state.revealed[i][j] = True
    if st.session_state.mines[i][j] == -1:
        st.session_state.game_over = True
        st.warning("💥 지뢰를 밟았습니다! 게임 종료.")
    else:
        count = count_adjacent_mines(i, j)
        if count == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < ROWS and 0 <= nj < COLS:
                        click_cell(ni, nj)

# 👉 클릭 처리 (세션에서 안전하게 접근)
clicked = st.session_state.get("clicked", None)
if clicked:
    i, j = clicked
    click_cell(i, j)
    st.session_state.clicked = None  # 클릭 후 초기화

# 게임판 출력
for i in range(ROWS):
    cols = st.columns(COLS)
    for j in range(COLS):
        key = f"{i}-{j}"
        if st.session_state.revealed[i][j]:
            if st.session_state.mines[i][j] == -1:
                cols[j].button("💣", key=key, disabled=True)
            else:
                count = count_adjacent_mines(i, j)
                label = str(count) if count > 0 else ""
                cols[j].button(label, key=key, disabled=True)
        else:
            if cols[j].button("❓", key=key):
                st.session_state.clicked = (i, j)

# 새 게임
st.markdown("---")
if st.button("🔄 새 게임 시작"):
    st.session_state.clear()
