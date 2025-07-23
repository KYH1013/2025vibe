import streamlit as st
import numpy as np
import random

# 게임 설정
GRID_SIZE = 5
NUM_MINES = 5

# 초기화
if "mines" not in st.session_state:
    # 0으로 채운 2D 배열 생성
    board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    
    # 무작위 지뢰 위치
    mine_positions = random.sample(range(GRID_SIZE * GRID_SIZE), NUM_MINES)
    for pos in mine_positions:
        x, y = divmod(pos, GRID_SIZE)
        board[x][y] = -1  # -1은 지뢰
    
    st.session_state.mines = board
    st.session_state.revealed = np.full((GRID_SIZE, GRID_SIZE), False)

st.title("💣 Streamlit 지뢰찾기")

row = st.number_input("행 선택 (0부터 시작)", min_value=0, max_value=GRID_SIZE-1, step=1)
col = st.number_input("열 선택 (0부터 시작)", min_value=0, max_value=GRID_SIZE-1, step=1)

if st.button("🔍 클릭"):
    row, col = int(row), int(col)
    board = st.session_state.mines

    if board[row][col] == -1:
        st.error("💥 지뢰! Game Over.")
        st.session_state.revealed[:, :] = True
    else:
        # 주변 지뢰 개수 계산
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = row + dx, col + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                    if board[nx][ny] == -1:
                        count += 1
        st.success(f"✅ 안전합니다! 주변 지뢰 수: {count}")
        st.session_state.revealed[row][col] = True

# 보드 출력
st.subheader("🧩 현재 보드")

def cell_display(x, y):
    if st.session_state.revealed[x][y]:
        if st.session_state.mines[x][y] == -1:
            return "💣"
        else:
            # 주변 지뢰 수 표시
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                        if st.session_state.mines[nx][ny] == -1:
                            count += 1
            return str(count)
    else:
        return "❓"

for i in range(GRID_SIZE):
    cols = st.columns(GRID_SIZE)
    for j in range(GRID_SIZE):
        cols[j].markdown(f"<div style='text-align:center;font-size:24px;'>{cell_display(i,j)}</div>", unsafe_allow_html=True)

# 재시작
if st.button("🔄 게임 재시작"):
    st.session_state.clear()
    st.experimental_rerun()
